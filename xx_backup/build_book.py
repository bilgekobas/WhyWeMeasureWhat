# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:32:02 2026

@author: kobas
"""

import os
import re
import subprocess
from pathlib import Path

import yaml
from slugify import slugify


REPO = Path(r"C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git")
DOCX = REPO / "WhyWeMeasureWhat_v04.docx"
BIB  = REPO / "WhyWeMeasure_v04.bib"

# JupyterBook content root (keep book sources separate from repo root clutter)
BOOK = REPO / "book"
CONTENT = BOOK / "content"


PANDOC_FROM = "docx"
# Pandoc markdown; we keep it conservative and do MyST-specific additions ourselves.
PANDOC_TO = "markdown"


def run_pandoc_docx_to_md(docx_path: Path, out_md: Path) -> None:
    """
    Convert DOCX to Markdown using pandoc.
    """
    out_md.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(docx_path),
        "-f", PANDOC_FROM,
        "-t", PANDOC_TO,
        "--wrap=none",
        # Preserve heading structure as ATX (# ## ### ...)
        "--markdown-headings=atx",
        "-o", str(out_md),
    ]
    subprocess.run(cmd, check=True)


def split_by_headings(raw_md: str):
    """
    Split a markdown document into:
      - H1 chunks (each becomes a chapter folder with index.md)
      - Within each H1 chunk: H2 pages
      - H3+ remain inside the H2 page (anchors)
    Returns a nested structure:
      chapters = [
        {
          "h1": "TITLE",
          "intro": "text between H1 and first H2",
          "pages": [
            {"h2": "TITLE", "body": "...markdown..."},
            ...
          ]
        },
        ...
      ]
    """
    # Normalize line endings
    md = raw_md.replace("\r\n", "\n").replace("\r", "\n")

    # Find H1 headings
    h1_pattern = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
    h1_matches = list(h1_pattern.finditer(md))

    if not h1_matches:
        raise ValueError("No H1 headings (# ...) found in the converted markdown.")

    chapters = []
    for i, m in enumerate(h1_matches):
        h1_title = m.group(1).strip()
        start = m.end()
        end = h1_matches[i + 1].start() if i + 1 < len(h1_matches) else len(md)
        h1_block = md[start:end].strip("\n")

        # Split inside H1 by H2
        h2_pattern = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
        h2_matches = list(h2_pattern.finditer(h1_block))

        if not h2_matches:
            # Entire H1 is just a landing page
            chapters.append({"h1": h1_title, "intro": h1_block.strip(), "pages": []})
            continue

        intro = h1_block[:h2_matches[0].start()].strip("\n")

        pages = []
        for j, h2m in enumerate(h2_matches):
            h2_title = h2m.group(1).strip()
            p_start = h2m.end()
            p_end = h2_matches[j + 1].start() if j + 1 < len(h2_matches) else len(h1_block)
            body = h1_block[p_start:p_end].strip("\n")

            # Re-add the H2 heading at the top of each page
            page_md = f"# {h2_title}\n\n{body}\n"
            pages.append({"h2": h2_title, "body": page_md})

        chapters.append({"h1": h1_title, "intro": intro.strip(), "pages": pages})

    return chapters


def ensure_jupyterbook_scaffold():
    BOOK.mkdir(exist_ok=True)
    CONTENT.mkdir(parents=True, exist_ok=True)

    # Minimal JupyterBook config enabling citations/bibliography
    config = {
        "title": "WHY WE MEASURE WHAT, HOW, AND WHERE",
        "author": "Bilge Kobas et al.",
        "only_build_toc_files": True,
        "sphinx": {
            "config": {
                # Show deeper nav; exact behaviour depends on theme, but this is the right knob.
                "html_show_sourcelink": False,
                "bibtex_bibfiles": [str(BIB.relative_to(BOOK)).replace("\\", "/")],
            }
        },
        "parse": {
            "myst_enable_extensions": [
                "colon_fence",
                "dollarmath",
                "linkify",
            ]
        }
    }

    (BOOK / "_config.yml").write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")

    # Copy/ensure bib lives under BOOK so relative paths work cleanly
    bib_target = BOOK / BIB.name
    if not bib_target.exists():
        bib_target.write_bytes(BIB.read_bytes())


def add_per_page_bibliography(md_text: str) -> str:
    """
    Append a per-page bibliography that includes only citations used in that page.
    This relies on sphinxcontrib-bibtex's :cited: option exposed by MyST/JupyterBook.
    """
    bib_rel = f"../{BIB.name}"  # pages will live in content/<chapter>/... so ../ is correct
    block = (
        "\n\n---\n\n"
        "## References\n\n"
        "```{bibliography} " + bib_rel + "\n"
        ":cited:\n"
        ":style: unsrt\n"
        "```\n"
    )
    # Avoid duplicating if re-running build
    if "```{bibliography}" in md_text:
        return md_text
    return md_text.rstrip() + block


def write_book_files(chapters):
    # Clean content directory on rebuild (safe, since it is generated)
    if CONTENT.exists():
        for p in CONTENT.glob("*"):
            if p.is_dir():
                for q in p.rglob("*"):
                    if q.is_file():
                        q.unlink()
                for q in sorted(p.rglob("*"), reverse=True):
                    if q.is_dir():
                        q.rmdir()
                p.rmdir()
            elif p.is_file():
                p.unlink()

    CONTENT.mkdir(parents=True, exist_ok=True)

    toc = {"format": "jb-book", "root": "content/index", "chapters": []}

    # Root landing page
    root_index = CONTENT / "index.md"
    root_index.write_text(
        "# WHY WE MEASURE WHAT, HOW, AND WHERE\n\n"
        "Methods for Human Thermal Physiology Experiments in Built Environment Studies\n",
        encoding="utf-8"
    )

    for ch in chapters:
        h1 = ch["h1"]
        ch_slug = slugify(h1, lowercase=True)
        ch_dir = CONTENT / ch_slug
        ch_dir.mkdir(parents=True, exist_ok=True)

        # H1 landing page = chapter/index.md
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

            # Add per-page references that list only citations used on that page
            md_body = add_per_page_bibliography(md_body)

            page_path.write_text(md_body, encoding="utf-8")
            ch_entry["sections"].append({"file": f"content/{ch_slug}/{page_slug}"})

        toc["chapters"].append(ch_entry)

    (BOOK / "_toc.yml").write_text(yaml.safe_dump(toc, sort_keys=False), encoding="utf-8")


def main():
    ensure_jupyterbook_scaffold()

    # Step 1: DOCX -> single markdown (temporary)
    tmp_md = BOOK / "_tmp_full.md"
    run_pandoc_docx_to_md(DOCX, tmp_md)

    raw_md = tmp_md.read_text(encoding="utf-8")
    chapters = split_by_headings(raw_md)

    # Step 2: write structured book files + TOC
    write_book_files(chapters)

    # Cleanup
    tmp_md.unlink(missing_ok=True)

    print("Done.")
    print("Next:")
    print(f"  cd {BOOK}")
    print("  jupyter-book build .")


if __name__ == "__main__":
    main()