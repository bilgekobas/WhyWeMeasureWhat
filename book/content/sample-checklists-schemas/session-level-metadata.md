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
| | Experiment ID | 1 | Stable experiment identifier | Foreign key |
| | Participant ID | 1 | Unique participant code linked to master table (P01, SL23_001, etc.) | Lab-defined |
| | Date | 1 | Calendar date | YYYY-MM-DD or format noted |
| | Session start time | 1 | 24-h clock time or UNIX timestamp | — |
| | Session end time | 1 | 24-h clock time or UNIX timestamp | — |
| | Condition / scenario code | 1 | Text label for assigned condition (e.g. C01_01, Heat_26C, Night_Armchair) | Lab-defined |
| | Actual normalisation duration (min) | 1 | Numeric minutes | Separate from planned normalisation and waiting |
| | Previous-session interval (days) | 2 | Numeric / not_applicable | Actual elapsed time |
| | Location / room | 1 | Room or laboratory code | — |
| | Researchers present | 2 | Initials or staff codes | — |
| | Sensor application record reference | 1 | Linked sensor-application record ID(s) or URI | Authoritative per-session link to actual unit, calibration, placement, configuration and recording times; inherit defaults |
| | Sequence position / randomisation code | 1 | Randomisation sequence label (e.g. "Sequence A: warm → neutral → cool") | Actual sequence/condition position, not the planned randomisation method |
| **Environment & exposure (session context)** | Clothing description | 1 | Free text description (e.g. “T-shirt, jeans, socks”) | Realised ensemble; can inherit planned experiment-level specification if unchanged |
| | Clothing insulation (clo) | 1 | Numeric clo value (approx. 0.5–1.5 etc.) | Realised or estimated clo; inherit planned value when unchanged; ISO 9920 {cite:p}`noauthor_iso_2007` |
| | Actual/estimated MET (session) | 2 | Numeric MET / not_applicable; method and timing | Record realised or estimated activity intensity; inherit planned activity/MET from experiment when unchanged |
| | Use of additional personal conditioning | 2–3 | Yes/No; type (fan, blanket, personal heater, etc.) | Observed + logged when allowed by protocol |
| **Protocol adherence** | Overall compliance | 1 | Yes / No / Partial; describe deviation | Summary adherence assessment; specific incidents are documented in Session events and deviations |
|  | Pre-session compliance | 2 | Yes / No / Partial / not_applicable | Compliance with pre-session restrictions |
|  | Clothing compliance | 1 (conditional) | Yes / No / Partial / not_applicable | Relative to prescribed clothing |
|  | Activity compliance | 1 (conditional) | Yes / No / Partial / not_applicable; describe any departure | Compare actual activity with prescribed activity; describe departures in Session events and deviations |
|  | Timing compliance | 1 (conditional) | Yes / No / Partial / not_applicable | Relative to scheduled exposure and measurement timing |
| **Scheduling & circadian context** | Sleep-wake times | 2 | Clock time, 24 h | Sleep log / app |
| | Sleep duration last night | 2 | Numeric (hours slept; e.g. 6.8) | Derived from log |
| | Sleep quality last night | 2 | 0–10 scale or 1–5 Likert | Subjective rating |
| | Recent night-shift work | 3 | Yes/No; description (e.g. “3 consecutive night shifts in last week”) | Sleep log / app |
| **Acute health state (today / last few days)** | Recent acute illness (last 7 days) | 1–2 | Yes/No; short description (e.g. “URI with fever”, “GI infection”) | PAR-Q+ style yes/no items; brief medical history |
| | Fever symptoms in last 48 h | 2 | Yes/No; peak temperature if known | — |
| | Antipyretic use (last 48 h) | 2 | Yes/No; drug name and approximate time (free text) | — |
| | Recent medication/supplement use | 2 | Free text: medication/supplement, dose and timing; none / unknown | Include new medication, melatonin, NSAIDs or analgesics when relevant; do not duplicate participant-level habitual medications |
| **Behaviour since waking (session-day)** | Time since last meal at start | 1–2 | Numeric (hours); optional category (light / normal / heavy); Yes/No if a specific fasting time was instructed (e.g. “Did not eat in the last 12 hours”) | — |
| | Time since last caffeine | 1–2 | Numeric (hours); type (coffee / tea / energy drink / other); Yes/No if a specific fasting time was instructed (e.g. “Did not drink coffee in the last 12 hours”) | — |
| | Time since last moderate/vigorous exercise | 2 | Numeric (hours); or category (<4 h, 4–12 h, >12 h); Yes/No if a specific fasting time was instructed (e.g. “Did not exercise in the last 12 hours”) | Short structured item; can echo IPAQ intensity definitions |
| | Alcohol intake in last 24 h | 2 | Yes/No; rough units or category (none / 1–2 / 3–5 / >5) | AUDIT-C wording if more structure is needed; alternatively an alcohol test can be done before each session |
| | Smoking / vaping today | 2–3 | Yes/No; approximate cigarettes/vapes since waking | — |
|  | Recent medication and supplement context | 2 | Use the single Recent medication/supplement use field | No duplicate entries; see acute health section |
| **Hormonal & reproductive (per session info)** | Menstrual cycle day | 1 (conditional) | Cycle day / unknown / not_applicable | Where scientifically and ethically applicable |
| | Menstrual {ref}`phase <label-phase>` at session | 1 (conditional) | Categorical (e.g. early follicular, late follicular, mid-luteal, perimenopausal, postmenopausal, unknown) | Derived from self-reported menstrual dates; optionally hormone assays |
| | Pregnancy / breastfeeding status | 2 | Yes/No; if Yes: notes | Pregnancy tests can be done before each experiment/session when needed |
| **Food & drink intake (realised)** | Food / drink consumed during session | 2 (conditional) | Item, quantity and time; optional kcal | Record actual intake or link to a separate time-stamped intake/event log; planned provision belongs to experiment level |
| **Events & deviations** | Session events and deviations | 1 (conditional) | Event type (physiological / behavioural / protocol / sensor-related); timestamp, duration, description and consequence; none if absent | One record per event, optionally in a linked time-stamped event log; includes interruptions, sensor problems and departures from protocol without duplicate fields |
| | Free-text notes | 2 | Any other remarks that help interpret data | — |

:::

+ For studies applying many sensors simultaneously, these per-device fields may be implemented as a separate *sensor_application.tsv* with one row per device per session, using the same field definitions. The Device IDs used and Calibration IDs active fields in the session row then serve as a summary index pointing to that file.

Experiment-level measurement definitions are inherited. For multiple simultaneous sensors, actual unit IDs, placement/configuration overrides, and application/recording times may be stored in a linked sensor-application table, referenced by session ID. Menstrual fields are conditionally Core.
