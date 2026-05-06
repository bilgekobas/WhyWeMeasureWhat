# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path, PurePosixPath
from typing import List, Dict, Tuple, Optional

import pypandoc
import yaml
from slugify import slugify

DOCX_PATH = Path("WhyWeMeasureWhat_v04.docx")
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets"
ASSETS_IMG_DIR = ASSETS_DIR / "img"
ASSETS_JS_DIR = ASSETS_DIR / "js"
ASSETS_STYLES_DIR = ASSETS_DIR / "styles"
FULL_MD = DOCS_DIR / "_full.md"


# -----------------------------
# Basic IO / setup
# -----------------------------
def ensure_dirs() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_IMG_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_JS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_STYLES_DIR.mkdir(parents=True, exist_ok=True)


def require_inputs() -> None:
    if not DOCX_PATH.exists():
        raise FileNotFoundError(f"Missing {DOCX_PATH.resolve()}")


def clean_generated_docs(keep_assets: bool = True) -> None:
    """Delete everything under docs/ except assets/ (assets are user-managed)."""
    if not DOCS_DIR.exists():
        return
    for child in DOCS_DIR.iterdir():
        if keep_assets and child.name == "assets":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            try:
                child.unlink()
            except OSError:
                pass


# -----------------------------
# Pandoc conversion + media normalization
# -----------------------------
def run_pandoc_docx_to_md() -> None:
    extra_args = [
        "--wrap=none",
        f"--extract-media={ASSETS_IMG_DIR.as_posix()}",
        "--standalone",
    ]
    md = pypandoc.convert_file(
        DOCX_PATH.as_posix(),
        to="gfm",
        format="docx",
        extra_args=extra_args,
    )
    FULL_MD.write_text(md, encoding="utf-8")


def normalize_media_paths() -> None:
    """
    Pandoc sometimes extracts into docs/assets/img/media/.
    Move those up one level and rewrite references in _full.md.
    """
    media_dir = ASSETS_IMG_DIR / "media"
    if media_dir.exists() and media_dir.is_dir():
        for p in media_dir.iterdir():
            if p.is_file():
                shutil.move(p.as_posix(), (ASSETS_IMG_DIR / p.name).as_posix())
        try:
            media_dir.rmdir()
        except OSError:
            pass

        txt = FULL_MD.read_text(encoding="utf-8")
        txt = txt.replace("assets/img/media/", "assets/img/")
        txt = txt.replace("./assets/img/media/", "./assets/img/")
        FULL_MD.write_text(txt, encoding="utf-8")


# -----------------------------
# Text cleanup helpers
# -----------------------------
def safe_slug(s: str) -> str:
    return slugify(s) or "section"


def strip_word_bookmark_links(md_text: str) -> str:
    """Remove Pandoc-preserved Word bookmark anchors like #_Toc123 or #_Ref456."""
    md_text = re.sub(r"\[([^\]]+)\]\(#_Toc[0-9]+\)", r"\1", md_text)
    md_text = re.sub(r"\[([^\]]+)\]\(#_Ref[0-9]+\)", r"\1", md_text)
    md_text = re.sub(r"\[([^\]]+)\]\(#_[A-Za-z0-9]+\)", r"\1", md_text)
    return md_text


def strip_word_toc_from_md(md_text: str) -> str:
    """
    Remove Word-exported TOC blocks that look like a contiguous run of link-only lines near the top.
    """
    lines = md_text.splitlines()
    toc_line_re = re.compile(r'^\s*\[.+\]\(.+\)\s*$')

    out: List[str] = []
    i = 0
    while i < len(lines):
        if toc_line_re.match(lines[i]) and i < 250:
            j = i
            while j < len(lines) and (toc_line_re.match(lines[j]) or lines[j].strip() == ""):
                j += 1
            i = j
            continue
        out.append(lines[i])
        i += 1

    return "\n".join(out).lstrip("\n")


