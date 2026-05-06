# Session-level metadata

Session-level metadata captures all information that varies from one visit or experimental condition to the next for a given participant. Many of the acute modifiers discussed in Section 2---such as last night'{ref}`s <label-heat-storage>` sleep, time since waking, recent illness, caffeine or meal timing, and daily hormonal fluctuations---change from day to day and therefore must be recorded at the session rather than participant level.

Each session is represented by one row in a dedicated metadata table, with one column per session field. As with the experiment- and participant-level schemas, fields are grouped by topic (e.g., Identifiers & Timing, Devices & Logistics, Protocol Adherence, Acute Health State) and assigned to informal tiers:

- <u>Tier 1 -- Core:</u> Essential variables recorded for every visit (e.g., session ID, date and time, condition code, clothing, sleep duration, pre-session restrictions, acute illness indicators).

- <u>Tier 2 -- Recommended:</u> Factors that meaningfully influence thermophysiological responses but may not always be collected (e.g., researchers present, {ref}`acclimation <label-acclimation>` period, night-shift work, time since exercise).

- <u>Tier 3 -- Specialised:</u> Detailed or study-specific variables, such as exact bathroom break volumes, caloric intake calculations, event logs, or fine-grained environmental contextualisation.

Individual studies may extend this table with experiment-specific columns, such as time points for discrete measurements, cognitive task blocks, stepwise heating/cooling adjustments, water-intake increments, or protocol deviations. The core fields remain comparable across studies, facilitating harmonisation and meta-analysis.

Session metadata can be recorded via paper logs, REDCap/Qualtrics forms, or digital forms directly linked to the underlying session table.

