
"""
Auto-link glossary terms across a Jupyter Book / MyST Markdown project.

This version includes curated aliases generated from the controlled vocabulary
and glossary. Aliases allow shorter or adjacent terms such as "anterior",
"posterior", "DLMO", "CO", or "skin blood flow" to link to the relevant
glossary entry.

Usage, from the book folder:
    python auto_link_glossary_terms.py
"""

from __future__ import annotations

import re
from pathlib import Path

BOOK_DIR = Path(".")
GLOSSARY_RELATIVE_PATH = Path("content/terminological-alignment/controlled-vocabulary-and-glossary.md")

EXCLUDE_DIRS = {"_build", ".jupyter_cache", ".ipynb_checkpoints", "_static", "assets"}
EXCLUDE_FILES = {"references.md", "bibliography.md"}

LINK_FIRST_OCCURRENCE_ONLY = True
MAX_LINKS_PER_FILE = 30

# First run should be True. Switch to False only after checking output.
DRY_RUN = False

MANUAL_ALIASES = {'Acclimation': ['heat acclimation'],
 'Acclimatization': ['heat acclimatization', 'acclimatisation', 'heat acclimatisation'],
 'Allostatic load': ['allostatic burden'],
 'Artefact': ['artifact', 'artefacts', 'artifacts'],
 'Arterial pressure': ['blood pressure', 'arterial blood pressure'],
 'Arteriovenous anastomoses (AVA)': ['AVA',
                                     'AVAs',
                                     'arteriovenous anastomosis',
                                     'vascular shunt',
                                     'vascular shunts'],
 'Autonomic heat-loss drive': ['heat-loss drive', 'heat loss drive'],
 'Autonomic regulation': ['autonomic control'],
 'Autonomic thermoeffector output': ['thermoeffector output'],
 'Baroreflex': ['baroreflex control', 'baroreflex response'],
 'Between-subject design': ['between-subjects design', 'between-participant design'],
 'Block design': ['blocking', 'blocked design'],
 'Body heat balance': ['heat balance', 'body thermal balance'],
 'Calorimetry (direct and indirect)': ['calorimetry', 'direct calorimetry', 'indirect calorimetry'],
 'Cardiac output (CO)': ['cardiac output'],
 'Cardiovascular regulation': ['cardiovascular control'],
 'Cardiovascular workload': ['cardiovascular load', 'circulatory workload'],
 'Central autonomic regulation': ['central autonomic control'],
 'Cholinergic pathways': ['cholinergic pathway',
                          'sympathetic cholinergic pathways',
                          'cholinergic activation'],
 'Chronotropic effort': ['chronotropic response', 'chronotropic load'],
 'Circadian rhythm': ['circadian rhythms', 'circadian timing'],
 'Cognitive or mental workload': ['cognitive workload', 'mental workload'],
 'Cross-over design': ['crossover design', 'cross-over study', 'crossover study'],
 'Cutaneous blood flow': ['skin blood flow', 'cutaneous perfusion', 'skin perfusion'],
 'Dim-light melatonin onset (DLMO)': ['DLMO',
                                      'dim light melatonin onset',
                                      'dim-light melatonin onset'],
 'Distal–proximal gradient (DPG)': ['distal-proximal gradient',
                                    'distal–proximal gradient',
                                    'distal proximal gradient',
                                    'DPG'],
 'Effective evaporation': ['evaporative efficiency', 'effective evaporative cooling'],
 'Effector activation thresholds': ['activation threshold',
                                    'activation thresholds',
                                    'effector threshold',
                                    'effector thresholds',
                                    'thermoeffector threshold',
                                    'thermoeffector thresholds'],
 'Energy expenditure (EE)': ['energy expenditure'],
 'Feedback and feed-forward control': ['feedback control',
                                       'feed-forward control',
                                       'feedforward control',
                                       'feedback and feedforward control'],
 'Heat storage (S)': ['heat storage'],
 'Heat-balance equation': ['heat balance equation', 'body heat-balance equation'],
 'Hormonal modulation': ['endocrine modulation', 'hormonal state'],
 'Hypothalamic thermoregulatory circuits': ['hypothalamic circuits',
                                            'hypothalamic thermoregulatory circuit',
                                            'hypothalamic thermoregulation'],
 'Hypothalamic–pituitary–adrenal (HPA) axis': ['HPA axis',
                                               'hypothalamic-pituitary-adrenal axis',
                                               'hypothalamic–pituitary–adrenal axis'],
 'Inclusion/Exclusion criteria': ['inclusion criteria',
                                  'exclusion criteria',
                                  'eligibility criteria',
                                  'inclusion and exclusion criteria'],
 'Interindividual variability': ['inter-individual variability',
                                 'between-person variability',
                                 'between-subject variability',
                                 'individual variability'],
 'Interthreshold zone': ['inter-threshold zone'],
 'Laterality (ipsilateral, contralateral, bilateral, unilateral)': ['laterality',
                                                                    'ipsilateral',
                                                                    'contralateral',
                                                                    'bilateral',
                                                                    'unilateral'],
 'Longitudinal position (proximal, distal)': ['longitudinal position', 'proximal', 'distal'],
 'Normalization': ['normalisation', 'normalization'],
 'PICOT': ['PICO', 'PICOT framework'],
 'Peripheral circulation': ['peripheral blood flow', 'peripheral perfusion'],
 'Peripheral resistance': ['vascular resistance', 'total peripheral resistance'],
 'Physiological signal': ['physiological signals'],
 'Proxy measure': ['proxy', 'surrogate measure', 'indirect measure'],
 'Respiratory sinus arrhythmia': ['RSA'],
 'Response time': ['time constant', 'response lag', 'physiological lag', 'sensor lag'],
 'Sample size': ['sample sizes', 'effective sample size'],
 'Sampling rate': ['sampling frequency', 'acquisition rate'],
 'Spatial orientation (anterior, posterior, medial, lateral, palmar, dorsal)': ['anterior',
                                                                                'posterior',
                                                                                'medial',
                                                                                'lateral',
                                                                                'palmar',
                                                                                'dorsal'],
 'Sympathetic and parasympathetic outflow': ['sympathetic outflow',
                                             'parasympathetic outflow',
                                             'autonomic outflow'],
 'Sympathetic load': ['sympathetic activation', 'sympathetic burden'],
 'Thermal history': ['prior thermal exposure', 'previous thermal exposure', 'exposure history'],
 'Thermal inertia': ['thermal lag'],
 'Thermal steady state': ['steady state', 'thermal steady-state', 'steady-state'],
 'Thermoeffector': ['thermoeffectors'],
 'Thermoeffector gain': ['thermoregulatory gain', 'effector gain'],
 'Thermogenesis': ['heat production'],
 'Thermoneutral zone': ['thermo-neutral zone', 'TNZ'],
 'Thermoregulatory control signal': ['control signal', 'thermoregulatory drive'],
 'Thermoregulatory set-point': ['set-point', 'set point', 'thermoregulatory set point'],
 'Time-of-day effect': ['time of day effect', 'time-of-day effects', 'time of day effects'],
 'Transient thermal response': ['transient response', 'dynamic thermal response'],
 'Vagal influences': ['vagal influence', 'vagal modulation', 'parasympathetic modulation'],
 'Vascular tone': ['baseline vascular tone'],
 'Vasoconstriction': ['vasoconstrictor response', 'cutaneous vasoconstriction'],
 'Vasodilation': ['vasodilatory response', 'cutaneous vasodilation'],
 'Vasomotor control': ['vasomotion',
                       'vasomotor response',
                       'vasomotor responses',
                       'cutaneous vasomotor control'],
 'Within-subject design': ['within-subjects design',
                           'within-participant design',
                           'repeated-measures design']}

