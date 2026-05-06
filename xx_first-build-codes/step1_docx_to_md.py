# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:43:10 2026

@author: kobas
"""

import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git")
DOCX = REPO / "WhyWeMeasureWhat_v04_static.docx"

OUT_DIR = REPO / "_build_intermediate"
OUT_MD = OUT_DIR / "WhyWeMeasureWhat_v04_full.md"

def main():
    if not DOCX.exists():
        raise FileNotFoundError(f"Cannot find DOCX at: {DOCX}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(DOCX),
        "-f", "docx",
        "-t", "markdown",
        "--wrap=none",
        "--markdown-headings=atx",
        "--extract-media", str(OUT_DIR / "media"),
        "-o", str(OUT_MD),
    ]

    subprocess.run(cmd, check=True)
    print(f"✅ Wrote: {OUT_MD}")

if __name__ == "__main__":
    main()