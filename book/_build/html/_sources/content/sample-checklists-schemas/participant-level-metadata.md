# Participant-level metadata

Participant-level metadata capture characteristics that are stable or slowly changing across the duration of a study. These variables describe each individual taking part in the experiment and provide the context needed to interpret physiological responses, account for relevant modifiers, and enable subgroup or meta-analytic work.

Each participant is represented by one row in a dedicated metadata table, with one column per field. As in the experiment-level schema, fields are grouped by topic (e.g., Demographics & Morphology, Health & Diagnoses, Lifestyle, Reproductive & Hormonal) and assigned to informal tiers indicating their importance:

- <u>Tier 1 -- Core:</u> Minimal information required in any thermal physiology experiment (e.g., age, sex at birth, height, weight, BMI, basic health status, habitual physical activity, key hormonal status).

- <u>Tier 2 -- Recommended:</u> Variables that strongly influence thermoregulation and improve interpretability, including body surface area, thermal history, smoking and alcohol use, typical sleep timing, menstrual cycle characteristics, hormone therapies, thermosensitivity, and selected built-environment descriptors.

- <u>Tier 3 -- Specialised:</u> More detailed or study-specific attributes, such as body composition, occupation, education, sensory-sensitivity or psychological scales, quality-of-life instruments, or vision/colour-vision assessments. These fields are optional but useful for specialised analyses or targeted protocols.

The participant metadata table can be implemented in a spreadsheet, REDCap form, or as structured CSV/TSV with accompanying JSON (e.g., a participants.tsv + participants.json pair following BIDS conventions).


