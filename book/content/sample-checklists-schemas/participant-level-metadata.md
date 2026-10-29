# Participant-level metadata

Participant-level metadata capture characteristics that are stable or slowly changing across the duration of a study. These variables describe each individual taking part in the experiment and provide the context needed to interpret physiological responses, account for relevant modifiers, and enable subgroup or meta-analytic work.

Each participant is represented by one row in a dedicated metadata table, with one column per field. As in the experiment-level schema, fields are grouped by topic (e.g., Demographics & Morphology, Health & Diagnoses, Lifestyle, Reproductive & Hormonal) and assigned to informal tiers indicating their importance:

- <u>Tier 1 -- Core:</u> Minimal information required in any thermal physiology experiment (e.g., age, sex at birth, height, weight, BMI, basic health status, habitual physical activity, key hormonal status).

- <u>Tier 2 -- Recommended:</u> Variables that strongly influence {ref}`thermoregulation <label-thermoregulation>` and improve interpretability, including body surface area, {ref}`thermal history <label-thermal-history>`, smoking and alcohol use, typical sleep timing, menstrual cycle characteristics, hormone therapies, thermosensitivity, and selected built-environment descriptors.

- <u>Tier 3 -- Specialised:</u> More detailed or study-specific attributes, such as body composition, occupation,  quality-of-life instruments, or vision/colour-vision assessments. These fields are optional but useful for specialised analyses or targeted protocols.

The participant metadata table can be implemented in a spreadsheet, REDCap form, or as structured CSV/TSV with accompanying JSON (e.g., a participants.tsv + participants.json pair following BIDS conventions).


