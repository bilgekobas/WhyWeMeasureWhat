# Participant-level metadata




Participant-level metadata capture characteristics that are stable or slowly changing across the duration of a study. These variables describe each individual taking part in the experiment and provide the context needed to interpret physiological responses, account for relevant modifiers, and enable subgroup or meta-analytic work.



Each participant is represented by one row in a dedicated metadata table, with one column per field. As in the experiment-level schema, fields are grouped by topic (e.g., Demographics & Morphology, Health & Diagnoses, Lifestyle, Reproductive & Hormonal) and assigned to informal tiers indicating their importance:



- <u>Tier 1 – Core:</u> Minimal information required in any thermal physiology experiment (e.g., age, sex at birth, height, weight, BMI, basic health status, habitual physical activity, key hormonal status).



- <u>Tier 2 – Recommended:</u> Variables that strongly influence thermoregulation and improve interpretability, including body surface area, thermal history, smoking and alcohol use, typical sleep timing, menstrual cycle characteristics, hormone therapies, thermosensitivity, and selected built-environment descriptors.



- <u>Tier 3 – Specialised:</u> More detailed or study-specific attributes, such as body composition, occupation, education, sensory-sensitivity or psychological scales, quality-of-life instruments, or vision/colour-vision assessments. These fields are optional but useful for specialised analyses or targeted protocols.



The participant metadata table can be implemented in a spreadsheet, REDCap form, or as structured CSV/TSV with accompanying JSON (e.g., a participants.tsv + participants.json pair following BIDS conventions).



<table style="width:98%;">

<caption><p>Table 10. Example participant-level metadata schema, including groups, field definitions, tiers, typical coding formats, and references to relevant standards or screening tools.</p></caption>

<colgroup>

<col style="width: 14%" />

<col style="width: 15%" />

<col style="width: 6%" />

<col style="width: 28%" />

<col style="width: 33%" />

</colgroup>

<thead>

<tr>

<th><strong>Group</strong></th>

<th><strong>Field name</strong></th>

<th><strong>Tier</strong></th>

<th><strong>Typical answers / coding</strong></th>

<th><strong>Example instruments / tools</strong></th>

</tr>

</thead>

<tbody>

<tr>

<td rowspan="2">Core IDs</td>

<td>Participant ID</td>

<td>1</td>

<td>Text ID (e.g. P01, SL23_001)</td>

<td>– (lab-defined)</td>

</tr>

<tr>

<td>Study / cohort</td>

<td>1</td>

<td>Text (e.g. PMV05 – Red, ACvsFR – AC)</td>

<td>– (lab-defined)</td>

</tr>

<tr>

<td rowspan="9">Demographics &amp; morphology</td>

<td>Age</td>

<td>1</td>

<td>Numeric (years at first session)</td>

<td>Direct (derived from DOB if stored). If ethics committees do not allow, then age group according to a medically agreed on standard <a class="citation" href="/09_references/09_01_references/#ref-527" data-cite="527">[527]</a></td>

</tr>

<tr>

<td>Sex</td>

<td>1</td>

<td>Categorical: female / male / trans f2m/ trans m2f</td>

<td>Trans categories only for active transitioning at the time of the experiment</td>

</tr>

<tr>

<td>Gender identity (optional)</td>

<td>2</td>

<td>Categorical or free text</td>

<td>– (lab-defined wording)</td>

</tr>

<tr>

<td>Height</td>

<td>1</td>

<td>Numeric (cm), self-reported or measured (flag which)</td>

<td>Stadiometer; self-report</td>

</tr>

<tr>

<td>Weight</td>

<td>1</td>

<td>Numeric (kg), self-reported or measured</td>

<td>Scale or self-report. If measured, note the method (e.g., in nude, in underwear, fasting morning, etc.)</td>

</tr>

<tr>

<td>BMI</td>

<td>1</td>

<td>Numeric (kg·m⁻²), derived</td>

<td>Calculation from height &amp; weight</td>

</tr>

<tr>

<td>Body surface area (BSA)</td>

<td>2</td>

<td>Numeric (m²)</td>

<td>DuBois &amp; DuBois, Mosteller, etc. (formula documented)</td>

</tr>

<tr>

<td>Body fat %</td>

<td>2</td>

<td>Numeric (%)</td>

<td>BIA, DXA, skinfolds, BodPod, etc.</td>

</tr>

<tr>

<td>Ethnic background / nationality</td>

<td>3</td>

<td>Categorical or free text; optional</td>

<td>– (decide based on ethics &amp; purpose)</td>

</tr>

<tr>

<td rowspan="3">Thermal history &amp; occupation</td>

