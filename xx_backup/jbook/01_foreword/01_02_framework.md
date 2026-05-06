# FRAMEWORK





Before methodological standards can be meaningfully discussed, conceptual alignment is required. Researchers must share a common understanding and language of:

* the mechanistic thermophysiological processes represented by each signal (why we measure them),
* the physical principles through which those processes are measured (how we measure them),
* the influence of anatomical site on signal meaning (where we measure them),
* the limits of agreement between different measurement approaches,
* the biological modifiers that shape responses, and
* the analytical transformations that convert raw time series into reported outcomes.

## 3.1. Mechanistic rationale (*Why*) 

The first requirement of any physiological measurement is clarity regarding the biological process it represents. This part is a response to the first-level fragmentation identified in Chapter 2.1 Interpretive fragmentation.

Thermoregulation is a coordinated control process involving internal heat storage, peripheral heat exchange, cardiovascular redistribution, and evaporative cooling \[12]. Commonly used signals in indoor environmental research, such as core temperature, skin temperature, heart rate, blood pressure, sweating, and electrodermal activity, all capture different components of this integrated response. None constitutes a direct measure of thermal stress or strain in isolation; each reflects a specific regulatory pathway.

Explicitly articulating the mechanistic rationale serves three purposes:

1. It specifies which subsystem is being interrogated. 

A study may target uncompensated heat storage, vasomotor adjustments, autonomic load, or evaporative drive. Without this distinction, signals risk being interpreted as general indicators of “thermal effect” despite their pathway specificity.

2\. It defines the limits of inference. 

For example, elevations in heart rate during warm exposure may reflect thermally induced vasodilation, emotional arousal, postural adjustment, dehydration, or prior activity \[13–16]. A rise in electrodermal activity may indicate sudomotor activation, emotional engagement, or cognitive load \[17–20]. In this sense, mechanistic framing prevents over-attribution.

3\. It clarifies temporal behaviour. 

Some signals reflect slow integrative processes, whereas others respond rapidly but are sensitive to multiple inputs. Some signals are impacted by accumulated exposure dose, while others do not have acclimation memory. Different signals have different circadian, monthly and seasonal rhythms. Recognising these dynamics is essential, especially when interpreting acute or short-term indoor exposures.

Explicitly stating why a signal is measured anchors study design in physiological reasoning rather than convention or convenience.

## 3.2. Measurement principles and sensor technologies (*How*) 

If the mechanistic rationale clarifies what biological process is being interrogated why, the measurement principle clarifies how that process becomes observable.

Physiological variables are not measured directly; they are inferred through physical transduction. Thermistors estimate temperature from conductive heat transfer. Oscillometric cuffs infer arterial pressure from cuff-pressure oscillations. Photoplethysmography detects pulsatile changes in light absorption associated with blood volume. Skin-conductance electrodes capture changes in electrical conductance linked to sweat-duct activity. Even comparatively direct approaches, such as ventilated capsules for local sweat rate, quantify a physical flux under defined assumptions. In all cases, the measured quantity is a proxy for a biological process (REF).

Making this explicit is essential for two reasons:

1. Different technologies may target related but non-identical constructs. Local sweat rate, whole-body sweat loss, skin wettedness, and electrodermal activity all relate to sudomotor function but are not interchangeable (REF). ECG-derived and optical heart rate reflect the same cardiac cycle but differ in waveform fidelity and artefact susceptibility (REF). Continuous and intermittent blood pressure methods rely on distinct modelling assumptions (REF). Conceptual similarity does not imply measurement equivalence.
2. Device-specific implementation matters. Sampling frequency, filtering strategy, proprietary algorithms, and calibration procedures can influence amplitude, dynamics, and variability. Validation studies often report acceptable agreement at the group level while revealing systematic bias or altered signal characteristics at the individual level (REF).

The measurement method, therefore, constrains interpretation. Without explicit recognition of the transduction principle and its limitations, physiological variability and instrumentation variability cannot be meaningfully separated.

## 3.3. Anatomical sites and site-specific considerations (*Where*) 

If mechanistic rationale clarifies what is being interrogated and measurement principle clarifies how it is transduced, anatomical site clarifies where the physiological process is sampled.

For many thermophysiological variables, location is intrinsic to signal meaning. Core body temperature may be assessed rectally, oesophageally, via ingestible telemetry, in the tympanic canal, or at the axilla. Although often grouped under a single term, these sites represent distinct thermal compartments with different perfusion characteristics, environmental exposure, and temporal dynamics (REF). These measurements are physiologically related but not interchangeable.