def promote_first_h2_to_h1(page_md: str) -> str:
    """
    In H2 pages, Pandoc produces "## Title" at the top.
    Convert ONLY the first occurrence to "# Title" so the page has a proper title.
    """
    return re.sub(r"(?m)^\s*##\s+", "# ", page_md, count=1)


def drop_duplicate_leading_heading(page_md: str) -> str:
    """
    Fix cases where Word contains a redundant heading immediately after the promoted title, e.g.

      # Core body temperature
      ## Core body temperature

    Drop that second one (and any immediate blank line after it).
    """
    # Extract first H1
    m = re.search(r"(?m)^\s*#\s+(.+?)\s*$", page_md)
    if not m:
        return page_md
    title = re.escape(m.group(1).strip())
    # Remove an immediate H2 with same text
    page_md = re.sub(
        rf"(?ms)^\s*#\s+{title}\s*\n\s*##\s+{title}\s*\n",
        lambda mm: re.search(r"(?ms)^\s*#\s+(.+?)\s*\n", mm.group(0)).group(0),
        page_md,
        count=1,
    )
    # If the lambda trick is too clever, do a simpler safe pass:
    page_md = re.sub(rf"(?m)^\s*##\s+{title}\s*$\n?", "", page_md, count=1)
    return page_md


# -----------------------------
# Splitting: H1 -> (intro, H2 pages)
# -----------------------------
def split_by_h1(md_text: str) -> List[Tuple[str, str]]:
    parts = re.split(r"(?m)^(# .+)$", md_text)
    front = parts[0].strip()
    pairs: List[Tuple[str, str]] = []

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        title = heading[2:].strip()
        body = (heading + "\n" + content).strip()

        if front and not pairs:
            body = front + "\n\n" + body

        pairs.append((title, body))

    return pairs


def split_h1_into_intro_and_h2pages(h1_body: str) -> tuple[str, List[Tuple[str, str]]]:
    """
    Given an H1 section markdown that starts with '# Title', return:
      (intro_text_between_h1_and_first_h2, list_of_h2_sections_as_(h2_title, h2_block_starting_with_##))

    IMPORTANT: we do NOT prepend intro into the first H2 page, because intro becomes index.md.
    """
    # Remove the first H1 line
    body_wo_h1 = re.sub(r"(?m)^\s*# .+\n", "", h1_body, count=1).strip()

    # Find the first H2
    m_first = re.search(r"(?m)^\s*##\s+.+$", body_wo_h1)
    if not m_first:
        return body_wo_h1.strip(), []

    intro = body_wo_h1[: m_first.start()].strip()
    rest = body_wo_h1[m_first.start() :].rstrip()

    # Split rest into H2 blocks
    h2_blocks = re.split(r"(?m)^(## .+)$", rest)
    pairs: List[Tuple[str, str]] = []
    for i in range(1, len(h2_blocks), 2):
        h2_heading = h2_blocks[i].strip()
        h2_content = h2_blocks[i + 1] if i + 1 < len(h2_blocks) else ""
        h2_title = h2_heading[3:].strip()
        h2_md = (h2_heading + "\n" + h2_content).strip()
        pairs.append((h2_title, h2_md))

    return intro, pairs


# -----------------------------
# Link rewriting
# -----------------------------
def rewrite_md_links_across_folders(docs_dir: Path) -> None:
    """
    Rewrite local markdown links like '(05_01_mean-skin-temperature-formulas.md#anchor)'
    so they point to the correct relative path across generated folders.
    """
    md_files = [p for p in docs_dir.rglob("*.md") if p.name != "_full.md"]

    basename_to_rel: Dict[str, str] = {}
    for p in md_files:
        basename_to_rel[p.name] = p.relative_to(docs_dir).as_posix()

    link_re = re.compile(r"\]\(([^)]+)\)")

    for p in md_files:
        text = p.read_text(encoding="utf-8")
        changed = False

        def repl(m: re.Match) -> str:
            nonlocal changed
            target = m.group(1).strip()

            if "://" in target or target.startswith("mailto:") or target.startswith("#"):
                return m.group(0)

            if "#" in target:
                path_part, anchor = target.split("#", 1)
                anchor = "#" + anchor
            else:
                path_part, anchor = target, ""

            path_part = path_part.strip().replace("\\", "/")
            if not path_part.lower().endswith(".md"):
                return m.group(0)

            base = Path(path_part).name
            real_rel = basename_to_rel.get(base)
            if not real_rel:
                return m.group(0)

            from_dir = p.parent
            real_abs = docs_dir / real_rel
            rel_path = Path(os.path.relpath(real_abs, from_dir)).as_posix()

            new_target = f"{rel_path}{anchor}"
            if new_target != target:
                changed = True
            return f"]({new_target})"

        new_text = link_re.sub(repl, text)
        if changed:
            p.write_text(new_text, encoding="utf-8")


