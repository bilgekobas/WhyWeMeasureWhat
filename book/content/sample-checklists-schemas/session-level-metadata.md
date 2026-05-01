# Session-level metadata

Session-level metadata captures all information that varies from one visit or experimental condition to the next for a given participant. Many of the acute modifiers discussed in Section 2---such as last night's sleep, time since waking, recent illness, caffeine or meal timing, and daily hormonal fluctuations---change from day to day and therefore must be recorded at the session rather than participant level.

Each session is represented by one row in a dedicated metadata table, with one column per session field. As with the experiment- and participant-level schemas, fields are grouped by topic (e.g., Identifiers & Timing, Devices & Logistics, Protocol Adherence, Acute Health State) and assigned to informal tiers:

- <u>Tier 1 -- Core:</u> Essential variables recorded for every visit (e.g., session ID, date and time, condition code, clothing, sleep duration, pre-session restrictions, acute illness indicators).

- <u>Tier 2 -- Recommended:</u> Factors that meaningfully influence thermophysiological responses but may not always be collected (e.g., researchers present, acclimation period, night-shift work, time since exercise).

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
| **Devices & protocol logistics** | Device IDs used | 1 | ID numbers for all devices applied to this participant | Internal device inventory |
|  | Device attachment / ingestion times | 1 | Clock times per device (e.g. “CBT pill ingested 17:50”, “Sensors attached 17:55”) | — |
|  | Device attachment type | 1 | Attachment type per device, when relevant (e.g. “Skin temperature sensor IDXXXXX: Medical tape”) | — |
|  | Condition order / randomisation code | 1 | Randomisation sequence label (e.g. “Sequence A: warm → neutral → cool”) | Study randomisation plan |
|  | Calibration / zeroing performed | 2 | Yes/No + short note (e.g. “BP device calibrated 2025-06-01”) | Device calibration logs |
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
|  | New medications since previous session | 2 | Yes/No; if Yes: names and doses (free text) | — |
| **Behaviour since waking (session-day)** | Time since last meal at start | 1–2 | Numeric (hours); optional category (light / normal / heavy); Yes/No if a specific fasting time was instructed (e.g. “Did not eat in the last 12 hours”) | — |
|  | Time since last caffeine | 1–2 | Numeric (hours); type (coffee / tea / energy drink / other); Yes/No if a specific fasting time was instructed (e.g. “Did not drink coffee in the last 12 hours”) | — |
|  | Time since last moderate/vigorous exercise | 2 | Numeric (hours); or category (<4 h, 4–12 h, >12 h); Yes/No if a specific fasting time was instructed (e.g. “Did not exercise in the last 12 hours”) | Short structured item; can echo IPAQ intensity definitions |
|  | Alcohol intake in last 24 h | 2 | Yes/No; rough units or category (none / 1–2 / 3–5 / >5) | AUDIT-C wording if more structure is needed; alternatively an alcohol test can be done before each session |
|  | Smoking / vaping today | 2–3 | Yes/No; approximate cigarettes/vapes since waking | — |
| **Hormonal & reproductive (per session info)** | Menstrual phase at session | 1 | Categorical (e.g. early follicular, late follicular, mid-luteal, perimenopausal, postmenopausal, unknown) | Derived from self-reported menstrual dates; optionally hormone assays |
|  | Pregnancy / breastfeeding status | 2 | Yes/No; if Yes: notes | Pregnancy tests can be done before each experiment/session when needed |
| **Events & deviations** | Acute events during session | 1–2 | Free text (e.g. “felt faint at 20:10, paused”, “strong emotional phone call at 21:00”) | End-of-session log entry |
|  | Bathroom visits | 2–3 | Times or time ranges; optional volume where measured | Manually logged; useful for future detection of outside-lab/uncontrolled exposure times |
|  | Food / drink provided | 2–3 | Type and energy content (kcal) if standardised | Study-specific (e.g. Huel Liquid Drink) |
|  | Required calories | 2–3 | Calculated kcal requirement via BMR equations | St. Jeor-Mifflin {cite:p}`mifflin_new_1990` or similar |
|  | Food / drink consumed | 2–3 | Estimated intake (kcal or %) + timing | Participant-specific |
|  | Major protocol deviations | 1–2 | Free text (e.g. “session ended early”, “CBT probe dislodged”, “BP failed for 30 min”) | Protocol deviation form |
|  | Free-text notes | 2 | Any other remarks that help interpret data | — |

:::