:::{table} Example participant-level metadata schema, including groups, field definitions, tiers, typical coding formats, and references to relevant standards or screening tools.
:name: tab-participant-metadata

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Example instruments / tools** |
|---|---|---|---|---|
| **Core IDs** | Participant ID | 1 | Text ID (e.g. P01, SL23_001) | — (lab-defined) |
|  | Study / cohort | 1 | Text (e.g. PMV05 – Red, ACvsFR – AC) | — (lab-defined) |
| **Demographics & morphology** | Age | 1 | Numeric (years at first session) | Direct (derived from DOB if stored). If ethics committees do not allow, then age group according to a medically agreed on standard {cite:p}`diaz_call_2021` |
|  | Sex | 1 | Categorical: female / male / trans f2m / trans m2f | Trans categories only for active transitioning at the time of the experiment |
|  | Gender identity (optional) | 2 | Categorical or free text | — (lab-defined wording) |
|  | Height | 1 | Numeric (cm), self-reported or measured (flag which) | Stadiometer; self-report |
|  | Weight | 1 | Numeric (kg), self-reported or measured | Scale or self-report. If measured, note method (e.g. nude, underwear, fasting morning, etc.) |
|  | BMI | 1 | Numeric (kg·m⁻²), derived | Calculation from height and weight |
|  | Body surface area (BSA) | 2 | Numeric (m²) | Du Bois & Du Bois, Mosteller, etc. (formula documented) |
|  | Body fat % | 2 | Numeric (%) | BIA, DXA, skinfolds, BodPod, etc. |
|  | Ethnic background / nationality | 3 | Categorical or free text; optional | — (decide based on ethics and purpose) |
| **Thermal history & occupation** | Thermal history / acclimation background | 2 | Free text or categories (e.g. “>5 y in hot climate”, “recently relocated from cold climate”) | Short structured items |
|  | Occupation / profession | 3 | Categorical or free text (e.g. student, office worker, outdoor labour) | — (decide based on ethics and purpose) |
|  | Education level | 3 | Categorical (e.g. secondary / bachelor / master / PhD) | — (decide based on ethics and purpose) |
| **Lifestyle & exposure** | Smoking status | 1 | Never / former / current; pack-years if known | PAR-Q+ {cite:p}`warburton_validation_2011` or simple screening form |
|  | Alcohol use (habitual) | 2 | Units per week or categories (none / occasional / regular) | AUDIT-C {cite:p}`lawford_alcohol_2012` or simple frequency |
|  | Regular caffeine intake | 2 | Cups per day or categories (low / moderate / high) | Simple frequency question |
|  | Physical activity / fitness level (habitual) | 1–2 | MET-min/week + category (low / moderate / high) | IPAQ-SF, IPAQ-LF {cite:p}`lee_validity_2011`, or GPAQ (WHO) {cite:p}`bull_global_2009` |
| **Health & diagnoses** | Overall health status | 1 | Healthy / controlled condition(s) / other + notes | Summary from screening; may combine PAR-Q+ with brief medical history |
|  | Cardiovascular diagnoses | 1 | Yes/No per condition (hypertension, arrhythmia, CAD, HF, etc.) | PAR-Q+, Charlson comorbidity list {cite:p}`charlson_charlson_2022`, or tailored checklist |
|  | Endocrine / metabolic diagnoses | 1 | Yes/No per condition (diabetes, thyroid disease, obesity, CKD, etc.) | PAR-Q+ or Charlson-based checklist |
|  | Neurological / autonomic disorders | 1 | Yes/No per condition (POTS, autonomic neuropathy, Parkinson’s, SCI, etc.) | Screening form referencing medical history |
|  | History of syncope / orthostatic intolerance | 2–3 | Yes/No + short description | PAR-Q+ style yes/no items |
|  | Diagnosed sleep disorder | 2–3 | None / OSA / insomnia / restless legs / other | PSQI / ISI + STOP-Bang / Berlin / Epworth, or clinical history |
|  | Neurodivergent diagnosis | 2–3 | None / ASD / ADHD / other / prefer not to say | Self-report; may link to ASD/ADHD screening tools |
|  | Other diagnoses relevant to thermoregulation | 2–3 | Free text + coded categories | Examples: autoimmune disease, large burns/grafts, chronic infection |
| **Medication** | Chronic medications (by class) | 1 | Yes/No per class (β-blockers, antihypertensives, anticholinergics, SSRIs, stimulants, etc.) | Simple class checklist; optionally ATC codes |
|  | Thermally relevant medication notes | 2 | Free text (drug names, dose, duration) | Structured notes |
| **Reproductive & hormonal** | Menstrual / reproductive status | 1 | Eumenorrheic / perimenopausal / postmenopausal / amenorrheic / pregnant / lactating | Simple categorical items |
|  | Cycle length & regularity | 2 | Numeric (days) + regular / irregular | Short structured questions |
|  | Hormonal contraception | 1 | Type (combined pill, progestin-only, IUD, implant, injection, none) + duration | Structured questionnaire |
|  | HRT (hormone replacement therapy) | 1 | Regimen (oestrogen, oestrogen+progestin, other) + duration | Medical history question |
|  | GAHT (gender-affirming hormone therapy) | 1 | Yes/No; regimen (e.g. oestradiol, testosterone, blockers) + duration | Optional and ethics-dependent |
| **Thermal sensitivity / preference & psychological traits** | Thermal sensitivity / preference | 1–2 | Scores + groupings (e.g. cold / neutral / warm-preferring) | ETSRS {cite:p}`van_someren_experienced_2016` or similar |
|  | Personality traits | 3 | Scores | Big Five {cite:p}`kang_validation_2024,rammstedt_measuring_2007`, BIS/BAS, {cite:p}`maack_re-examination_2018` etc. |
|  | General sensory / emotional sensitivity | 3 | Score(s) | Highly Sensitive Person Scale (HSPS) {cite:p}`aron_highly_2011` |
|  | Psychological / psychiatric scales | 2–3 | Scores; cut-offs for depression, anxiety, etc. | PHQ-9, GAD-7, DASS-21 |
| **Sleep & chronobiology** | Chronotype | 1 | Continuous score + category (morning / intermediate / evening) | Morningness--Eveningness Questionnaire (MEQ) {cite:p}`horne_self-assessment_1976`, Composite Scale of Morningness (CSM) {cite:p}`smith_composite_1989`, and/or Munich Chronotype Questionnaire {cite:p}`roenneberg_human_2015`. |
|  | Habitual bedtime | 1–2 | Typical bed and wake times (work days vs free days) | Often collected with MCTQ |
|  | Habitual sleep quality | 2–3 | Global score; optionally “good vs poor sleeper” | Pittsburgh Sleep Quality Index (PSQI) for overall sleep quality {cite:p}`buysse_pittsburgh_1989` |
| **Built-environment context (optional)** | Main dwelling type | 3 | Detached house / apartment / dormitory / informal | Simple categorical question |
|  | Home and/or office heating/cooling systems | 2 | Multi-select: central heating, floor heating, AC, fans, none, etc. | Simple checklist |
|  | Typical bedroom temperature | 3 | °C or cool/neutral/warm category | Self-estimate question |
| **Vision & sensory (for light/EEG-heavy protocols)** | Vision status | 3 | Normal with/without correction / impaired | Snellen or LogMAR chart; self-report |
|  | Colour vision | 3 | Normal / red–green deficiency / other | Ishihara plates or equivalent test |

:::

Note. Some questions may be redundant when already used as an exclusion criterion, e.g., if having any CV history is an exclusion reason, then no need to repeat it in participant metadata.