ENTRY_RE = re.compile(
    r"^\((label-[^)]+)\)=\s*\n:::\{dropdown\}\s*(.+?)\s*$",
    re.MULTILINE,
)

def extract_glossary_entries(glossary_text: str) -> list[tuple[str, str]]:
    entries = []
    for label, title in ENTRY_RE.findall(glossary_text):
        title = re.sub(r"\s+", " ", title.strip())
        if title:
            entries.append((title, label))
    entries.sort(key=lambda item: len(item[0]), reverse=True)
    return entries

def aliases_for_title(title: str) -> list[str]:
    aliases = [title]
    no_parentheses = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()
    if no_parentheses and no_parentheses != title:
        aliases.append(no_parentheses)
    aliases.extend(MANUAL_ALIASES.get(title, []))
    aliases = [a.strip() for a in aliases if a and a.strip()]
    return sorted(set(aliases), key=len, reverse=True)

def split_fenced_code_blocks(text: str) -> list[tuple[str, bool]]:
    fence_re = re.compile(r"(^[ \t]*(```|~~~).*$)", re.MULTILINE)
    parts = []
    pos = 0
    in_code = False
    start = 0
    for match in fence_re.finditer(text):
        fence_start, fence_end = match.start(), match.end()
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

def protected_spans(chunk: str) -> list[tuple[int, int]]:
    patterns = [
        r"\{ref\}`[^`]+`",
        r"\{cite[^}]*\}`[^`]+`",
        r"\[[^\]]+\]\([^)]+\)",
        r"!\[[^\]]*\]\([^)]+\)",
        r"https?://[^\s)]+",
        r"`[^`\n]+`",
        r"^\s*#{1,6}\s+.*$",
        r"^\s*\.\.\s+.*$",
        r"^\s*:::\{.*$",
        r"^\s*\([^)]+\)=\s*$",
        r"^\s*\|.*\|\s*$",
        r"^\s*:\w+:.*$",
    ]
    spans = []
    for pattern in patterns:
        for m in re.finditer(pattern, chunk, re.MULTILINE):
            spans.append((m.start(), m.end()))
    return merge_spans(spans)

