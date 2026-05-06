import subprocess

author = "Bilge Kobas et al."
project = "WHY WE MEASURE WHAT, HOW, AND WHERE"

def get_git_year():
    try:
        year = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=format:%Y"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
        return year
    except Exception:
        return "2026"  # fallback

START_YEAR = "2023"
year = get_git_year()

if year == START_YEAR:
    copyright = f"{year}, {author}"
else:
    copyright = f"{START_YEAR}–{year}, {author}"