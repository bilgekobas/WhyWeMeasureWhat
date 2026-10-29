# Experiment-level metadata

Experiment-level metadata capture the high-level characteristics of a study: where and when it was conducted, by whom, under which ethical approvals, and what its overall design and planned exposures were. These fields describe the protocol as a whole, independently of any particular participant or session, and form the top level of the metadata hierarchy.

To make the schema easier to reuse across different laboratories and study types, fields are grouped by topic and are assigned to three informal tiers:

- <u>Tier 1 -- Core experiment descriptors:</u> Essential information needed to interpret or reuse a study, including experiment identifiers, institutional affiliation, ethics approval, study design and environment, recruitment window, and the main exposure/intervention categories.
- <u>Tier 2 -- Recommended descriptors:</u> Information that improves reproducibility and interpretability but may not always be available, such as randomisation method, {ref}`blinding <label-blinding>`, standardised behavioural instructions, condition naming, and detailed environmental or HVAC descriptions.
- <u>Tier 3 -- Specialised descriptors:</u> More specific contextual information that is useful for certain study types or advanced meta-analyses, including room geometry, calibration summaries, or detailed equipment notes. These fields are optional but help achieve FAIR-level documentation when available.

To aid cross-study comparison, we also include a concise {ref}`PICOT <label-picot>` summary for each experiment. PICOT provides a high-level, non-redundant synopsis of the Population, Intervention, Comparison, Outcomes, and Time frame, complementing (but not duplicating) the detailed metadata fields.

