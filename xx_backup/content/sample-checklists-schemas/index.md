# SAMPLE CHECKLISTS & SCHEMAS

This appendix illustrates one practical way to structure experiment-, participant-, and session-level documentation for human thermal physiology studies. The goal is not to prescribe a new field-wide standard, but to make our own approach transparent and to provide concrete examples that other groups can adapt and share. By circulating comparable schemas, the field can gradually converge on common reporting practices and enable more reproducible, interoperable datasets.

The structure mirrors other established data standards for human studies, such as the Brain Imaging Data Structure (BIDS) []{cite:p}`gorgolewski_brain_2016`, which separates participants.tsv and sessions.tsv files, and the ISA-Tab framework []{cite:p}`sansone_toward_2012`, which distinguishes investigation, study, and assay metadata. Our schema follows a similar logic: clean separation of persistent attributes, per-experiment descriptors, and per-visit variables.

We distinguish three levels:

- Experiment metadata: one record per study or protocol. Stores high-level information: title, lab, institute, recruitment window, primary endpoints, general exposure types (lab vs field, heat vs cold vs neutral), and ethics approval identifiers.

- Participant metadata: one record per person, containing attributes that change slowly or not at all during the study. Stores demographics, morphology, health and diagnoses, hormonal status, lifestyle, sleep and chronotype, thermal sensitivity, and (optionally) built-environment context.

- Session metadata: one record per visit or experimental condition per person. Stores per-visit timing, condition labels, acute state (sleep, illness, recent behaviour), clothing and activity, and key protocol deviations.

- 

- This separation reflects how physiological data are actually generated: experiments define the protocol; participants bring stable individual characteristics; and sessions capture the day-to-day variability that strongly shapes thermoregulatory responses.

Device inventories (sensor IDs, firmware versions, calibration logs) are stored in separate tables and linked to specific sessions and experiments. Separating device metadata helps manage multi-sensor setups, facilitates troubleshooting, and supports later data harmonisation.
