# Session-level metadata




Session-level metadata captures all information that varies from one visit or experimental condition to the next for a given participant. Many of the acute modifiers discussed in Section 2—such as last night’s sleep, time since waking, recent illness, caffeine or meal timing, and daily hormonal fluctuations—change from day to day and therefore must be recorded at the session rather than participant level.



Each session is represented by one row in a dedicated metadata table, with one column per session field. As with the experiment- and participant-level schemas, fields are grouped by topic (e.g., Identifiers & Timing, Devices & Logistics, Protocol Adherence, Acute Health State) and assigned to informal tiers:



- <u>Tier 1 – Core:</u> Essential variables recorded for every visit (e.g., session ID, date and time, condition code, clothing, sleep duration, pre-session restrictions, acute illness indicators).



- <u>Tier 2 – Recommended:</u> Factors that meaningfully influence thermophysiological responses but may not always be collected (e.g., researchers present, acclimation period, night-shift work, time since exercise).



- <u>Tier 3 – Specialised:</u> Detailed or study-specific variables, such as exact bathroom break volumes, caloric intake calculations, event logs, or fine-grained environmental contextualisation.



Individual studies may extend this table with experiment-specific columns, such as time points for discrete measurements, cognitive task blocks, stepwise heating/cooling adjustments, water-intake increments, or protocol deviations. The core fields remain comparable across studies, facilitating harmonisation and meta-analysis.



Session metadata can be recorded via paper logs, REDCap/Qualtrics forms, or digital forms directly linked to the underlying session table.



<table style="width:97%;">

<caption><p>Table 11. Example session-level metadata schema, organised by group, tier, and typical data formats, with optional references to instruments or logging tools.</p></caption>

<colgroup>

<col style="width: 18%" />

<col style="width: 16%" />

<col style="width: 5%" />

<col style="width: 28%" />

<col style="width: 28%" />

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

<td>Identifiers &amp; timing</td>

<td>Session ID</td>

<td>1</td>

<td>Unique ID per visit/condition (e.g. P01_S1, P03_C01_Armchair)</td>

<td>Lab-defined</td>

</tr>

<tr>

<td></td>

<td>Participant ID</td>

<td>1</td>

<td>Unique participant code linked to master table (P01, SL23_001, etc.)</td>

<td>Lab-defined</td>

</tr>

<tr>

<td></td>

<td>Date</td>

<td>1</td>

<td>Calendar date</td>

<td>– YYYY-MM-DD or format noted</td>

</tr>

<tr>

<td></td>

<td>Session start time</td>

<td>1</td>

<td>24-h clock time or UNIX timestamp</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Session end time</td>

<td>1</td>

<td>24-h clock time or UNIX timestamp</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Condition / scenario code</td>

<td>1</td>

<td>Text label for assigned condition (e.g. C01_01, Heat_26C, Night_Armchair)</td>

<td>Lab-defined</td>

</tr>

<tr>

<td></td>

<td>Location / room</td>

<td>1</td>

<td>Room or laboratory code</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Researchers present</td>

<td>2</td>

<td>Initials or staff codes</td>

<td>–</td>

</tr>

<tr>

<td>Devices &amp; protocol logistics</td>

<td>Device IDs used</td>

<td>1</td>

<td>ID numbers for all devices applied to this participant</td>

<td>Internal device inventory</td>

</tr>

<tr>

<td></td>

<td>Device attachment / ingestion times</td>

<td>1</td>

<td>Clock times per device (e.g., “CBT pill ingested 17:50”, “Sensors attached 17:55”)</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Device attachment type</td>

<td>1</td>

<td>Attachment type per device, when relevant (e.g., “Skin temperature sensor IDXXXXX: Medical tape”)</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Condition order / randomisation code</td>

<td>1</td>

<td>Randomisation sequence label (e.g., “Sequence A: warm → neutral → cool”)</td>

<td>Study randomisation plan</td>

</tr>

<tr>

<td></td>

<td>Calibration / zeroing performed</td>

<td>2</td>

<td>Yes/No + short note (e.g., “BP device calibrated 2025-06-01”)</td>

<td>Device calibration logs</td>

</tr>

<tr>

<td rowspan="4">Environment &amp; exposure (session context)</td>

<td>Clothing description</td>

<td>1</td>

<td>Free text description (e.g. “T-shirt, jeans, socks”)</td>

<td>–</td>

</tr>

<tr>

<td>Clothing insulation (clo)</td>

<td>1</td>

<td>Numeric clo value (approx. 0.5–1.5 etc.)</td>

<td>Estimation based on ISO 9920 tables; or lab-specific lookup</td>

</tr>

<tr>

<td>Outdoor weather context</td>

<td>2–3</td>

<td>Simple categories: “cold spell”, “typical”, “heatwave”, or link to local weather series</td>

<td>Researcher notes – weather data assumed to be measured or obtained from nearest meteorological station</td>

</tr>

<tr>

<td>Use of additional personal conditioning</td>

<td>2–3</td>

<td>Yes/No; type (fan, blanket, personal heater, etc.)</td>

<td>Observed + logged when allowed by protocol</td>

</tr>

<tr>

<td>Protocol adherence</td>

<td>Pre-session restriction compliance</td>

<td>1–2</td>

<td>Yes/No; if No: short description (e.g. “coffee 2 h before”, “ran to lab”)</td>

<td>Checklist based on study instructions (no alcohol, no caffeine, etc.)</td>

</tr>

<tr>

<td></td>