:::{table} Example session-level metadata schema, organised by group, tier, and typical data formats, with optional references to instruments or logging tools.
:name: tab-session-metadata

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Example instruments / tools** |
|---|---|---|---|---|
| **Identifiers & timing** | Session ID | 1 | Unique ID per visit/condition (e.g. P01_S1, P03_C01_Armchair) | Lab-defined |
|  | Participant ID | 1 | Unique participant code linked to master table (P01, SL23_001, etc.) | Lab-defined |
|  | Date | 1 | Calendar date | YYYY-MM-DD or format noted |
|  | Session start time | 1 | 24-h clock time or UNIX timestamp | — |
|  | Session end time | 1 | 24-h clock time or UNIX timestamp | — |
|  | Condition / scenario code | 1 | Text label for assigned condition (e.g. C01_01, Heat_26C, Night_Armchair) | Lab-defined |
|  | Location / room | 1 | Room or laboratory code | — |
|  | Researchers present | 2 | Initials or staff codes | — |
| **Devices & sensor application +** | Device IDs used | 1 | List of Device IDs applied this session (e.g. TMP-01, TMP-03, ECG-A) | Foreign key → Device Registry in sensor-device-metadata |
|  | Calibration IDs active | 1 | List of Calibration IDs currently valid for each device (e.g. CAL-003, CAL-007) | Foreign key → Calibration Log in sensor-device-metadata; confirms which correction equation was applied |
|  | Condition order / randomisation code | 1 | Randomisation sequence label (e.g. "Sequence A: warm → neutral → cool") | Study randomisation plan |
|  | Body site per device | 1 | Device ID → site (e.g. TMP-01 → left forearm anterior / TMP-02 → right anterior thigh) | Use anatomical taxonomy site labels; laterality and aspect required |
|  | Attachment method per device | 1 | Device ID → method (e.g. TMP-01 → Transpore tape / ECG-A → elastic chest strap) | — |
|  | Application time per device | 1 | Device ID → hh:mm (e.g. TMP-01 → 17:55 / pill → ingested 17:50) | Time sensor was placed on or ingested by participant |
|  | Recording start time per device | 1 | Device ID → hh:mm | May differ from application time if equilibration period applies |
|  | Recording end time per device | 1 | Device ID → hh:mm | — |
|  | Equilibration time (min) | 2 | Device ID → numeric (e.g. TMP-01 → 10 min) | Time between application and first data point included in analysis |
|  | Skin preparation per device | 2 | Device ID → method (e.g. EDA-03 → alcohol wipe + dry / TMP-01 → none) | — |
|  | Shielding from airflow | 2 | Device ID → Yes/No | Particularly relevant for skin temperature contact sensors |
|  | Signal quality per device | 2 | Device ID → 1 (poor) – 5 (excellent) | Operator assessment at session end |
|  | Sensor deviations | 2 | Free text (e.g. "TMP-02 detached at 19:30, reattached 19:35"; "ECG-A lost signal 20:10–20:15") | Any deviation from standard placement or signal interruption |
| **Environment & exposure (session context)** | Clothing description | 1 | Free text description (e.g. “T-shirt, jeans, socks”) | — |
|  | Clothing insulation (clo) | 1 | Numeric clo value (approx. 0.5–1.5 etc.) | Estimation based on ISO 9920 tables {cite:p}`noauthor_iso_2007`; or lab-specific lookup |
|  | Outdoor weather context | 2–3 | Simple categories: “cold spell”, “typical”, “heatwave”, or link to local weather series | Researcher notes — weather data assumed to be measured or obtained from nearest meteorological station |
|  | Use of additional personal conditioning | 2–3 | Yes/No; type (fan, blanket, personal heater, etc.) | Observed + logged when allowed by protocol |
| **Protocol adherence** | Pre-session restriction compliance | 1–2 | Yes/No; if No: short description (e.g. “coffee 2 h before”, “ran to lab”) | Checklist based on study instructions (no alcohol, no caffeine, etc.) |
|  | Arrival time to lab | 2 | Clock time | — |
|  | Waiting / acclimation period | 2 | Minutes from arrival to session start (numeric) | Derived from times; duration should be standardised |
| **Scheduling & circadian context** | Sleep-wake times | 1–2 | Clock time, 24 h | Sleep log / app |
|  | Sleep duration last night | 1 | Numeric (hours slept; e.g. 6.8) | Derived from log |
|  | Sleep quality last night | 1–2 | 0–10 scale or 1–5 Likert | Subjective rating |
|  | Recent night-shift work | 2 | Yes/No; description (e.g. “3 consecutive night shifts in last week”) | Sleep log / app |
| **Acute health state (today / last few days)** | Recent acute illness (last 7 days) | 1–2 | Yes/No; short description (e.g. “URI with fever”, “GI infection”) | PAR-Q+ style yes/no items; brief medical history |
|  | Fever symptoms in last 48 h | 2 | Yes/No; peak temperature if known | — |
|  | Antipyretic use (last 48 h) | 2 | Yes/No; drug name and approximate time (free text) | — |
|  | Compression garments worn today | 2 | Yes/No; if Yes: type and sites covered | Compression lowers local Tsk at covered sites; flag if measurement site is affected {cite:p}`partsch_compression_2012` |
|  | Post-viral / long COVID symptoms today | 2 | Yes/No; if Yes: temperature dysregulation / sweating abnormality / orthostatic intolerance / other | Acute-day expression of chronic dysautonomia may vary; capture alongside stable participant-level flag {cite:p}`dani_autonomic_2021` |
|  | New medications since previous session | 2 | Yes/No; if Yes: names and doses (free text) | — |
| **Behaviour since waking (session-day)** | Time since last meal at start | 1–2 | Numeric (hours); optional category (light / normal / heavy); Yes/No if a specific fasting time was instructed (e.g. “Did not eat in the last 12 hours”) | — |
|  | Time since last caffeine | 1–2 | Numeric (hours); type (coffee / tea / energy drink / other); Yes/No if a specific fasting time was instructed (e.g. “Did not drink coffee in the last 12 hours”) | — |
|  | Time since last moderate/vigorous exercise | 2 | Numeric (hours); or category (<4 h, 4–12 h, >12 h); Yes/No if a specific fasting time was instructed (e.g. “Did not exercise in the last 12 hours”) | Short structured item; can echo IPAQ intensity definitions |
|  | Alcohol intake in last 24 h | 2 | Yes/No; rough units or category (none / 1–2 / 3–5 / >5) | AUDIT-C wording if more structure is needed; alternatively an alcohol test can be done before each session |
|  | Antiperspirant applied to measurement sites (last 48 h) | 2 | Yes/No; if Yes: which sites | Aluminium-based antiperspirants reduce local sweat rate by 20–60 % for 24–48 h. Participants should be instructed to abstain from application to measurement sites before the session {cite:p}`quatrale_mechanism_1981,baker_physiology_2019` |
|  | Melatonin taken (last 4 h) | 2 | Yes/No; if Yes: dose (mg) and time taken | Exogenous melatonin raises distal Tsk and DPG; acutely relevant for skin temperature and sleep protocols {cite:p}`krauchi_thermoregulatory_2006` |
|  | NSAIDs or analgesics taken (last 12 h) | 2 | Yes/No; if Yes: drug name and approximate time | NSAIDs can transiently alter autonomic tone; document alongside other acute medications {cite:p}`thayer_relationship_2010` |
|  | Smoking / vaping today | 2–3 | Yes/No; approximate cigarettes/vapes since waking | — |
| **Hormonal & reproductive (per session info)** | Menstrual {ref}`phase <label-phase>` at session | 1 | Categorical (e.g. early follicular, late follicular, mid-luteal, perimenopausal, postmenopausal, unknown) | Derived from self-reported menstrual dates; optionally hormone assays |
|  | Pregnancy / breastfeeding status | 2 | Yes/No; if Yes: notes | Pregnancy tests can be done before each experiment/session when needed |
| **Events & deviations** | Acute events during session | 1–2 | Free text (e.g. “felt faint at 20:10, paused”, “strong emotional phone call at 21:00”) | End-of-session log entry |
|  | Bathroom visits | 2–3 | Times or time ranges; optional volume where measured | Manually logged; useful for future detection of outside-lab/uncontrolled exposure times |
|  | Food / drink provided | 2–3 | Type and energy content (kcal) if standardised | Study-specific (e.g. Huel Liquid Drink) |
|  | Required calories | 2–3 | Calculated kcal requirement via BMR equations | St. Jeor-Mifflin {cite:p}`mifflin_new_1990` or similar |
|  | Food / drink consumed | 2–3 | Estimated intake (kcal or %) + timing | Participant-specific |
|  | Major protocol deviations | 1–2 | Free text (e.g. “session ended early”, “CBT probe dislodged”, “BP failed for 30 min”) | Protocol deviation form |
|  | Free-text notes | 2 | Any other remarks that help interpret data | — |

:::

+ For studies applying many sensors simultaneously, these per-device fields may be implemented as a separate *sensor_application.tsv* with one row per device per session, using the same field definitions. The Device IDs used and Calibration IDs active fields in the session row then serve as a summary index pointing to that file.