def rewrite_image_paths_to_root(docs_dir: Path) -> None:
    """
    Fix broken image links after moving pages into folders.

    Goal: ALWAYS reference images under /assets/img/... regardless of the current page depth.

    We rewrite both markdown images:
      ![alt](assets/img/x.png) or ![alt](docs/assets/img/x.png) or ![alt](../assets/img/x.png)
    and HTML images:
      <img src="assets/img/x.png">

    into:
      ![alt](/assets/img/x.png)
      <img src="/assets/img/x.png">
    """
    md_files = [p for p in docs_dir.rglob("*.md") if p.name != "_full.md"]

    # Markdown image/link targets in parentheses
    paren_re = re.compile(r"(?P<prefix>!\[[^\]]*\]\()(?P<url>[^)]+)(?P<suffix>\))")
    # HTML img src
    html_re = re.compile(r'(<img\s+[^>]*src=["\'])([^"\']+)(["\'])', re.IGNORECASE)

    def fix_url(u: str) -> str:
        u2 = u.strip().replace("\\", "/")
        # ignore external
        if "://" in u2 or u2.startswith("data:"):
            return u
        # remove leading ./ or ../ segments
        u2 = re.sub(r"^(?:\./)+", "", u2)
        u2 = re.sub(r"^(?:\.\./)+", "", u2)
        # remove an accidental leading docs/
        u2 = re.sub(r"^docs/", "", u2)
        # normalize to assets/img if it contains it anywhere
        m = re.search(r"(assets/img/.*)$", u2)
        if m:
            return "/" + m.group(1)
        return u  # leave untouched

    for p in md_files:
        text = p.read_text(encoding="utf-8")

        def repl_img(m: re.Match) -> str:
            return f"{m.group('prefix')}{fix_url(m.group('url'))}{m.group('suffix')}"

        text2 = paren_re.sub(repl_img, text)

        def repl_html(m: re.Match) -> str:
            return f"{m.group(1)}{fix_url(m.group(2))}{m.group(3)}"

        text2 = html_re.sub(repl_html, text2)

        if text2 != text:
            p.write_text(text2, encoding="utf-8")


# -----------------------------
# Citations: make [n] clickable + reference anchors
# -----------------------------
CITE_GROUP_RE = re.compile(r"\[(\s*\d+(?:\s*[-–]\s*\d+)?(?:\s*,\s*\d+(?:\s*[-–]\s*\d+)?)*)\s*\]")

def add_reference_anchors(ref_md: str) -> str:
    """
    Add <span id="ref-N"></span> before ordered-list items in the references page.

    Pandoc typically emits:
      1. Author...
      2. Author...

    We transform into:
      1. <span id="ref-1"></span> Author...
    """
    def repl(m: re.Match) -> str:
        n = m.group(1)
        rest = m.group(2)
        return f"{n}. <span id=\"ref-{n}\"></span>{rest}"
    return re.sub(r"(?m)^\s*(\d+)\.\s+(.*)$", repl, ref_md)


