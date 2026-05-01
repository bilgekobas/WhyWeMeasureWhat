"""
Auto-link glossary terms across a Jupyter Book / MyST Markdown project.

What it does
------------
- Reads glossary entries from a MyST glossary page using this pattern:

    (label-term)=
    :::{dropdown} Term title

- Scans other .md files in the book.
- Replaces the first plain-text occurrence of each glossary title per file with a MyST cross-reference:

    {ref}`Term title <label-term>`

- Skips:
    - the glossary file itself
    - fenced code blocks
    - existing MyST refs
    - Markdown links
    - raw URLs
    - headings
    - image syntax

Recommended workflow
--------------------
1. Commit your current files first, or make a copy.
2. Run this script.
3. Inspect the git diff.
4. Build the book.
5. If needed, revert and adjust EXCLUDE_DIRS / EXCLUDE_FILES / MAX_LINKS_PER_FILE.

Usage
-----
From the repository root or from the book folder:

    python auto_link_glossary_terms.py

If your paths differ, edit BOOK_DIR and GLOSSARY_RELATIVE_PATH below.
"""

from __future__ import annotations

import re
from pathlib import Path


# ---------------------------------------------------------------------
# EDIT THESE PATHS IF NEEDED
# ---------------------------------------------------------------------

# If you run this from the book folder, keep BOOK_DIR = Path(".")
# If you run this from the repo root and your book folder is called "book",
# change this to: BOOK_DIR = Path("book")
BOOK_DIR = Path(".")

# Path to your glossary file relative to BOOK_DIR.
# Change this if your file is elsewhere, for example:
# GLOSSARY_RELATIVE_PATH = Path("content/controlled-vocabulary-and-glossary.md")
GLOSSARY_RELATIVE_PATH = Path("content/terminological-alignment/controlled-vocabulary-and-glossary.md")

# Avoid auto-linking inside these folders.
EXCLUDE_DIRS = {
    "_build",
    ".jupyter_cache",
    ".ipynb_checkpoints",
    "_static",
    "assets",
}

# Avoid auto-linking these files by name.
EXCLUDE_FILES = {
    "references.md",
    "bibliography.md",
}

# To avoid visual clutter, link only the first occurrence of each term per file.
LINK_FIRST_OCCURRENCE_ONLY = True

# Optional safety limit. Set to None for no limit.
MAX_LINKS_PER_FILE = 30

# If True, the script only prints what it would change and writes no files.
DRY_RUN = False


# ---------------------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------------------

ENTRY_RE = re.compile(
    r"^\((label-[^)]+)\)=\s*\n:::\{dropdown\}\s*(.+?)\s*$",
    re.MULTILINE,
)


def extract_glossary_entries(glossary_text: str) -> list[tuple[str, str]]:
    """Return [(term_title, label), ...] from the glossary markdown."""
    entries: list[tuple[str, str]] = []

    for label, title in ENTRY_RE.findall(glossary_text):
        title = clean_title(title)
        if title:
            entries.append((title, label))

    # Longest terms first prevents linking "Phase" inside "Time-of-day phase..."
    entries.sort(key=lambda item: len(item[0]), reverse=True)

    return entries


def clean_title(title: str) -> str:
    """Remove common display additions that should not be required for matching."""
    title = title.strip()

    # Keep the visible title as link text, but remove trailing acronym if needed
    # only for generating aliases later.
    title = re.sub(r"\s+", " ", title)

    return title


def aliases_for_title(title: str) -> list[str]:
    """Generate conservative aliases for matching."""
    aliases = [title]

    # "Cardiac output (CO)" -> "Cardiac output"
    no_parentheses = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()
    if no_parentheses and no_parentheses != title:
        aliases.append(no_parentheses)

    # "Vasodilation (active and passive)" -> "Vasodilation"
    # already handled by no_parentheses.

    # Keep unique, longest first.
    aliases = sorted(set(aliases), key=len, reverse=True)
    return aliases


def split_fenced_code_blocks(text: str) -> list[tuple[str, bool]]:
    """
    Split text into [(chunk, is_code_block), ...] based on fenced code blocks.

    Handles ``` and ~~~ fences.
    """
    fence_re = re.compile(r"(^[ \t]*(```|~~~).*$)", re.MULTILINE)
    parts: list[tuple[str, bool]] = []

    pos = 0
    in_code = False
    start = 0

    for match in fence_re.finditer(text):
        fence_start = match.start()
        fence_end = match.end()

        if not in_code:
            if fence_start > pos:
                parts.append((text[pos:fence_start], False))
            start = fence_start
            in_code = True
            pos = fence_end
        else:
            parts.append((text[start:fence_end], True))
            in_code = False
            pos = fence_end

    if pos < len(text):
        parts.append((text[pos:], in_code))

    return parts


def protected_spans(chunk: str) -> list[tuple[int, int]]:
    """
    Return spans that should not be modified inside a non-code markdown chunk.
    """
    patterns = [
        r"\{ref\}`[^`]+`",                 # existing MyST ref
        r"\[[^\]]+\]\([^)]+\)",           # markdown links
        r"!\[[^\]]*\]\([^)]+\)",          # markdown images
        r"https?://[^\s)]+",              # raw URLs
        r"`[^`\n]+`",                     # inline code
        r"^\s*#{1,6}\s+.*$",              # headings
        r"^\s*\.\.\s+.*$",                # directives-ish
        r"^\s*:::\{.*$",                  # MyST directives
        r"^\s*\([^)]+\)=\s*$",            # labels
    ]

    spans: list[tuple[int, int]] = []
    for pattern in patterns:
        flags = re.MULTILINE
        for m in re.finditer(pattern, chunk, flags):
            spans.append((m.start(), m.end()))

    return merge_spans(spans)


