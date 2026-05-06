# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:48:19 2026

@author: kobas
"""

import re
import shutil
from pathlib import Path

import yaml
from slugify import slugify

REPO = Path(r"C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git")

IN_MD = REPO / "_build_intermediate" / "WhyWeMeasureWhat_v04_full.md"

BOOK = REPO / "book"
CONTENT = BOOK / "content"

# If you want, we can later insert per-page bibliographies automatically.
ADD_PER_PAGE_BIB = False
BIB_NAME = "WhyWeMeasure_v04.bib"


def clean_generated_content():
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True, exist_ok=True)


def extract_front_matter(md: str):
    """
    Everything before first H1 (# ...) is treated as the book landing page intro.
    """
    m = re.search(r"^#\s+.+$", md, flags=re.MULTILINE)
    if not m:
        raise ValueError("No H1 headings found.")
    front = md[: m.start()].strip()
    rest = md[m.start():].lstrip()
    return front, rest


def split_into_chapters(md: str):
    """
    Split by H1. Within each H1 block, split by H2 into separate pages.
    Rules:
      - H1 => chapter folder with index.md (landing page)
      - Text between H1 and first H2 => goes to that H1 index.md
      - H2 => separate page within chapter folder
      - H3+ stay within the H2 page as anchors
    """
    md = md.replace("\r\n", "\n").replace("\r", "\n")

    h1_pat = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
    h1_matches = list(h1_pat.finditer(md))
    if not h1_matches:
        raise ValueError("No H1 headings (# ...) found.")

    chapters = []
    for i, m in enumerate(h1_matches):
        h1_title = m.group(1).strip()
        start = m.end()
        end = h1_matches[i + 1].start() if i + 1 < len(h1_matches) else len(md)
        h1_block = md[start:end].strip("\n")

        h2_pat = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
        h2_matches = list(h2_pat.finditer(h1_block))

        if not h2_matches:
            chapters.append({"h1": h1_title, "intro": h1_block.strip(), "pages": []})
            continue

        intro = h1_block[: h2_matches[0].start()].strip("\n")

        pages = []
        for j, h2m in enumerate(h2_matches):
            h2_title = h2m.group(1).strip()
            p_start = h2m.end()
            p_end = h2_matches[j + 1].start() if j + 1 < len(h2_matches) else len(h1_block)
            body = h1_block[p_start:p_end].strip("\n")

            # Each H2 page gets its own H1 heading so the page title is correct
            page_md = f"# {h2_title}\n\n{body}\n"
            pages.append({"h2": h2_title, "body": page_md})

        chapters.append({"h1": h1_title, "intro": intro.strip(), "pages": pages})

    return chapters


def ensure_jupyterbook_scaffold():
    BOOK.mkdir(exist_ok=True)
    CONTENT.mkdir(parents=True, exist_ok=True)

    # Minimal config; we’ll expand this later.
    config_path = BOOK / "_config.yml"
    if not config_path.exists():
        config_path.write_text(
            yaml.safe_dump(
                {
                    "title": "WHY WE MEASURE WHAT, HOW, AND WHERE",
                    "author": "Bilge Kobas et al.",
                    "only_build_toc_files": True,
                    "parse": {"myst_enable_extensions": ["colon_fence", "linkify"]},
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )

    # Copy bib into book/ so later bibliography blocks can use a stable relative path
    bib_src = REPO / BIB_NAME
    bib_dst = BOOK / BIB_NAME
    if bib_src.exists() and not bib_dst.exists():
        bib_dst.write_bytes(bib_src.read_bytes())


def maybe_add_per_page_bibliography(md_text: str, level_up: str = "../") -> str:
    """
    (Optional) Append a per-page bibliography listing only cited entries.
    Requires later citation conversion to MyST {cite}`...` and sphinx bib config.
    """
    if not ADD_PER_PAGE_BIB:
        return md_text

    if "```{bibliography}" in md_text:
        return md_text

    block = (
        "\n\n---\n\n"
        "## References\n\n"
        f"```{{bibliography}} {level_up}{BIB_NAME}\n"
        ":cited:\n"
        ":style: unsrt\n"
        "```\n"
    )
    return md_text.rstrip() + block


def write_book(front: str, chapters):
    clean_generated_content()

    # Root landing page
    root_index = CONTENT / "index.md"
    title = "# WHY WE MEASURE WHAT, HOW, AND WHERE\n"
    subtitle = "Methods for human thermal physiology experiments in built environment studies\n"
    body = f"{front}\n" if front else ""
    root_index.write_text(f"{title}\n{subtitle}\n\n{body}", encoding="utf-8")

    toc = {"format": "jb-book", "root": "content/index", "chapters": []}

    for ch in chapters:
        h1 = ch["h1"]
        ch_slug = slugify(h1, lowercase=True)
        ch_dir = CONTENT / ch_slug
        ch_dir.mkdir(parents=True, exist_ok=True)

        # Chapter landing page
        ch_index = ch_dir / "index.md"
        intro = ch["intro"].strip()
        ch_index.write_text(f"# {h1}\n\n{intro}\n" if intro else f"# {h1}\n", encoding="utf-8")

        ch_entry = {"file": f"content/{ch_slug}/index"}

        if ch["pages"]:
            ch_entry["sections"] = []

        for page in ch["pages"]:
            h2 = page["h2"]
            page_slug = slugify(h2, lowercase=True)
            page_path = ch_dir / f"{page_slug}.md"

            md_body = page["body"]
            md_body = maybe_add_per_page_bibliography(md_body, level_up="../")

            page_path.write_text(md_body, encoding="utf-8")
            ch_entry["sections"].append({"file": f"content/{ch_slug}/{page_slug}"})

        toc["chapters"].append(ch_entry)

    (BOOK / "_toc.yml").write_text(yaml.safe_dump(toc, sort_keys=False), encoding="utf-8")


def main():
    if not IN_MD.exists():
        raise FileNotFoundError(f"Missing input markdown: {IN_MD}")

    ensure_jupyterbook_scaffold()

    raw = IN_MD.read_text(encoding="utf-8")
    front, rest = extract_front_matter(raw)
    chapters = split_into_chapters(rest)

    write_book(front, chapters)

    print("✅ Step 2 complete.")
    print(f"Generated book sources at: {BOOK}")
    print("Next:")
    print(f"  cd {BOOK}")
    print("  jupyter-book build .")


if __name__ == "__main__":
    main()