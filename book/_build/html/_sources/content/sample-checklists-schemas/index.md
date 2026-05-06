# SAMPLE CHECKLISTS & SCHEMAS

This section provides structured documentation templates for human thermal physiology studies. The goal is not to prescribe a field-wide standard, but to make one coherent implementation transparent and to provide concrete examples that other groups can adapt and share. By circulating comparable schemas, the field can gradually converge on common reporting practices and enable more reproducible, interoperable datasets.

## Structure

The documentation is organised across two parallel axes. The diagram below shows how the five tables relate to each other: solid arrows indicate hierarchy (one record contains or generates the next), and dashed arrows indicate foreign key references (a field in one table points to a record in another).

:::{mermaid}
flowchart TD
    subgraph CTX["Experimental context"]
        E["Experiment\none record per study\ndesign, ethics, PICOT\ninstruments, data availability"]
        P["Participant\none record per person\ndemographics, health\nhormonal status, lifestyle"]
        S["Session\none record per visit\nacute state, clothing\nsensor application"]
        E --> P
        E --> S
        P --> S
    end
    subgraph DEV["Sensor and device documentation"]
        DR["Device Registry\none record per device\nbrand, model, serial number\nsensor principle, specs"]
        CL["Calibration Log\none record per calibration\nmethod, correction equation\nreference instrument, pass/fail"]
        DR --> CL
    end
    E -. "Primary instruments used" .-> DR
    E -. "Calibration reference" .-> CL
    S -. "Device IDs used / Calibration IDs active" .-> DR
    S -. "Calibration IDs active" .-> CL
:::

**Experimental context** follows a three-level hierarchy. Each level corresponds to a separate metadata table:

- [Experiment metadata](experiment-level-metadata): one record per study or protocol. Stores high-level information: title, lab, institute, recruitment window, primary endpoints, general exposure types (lab vs field, heat vs cold vs neutral), ethics approval identifiers, and links to the instruments and calibration records used.
- [Participant metadata](participant-level-metadata): one record per person, containing attributes that change slowly or not at all during the study. Stores demographics, morphology, health and diagnoses, hormonal status, lifestyle, sleep and {ref}`chronotype <label-chronotype>`, thermal sensitivity, and (optionally) built-environment context.
- [Session metadata](session-level-metadata): one record per visit or experimental condition per person. Stores per-visit timing, condition labels, acute state (sleep, illness, recent behaviour), clothing, activity, and sensor application details (placement, attachment, timing, and signal quality for each device used that session).

**Sensor and device documentation** sits on a parallel axis and is described in a separate page:

- [Sensor & device metadata](sensor-device-metadata): two linked tables. The **Device Registry** holds static properties of each physical device unit (brand, model, serial number, sensor principle, specifications) and is filled once per device, reused across studies. The **Calibration Log** holds one record per calibration event per device (method, reference instrument, correction equation, pass/fail). Both tables connect to the experimental context hierarchy via Device IDs and Calibration IDs, which are referenced as foreign keys in the experiment and session schemas.

## Design principles

The schema follows the logic of established data standards for human studies. The three-level experimental hierarchy mirrors the Brain Imaging Data Structure (BIDS) {cite:p}`gorgolewski_brain_2016`, which separates `participants.tsv` and `sessions.tsv`, and the ISA-Tab framework {cite:p}`sansone_toward_2012`, which distinguishes investigation, study, and assay metadata. The Device Registry and Calibration Log extend this logic by treating measurement equipment as a separately maintained reference table — analogous to how BIDS handles electrode and channel descriptions.

All fields are assigned to one of three informal tiers:

- **Tier 1 — Core:** Essential for basic interpretability and reuse. Should be completed for every study.
- **Tier 2 — Recommended:** Meaningfully improves reproducibility and comparability. Complete where feasible.
- **Tier 3 — Specialised:** Useful for specific study types, meta-analyses, or FAIR-level documentation. Optional.

The specific fields and tiering logic presented here should be treated as provisional. Determining which descriptors are essential, recommended, or specialised ultimately requires community agreement. This schema is a structured starting point for iterative refinement.