<td>Arrival time to lab</td>

<td>2</td>

<td>Clock time</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Waiting / acclimation period</td>

<td>2</td>

<td>Minutes from arrival to session start (numeric)</td>

<td>Derived from times, duration should be standardised</td>

</tr>

<tr>

<td>Scheduling &amp; circadian context</td>

<td>Sleep-wake times</td>

<td>1–2</td>

<td>Clock time, 24 h</td>

<td>Sleep log / app</td>

</tr>

<tr>

<td></td>

<td>Sleep duration last night</td>

<td>1</td>

<td>Numeric (hours slept; e.g. 6.8)</td>

<td>Derived from log</td>

</tr>

<tr>

<td></td>

<td>Sleep quality last night</td>

<td>1–2</td>

<td>0–10 scale or 1–5 Likert</td>

<td>Subjective rating</td>

</tr>

<tr>

<td></td>

<td>Recent night-shift work</td>

<td>2</td>

<td>Yes/No; description (e.g. “3 consecutive night shifts in last week”)</td>

<td>Sleep log / app</td>

</tr>

<tr>

<td>Acute health state (today / last few days)</td>

<td>Recent acute illness (last 7 days)</td>

<td>1–2</td>

<td>Yes/No; short description (“URI with fever”, “GI infection”)</td>

<td>PAR-Q+ style yes/no items; brief medical history</td>

</tr>

<tr>

<td></td>

<td>Fever symptoms in last 48 h</td>

<td>2</td>

<td>Yes/No; peak temperature if known</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Antipyretic use (last 48 h)</td>

<td>2</td>

<td>Yes/No; drug name and approximate time (free text)</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>New medications since previous session</td>

<td>2</td>

<td>Yes/No; if Yes: names and doses (free text)</td>

<td>–</td>

</tr>

<tr>

<td>Behaviour since waking (session-day)</td>

<td>Time since last meal at start</td>

<td>1–2</td>

<td>Numeric (hours); optional category (light / normal / heavy); Yes/No if a specific fasting time was instructed (e.g. “Did not eat in the last 12 hours”)</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Time since last caffeine</td>

<td>1–2</td>

<td>Numeric (hours); type (coffee / tea / energy drink / other); Yes/No if a specific fasting time was instructed (e.g. “Did not drink coffee in the last 12 hours”)</td>

<td>–</td>

</tr>

<tr>

<td></td>

<td>Time since last moderate/vigorous exercise</td>

<td>2</td>

<td>Numeric (hours); or category (&lt;4 h, 4–12 h, &gt;12 h); Yes/No if a specific fasting time was instructed (e.g. “Did not exercise in the last 12 hours”)</td>

<td>Short structured item; can echo IPAQ intensity definitions</td>

</tr>

<tr>

<td></td>

<td>Alcohol intake in last 24 h</td>

<td>2</td>

<td>Yes/No; rough units or category (none / 1–2 / 3–5 / &gt;5)</td>

<td>AUDIT-C wording if more structure needed; alternatively an alcohol test can be done before each session</td>

</tr>

<tr>

<td></td>

<td>Smoking / vaping today</td>

<td>2–3</td>

<td>Yes/No; approximate cigarettes/vapes since waking</td>

<td>–</td>

</tr>

<tr>

<td>Hormonal &amp; reproductive (per session info)</td>

<td>Menstrual phase at session</td>

<td>1</td>

<td>Categorical (e.g. early follicular, late follicular, mid-luteal, perimenopausal, postmenopausal, unknown)</td>

<td>Derived from self-reported menstrual dates; optionally hormone assays</td>

</tr>

<tr>

<td></td>

<td>Pregnancy / breastfeeding status</td>

<td>2</td>

<td>Yes/No; if Yes: notes</td>

<td>Pregnancy tests can be done before each experiment/session when needed</td>

</tr>

<tr>

<td>Events &amp; deviations</td>

<td>Acute events during session</td>

<td>1–2</td>

<td>Free text (e.g. “felt faint at 20:10, paused”, “strong emotional phone call at 21:00”)</td>

<td>End-of-session log entry</td>

</tr>

<tr>

<td></td>

<td>Bathroom visits</td>

<td>2–3</td>

<td>Times or time ranges; optional volume where measured</td>

<td>Manually logged, useful for future detection of outside-lab/uncontrolled exposure times</td>

</tr>

<tr>

<td></td>

<td>Food / drink provided</td>

<td>2–3</td>

<td>Type and energy content (kcal) if standardised</td>

<td>Study-specific (e.g. Huel Liquid Drink)</td>

</tr>

<tr>

<td></td>

<td>Required calories</td>

<td>2–3</td>

<td>Calculated kcal requirement via BMR equations</td>

<td>Formulas St. Jeor-Mifflin <a class="citation" href="/09_references/09_01_references/#ref-538" data-cite="538">[538]</a> or similar</td>

</tr>

<tr>

<td></td>

<td>Food / drink consumed</td>

<td>2–3</td>

<td>Estimated intake (kcal or %) + timing</td>

<td>Participant-specific</td>

</tr>

<tr>

<td></td>

<td>Major protocol deviations</td>

<td>1–2</td>

<td>Free text (e.g. “session ended early”, “CBT probe dislodged”, “BP failed for 30 min”)</td>

<td>Protocol deviation form</td>

</tr>

<tr>

<td></td>

<td>Free-text notes</td>

<td>2</td>

<td>Any other remarks that help interpret data</td>

<td>–</td>

</tr>

</tbody>

</table>