Skin temperature illustrates anatomical dependence even more clearly. The skin functions as a heterogeneous thermoeffector surface. Regional values vary according to local vasomotor control, subcutaneous insulation, gland density, and environmental exposure (REF). The same environmental stimulus may produce divergent trajectories across body regions, each reflecting a different aspect of thermoregulatory strategy.

Comparable considerations apply to other signals. Electrodermal activity differs between palmar and forearm sites due to variations in eccrine gland density (REF). Blood pressure measurements may vary with limb position and hydrostatic reference relative to the heart (REF).

Anatomical location constrains interpretation. Without explicit recognition of site-specific physiology, regional responses may be misattributed to whole-body regulation.

3.4.	Cross-method agreement and validation considerations 

If mechanistic rationale clarifies what is measured, measurement principle clarifies how it is transduced, and anatomical site clarifies where it is sampled, cross-method agreement clarifies whether different implementations of the same nominal variable can be interpreted as equivalent.

Many physiological variables can be obtained through distinct sensing paradigms that target the same underlying process but do not yield interchangeable outputs. For example, heart rate derived from electrocardiography and from optical photoplethysmography may show strong correlation while differing in beat detection fidelity, artefact sensitivity, and variability metrics (REF). Measures related to sweating may be derived from evaporative flux, body mass change, or electrodermal conductance, each reflecting different physiological dimensions (REF). Even when labelled identically, these outputs embody different measurement histories.

Importantly, non-equivalence is not limited to differences in sensing principle. Devices based on the same physical method may also diverge. Differences in sensor hardware, analogue-to-digital resolution, sampling frequency, filtering strategies, proprietary algorithms, and firmware updates can alter amplitude, smoothing characteristics, event detection thresholds, and derived indices (REF). Comparative studies frequently demonstrate acceptable agreement at the group level while revealing systematic bias or altered dynamics at the individual level (REF). Such differences may remain negligible in some contexts yet become consequential under thermal stress, altered perfusion, or movement.

High correlation therefore does not imply interchangeability. Without consideration of validation context and limits of agreement, differences between studies may reflect instrumentation characteristics rather than physiological modulation.

Comparability constrains interpretation. Explicit recognition of agreement boundaries strengthens cumulative inference and prevents methodological heterogeneity from being mistaken for biological variability.

3.5.	Known confounders and modifiers 

Thermoregulatory responses are shaped not only by environmental exposure but also by individual biological context. Sex and hormonal status influence vasomotor control and sweating thresholds \[21,22]. Age modifies peripheral vasodilatory capacity and sudomotor responsiveness \[23,24]. Body composition alters insulation, heat capacity, and surface-to-mass relationships \[25,26]. Circadian phase and chronotype affect baseline core temperature, distal vasomotor tone, and autonomic regulation \[27,28]. Acclimation state, hydration level, fitness, and nutritional status shift effector sensitivity and cardiovascular strain \[29–32]. Medication use, neurodevelopmental profiles, and chronic disease further modulate thermal and autonomic regulation \[33–35].

These factors do not introduce random variability; they shift response thresholds, alter effector gain, and redefine the operating range of thermoregulatory systems. Many physiological signals, therefore, exhibit systematic differences across sex, age groups, circadian timing, and acclimation state (REF).

In indoor environmental research, physical parameters are often tightly controlled, whereas biological variability is commonly treated as residual noise. Unexplained variance is frequently attributed to inter-individual variability without interrogation of its physiological basis. Without explicit consideration of relevant modifiers, observed differences may be attributed solely to environmental manipulation despite being shaped by underlying biological state.

Biological context constrains interpretation. Recognising these conditioning factors strengthens internal validity and supports meaningful comparison across studies.

3.6.	Data handling and processing practices 

If mechanistic rationale clarifies what is being measured, measurement principle clarifies how it is transduced, anatomical site clarifies where it is sampled, cross-method agreement clarifies comparability, and biological modifiers clarify context, data handling clarifies how raw signals become reported outcomes.

Physiological measurements are typically acquired as continuous time-series data with different native resolutions, depending on the signal and the sensing equipment. The transformation from raw recordings to reported metrics begins with calibration and includes filtering, artefact correction, segmentation, and the derivation of summary parameters. At each step, methodological decisions shape the resulting signal.

Calibration influences baseline accuracy. Filtering and smoothing alter signal dynamics. Artefact detection and interpolation determine valid data segments. Derived metrics such as means, slopes, area under the curve, or variability indices depend on window length and mathematical formulation (REF). Normalisation strategies and exclusion criteria further shape interpretation (REF). 

Analytical transformation is therefore part of measurement. Without transparency regarding processing choices, differences across studies may reflect computational variation rather than physiological effect.

As with the preceding layers, analytical treatment constrains interpretation. Explicit recognition of the signal-processing pathway strengthens reproducibility and cumulative knowledge development.



