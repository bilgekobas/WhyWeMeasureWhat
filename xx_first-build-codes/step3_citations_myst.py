# -*- coding: utf-8 -*-
"""
Step 3: Convert (Author, Year) parenthetical citations to MyST cite roles,
configure JupyterBook bibtex, and enforce a SINGLE References chapter.

- Converts: (ISO, 2004; Kenny, 2010)  ->  []{cite:p}`ISO9886_2004,Kenny2010`
- Removes any previously injected per-page "## References" blocks
- Removes any remaining ```{bibliography}``` blocks from all pages EXCEPT the single global references page
- Writes/overwrites content/references/index.md as the global bibliography page
"""

import re
import csv
from pathlib import Path
from collections import defaultdict
import yaml


REPO = Path(r"C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git")

BOOK = REPO / "book"
CONTENT = BOOK / "content"

BIB_IN_REPO = REPO / "WhyWeMeasure_v04.bib"
BIB_IN_BOOK = BOOK / "WhyWeMeasure_v04.bib"

AUDIT_DIR = REPO / "_build_audit"
AUDIT_CSV = AUDIT_DIR / "citation_audit.csv"

# Enforce a single References chapter
ADD_PER_PAGE_REFERENCES = False

# Where the single references chapter will live
REFERENCES_MD = CONTENT / "references" / "index.md"
REFERENCES_REL_SUFFIX = "book/content/references/index.md"


# -----------------------------
# BibTeX parsing
# -----------------------------
ENTRY_START = re.compile(r"@\w+\s*{\s*([^,]+)\s*,", re.IGNORECASE)
FIELD = re.compile(r"^\s*([a-zA-Z_]+)\s*=\s*(.+?)\s*,?\s*$")


def _strip_bib_value(v: str) -> str:
    v = v.strip()
    if (v.startswith("{") and v.endswith("}")) or (v.startswith('"') and v.endswith('"')):
        v = v[1:-1].strip()
    return v


