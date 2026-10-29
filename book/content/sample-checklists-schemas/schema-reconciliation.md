# Schema reconciliation and provenance

**Status:** Proposed merged implementation for review; not a new consensus standard.

**Reference sources:** (1) published *Building and Environment* Supplementary Document 2, Tables S1–S6 (four illustrative SenseLab studies); (2) pre-merge wiki experiment, participant, session, and sensor/device schemas. Supplementary Document 1 reports the empirical metadata analysis and is not the normative schema dictionary.

## Mapping of source tables

| Supplement | Merged wiki location | Relationship |
|---|---|---|
| S1 Experiment-level records | Experiment-level metadata | Core fields, detailed sample flow, research rationale, analysis, data access |
| S2 Questionnaire and non-physiological task definitions | Linked measurement definitions | Separate item/task table, not flattened into experiment notes |
| S3 Direct measurement and device definitions | Linked measurement definitions | One signal–device–default-placement record |
| S4 Session records | Session-level metadata | Actual timing, adherence, activity and data references |
| S5 Participant records | Participant-level metadata | Stable characteristics, modifiers, provenance |
| S6 Cross-study sensor inventory | Sensor/device + linked model–signal catalogue | Device model × signal, separate from physical unit |

## Approved reconciliation decisions

| ID | Approved rule |
|---|---|
| E1 | Number of conditions: Tier 1 |
| E2 | Randomisation status Tier 1; method Tier 2 |
| E3 | Participant and investigator blinding separate, Tier 2 |
| E4 | Detailed sample-flow counts; analysis N and sample-size method Tier 1 |
| E5 | Secondary outcomes Tier 2 |
| E6 | Demographic summary counts derived from participant records, optional |
| P1 | Thermal/climatic history Tier 1 |
| P2 | Habitual physical activity Tier 2 |
| P3 | Smoking status Tier 2 |
| P4 | Hormonal contraception Tier 1 |
| P5 | Chronotype Tier 1 |
| P6 | Thermal preference/sensitivity Tier 1 |
| P7 | General diagnosis/medication Core; specific diagnoses and hormonal therapies conditional |
| P8 | Sex-related and gender-related variables separate, operationally defined |
| S1 | Actual normalisation Tier 1; waiting time separate |
| S2 | Menstrual cycle day and phase conditionally Core |
| S3 | Overall compliance Tier 1, pre-session restrictions Tier 2 |
| S4 | Separate linked sensor application table; inherit experiment defaults |
| S5 | Planned activity and estimated MET separate |
| D1 | Model, signal, and physical-unit records separate |
| D2 | Both verification summary and calibration-event log |
| D3 | Supported versus configured sampling rates separate |

## Interpretation and data governance

The supplementary tables are **retrospectively populated examples**, not an exhaustive universal minimum dataset. Wiki-only fields remain as extensions, and supplementary-only fields are integrated rather than replacing them. A field absent from a populated example is not necessarily inapplicable to future studies.

Tier 1 means necessary for interpretability **when applicable**. Sensitive data must be collected only with an appropriate scientific rationale, consent and data protection. Distinguish `not_reported`, `not_applicable`, and `protocol-derived`. Avoid treating absent information as zero or no.

## Review checks before publication

- Confirm all original wiki field rows remain accessible and that appended supplementary fields are not duplicate semantic definitions.
- Verify participant sex/gender field definitions and coding against ethics requirements.
- Verify per-signal model/measurement records and sensor applications use stable foreign keys.
- Confirm tier 1/2 changes and conditional Core terminology are reflected in every table and narrative.
- Validate the Jupyter Book build and inspect the rendered pages, especially wide tables.
- Keep the original published supplementary files and DOI unchanged.
