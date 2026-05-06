# Experiment-level metadata




Experiment-level metadata capture the high-level characteristics of a study: where and when it was conducted, by whom, under which ethical approvals, and what its overall design and planned exposures were. These fields describe the protocol as a whole, independently of any particular participant or session, and form the top level of the metadata hierarchy.



To make the schema easier to reuse across different laboratories and study types, fields are grouped by topic and are assigned to three informal tiers:



- <u>Tier 1 – Core experiment descriptors:</u> Essential information needed to interpret or reuse a study, including experiment identifiers, institutional affiliation, ethics approval, study design and environment, recruitment window, and the main exposure/intervention categories.



- <u>Tier 2 – Recommended descriptors:</u> Information that improves reproducibility and interpretability but may not always be available, such as randomisation method, blinding, standardised behavioural instructions, number and naming of conditions, and detailed environmental or HVAC descriptions.



- <u>Tier 3 – Specialised descriptors:</u> More specific contextual information that is useful for certain study types or advanced meta-analyses, including room geometry, calibration summaries, or detailed equipment notes. These fields are optional but help achieve FAIR-level documentation when available.



To aid cross-study comparison, we also include a concise PICOT summary for each experiment. PICOT provides a high-level, non-redundant synopsis of the Population, Intervention, Comparison, Outcomes, and Time frame, complementing (but not duplicating) the detailed metadata fields.



<table>

<caption><p>Table 9. Experiment-level metadata schema, organised by group and tier.</p></caption>

<colgroup>

<col style="width: 13%" />

<col style="width: 20%" />

<col style="width: 5%" />

<col style="width: 29%" />

<col style="width: 30%" />

</colgroup>

<thead>

<tr>

<th><strong>Group</strong></th>

<th><strong>Field name</strong></th>

<th><strong>Tier</strong></th>

<th><strong>Typical answers / coding</strong></th>

<th><strong>Notes / considerations</strong></th>

</tr>

</thead>

<tbody>

<tr>

<td rowspan="9">Core IDs</td>

<td>Experiment ID</td>

<td>1</td>

<td>Unique alphanumeric code</td>

<td>–</td>

</tr>

<tr>

<td>Experiment name</td>

<td>1</td>

<td>Descriptive title</td>

<td>–</td>

</tr>

<tr>

<td>Principal investigator/s</td>

<td>1</td>

<td>Name/s or initials</td>

<td>–</td>

</tr>

<tr>

<td>Researcher/s</td>

<td>1</td>

<td>Name/s or initials</td>

<td>–</td>

</tr>

<tr>

<td>Contact person</td>

<td>1</td>

<td>Single designated contact</td>

<td>–</td>

</tr>

<tr>

<td>Contact information</td>

<td>1</td>

<td>Email</td>

<td>–</td>

</tr>

<tr>

<td>Lab/s</td>

<td>1</td>

<td>Lab or unit name</td>

<td>–</td>

</tr>

<tr>

<td>Institute/s</td>

<td>1</td>

<td>Organisational affiliation</td>

<td>–</td>

</tr>

<tr>

<td>Location/s</td>

<td>1</td>

<td>City, country, optionally coordinates or street address</td>

<td>High-resolution location info helps with automated climate data and time zone</td>

</tr>

<tr>

<td rowspan="6">Ethics &amp; governance</td>

<td>Ethics committee</td>

<td>1</td>

<td>Full name</td>

<td>–</td>

</tr>

<tr>

<td>Ethics approval ID/Code</td>

<td>1</td>

<td>Approval number</td>

<td>–</td>

</tr>

<tr>

<td>Approval date</td>

<td>2</td>

<td>YYYY-MM-DD</td>

<td>–</td>

</tr>

<tr>

<td>Amendments/versions</td>

<td>2</td>

<td>Yes/No; brief notes</td>

<td>–</td>

</tr>

<tr>

<td>Data protection compliance</td>

<td>1</td>

<td>GDPR, HIPAA, other</td>

<td>–</td>

</tr>

<tr>

<td>Preregistration ID</td>

<td>2–3</td>

<td>OSF/clinicaltrials.gov link</td>

<td>–</td>

</tr>

<tr>

<td rowspan="5">Study type</td>

<td>Study environment</td>

<td>1</td>

<td>Laboratory, Field, Hybrid</td>

<td>–</td>

</tr>

<tr>

<td>Study design</td>

<td>1</td>

<td>Controlled/Observational/Interventional</td>

<td>–</td>

</tr>

<tr>

<td>Experimental structure</td>

<td>2</td>

<td>Between-subjects, Within-subjects, Repeated measures, Crossover, Pre-Post, etc.</td>

<td>Multiple can apply</td>

</tr>

<tr>

<td>Randomisation</td>

<td>2</td>

<td>Yes/No; method (simple, block, Latin square)</td>

<td>Links to randomisation table</td>

</tr>

<tr>

<td>Blinding</td>

<td>1</td>

<td>None/Single-blind/Double-blind</td>

<td>If None, a short description nice to have</td>

</tr>

<tr>

<td rowspan="5">Timing &amp; Schedule</td>

<td>Start date of the experiment</td>

<td>1</td>

<td>YYYY-MM-DD</td>

<td>–</td>

</tr>

<tr>

<td>End date of the experiment</td>