<td>Thermal history / acclimation background</td>

<td>2</td>

<td>Free text or categories (e.g. “&gt;5 y in hot climate”, “recently relocated from cold climate”)</td>

<td>– (short structured items)</td>

</tr>

<tr>

<td>Occupation / profession</td>

<td>3</td>

<td>Categorical / free text (e.g. student, office worker, outdoor labour)</td>

<td>– (decide based on ethics &amp; purpose)</td>

</tr>

<tr>

<td>Education level</td>

<td>3</td>

<td>Categorical (e.g. secondary / bachelor / master / PhD)</td>

<td>– (decide based on ethics &amp; purpose)</td>

</tr>

<tr>

<td rowspan="4">Lifestyle &amp; exposure</td>

<td>Smoking status</td>

<td>1</td>

<td>Never / former / current; pack-years if known</td>

<td>Can be taken from PAR-Q+ or simple lab form</td>

</tr>

<tr>

<td>Alcohol use (habitual)</td>

<td>2</td>

<td>Units per week or categories (none / occasional / regular)</td>

<td>AUDIT-C <a class="citation" href="/09_references/09_01_references/#ref-528" data-cite="528">[528]</a> or simple frequency question</td>

</tr>

<tr>

<td>Regular caffeine intake</td>

<td>2</td>

<td>Cups per day or categories (low / moderate / high)</td>

<td>Simple frequency question</td>

</tr>

<tr>

<td>Physical activity / fitness level (habitual)</td>

<td>1–2</td>

<td>MET-min/week + category (low / moderate / high)</td>

<td>IPAQ-SF, IPAQ-LF <a class="citation" href="/09_references/09_01_references/#ref-529" data-cite="529">[529]</a>, or GPAQ (WHO) <a class="citation" href="/09_references/09_01_references/#ref-530" data-cite="530">[530]</a></td>

</tr>

<tr>

<td rowspan="8">Health &amp; diagnoses</td>

<td>Overall health status</td>

<td>1</td>

<td>Healthy / controlled condition(s) / other + notes</td>

<td>Summary from screening; may combine PAR-Q+ <a class="citation" href="/09_references/09_01_references/#ref-531" data-cite="531">[531]</a> + brief medical history</td>

</tr>

<tr>

<td>Cardiovascular diagnoses</td>

<td>1</td>

<td>Yes/No per condition (hypertension, arrhythmia, CAD, HF, etc.)</td>

<td>PAR-Q+, Charlson comorbidity list <a class="citation" href="/09_references/09_01_references/#ref-532" data-cite="532">[532]</a>, or tailored checklist</td>

</tr>

<tr>

<td>Endocrine / metabolic diagnoses</td>

<td>1</td>

<td>Yes/No per condition (diabetes, thyroid disease, obesity, CKD, etc.)</td>

<td>PAR-Q+, Charlson-based checklist</td>

</tr>

<tr>

<td>Neurological / autonomic disorders</td>

<td>1</td>

<td>Yes/No per condition (POTS, autonomic neuropathy, Parkinson’s, SCI, etc.)</td>

<td>Screening form referencing medical history</td>

</tr>

<tr>

<td>History of syncope / orthostatic intolerance</td>

<td>2–3</td>

<td>Yes/No + short description</td>

<td>PAR-Q+ style yes/no item(s)</td>

</tr>

<tr>

<td>Diagnosed sleep disorder</td>

<td>2–3</td>

<td>None / OSA / insomnia / restless legs / other</td>

<td>PSQI/ISI + STOP-Bang / Berlin / Epworth, or clinical history</td>

</tr>

<tr>

<td>Neurodivergent diagnosis</td>

<td>2–3</td>

<td>None / ASD / ADHD / other / prefer not to say</td>

<td>Self-report; may link to ASD/ADHD screening tools if used</td>

</tr>

<tr>

<td>Other diagnoses relevant to thermoregulation</td>

<td>2–3</td>

<td>Free text + coded categories</td>

<td>Examples: autoimmune disease, large burns/grafts, chronic infection, etc.</td>

</tr>

<tr>

<td rowspan="2">Medication</td>

<td>Chronic medications (by class)</td>

<td>1</td>

<td>Yes/No per class (β-blockers, antihypertensives, anticholinergics, SSRIs, stimulants, etc.)</td>

<td>Simple class checklist; optionally ATC codes</td>

</tr>

<tr>

<td>Thermally relevant medication notes</td>

<td>2</td>

<td>Free text (drug names, dose, duration)</td>

<td>– (structured notes)</td>

</tr>

<tr>

<td rowspan="5">Reproductive &amp; hormonal</td>

<td>Menstrual / reproductive status</td>

