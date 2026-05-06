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
| **Core IDs** | Device ID | 1 | Unique alphanumeric code (e.g. `TMP-01`, `ECG-A`) | Primary key; used as foreign key in all linked tables |
| | Signal / modality | 1 | Skin temperature / HR+HRV / EDA / CBT / BP / Sweat | Maps to signal chapter |
| | Sensor principle | 1 | NTC thermistor / Ag/AgCl electrode / optical PPG / oscillometric cuff / ventilated capsule | Physical transduction method |
| **Device identity** | Brand | 1 | Maxim Integrated / Biopac / Polar / Finapres | Manufacturer name |
| | Model | 1 | DS1922L / MP160 / H10 / Nova 2 | Commercial model name |
| | Serial number | 1 | Alphanumeric from device label | — |
| | Firmware / software version | 2 | v3.2.1 / HOBOware 3.7 | Record at time of study; can change between experiments |
| **Specifications** | Nominal accuracy | 2 | ±0.5 °C / ±3 mmHg / ±0.001 µS | From manufacturer specification sheet |
| | Sampling rate (Hz) | 2 | 1 / 256 / 4 | As configured; not maximum capability |
| | Resolution | 2 | 0.0625 °C / 1 ms IBI / 0.001 µS | From specification sheet |
| **History** | Date first used | 3 | YYYY-MM-DD | Useful for tracking drift over device lifetime |
| | Notes | 3 | Free text | Hardware faults, repairs, firmware updates, modifications |

:::
Notes. One row per physical device unit. If a lab owns three iButton loggers, each has its own row and its own ID — they may have different calibration curves.

:::{table} Calibration log schema.
:name: tab-calibration-log

| **Group** | **Field name** | **Tier** | **Typical answers / coding** | **Notes** |
|---|---|---|---|---|
| **Core IDs** | Calibration ID | 1 | Unique code (e.g. `CAL-001`) | Primary key |
| | Device ID | 1 | Foreign key → Device Registry | |
| | Calibration date | 1 | YYYY-MM-DD | |
| **Method** | Calibration method | 1 | Water bath 5-point / manometer check / electronic bridge check / flow-meter verification | Matches methods described in signal chapter Data handling sections |
| | Reference instrument | 1 | Brand + model (e.g. Fluke 1502A / Heidolph reference manometer) | |
| | Reference accuracy | 2 | ±0.01 °C / ±0.1 mmHg | Traceability of the reference |
| **Results** | Calibration points tested | 2 | List of values (e.g. 30, 34, 37, 40 °C) | |
| | Raw offset per point | 2 | Measured − reference at each point | e.g. +0.12 °C at 34 °C, −0.03 °C at 37 °C |
| | Correction equation | 1 | y = 0.998x + 0.14 | Applied to raw signal during processing; store per device |
| | Pass / fail | 1 | Pass / Fail / Conditional | Based on protocol acceptance threshold |
| **Administration** | Operator | 2 | Initials or name | |
| | Next calibration due | 2 | YYYY-MM-DD or "before experiment X" | |
| | Notes | 3 | Free text | Drift patterns, anomalies, unusual readings |

:::

**Signal-specific calibration notes:**
| Signal | Method | Key output |
|---|---|---|
| Skin temperature / CBT (contact sensors) | Stirred water bath, 3–5 temperature points | Individual linear correction equation per sensor unit |
| CBT (GI telemetry pills) | Same water bath method; each capsule is a separate Device ID (single-use) | Correction equation applied before ingestion |
| EDA | Electronic Wheatstone bridge balance; gain verification | Gain setting, bridge offset value |
| LSR (ventilated capsule) | Flow meter verification; humidity sensor linearity across 0–100 % RH | Verified flow rate (L·min⁻¹); zero-offset value |
| ECG / chest-strap | No physical calibration; record software version and filter settings as the equivalent | Software version; filter cutoffs; R-peak detection algorithm |
| Oscillometric BP | Manometer verification against traceable reference | Bias at rest; acceptance threshold (typically ±3 mmHg) |

Notes. One row per calibration event per device. A device may appear multiple times as it is recalibrated across studies or time periods.