<td>1</td>

<td>YYYY-MM-DD</td>

<td>–</td>

</tr>

<tr>

<td>Typical session duration</td>

<td>1</td>

<td>Minutes or hours</td>

<td>–</td>

</tr>

<tr>

<td>Standard session start time</td>

<td>1</td>

<td>hh:mm, 24 h time</td>

<td>–</td>

</tr>

<tr>

<td>Standard session end time</td>

<td>1</td>

<td>hh:mm, 24 h time</td>

<td>–</td>

</tr>

<tr>

<td rowspan="9">Study population</td>

<td>Target sample size</td>

<td>1</td>

<td>Integer</td>

<td>–</td>

</tr>

<tr>

<td>Achieved sample size</td>

<td>1</td>

<td>Integer</td>

<td>–</td>

</tr>

<tr>

<td>Male participants</td>

<td>1</td>

<td>Integer</td>

<td>–</td>

</tr>

<tr>

<td>Female participants</td>

<td>1</td>

<td>Integer</td>

<td>–</td>

</tr>

<tr>

<td>Intersex participants</td>

<td>1</td>

<td>Integer</td>

<td>–</td>

</tr>

<tr>

<td>Age range</td>

<td>1</td>

<td>Minimum-maximum</td>

<td>“21–35 years”</td>

</tr>

<tr>

<td>Population description</td>

<td>1</td>

<td>Free text</td>

<td>e.g., “Healthy university students”, “Sedentary adults aged 20–40”</td>

</tr>

<tr>

<td>Inclusion criteria</td>

<td>1</td>

<td>Free text or list</td>

<td>–</td>

</tr>

<tr>

<td>Exclusion criteria</td>

<td>1</td>

<td>Free text or list</td>

<td>–</td>

</tr>

<tr>

<td rowspan="5">Intervention</td>

<td>Study domain/s</td>

<td>1</td>

<td>Thermal / Humidity / Air velocity / Lighting / Air quality / Noise</td>

<td>Multiple allowed</td>

</tr>

<tr>

<td>Intervention description</td>

<td>1</td>

<td>Free text</td>

<td>Describe all manipulated variables</td>

</tr>

<tr>

<td>Number of conditions</td>

<td>2</td>

<td></td>

<td>–</td>

</tr>

<tr>

<td>Condition labels</td>

<td>2</td>

<td></td>

<td>–</td>

</tr>

<tr>

<td>Standardised behaviour rules</td>

<td>1</td>

<td>Resting, sitting, acclimatisation/normalisation, movement, eating, drinking protocols, etc.</td>

<td>–</td>

</tr>

<tr>

<td rowspan="6">Environment &amp; equipment (experiment-level)</td>

<td>Spatial typology</td>

<td>1</td>

<td>Office / Residential / Educational / Public / etc.</td>

<td>–</td>

</tr>

<tr>

<td>HVAC system description</td>

<td>2</td>

<td>AC model, radiant panel specs, air velocity sources</td>

<td>–</td>

</tr>

<tr>

<td>Room dimensions</td>

<td>3</td>

<td>m² or m³</td>

<td>–</td>

</tr>

<tr>

<td>Baseline environmental control</td>

<td>1</td>

<td>Air temperature, radiant temperature, humidity, lighting ranges, etc.</td>

<td>Multiple allowed</td>

</tr>

<tr>

<td>Primary instruments used</td>

<td>1</td>

<td>Names + IDs</td>

<td>Linked to external Sensors table if exists</td>

</tr>

<tr>

<td>Instrument calibration notes</td>

<td>3</td>

<td>Summary + links to logs</td>

<td>Linked to external Sensors table if exists</td>

</tr>

<tr>

<td>PICOT Summary</td>

<td>P – Population</td>

<td>1</td>

<td>Short description of target group and key eligibility criteria</td>

<td>“Healthy adults 18–35, BMI 18–25, non-smokers; no CV/metabolic disease; regular sleep schedule”</td>

</tr>

<tr>

<td></td>

<td>I – Intervention / exposure</td>

<td>1</td>

<td>Summary of main exposure(s) or experimental condition(s)</td>

<td>“14-day heat acclimation: AC at 26 °C vs free-running apartment (summer conditions)”</td>

</tr>

<tr>

<td></td>

<td>C – Comparison / control conditions</td>

<td>1</td>

<td>Description of comparator condition(s)</td>

<td>“Free-running cooling vs constant AC; within-subject crossover” or “Neutral 24 °C control”</td>

</tr>

<tr>

<td></td>

<td>O – Primary outcome(s</td>

<td>1</td>

<td>List main endpoints and how they are quantified</td>

<td>“Core body temperature, neck/ankle skin temp, HR, BP, HRV (RMSSD), thermal sensation”</td>

</tr>

<tr>

<td></td>

<td>O – Secondary outcomes</td>

<td>2</td>

<td>Additional exploratory endpoints (no units or detail)</td>

<td>“Sleep onset latency, actigraphy-based sleep efficiency, melatonin AUC”</td>

</tr>

<tr>

<td></td>

<td>T – Time frame</td>

<td>1</td>

<td>Time horizon for the effect and measurement</td>

<td>“Pre–post mild heat stress test before and after 14-day exposure; tests between 09:00–16:00”</td>

</tr>

</tbody>

</table>