def link_citations(md: str, references_page_url: str) -> str:
    """
    Convert citation groups like [12] or [4, 9, 100] or [12–15] into clickable anchors.

    We output <a class="citation" ...>[12]</a> etc.

    citations.js can intercept clicks to show a popup (so it won't navigate away).
    """
    def expand_range(a: int, b: int) -> List[int]:
        if b < a:
            return [a]
        # cap to avoid accidents
        if b - a > 200:
            return [a, b]
        return list(range(a, b + 1))

    def render_one(n: int) -> str:
        href = f"{references_page_url}#ref-{n}"
        return f'<a class="citation" href="{href}" data-cite="{n}">[{n}]</a>'

    def repl(m: re.Match) -> str:
        inside = m.group(1)
        tokens = [t.strip() for t in inside.split(",")]
        rendered: List[str] = []
        for t in tokens:
            if not t:
                continue
            # normalize en-dash
            t = t.replace("–", "-")
            if "-" in t:
                a_s, b_s = [x.strip() for x in t.split("-", 1)]
                if a_s.isdigit() and b_s.isdigit():
                    nums = expand_range(int(a_s), int(b_s))
                    if len(nums) == 2 and nums[0] != nums[1] and (nums[1] - nums[0] > 200):
                        rendered.append(render_one(nums[0]) + "–" + render_one(nums[1]))
                    else:
                        rendered.append("–".join(render_one(x) for x in nums))
                    continue
            if t.isdigit():
                rendered.append(render_one(int(t)))
            else:
                # fallback: keep original bracket group
                return m.group(0)
        return ", ".join(rendered) if rendered else m.group(0)

    # Avoid touching markdown links like [text](...) by only replacing when it's a pure numeric bracket group.
    return CITE_GROUP_RE.sub(repl, md)


def apply_citation_linking(docs_dir: Path, references_rel: str) -> None:
    """
    - Add ref anchors in the references page
    - Link all numeric citations across all pages to those anchors
    """
    ref_path = docs_dir / references_rel
    if not ref_path.exists():
        return

    # MkDocs URL path for the references page (starts with /)
    references_page_url = "/" + references_rel.replace("\\", "/").replace(".md", "/")

    ref_md = ref_path.read_text(encoding="utf-8")
    ref_md2 = add_reference_anchors(ref_md)
    ref_path.write_text(ref_md2, encoding="utf-8")

    for p in docs_dir.rglob("*.md"):
        if p.name == "_full.md":
            continue
        md = p.read_text(encoding="utf-8")
        md2 = link_citations(md, references_page_url=references_page_url)
        if md2 != md:
            p.write_text(md2, encoding="utf-8")


