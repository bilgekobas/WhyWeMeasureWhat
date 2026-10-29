# SAMPLE CHECKLISTS & SCHEMAS

This section provides structured documentation templates for human thermal physiology studies. The goal is not to prescribe a field-wide standard, but to make one coherent implementation transparent and to provide concrete examples that other groups can adapt and share. By circulating comparable schemas, the field can gradually converge on common reporting practices and enable more reproducible, interoperable datasets.

## Why these schemas are needed

Physiological variables with the same name are not necessarily comparable across studies. Their interpretation depends on the physiological process of interest, sensing method, anatomical location, timing, participant state, and the processing used to derive reported outcomes. These schemas are intended to document those dependencies, rather than require identical instruments or experimental protocols. They complement established standards for environmental measurement; they do not replace them.

The distinction is between *nominal completeness* (a signal or outcome is named) and *interpretive completeness* (the information needed to understand how it was obtained and whether it can be compared is available). The tables provide a practical starting point for documenting the latter.

## Structure

The documentation is organised across two parallel axes:

**Experimental context** follows a three-level hierarchy. Each level corresponds to a separate metadata table:

- [Experiment metadata](experiment-level-metadata): one record per study or protocol. Stores high-level information: title, lab, institute, recruitment window, primary endpoints, general exposure types (lab vs field, heat vs cold vs neutral), ethics approval identifiers, and links to the instruments and calibration records used.
- [Participant metadata](participant-level-metadata): one record per person, containing attributes that change slowly or not at all during the study. Stores demographics, morphology, health and diagnoses, hormonal status, lifestyle, sleep and {ref}`chronotype <label-chronotype>`, thermal sensitivity, and (optionally) built-environment context.
- [Session metadata](session-level-metadata): one record per visit or experimental condition per person. Stores realised timing, conditions, acute state, clothing and activity, adherence, and event records. Detailed sensor applications may be held in a linked table and referenced from the session.

**Sensor and device documentation** sits on a parallel axis and is described in a separate page:

- [Sensor & device metadata](sensor-device-metadata): two linked tables. The **Device Registry** identifies physical units (unique Device ID and serial number) and links each to its distinct model ID and signal-specific specifications and is filled once per device, reused across studies. The **Calibration Log** holds one record per calibration event per device (method, reference instrument, correction equation, pass/fail). Both tables connect to the experimental context hierarchy via Device IDs and Calibration IDs, which are referenced as foreign keys in the experiment and session schemas.

## Design principles

The schema follows the logic of established data standards for human studies. The three-level experimental hierarchy mirrors the Brain Imaging Data Structure (BIDS) {cite:p}`gorgolewski_brain_2016`, which separates `participants.tsv` and `sessions.tsv`, and the ISA-Tab framework {cite:p}`sansone_toward_2012`, which distinguishes investigation, study, and assay metadata. The Device Registry and Calibration Log extend this logic by treating measurement equipment as a separately maintained reference table — analogous to how BIDS handles electrode and channel descriptions.

All fields are assigned to one of three informal tiers:

- **Tier 1 — Core:** Essential for basic interpretability and reuse when applicable. Conditional requirements must be justified by the study design, population and signal.
- **Tier 2 — Recommended:** Meaningfully improves reproducibility and comparability. Complete where feasible.
- **Tier 3 — Specialised:** Useful for specific study types, meta-analyses, or FAIR-level documentation. Optional.

The specific fields and tiering logic presented here should be treated as provisional. Determining which descriptors are essential, recommended, or specialised ultimately requires community agreement. This schema is a structured starting point for iterative refinement.


## Applying the schemas

**Define measurements and questionnaires once.** At experiment level, describe each directly measured signal with its sensing method, default anatomical or environmental location, configured acquisition settings, and any derived metrics or formulas. Define questionnaire and task constructs, exact wording, response coding, verbal anchors, language, and planned administration timing. Session records inherit these definitions and document actual differences rather than repeating the complete protocol. Detailed processing and artefact handling may be maintained in linked methods or code documentation.

**Document the limits of comparability.** A common field name or shared schema does not establish equivalence of devices, physiological compartments, preprocessing, or derived outcomes. The purpose is to make these differences visible so that researchers can judge whether datasets can be compared, adjusted, stratified, or should remain analytically distinct.

**Scope and refinement.** The present templates are primarily oriented toward indoor human studies with sedentary or light activity and relatively short-term exposures. Longitudinal, occupational, outdoor, and specialised clinical applications may require extensions. The field definitions are provisional and intended for iterative refinement through use and community feedback, not a field-endorsed reporting standard.

## Shared rules for identifiers, timing and provenance

**Identifiers and relationships.** An Experiment ID uniquely identifies a study/protocol. A Participant ID identifies a person within a study and links to Experiment ID; if reused across studies, its scope must be explicitly documented. A Session ID uniquely identifies a participant visit/condition and links to Participant ID and Experiment ID. A Device model ID identifies a manufacturer/model (and is shared by multiple physical units); a Device ID identifies one physical device unit, typically distinguished by serial number. A Calibration ID identifies one calibration or verification event for a physical Device ID. A session sensor-application record links Session ID, Device ID and the relevant measurement definition; it carries actual placement, times, configuration and applicable Calibration ID. For multimodal instruments, measurement characteristics are signal-specific even when one physical unit is reused. No identifier should be inferred from a display name.

**Planned versus realised conditions.** Experiment-level records describe planned exposure, timing, activity, clothing, environmental measurements and measurement configuration. Participant-level records describe stable or slowly changing individual characteristics. Session-level records describe realised timing, condition, clothing, activity, acute modifiers, adherence and deviations. Session values inherit experiment defaults when unchanged; an explicit override records differences. Device-model capabilities and physical-unit identity belong to the device registry; calibration events belong to the calibration log. Where per-device details are numerous, store them in a linked sensor-application table rather than repeating them as session columns. Environmental measurements should be linked to their actual time series; do not substitute subjective outdoor-weather labels for measured exposure.

**Shared missingness and provenance vocabulary.** Use these codes consistently across the five tables and linked datasets:

| Code | Meaning |
|---|---|
| `not_reported` | Not available in accessible source documentation; not evidence of non-collection |
| `not_collected` | Confirmed not collected or recorded |
| `not_applicable` | Field does not apply to the study, participant or session |
| `unknown` | Applicable, but value is unknown |
| `protocol_derived` | Value is supported by a documented study-wide protocol rule, not an independent individual observation |

These codes are not interchangeable with numeric zero, a negative response or an empty string. For retrospective datasets, retain the source document and coding basis where available. The published supplement's `protocol-derived` label corresponds to `protocol_derived` here; the mapping should be explicit in exported datasets.