def parse_bibtex(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    entries = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        m = ENTRY_START.search(line)
        if not m:
            i += 1
            continue

        citekey = m.group(1).strip()
        fields = {}

        i += 1
        brace_depth = line.count("{") - line.count("}")
        while i < len(lines) and brace_depth > 0:
            line = lines[i]
            brace_depth += line.count("{") - line.count("}")

            fm = FIELD.match(line)
            if fm:
                fname = fm.group(1).lower().strip()
                fval = _strip_bib_value(fm.group(2))
                fields[fname] = fval

            i += 1

        entries[citekey] = fields

    return entries


def normalize_lastname(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z\u00C0-\u017F\-']", "", s)
    return s


def first_author_lastname(author_field: str) -> str | None:
    if not author_field:
        return None

    first = author_field.split(" and ")[0].strip()

    if "," in first:
        last = first.split(",")[0].strip()
        return last if last else None

    parts = first.split()
    if not parts:
        return None
    return parts[-1].strip()


def build_key_index(entries: dict):
    by_author_year = defaultdict(list)

    for key, fields in entries.items():
        y = fields.get("year")
        a = fields.get("author", "")
        if not y:
            continue
        ln = first_author_lastname(a) or ""
        ln_norm = normalize_lastname(ln) if ln else ""
        if not ln_norm:
            continue
        by_author_year[(ln_norm, y)].append(key)

    for k in list(by_author_year.keys()):
        by_author_year[k] = sorted(by_author_year[k], key=lambda x: x.lower())

    return by_author_year


# -----------------------------
# Citation matching + replacement
# -----------------------------
CIT_ITEM = re.compile(
    r"""
    ^\s*
    (?P<a1>[A-Za-z\u00C0-\u017F'\-]+)
    (?:\s+et\ al\.)?
    (?:\s+(?:and|&)\s+(?P<a2>[A-Za-z\u00C0-\u017F'\-]+))?
    \s*,\s*
    (?P<year>\d{4})
    (?P<suffix>[a-z])?
    \s*$
    """,
    re.VERBOSE,
)

PAREN_GROUP = re.compile(r"\(([^()]*,\s*(?:19|20)\d{2}[a-z]?[^()]*)\)")


def resolve_citekey(item_text: str, idx: dict):
    m = CIT_ITEM.match(item_text)
    if not m:
        return None, "pattern_not_matched"

    a1 = normalize_lastname(m.group("a1"))
    year = m.group("year")
    suffix = m.group("suffix")

    keys = idx.get((a1, year), [])
    if not keys:
        return None, "no_bib_match"

    if len(keys) == 1:
        return keys[0], None

    if suffix:
        j = ord(suffix) - ord("a")
        if 0 <= j < len(keys):
            return keys[j], None
        return None, "suffix_out_of_range"

    return None, "ambiguous_author_year"


def convert_parenthetical_group(group_text: str, idx: dict, audit_rows: list, file_rel: str):
    parts = [p.strip() for p in group_text.split(";")]
    resolved = []

    any_fail = False
    for p in parts:
        if not p:
            continue

        key, reason = resolve_citekey(p, idx)
        if key:
            resolved.append(key)
        else:
            any_fail = True
            audit_rows.append(
                {"file": file_rel, "original_group": group_text, "item": p, "reason": reason}
            )

    if any_fail or not resolved:
        return f"({group_text})"

    # Deduplicate keys within a citation group (prevents "duplicate citation" warnings)
    seen = set()
    dedup = []
    for k in resolved:
        if k not in seen:
            seen.add(k)
            dedup.append(k)

    return f"[]{{cite:p}}`{','.join(dedup)}`"


# -----------------------------
# Remove previously injected per-page References blocks
# -----------------------------
# Tolerant matcher for trailing per-page blocks like:
# --- (optional)
# ## References
# ```{bibliography}
# :cited:
# ...
# ```
PER_PAGE_REFS_BLOCK = re.compile(
    r"""
    (?:\n+\s*---\s*\n+)?         # optional horizontal rule
    \n*\s*##\s+References\s*\n+  # References heading
    \s*```{bibliography}\s*\n    # bibliography directive
    .*?\n\s*```                 # until closing fence
    \s*$
    """,
    re.VERBOSE | re.DOTALL,
)


def strip_per_page_references(md: str) -> str:
    return PER_PAGE_REFS_BLOCK.sub("", md.rstrip()) + "\n"


# Remove any bibliography directive block anywhere (belt-and-suspenders)
ANY_BIB_BLOCK = re.compile(r"\n\s*```{bibliography}\s*\n.*?\n\s*```\s*\n?", re.DOTALL)


def ensure_config_for_bib():
    config_path = BOOK / "_config.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Missing JupyterBook config: {config_path}")

    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    cfg.setdefault("parse", {})
    cfg["parse"].setdefault("myst_enable_extensions", [])
    for ext in ["colon_fence", "linkify"]:
        if ext not in cfg["parse"]["myst_enable_extensions"]:
            cfg["parse"]["myst_enable_extensions"].append(ext)

    cfg.setdefault("sphinx", {})
    cfg["sphinx"].setdefault("config", {})
    cfg["sphinx"]["config"].setdefault("bibtex_bibfiles", [])

    bib_rel = BIB_IN_BOOK.name
    if bib_rel not in cfg["sphinx"]["config"]["bibtex_bibfiles"]:
        cfg["sphinx"]["config"]["bibtex_bibfiles"].append(bib_rel)

    config_path.write_text(yaml.safe_dump(cfg, sort_keys=False), encoding="utf-8")


def write_global_references_page():
    REFERENCES_MD.parent.mkdir(parents=True, exist_ok=True)
    REFERENCES_MD.write_text(
        "# References\n\n"
        "```{bibliography}\n"
        ":style: unsrt\n"
        "```\n",
        encoding="utf-8",
    )


def main():
    if not BIB_IN_REPO.exists():
        raise FileNotFoundError(f"Missing bib in repo root: {BIB_IN_REPO}")
    BOOK.mkdir(exist_ok=True)
    if not BIB_IN_BOOK.exists():
        BIB_IN_BOOK.write_bytes(BIB_IN_REPO.read_bytes())

    ensure_config_for_bib()

    entries = parse_bibtex(BIB_IN_BOOK)
    idx = build_key_index(entries)

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    audit_rows = []

    md_files = sorted(CONTENT.rglob("*.md"))
    for fp in md_files:
        rel = fp.relative_to(REPO).as_posix()
        text = fp.read_text(encoding="utf-8", errors="replace")

        # Keep the one global bibliography page intact
        if rel.endswith(REFERENCES_REL_SUFFIX):
            cleaned = text
        else:
            # Strip a trailing "## References" + bibliography block (older per-page injection)
            cleaned = strip_per_page_references(text)
            # Belt-and-suspenders: remove ANY remaining bibliography directive blocks anywhere
            cleaned = ANY_BIB_BLOCK.sub("\n", cleaned)
        # 🔹 remove stray empty brackets like [](...)
        cleaned = re.sub(r"\[\]\s*(\()", r"\1", cleaned)

        def repl(m):
            inner = m.group(1)
            return convert_parenthetical_group(inner, idx, audit_rows, rel)

        new_text = PAREN_GROUP.sub(repl, cleaned)

        if ADD_PER_PAGE_REFERENCES:
            raise RuntimeError("Per-page references are disabled for single References chapter mode.")

        if new_text != text:
            fp.write_text(new_text, encoding="utf-8")

    # Write/overwrite the global References chapter (single bibliography directive in the book)
    write_global_references_page()

    with AUDIT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "original_group", "item", "reason"])
        w.writeheader()
        for r in audit_rows:
            w.writerow(r)

    print("✅ Step 3 complete (single References chapter).")
    print(f"Updated citations in: {CONTENT}")
    print(f"Wrote global references page: {REFERENCES_MD}")
    print(f"Wrote citation audit: {AUDIT_CSV}")
    print("Next:")
    print(f"  cd {BOOK}")
    print("  jupyter-book clean .")
    print("  jupyter-book build .")
    print("Verification:")
    print(r'  findstr /S /N "```{bibliography}" book\content\*.md')


if __name__ == "__main__":
    main()