:::{table} Example participant-level metadata schema, including groups, field definitions, tiers, typical coding formats, and references to relevant standards or screening tools.
:name: tab-participant-metadata

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Example instruments / tools** |
|---|---|---|---|---|
| **Core IDs** | Participant ID | 1 | Text ID (e.g. P01, SL23_001) | — (lab-defined) |
| | Experiment ID | 1 | Stable experiment code | Foreign key |
| | Study / cohort | 1 | Text (e.g. PMV05 – Red, ACvsFR – AC) | — (lab-defined) |
| | Arm / group | 1 | Allocation label / not_applicable | If assigned |
| **Demographics & morphology** | Age | 1 | Numeric (years at first session) | Direct (derived from DOB if stored). If ethics committees do not allow, then age group according to a medically agreed on standard {cite:p}`diaz_call_2021` |
| | Sex-related variable | 1 | Study-defined sex-related measure/category | Define construct and coding; transgender identity is not a sex category |
| | Gender identity (optional; separately coded) | 2 | Categorical or free text | — (lab-defined wording) |
| | Height | 1 | Numeric (cm), self-reported or measured (flag which) | Stadiometer; self-report |
| | Weight | 1 | Numeric (kg), self-reported or measured | Scale or self-report. If measured, note method (e.g. nude, underwear, fasting morning, etc.) |
| | BMI | 1 | Numeric (kg·m⁻²), derived | Calculation from height and weight |
| | Body surface area (BSA) | 2 | Numeric (m²) | Du Bois & Du Bois, Mosteller, etc. (formula documented) |
| | Body fat % | 2 | Numeric (%) | BIA, DXA, skinfolds, BodPod, etc. |
| | Muscle (%) | 2 | Percentage | Specify measurement method |
| | BMR/RMR (kcal/day) | 2 | Numeric | Specify measured or estimated |
|  | Estimated energy requirement (kcal/day) | 3 (conditional) | Numeric; specify formula, inputs and activity factor | Participant-level estimate; not equivalent to BMR/RMR and only relevant for nutritional control |
| | Body-composition method | 2 | BIA / DXA / predictive equation / other | Record provenance |
| | Ethnic background / nationality | 3 | Categorical or free text; optional | Optional only with a specific scientific/ethical rationale; nationality is not a physiological proxy |
| **Thermal history & occupation** | Thermal history / {ref}`acclimation <label-acclimation>` background | 1 | Free text or categories (e.g. “>5 y in hot climate”, “recently relocated from cold climate”) | Short structured items |
| | Occupation / profession | 3 | Categorical or free text (e.g. student, office worker, outdoor labour) | — (decide based on ethics and purpose) |
| **Lifestyle & exposure** | Smoking status | 2 | Never / former / current; pack-years if known | PAR-Q+ {cite:p}`warburton_validation_2011` or simple screening form |
| | Alcohol use (habitual) | 2 | Units per week or categories (none / occasional / regular) | AUDIT-C {cite:p}`lawford_alcohol_2012` or simple frequency |
| | Regular caffeine intake | 2 | Cups per day or categories (low / moderate / high) | Simple frequency question |
| | Physical activity / fitness level (habitual) | 1–2 | MET-min/week + category (low / moderate / high) | IPAQ-SF, IPAQ-LF {cite:p}`lee_validity_2011`, or GPAQ (WHO) {cite:p}`bull_global_2009` |
| **Health & diagnoses** | Overall health status | 1 | Healthy / Relevant health condition / Unknown | Specify screening or assessment basis; eligibility criteria alone do not establish absence of diagnoses |
|  | Relevant medical conditions | 1 (conditional) | None / Present / Unknown; specify condition(s) where relevant | Broad medical context, including cardiovascular, metabolic, neurological, sleep-related or post-viral conditions where applicable; avoid mandatory diagnosis-specific checklists |
| | Relevant medications (by class) | 1 | None / Present / Unknown; classes or medications relevant to physiology | Single medication screening field; record classes, and use notes for dose/timing where justified |
| | Thermally relevant medication notes | 2 | Free text (drug names, dose, duration) | Structured notes |
| | Habitual melatonin supplementation | 2 | Yes/No; if Yes: typical dose (mg) and timing | Melatonin raises distal Tsk and DPG; relevant for sleep and circadian protocols. Acute use captured at session level |
| **Reproductive & hormonal** | Menstrual / reproductive status | 1 | Eumenorrheic / perimenopausal / postmenopausal / amenorrheic / pregnant / lactating | Simple categorical items |
| | Pregnancy status | 1 (conditional) | Yes / No / Unknown / not_applicable | Only when justified and ethically appropriate |
| | Cycle length & regularity | 2 | Numeric (days) + regular / irregular | Short structured questions |
| | Hormonal contraception | 1 | Type (combined pill, progestin-only, IUD, implant, injection, none) + duration | Structured questionnaire |
| | Hormonal therapy (HRT/GAHT or other) | 2 (conditional) | None / Present / Unknown; regimen and duration when relevant | Mechanism and regimen rather than indication alone; collect with ethical justification |
| **Thermal sensitivity / preference & psychological traits** | Thermal sensitivity / preference | 1 | Scores + groupings (e.g. cold / neutral / warm-preferring) | ETSRS {cite:p}`van_someren_experienced_2016` or similar |
| **Sleep & chronobiology** | {ref}`Chronotype <label-chronotype>` | 1–2 | Continuous score + category (morning / intermediate / evening) | Morningness--Eveningness Questionnaire (MEQ) {cite:p}`horne_self-assessment_1976`, Composite Scale of Morningness (CSM) {cite:p}`smith_composite_1989`, and/or Munich Chronotype Questionnaire {cite:p}`roenneberg_human_2015`. |
| | Habitual bedtime | 1–2 | Typical bed and wake times (work days vs free days) | Often collected with MCTQ |
| | Habitual sleep quality | 2–3 | Global score; optionally “good vs poor sleeper” | Pittsburgh Sleep Quality Index (PSQI) for overall sleep quality {cite:p}`buysse_pittsburgh_1989` |
| | Habitual shift work | 2 | Never / former / current; if current: rotating / permanent nights / early starts | Chronic circadian misalignment shifts CBT and HRV rhythms independently of chronotype. Document pattern and duration {cite:p}`sack_circadian_2007,arendt_shift_2010` |
| | Home and/or office heating/cooling systems | 2 (conditional) | Multi-select: central heating, floor heating, AC, fans, none, etc. | Simple checklist |
| **Vision & sensory (for light/EEG-heavy protocols)** | Vision status | 3 | Normal with/without correction / impaired | Snellen or LogMAR chart; self-report |
| | Colour vision | 3 | Normal / red–green deficiency / other | Ishihara plates or equivalent test |

:::

Note. Some questions may be redundant when already used as an exclusion criterion, e.g., if having any CV history is an exclusion reason, then no need to repeat it in participant metadata.

Core means essential where applicable, not a requirement to disclose sensitive information without scientific and ethical justification. Sex-related variables and gender identity are separately defined and coded; relevant medical conditions are conditionally Core; detailed clinical descriptors may be added for specialised protocols. Hormonal therapies remain conditional.
