from pathlib import Path
import textwrap

try:
    import yaml
except ImportError as e:
    raise SystemExit("Missing dependency: pyyaml. Install with: pip install pyyaml") from e

REPO = Path(r"C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git")
YAML_IN = REPO / "book" / "contributors.yml"

# ONLY this file will be overwritten by this script:
OUT_MD = REPO / "book" / "content" / "contribution" / "list-of-contributors.md"

CSS = """
<style>
.contributors-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
gap:1.4rem;
margin-top:1.5rem;
}
.contributor-card{
border:1px solid #ddd;
border-radius:10px;
padding:1.2rem;
background:#fff;
display:flex;
flex-direction:column;
gap:0.6rem;
}
.contributor-header{
display:flex;
align-items:center;
gap:0.8rem;
}
.contributor-photo{
width:54px;
height:54px;
border-radius:50%;
object-fit:cover;
border:1px solid #ddd;
}
.contributor-name{
font-size:1.05rem;
font-weight:600;
}
.contributor-role{
font-size:0.8rem;
background:#f0f0f0;
padding:2px 6px;
border-radius:4px;
display:inline-block;
margin-top:3px;
margin-right:6px;
}
.contributor-affiliation{
font-size:0.88rem;
color:#666;
}
.contributor-links a{
font-size:0.9rem;
margin-right:0.7rem;
text-decoration:none;
}
.contributor-links a:hover{
text-decoration:underline;
}
details.bio{
font-size:0.9rem;
line-height:1.4;
margin-top:0.3rem;
}
details.bio summary{
cursor:pointer;
font-weight:500;
}
</style>
""".strip()

def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
    )

def render_card(person: dict) -> str:
    name = esc(person.get("name", ""))
    affiliation = esc(person.get("affiliation", ""))
    roles = person.get("roles", []) or []
    photo = esc(person.get("photo", "../../assets/contributors/placeholder.jpg"))
    links = person.get("links", {}) or {}
    bio = esc(person.get("bio", "")).strip()

    role_html = " ".join(f'<span class="contributor-role">{esc(r)}</span>' for r in roles)

    links_html = ""
    if links:
        links_html = '<div class="contributor-links">' + " ".join(
            f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in links.items() if url
        ) + "</div>"

    bio_html = ""
    if bio:
        bio_html = f"""
<details class="bio">
<summary>Short biography</summary>

{bio}

</details>
""".strip()

    return f"""
<div class="contributor-card">

<div class="contributor-header">
  <img class="contributor-photo" src="{photo}" alt="Photo of {name}">
  <div>
    <div class="contributor-name">{name}</div>
    <div>{role_html}</div>
  </div>
</div>

<div class="contributor-affiliation">{affiliation}</div>

{links_html}

{bio_html}

</div>
""".strip()

def main():
    if not YAML_IN.exists():
        raise FileNotFoundError(f"Missing: {YAML_IN}")

    data = yaml.safe_load(YAML_IN.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("contributors.yml must be a list of contributor objects")

    cards = "\n\n".join(render_card(p) for p in data)

    body = f"""\
# List of contributors

This page lists contributors to the *Why We Measure What, How, and Where* living document. 

{CSS}

<div class="contributors-grid">

{cards}

</div>
"""

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(textwrap.dedent(body).strip() + "\n", encoding="utf-8")
    print(f"✅ Wrote contributors page: {OUT_MD}")

if __name__ == "__main__":
    main()