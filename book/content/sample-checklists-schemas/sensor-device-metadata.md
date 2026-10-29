# Sensor & device metadata

Sensor and device metadata sit on a parallel axis to the experimental context hierarchy. Rather than repeating instrument information across every experiment or session record, these two tables capture device properties once and reference them by ID wherever needed.

The two tables operate on different time scales:

- <u>Device Registry</u>. Static properties of each physical device unit. Filled once per device, reused across all studies.
- <u>Calibration Log</u>. One record per calibration event per device. Updated whenever a device is recalibrated.

A third table, *Sensor Application*, captures per-session placement and configuration for each device. Because it describes what happened during a specific session, it lives in the [session-level metadata](session-level-metadata) schema under the *Devices & sensor application* group.

:::{table} Device registry schema.
:name: tab-device-registry

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Notes** |
|---|---|---|---|---|
| **Core IDs** | Device ID | 1 | Unique alphanumeric code (e.g. `TMP-01`, `ECG-A`) | Unique physical device unit ID, not a model or signal ID; primary key used by session applications and calibration logs |
| | Sensor principle | 1 | NTC thermistor / Ag/AgCl electrode / optical PPG / oscillometric cuff / ventilated capsule | Signal-specific where necessary; identify modality in experiment-level measurement definitions |
| **Device identity** | Brand | 1 | Maxim Integrated / Biopac / Polar / Finapres | Manufacturer name |
| | Model | 1 | DS1922L / MP160 / H10 / Nova 2 | Commercial model name |
| | Device model ID | 1 | Stable manufacturer/model identifier | Shared across units of the same model; distinct from physical Device ID |
| | Serial number | 1 | Alphanumeric from device label | — |
| | Firmware / software version | 2 | v3.2.1 / HOBOware 3.7 | Record at time of study; can change between experiments |
| **Specifications** | Nominal accuracy | 2 | ±0.5 °C / ±3 mmHg / ±0.001 µS | Manufacturer specification; specify signal/modality if device is multimodal |
| | Resolution | 2 | 0.0625 °C / 1 ms IBI / 0.001 µS | Manufacturer specification; specify signal/modality if device is multimodal |
| | Measurement range | 2 | Numeric range and units | Specify signal and units if device is multimodal |
| | Supported sampling configuration | 2 | Supported rate(s)/range in Hz or spot measurement; per signal if needed | Capability, not actual configured rate; experiment default and session overrides stored separately |
| | Notes | 3 | Free text | Hardware faults, repairs, firmware updates, modifications |

:::
Notes. One row per physical device unit. If a lab owns three iButton loggers, each has its own row and its own ID — they may have different calibration curves.

:::{table} Calibration log schema.
:name: tab-calibration-log

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Notes** |
|---|---|---|---|---|
| **Core IDs** | Calibration ID | 1 | Unique code (e.g. `CAL-001`) | Primary key |
| | Device ID | 1 | Foreign key → Device Registry | Unique physical device unit ID, not a model or signal ID; primary key used by session applications and calibration logs |
| | Calibration date | 1 | YYYY-MM-DD | |
| **Method** | Calibration method | 1 (conditional) | Water bath 5-point / manometer check / electronic bridge check / flow-meter verification | Distinguish calibration from functional verification and software/signal-processing validation |
| | Reference instrument | 1 (conditional) | Brand + model (e.g. Fluke 1502A / Heidolph reference manometer) | |
| | Reference accuracy | 2 | ±0.01 °C / ±0.1 mmHg | Traceability of the reference |
| **Results** | Calibration points tested | 2 | List of values (e.g. 30, 34, 37, 40 °C) | |
| | Raw offset per point | 2 (conditional) | Measured − reference at each point | e.g. +0.12 °C at 34 °C, −0.03 °C at 37 °C |
| | Correction equation | 1 (conditional) | y = 0.998x + 0.14 | Only when calibration yields a correction; not applicable to verification-only procedures |
| | Pass / fail | 1 (conditional) | Pass / Fail / Conditional | When defined acceptance criteria exist; include criterion and outcome |
| **Administration** | Operator | 3 | Initials or name | |
| | Next calibration due | 3 | YYYY-MM-DD or "before experiment X" | |
| | Notes | 3 | Free text | Drift patterns, anomalies, unusual readings |

:::

**Signal-specific calibration and verification notes:**
| Signal | Method | Key output |
|---|---|---|
| Skin temperature / CBT (contact sensors) | Stirred water bath, 3–5 temperature points | Individual linear correction equation per sensor unit |
| CBT (GI telemetry pills) | Same water bath method; each capsule is a separate Device ID (single-use) | Correction equation applied before ingestion |
| EDA | Electronic Wheatstone bridge balance; gain verification | Gain setting, bridge offset value |
| LSR (ventilated capsule) | Flow meter verification; humidity sensor linearity across 0–100 % RH | Verified flow rate (L·min⁻¹); zero-offset value |
| ECG / chest-strap | No physical calibration; record software version and filter settings as the equivalent | Software version; filter cutoffs; R-peak detection algorithm |
| Oscillometric BP | Manometer verification against traceable reference | Bias at rest; acceptance threshold (typically ±3 mmHg) |

Notes. One row per calibration event per device. A device may appear multiple times as it is recalibrated across studies or time periods.

**Identity and sampling:** The model–signal catalogue describes device-model capabilities, while the Device Registry above identifies each physical unit. Experiment-level measurement definitions record the actual configured sampling rate and default placement. Session records document actual applications and overrides. Retain both a verification summary and the per-device calibration-event log.
