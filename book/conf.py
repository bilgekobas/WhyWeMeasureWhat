import subprocess

author = "Bilge Kobas et al."
project = "Why We Measure What, How, and Where"

def get_git_year():
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=format:%Y"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
    except Exception:
        return "2026"

START_YEAR = "2026"
year = get_git_year()

if year == START_YEAR:
    copyright = f"{year}, {author} · CC BY 4.0"
else:
    copyright = f"{START_YEAR}–{year}, {author} · CC BY 4.0"