def is_inside_spans(index: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)

def make_term_pattern(alias: str) -> re.Pattern[str]:
    escaped = re.escape(alias)
    return re.compile(rf"(?<![\w`])({escaped})(?![\w`])", flags=re.IGNORECASE)

def link_terms_in_chunk(
    chunk: str,
    entries: list[tuple[str, str]],
    already_linked_terms: set[str],
    remaining_link_budget: int | None,
) -> tuple[str, int]:
    protected = protected_spans(chunk)
    total_links = 0

    for title, label in entries:
        if remaining_link_budget is not None and total_links >= remaining_link_budget:
            break
        if LINK_FIRST_OCCURRENCE_ONLY and title.lower() in already_linked_terms:
            continue

        for alias in aliases_for_title(title):
            pattern = make_term_pattern(alias)

            def replace_one(match: re.Match[str]) -> str:
                nonlocal total_links, protected
                if remaining_link_budget is not None and total_links >= remaining_link_budget:
                    return match.group(0)
                if is_inside_spans(match.start(), protected):
                    return match.group(0)
                visible_text = match.group(1)
                total_links += 1
                return f"{{ref}}`{visible_text} <{label}>`"

            new_chunk, n = pattern.subn(replace_one, chunk, count=1)
            if n and new_chunk != chunk:
                chunk = new_chunk
                already_linked_terms.add(title.lower())
                protected = protected_spans(chunk)
                break

    return chunk, total_links

def link_terms_in_text(text: str, entries: list[tuple[str, str]]) -> tuple[str, int]:
    parts = split_fenced_code_blocks(text)
    new_parts = []
    total_links = 0
    already_linked_terms = set()

    for chunk, is_code in parts:
        if is_code:
            new_parts.append(chunk)
            continue
        remaining = None
        if MAX_LINKS_PER_FILE is not None:
            remaining = max(MAX_LINKS_PER_FILE - total_links, 0)
        linked_chunk, n_links = link_terms_in_chunk(chunk, entries, already_linked_terms, remaining)
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
        raise RuntimeError("No glossary entries found.")

    print(f"Found {len(entries)} glossary entries.")
    print(f"Glossary file: {glossary_path}")
    print(f"DRY_RUN = {DRY_RUN}")

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
    print("Dry run complete." if DRY_RUN else "Done.")
    print(f"Files changed: {changed_files}")
    print(f"Links added: {total_links}")

    if not DRY_RUN:
        print()
        print("Next steps:")
        print("1. Inspect the changed markdown files.")
        print("2. Run: jupyter-book clean .")
        print("3. Run: jupyter-book build .")

if __name__ == "__main__":
    main()