:::{table} Experiment-level metadata schema, organised by group and tier.
:name: tab-experiment-metadata

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Notes / considerations** |
|---|---|---|---|---|
| **Core IDs** | Experiment ID | 1 | Unique alphanumeric code | — |
| | Experiment name | 1 | Descriptive title | — |
| | Related paper(s) | 1 | Publication title(s) / stable IDs | Link publications |
| | Related paper DOI(s) | 1 | DOI list | One or multiple papers |
| | Principal investigator(s) | 1 | Name(s) or initials | — |
| | Researcher(s) | 1 | Name(s) or initials | — |
| | Contact person | 1 | Single designated contact | — |
| | Contact information | 1 | Email | — |
| | Lab(s) | 1 | Lab or unit name | — |
| | Institute(s) | 1 | Organisational affiliation | — |
| | Location(s) | 1 | City, country; optionally coordinates or street address | High-resolution location information enables automated climate data and time-zone alignment |
| **Ethics & governance** | Ethics status | 1 | Approved / exempt / pending / not_reported | Separate from committee and approval ID |
| | Ethics committee | 1 | Full name | — |
| | Ethics approval ID / Code | 1 | Approval number | — |
| | Registration timing | 2 | Prospective / retrospective / not_applicable | If registered |
| | Approval date | 2 | YYYY-MM-DD | — |
| | Amendments / versions | 2 | Yes/No; brief notes | — |
| | Data protection compliance | 1 | GDPR, HIPAA, other | — |
| | Preregistration ID | 2–3 | OSF / clinicaltrials.gov link | — |
| **Study type** | Study environment | 1 | Laboratory / Field / Hybrid | — |
| | Study design | 1 | Controlled / Observational / Interventional | — |
| | Experimental structure | 2 | Between-subjects, Within-subjects, Repeated measures, Crossover, Pre–Post | Multiple can apply |
| | Randomisation used | 1 | Yes / No / not_applicable | Separate from Tier 2 method |
| | Randomisation method | 2 | Yes/No; method (simple, block, Latin square) | Link to randomisation table if available |
| | Allocation concealment | 2 | Yes / No / not_reported / not_applicable | When applicable |
| | Participant blinding | 2 | None / Single-blind / Double-blind | If none, a brief explanation recommended |
| | Investigator blinding | 2 | Yes / No / not feasible | Separate from participant blinding |
| **Timing & schedule** | Start date of experiment | 1 | YYYY-MM-DD | — |
| | End date of experiment | 1 | YYYY-MM-DD | — |
| | Typical session duration | 1 | Minutes or hours | — |
| | Typical normalisation duration (min) | 1 | Numeric minutes | Planned; actual recorded per session |
| | Standard session start time | 1 | hh:mm (24-h format) | — |
| | Standard session end time | 1 | hh:mm (24-h format) | — |
| | Planned sessions per participant | 1 | Integer | Protocol-defined |
| | Intersession rule | 2 | Washout / interval / scheduling rule | Planned minimum interval |
| **Study population** | Sample-size method | 1 | A priori / pilot / feasibility / other | State method or calculation |
| | Target {ref}`sample size <label-sample-size>` | 2 | Integer | — |
| | Screened N | 2 | Integer | Recruitment denominator |
| | Enrolled N | 2 | Integer | Recruitment denominator |
| | Randomised N | 2 | Integer / not_applicable | Allocation denominator |
| | Completed N | 2 | Integer | — |
| | Primary-analysis N | 1 | Integer | Primary outcome denominator |
| | Recruitment method | 3 | Text | Recruitment provenance |
| | Compensation | 2 | Amount, currency and conditions | If applicable |
| | Demographic summary counts (derived) | 2 | Counts calculated from participant records | Optional; do not duplicate manual sex/gender coding |
| | Age range | 1 | Minimum–maximum | e.g. “21–35 years” |
| | Population description | 1 | Free text | e.g. “Healthy university students”, “Sedentary adults aged 20–40” |
| | Inclusion criteria | 1 | Free text or list | — |
| | Exclusion criteria | 1 | Free text or list | — |
| **Intervention** | Study domain(s) | 1 | Thermal / Humidity / Air movement / Light / IAQ / Acoustics | Multiple allowed |
| | Intervention description | 1 | Free text | Describe manipulated variables |
| | Number of conditions | 1 | Integer | — |
| | Condition labels | 2 | Text labels | — |
| | Temperature-series type | 2 | Fixed / stepped / variable / mixed / not_applicable | For thermal exposure |
| | Tested temperature minimum (°C) | 1 | Numeric / not_applicable | If temperature is manipulated |
| | Tested temperature maximum (°C) | 1 | Numeric / not_applicable | If temperature is manipulated |
| | Tested temperature targets (°C) | 1 | List / not_applicable | All planned targets |
| | Condition notes | 2 | Text | Describe exposure schedule |
| | Standardised behaviour rules | 1 | Resting, sitting, acclimatisation / normalisation, movement, eating, drinking protocols | — |
|  | Planned food / drink provision | 2 (conditional) | Types, quantities, timing, nutritional standardisation | Protocol-level provisions; actual consumption recorded at session level |
| **Environment & equipment (experiment-level)** | Spatial typology | 1 | Office / Residential / Educational / Public / etc. | — |
| | HVAC system description | 2 | AC model, radiant panel specifications, air-velocity sources | — |
| | Room dimensions | 3 | m² or m³ | — |
| | Planned environmental variables | 1 | List of quantities | Define methods and sampling in linked data |
| | Environmental instrument heights | 1 | Height(s) and units | When applicable |
| | Primary instruments used | 1 | List of Device IDs (e.g. TMP-01, TMP-02, ECG-A) | Foreign keys to devices.tsv (Device Registry); full specifications recorded there |
| | Questionnaire/task definitions reference | 1 | URI / table identifier | Exact wording, codes, anchors, language, timing |
| | Direct measurement definitions reference | 1 | URI / table identifier | Signal, device, default placement, configured rate, derived metrics |
| | {ref}`Baseline <label-baseline>` environmental control | 1 | Air temperature, radiant temperature, humidity, lighting ranges | Multiple allowed |
| | Calibration reference | 2 | Link to calibration log entries for this study | Foreign key to calibrations.tsv; replaces free-text calibration notes |
| **PICOT summary** | Primary research question | 1 | Text | Distinct from PICOT synopsis |
| | Target physiological process / construct | 1 | Text | Mechanistic rationale |
| | Primary outcome definition | 1 | Operational definition | Include analysis windows and metrics |
| | Primary analysis approach | 1 | Method / statistical model | Link plan or code |
| | P – Population | 1 | Short description of target group and key eligibility criteria | “Healthy adults 18–35, BMI 18–25, non-smokers; no cardiovascular/metabolic disease; regular sleep schedule” |
| | I – Intervention / exposure | 1 | Summary of main exposure(s) or experimental condition(s) | “14-day heat {ref}`acclimation <label-acclimation>`: AC at 26 °C vs free-running apartment (summer conditions)” |
| | C – Comparison / control conditions | 1 | Description of comparator condition(s) | “Free-running cooling vs constant AC; within-subject crossover” |
| | O – Primary outcomes | 1 | Main endpoints and quantification | “Core body temperature, neck/ankle skin temperature, HR, BP, HRV (RMSSD), thermal sensation” |
| | O – Secondary outcomes | 2 | Additional exploratory endpoints | “Sleep {ref}`onset <label-onset>` latency, actigraphy-based sleep efficiency, melatonin AUC” |
| | T – Time frame | 1 | Time horizon for effect and measurement | “Pre–post mild heat-stress test before and after 14-day exposure; tests between 09:00–16:00” |
| **Data availability** | Data repository | 1 | OSF / Zenodo / Figshare / institutional repository / none | Where the dataset will be or is deposited |
| | Dataset DOI / link | 1 | URL or DOI; "in preparation" if not yet available | — |
| | Raw-data access | 1 | Open / restricted / request / unavailable | Separate from processed data |
| | Processed-data access | 1 | Open / restricted / request / unavailable | Separate from raw data |
| | Code access | 1 | Repository URL or access status | Analysis and processing scripts |
| | Licence | 2 | Licence identifier | For data/code as applicable |
| | Data access conditions | 1 | Open / Restricted / Embargoed (with date) / Available on request | "Available on request" alone is insufficient for reproducibility; prefer open or restricted with documented process |
| | Metadata availability | 1 | Whether structured metadata (this schema) is shared independently of raw data | Metadata can often be shared even when raw data cannot |

:::