# -----------------------------
# Page generation + mkdocs.yml
# -----------------------------
def write_chapter_folders_and_pages(h1_sections: List[Tuple[str, str]]) -> tuple[List[Dict[str, object]], Optional[str]]:
    """
    Returns:
      nav_items, references_rel_md (like '09_references/09_01_references.md' if found)
    """
    nav: List[Dict[str, object]] = []
    references_rel: Optional[str] = None

    clean_generated_docs(keep_assets=True)
    ensure_dirs()

    for h1_idx, (h1_title, h1_body_raw) in enumerate(h1_sections, start=1):
        h1_num = f"{h1_idx:02d}"
        folder_slug = safe_slug(h1_title)
        folder_name = f"{h1_num}_{folder_slug}"
        ch_dir = DOCS_DIR / folder_name
        ch_dir.mkdir(parents=True, exist_ok=True)

        h1_body = strip_word_toc_from_md(h1_body_raw).strip()

        intro, h2_pairs = split_h1_into_intro_and_h2pages(h1_body)

        # --- No H2 => single page (shows text directly; no empty Overview)
        if not h2_pairs:
            filename = f"{h1_num}_01_{safe_slug(h1_title)}.md"
            out_path = ch_dir / filename
            out_path.write_text(h1_body + "\n", encoding="utf-8")

            rel = PurePosixPath(f"{folder_name}/{filename}").as_posix()
            nav.append({f"{h1_num} {h1_title}": [rel]})

            if h1_title.strip().lower() == "references":
                references_rel = rel
            continue

        # --- Has H2 => index.md is landing page with intro text
        index_md = f"# {h1_title}\n\n"
        if intro.strip():
            index_md += intro.strip() + "\n"
        index_out = ch_dir / "index.md"
        index_out.write_text(index_md.rstrip() + "\n", encoding="utf-8")

        pages_for_nav: List[Dict[str, str]] = [{"Overview": PurePosixPath(f"{folder_name}/index.md").as_posix()}]

        for h2_idx, (h2_title, h2_md) in enumerate(h2_pairs, start=1):
            h2_num = f"{h1_num}_{h2_idx:02d}"
            filename = f"{h2_num}_{safe_slug(h2_title)}.md"
            out_path = ch_dir / filename

            page_md = strip_word_toc_from_md(h2_md).strip()
            page_md = promote_first_h2_to_h1(page_md)
            page_md = drop_duplicate_leading_heading(page_md)

            out_path.write_text(page_md + "\n", encoding="utf-8")
            rel = PurePosixPath(f"{folder_name}/{filename}").as_posix()
            pages_for_nav.append({h2_title: rel})

            if h1_title.strip().lower() == "references" and references_rel is None:
                references_rel = rel

        nav.append({f"{h1_num} {h1_title}": pages_for_nav})

    # Cross-folder md link fixes + image path fixes
    rewrite_md_links_across_folders(DOCS_DIR)
    rewrite_image_paths_to_root(DOCS_DIR)

    return nav, references_rel


def write_root_index() -> None:
    (DOCS_DIR / "index.md").write_text(
        "# Why we measure what\n\n"
        "Living long-form manuscript (Word → Markdown → MkDocs).\n",
        encoding="utf-8",
    )


def write_mkdocs_yml(nav_items: List[Dict[str, object]]) -> None:
    """
    Notes on navigation:
      - With 'navigation.tabs' enabled, Material's sidebar shows only the active tab's section.
        That's core theme behavior; to have a single global sidebar you must disable tabs.
    """
    mkdocs = {
        "site_name": "Why we measure what, how, and where",
        "exclude_docs": "_full.md",
        "theme": {
            "name": "material",
            "features": [
                "navigation.tabs",
                "navigation.sections",
                "navigation.expand",
                "toc.integrate",
            ],
        },
        "markdown_extensions": [
            "footnotes",
            "admonition",
            "tables",
            {"toc": {"permalink": True, "toc_depth": 3}},
        ],
        "extra_css": [
            "assets/styles/extra.css",
        ],
        "extra_javascript": [
            "assets/js/citations.js",
        ],
        "nav": [{"Home": "index.md"}] + nav_items,
    }
    Path("mkdocs.yml").write_text(
        yaml.safe_dump(mkdocs, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def main() -> None:
    ensure_dirs()
    require_inputs()

    run_pandoc_docx_to_md()
    normalize_media_paths()

    md = FULL_MD.read_text(encoding="utf-8")
    md = strip_word_bookmark_links(md)

    h1_sections = split_by_h1(md)
    if not h1_sections:
        raise RuntimeError(
            "No H1 (# ...) headings found after conversion. "
            "Check that your Word chapter titles are styled as Heading 1."
        )

    nav_items, references_rel = write_chapter_folders_and_pages(h1_sections)
    write_root_index()
    write_mkdocs_yml(nav_items)

    # Citation linking pass (after mkdocs.yml exists, pages exist)
    if references_rel:
        apply_citation_linking(DOCS_DIR, references_rel=references_rel)

    # Final pass: image paths again (citation linking shouldn't affect, but safe)
    rewrite_image_paths_to_root(DOCS_DIR)

    print("Done.")
    print(f"- Full markdown: {FULL_MD}")
    print(f"- Pages written under: {DOCS_DIR}")
    print(f"- Images: {ASSETS_IMG_DIR}")
    print("- Preview: mkdocs serve")


if __name__ == "__main__":
    main()
