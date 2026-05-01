# Symbolic notation and variable conventions
The table below summarises commonly used symbolic conventions and variable names for physiological measurements relevant to thermal physiology research. Because the field draws on multiple disciplines; including physiology, ergonomics, environmental medicine, and building science; identical quantities are frequently reported using different abbreviations or symbols. These differences typically reflect disciplinary conventions rather than differences in the underlying measurement. The table therefore compiles commonly used variable names, units, and aliases to clarify equivalences across studies and to support more consistent terminology in reporting and data exchange.

:::{table} Physiological variable naming conventions in thermal physiology studies
:name: tab-physio-variable-naming

| **Metric family** | **Specific variable / measure** | **Unit** | **Common aliases / symbols** | **Notes** |
|---|---|---|---|---|
| **Core body temperature (CBT, Tcore, tcore, *t*<sub>cr</sub>)** | Rectal temperature | °C | tre, t<sub>re</sub>, Trect, Trec | *t*<sub>re</sub> in ISO 9886 |
|  | Oesophageal temperature | °C | tes, t<sub>es</sub>, Teso | *t*<sub>es</sub> in ISO 9886 |
|  | Gastrointestinal / intra-abdominal temperature | °C | tab, Tgi, TGI, Tpill | Telemetry pill is a **measurement method**, not the variable itself; *t*<sub>ab</sub> in ISO 9886 |
|  | Tympanic temperature | °C | tty, Tty, Ttym | *t*<sub>ty</sub> in ISO 9886 |
|  | Auditory canal temperature | °C | tac, Tac | *t*<sub>ac</sub> in ISO 9886 |
|  | Oral temperature | °C | tor, t<sub>or</sub>, Tor | *t*<sub>or</sub> in ISO 9886 |
| **Skin temperature** | Local skin temperature | °C | t<sub>sk,i</sub>, T<sub>sk,i</sub>, Tskin<sub>i</sub> | Index *i* denotes anatomical site (e.g. T<sub>sk,chest</sub>); canonical ISO form t<sub>sk,i</sub> |
|  | Mean skin temperature | °C | T̄<sub>sk</sub>, Tsk_mean, MST | Overbar notation common in physiology; MST common in building science |
|  | Temperature gradients | °C, K | ΔT<sub>core–skin</sub>, ΔT<sub>neck–ankle</sub>, ΔT<sub>prox–dist</sub>, DPG | Distal–proximal gradient widely used in thermoregulation studies |
| **Sweat / skin moisture** | Local sweat rate | mg·cm<sup>−2</sup>·min<sup>−1</sup>, g·h<sup>−1</sup> | LSR, SR<sub>local</sub>, ṁ<sub>sw</sub> | Measured via ventilated capsule, sweat patches, etc. |
|  | Whole-body sweat loss | kg, g, mL, % body mass | WBSL, Δm<sub>sw</sub>, Δm<sub>body</sub> | Often derived from pre- and post-exercise body mass |
|  | Skin wettedness | – | w | Dimensionless ratio of evaporative heat loss to maximum evaporative capacity |
|  | Electrodermal activity (signal family) | typically µS or mS | EDA, SC, GSR | EDA preferred umbrella term; GSR considered outdated |
|  | Tonic component | µS, mS | SCL | Skin conductance level (baseline component) |
|  | Phasic component | µS | SCR | Skin conductance response (transient responses) |
| **Cardiovascular** | Heart rate | beats·min<sup>−1</sup> | HR, bpm | — |
|  | Inter-beat interval | ms | IBI, RR, RRi | RR derived from ECG R-wave intervals; IBI common for PPG |
|  | Systolic blood pressure | mmHg | SBP, P<sub>s</sub> | Clinical standard SBP |
|  | Diastolic blood pressure | mmHg | DBP, P<sub>d</sub> | Clinical standard DBP |
|  | Mean arterial pressure | mmHg | MAP, P<sub>m</sub> | Often approximated from SBP and DBP |
|  | Stroke volume | mL | SV | — |
|  | Cardiac output | L·min<sup>−1</sup> | CO, Q̇ | CO most common in clinical literature |
| **Autonomic modulation (HRV)** | Time-domain indices | ms | RMSSD, SDNN, pNN50, NNmean | Standardised by HRV Task Force (1996) |
|  | Frequency-domain indices | ms<sup>2</sup> or n.u. | LF, HF, LF/HF, TP | n.u. = normalised units |
|  | Nonlinear indices | – | SD1, SD2, SampEn, ApEn | Case-sensitive notation |
| **Vascular control** | Skin blood flow | PU, % max | SkBF, SBF, Flux | Flux commonly used in laser Doppler measurements |
|  | Cutaneous vascular conductance | PU·mmHg<sup>−1</sup> | CVC, CVC<sub>norm</sub> | CVC = SkBF / MAP |
|  | Forearm blood flow | mL·min<sup>−1</sup>·100 mL<sup>−1</sup> | FBF | Standard plethysmography metric |
| **Metabolic / systemic** | Oxygen consumption | mL·min<sup>−1</sup>, mL·kg<sup>−1</sup>·min<sup>−1</sup> | VO<sub>2</sub>, V̇O<sub>2</sub> | Absolute or body-mass-specific values reported |
|  | Carbon dioxide production | mL·min<sup>−1</sup>, mL·kg<sup>−1</sup>·min<sup>−1</sup> | VCO<sub>2</sub>, V̇CO<sub>2</sub> | Analogous to VO₂ notation |
|  | Metabolic rate | W·m<sup>−2</sup>, met | M | Variable M; unit “met” commonly used in building science |
|  | Respiratory exchange ratio | – | RER, RQ | RER short-term; RQ steady-state metabolic ratio |
|  | Heat storage | kJ·kg<sup>−1</sup>, W | S | Represents change in body heat content |
|  | Body surface area | m<sup>2</sup> | BSA | Derived using Du Bois, Mosteller, or similar formulas |

:::