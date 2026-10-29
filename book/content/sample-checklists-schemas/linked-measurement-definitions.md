# Linked measurement, questionnaire and sensor-application schemas

These tables extend the four-level wiki hierarchy without replacing the original schemas. They correspond to Supplementary Document 2, Tables S2 and S3, and the session-specific sensor-application records described in its notes.

## Experiment-level questionnaire and task definitions

One row per questionnaire item, module or non-physiological task. Reuse the definition across sessions; record overrides only where actual administration differs.

| Field | Tier | Notes |
|---|---|---|
| Experiment ID | 1 | Foreign key |
| Definition / item ID | 1 | Unique within experiment |
| Class | 1 | Questionnaire / cognitive task / other |
| Construct | 1 | E.g., thermal sensation, vigilance |
| Exact item wording / task | 1 | Verbatim item or referenced protocol |
| Construct type | 1 | Perception, affective evaluation, preference, etc. |
| Scale type | 1 | Stepped, continuous, binary, task-specific |
| Minimum, maximum, step | 1 conditional | When numeric scale applies |
| Numeric response codes | 1 conditional | Preserve administered order |
| Verbal anchors / response options | 1 conditional | Preserve administered order |
| Language(s) | 1 | Actual versions available |
| Default administration mode | 1 | Paper / tablet / online / other |
| Default timing | 1 | Relative to session/exposure |
| Data / document reference | 1 | Instrument and response-data linkage |

## Experiment-level direct measurement definitions

One row per direct signal × device model × default placement or room position. A multimodal device appears once for each measured signal. Link derived outcomes to their source signals.

| Field | Tier | Notes |
|---|---|---|
| Experiment ID | 1 | Foreign key |
| Measurement definition ID | 1 | Stable key |
| Domain | 1 | Physiological / environmental / personal exposure |
| Signal type | 1 | Controlled vocabulary |
| Device model ID | 1 | Foreign key to model catalogue |
| Body site / room site | 1 conditional | Anatomical or environmental location |
| Laterality | 1 conditional | Where anatomically applicable |
| Surface / orientation | 1 conditional | Where applicable |
| Configured sampling rate and unit | 1 | Actual experiment configuration; allow spot measurements |
| Derived metrics | 2 | Explicitly identify source variables |
| Formulas / methods | 1 conditional | When metrics are derived |
| Calibration / verification status or reference | 2 | Link to unit-specific calibration record |
| Data / document reference | 1 | Identifier or URI |

## Device model and signal catalogue

Separate model capabilities from the individual physical units described in the [device registry](sensor-device-metadata).

| Field | Tier | Notes |
|---|---|---|
| Device model ID | 1 | Shared by physical units of same model |
| Manufacturer and model | 1 | Identity |
| Signal / modality | 1 | One row per supported direct signal |
| Sensing principle | 1 | Physical measurement mechanism |
| Units | 1 | SI or declared units |
| Nominal accuracy and resolution | 2 | Manufacturer specifications and context |
| Measurement range | 2 | Supported range |
| Supported sampling rate(s) | 2 | Capability, **not** configured rate |
| Calibration / verification summary | 2 | Method and reference, where applicable |

## Session-level sensor applications

One row per physical device unit per session and measurement definition. Experiment-level defaults are inherited; only actual identifiers, timing and deviations are required unless an override occurs.

| Field | Tier | Notes |
|---|---|---|
| Experiment ID / participant ID / session ID | 1 | Foreign keys |
| Measurement definition ID | 1 | Inherited default |
| Physical device unit ID | 1 | Unit-specific identifier |
| Calibration event ID | 1 conditional | Applicable verification |
| Actual application time | 1 | Timestamp |
| Recording start / end | 1 | Timestamps |
| Placement / orientation override | 1 conditional | Only when different from default |
| Sampling / configuration override | 1 conditional | Only when different from default |
| Interruption / quality / deviation | 2 | Structured note |
| Raw-data reference | 1 | Filename, URI or resource ID |

## Coding and inheritance

Use `not_reported` for information absent from accessible records, `not_applicable` where a field does not apply, and `protocol-derived` for participant/session values supported only by protocol rules. These are not interchangeable. Experiment-level definitions are inherited; realised differences belong in session and application records. Tier 1 means essential **where applicable**, not a requirement to collect sensitive information indiscriminately.