def merge_spans(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not spans:
        return []

    spans = sorted(spans)
    merged = [spans[0]]

    for start, end in spans[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def is_inside_spans(index: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)


def make_term_pattern(alias: str) -> re.Pattern[str]:
    """
    Build a case-insensitive term pattern.

    Uses negative lookarounds rather than \\b so terms with punctuation
    such as distal–proximal gradient behave better.
    """
    escaped = re.escape(alias)
    return re.compile(
        rf"(?<![\w`])({escaped})(?![\w`])",
        flags=re.IGNORECASE,
    )


def link_terms_in_chunk(
    chunk: str,
    entries: list[tuple[str, str]],
    already_linked_terms: set[str],
    remaining_link_budget: int | None,
) -> tuple[str, int]:
    """
    Link terms in one non-code chunk.
    """
    protected = protected_spans(chunk)
    total_links = 0

    for title, label in entries:
        if remaining_link_budget is not None and total_links >= remaining_link_budget:
            break

        if LINK_FIRST_OCCURRENCE_ONLY and title.lower() in already_linked_terms:
            continue

        linked_this_title = False

        for alias in aliases_for_title(title):
            pattern = make_term_pattern(alias)

            def replace_one(match: re.Match[str]) -> str:
                nonlocal total_links, linked_this_title, protected

                if remaining_link_budget is not None and total_links >= remaining_link_budget:
                    return match.group(0)

                if is_inside_spans(match.start(), protected):
                    return match.group(0)

                visible_text = match.group(1)
                replacement = f"{{ref}}`{visible_text} <{label}>`"

                total_links += 1
                linked_this_title = True
                return replacement

            new_chunk, n = pattern.subn(replace_one, chunk, count=1)

            if n and new_chunk != chunk:
                chunk = new_chunk
                already_linked_terms.add(title.lower())

                # Recompute protected spans after insertion.
                protected = protected_spans(chunk)
                break

        if linked_this_title and LINK_FIRST_OCCURRENCE_ONLY:
            continue

    return chunk, total_links


def link_terms_in_text(text: str, entries: list[tuple[str, str]]) -> tuple[str, int]:
    parts = split_fenced_code_blocks(text)
    new_parts: list[str] = []
    total_links = 0
    already_linked_terms: set[str] = set()

    for chunk, is_code in parts:
        if is_code:
            new_parts.append(chunk)
            continue

        remaining = None
        if MAX_LINKS_PER_FILE is not None:
            remaining = max(MAX_LINKS_PER_FILE - total_links, 0)

        linked_chunk, n_links = link_terms_in_chunk(
            chunk,
            entries,
            already_linked_terms,
            remaining,
        )
        total_links += n_links
        new_parts.append(linked_chunk)

    return "".join(new_parts), total_links


def should_skip_file(path: Path, glossary_path: Path) -> bool:
    if path == glossary_path:
        return True

    if path.name in EXCLUDE_FILES:
        return True

    if any(part in EXCLUDE_DIRS for part in path.parts):
        return True

    return False


def main() -> None:
    book_dir = BOOK_DIR.resolve()
    glossary_path = (book_dir / GLOSSARY_RELATIVE_PATH).resolve()

    if not glossary_path.exists():
        raise FileNotFoundError(
            f"Could not find glossary file:\n{glossary_path}\n\n"
            "Edit GLOSSARY_RELATIVE_PATH or BOOK_DIR in the script."
        )

    glossary_text = glossary_path.read_text(encoding="utf-8")
    entries = extract_glossary_entries(glossary_text)

    if not entries:
        raise RuntimeError(
            "No glossary entries found. Check that entries use:\n"
            "(label-...)=\n:::{dropdown} Entry title"
        )

    print(f"Found {len(entries)} glossary entries.")
    print(f"Glossary file: {glossary_path}")

    changed_files = 0
    total_links = 0

    for md_path in sorted(book_dir.rglob("*.md")):
        md_path = md_path.resolve()
        if should_skip_file(md_path, glossary_path):
            continue

        original = md_path.read_text(encoding="utf-8")
        updated, n_links = link_terms_in_text(original, entries)

        if updated != original:
            changed_files += 1
            total_links += n_links
            rel = md_path.relative_to(book_dir)
            print(f"{'Would update' if DRY_RUN else 'Updated'} {rel} ({n_links} links)")

            if not DRY_RUN:
                md_path.write_text(updated, encoding="utf-8")

    print()
    print(f"{'Dry run complete.' if DRY_RUN else 'Done.'}")
    print(f"Files changed: {changed_files}")
    print(f"Links added: {total_links}")

    if not DRY_RUN:
        print()
        print("Next steps:")
        print("1. Inspect your git diff carefully.")
        print("2. Run: jupyter-book clean .")
        print("3. Run: jupyter-book build .")


if __name__ == "__main__":
    main()