<td>1</td>

<td>Eumenorrheic / perimenopausal / postmenopausal / amenorrheic / pregnant / lactating</td>

<td>Simple categorical items</td>

</tr>

<tr>

<td>Cycle length &amp; regularity</td>

<td>2</td>

<td>Numeric (days) + regular / irregular</td>

<td>Short structured questions</td>

</tr>

<tr>

<td>Hormonal contraception</td>

<td>1</td>

<td>Type (combined pill, progestin-only, IUD, implant, injection, none) + duration</td>

<td>Short structured questions</td>

</tr>

<tr>

<td>HRT (hormone replacement therapy)</td>

<td>1</td>

<td>Regimen (oestrogen, oestrogen+progestin, other) + duration</td>

<td>Medical history question</td>

</tr>

<tr>

<td>GAHT (gender-affirming hormone therapy)</td>

<td>1</td>

<td>Yes/No; regimen (e.g. oestradiol, testosterone, blockers) + duration</td>

<td>Medical history; optional and ethics-dependent</td>

</tr>

<tr>

<td rowspan="4">Thermal sensitivity / preference &amp; psychological traits</td>

<td>Thermal sensitivity / preference</td>

<td>1–2</td>

<td>Scores + groupings (e.g. cold / neutral / warm-preferring)</td>

<td>ETSRS <a class="citation" href="/09_references/09_01_references/#ref-533" data-cite="533">[533]</a> or similar</td>

</tr>

<tr>

<td>Personality traits</td>

<td>3</td>

<td>Scores on Big Five, BIS/BAS, etc.</td>

<td>Big Five (e.g. BFI, NEO-FFI), BIS/BAS scales, etc.</td>

</tr>

<tr>

<td>General sensory / emotional sensitivity</td>

<td>3</td>

<td>Score(s)</td>

<td>Highly Sensitive Person Scale (HSPS) or similar, if used</td>

</tr>

<tr>

<td>Psychological / psychiatric scales</td>

<td>2–3</td>

<td>Scores, cut-offs for depression, anxiety, etc.</td>

<td>e.g. PHQ-9, GAD-7, DASS-21</td>

</tr>

<tr>

<td rowspan="3">Sleep &amp; chronobiology</td>

<td>Chronotype</td>

<td>1</td>

<td>Continuous score + category (morning / intermediate / evening)</td>

<td>Morningness–Eveningness Questionnaire (MEQ) <a class="citation" href="/09_references/09_01_references/#ref-534" data-cite="534">[534]</a>, Composite Scale of Morningness (CSM) <a class="citation" href="/09_references/09_01_references/#ref-535" data-cite="535">[535]</a>, and/or Munich Chronotype Questionnaire <a class="citation" href="/09_references/09_01_references/#ref-536" data-cite="536">[536]</a>.<br />

Store instrument name + score/category</td>

</tr>

<tr>

<td>Habitual bedtime</td>

<td>1–2</td>

<td>Typical bed and wake times (work days vs free days)</td>

<td>Often comes with MCTQ; or simple timing questions</td>

</tr>

<tr>

<td>Habitual sleep quality</td>

<td>2–3</td>

<td>Global score, and optionally “good vs poor sleeper”</td>

<td>Pittsburgh Sleep Quality Index (PSQI) for overall sleep quality <a class="citation" href="/09_references/09_01_references/#ref-537" data-cite="537">[537]</a></td>

</tr>

<tr>

<td rowspan="3">Built-environment context (optional)</td>

<td>Main dwelling type</td>

<td>3</td>

<td>Detached house / apartment / dorm / informal etc.</td>

<td>Simple categorical question</td>

</tr>

<tr>

<td>Home and/or office heating/cooling systems</td>

<td>2</td>

<td>Multi-select: central heating, floor heating, AC, fans, none, etc.</td>

<td>Simple checklist</td>

</tr>

<tr>

<td>Typical bedroom temperature</td>

<td>3</td>

<td>°C or cool/neutral/warm category</td>

<td>Self-estimate question</td>

</tr>

<tr>

<td rowspan="2">Vision &amp; sensory (for light/EEG-heavy protocols)</td>

<td>Vision status</td>

<td>3</td>

<td>Normal with/without correction / impaired</td>

<td>Snellen or LogMAR chart; self-report of correction</td>

</tr>

<tr>

<td>Colour vision</td>

<td>3</td>

<td>Normal / red–green deficiency / other</td>

<td>Ishihara plates or equivalent test</td>

</tr>

</tbody>

</table>



Note. Some questions may be redundant when already used as an exclusion criterion, e.g., if having any CV history is an exclusion reason, then no need to repeat it in participant metadata.
