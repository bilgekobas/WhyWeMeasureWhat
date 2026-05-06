WHY WE MEASURE WHAT, HOW, AND WHERE:\
Methods for human thermal physiology experiments in built environment studies

Version: v0.4 (2026-03-01)

# FOREWORD

## Background

Physiological measurements provide evidence of how humans respond to thermal environments. A century-old field of thermophysiology offers very strong foundations in methodologies, however in building research not all of these are consistently adopted. This manuscript consolidates established knowledge from thermal physiology, environmental ergonomics, and chronobiology to clarify the rationale behind the variables most commonly used to characterise thermoregulatory function under sedentary and light-activity conditions. It currently outlines five commonly used signals; core body temperature, skin temperature, heart rate/heart-rate variability, blood pressure, and sweating/electrodermal activity. For each, the paper summarises its mechanistic meaning (*why* we measure it), commonly used measurement types (*how* we measure it), typical body sites (*where* we measure it), influencing factors, and data-handling conventions. The goal is to provide a systematic snapshot of the existing know-how, rather than document what the field currently is doing. By doing so, it aims to provide a shared foundation for more comparable, transparent, and physiologically grounded research on human thermal responses in buildings.

## Framework 

Lorem ipsum

# INTRODUCTION

Physiological measurements can be crucial to understanding how the thermal environment impacts human physiology, well-being, and, in the long term, health. In building and environmental design research, however, they are often used pragmatically; selected for convenience, familiarity, or sensor availability, rather than from a coherent physiological rationale. Meanwhile, closely related disciplines such as thermal physiology, environmental ergonomics, and chronobiology have developed precise conventions for assessing thermoregulatory function. These frameworks already describe *what* to measure, *why* it matters, and *how* to interpret it under defined experimental conditions.

The present paper revisits those established foundations with the aim of translating them into the context of built-environment research. Rather than documenting how studies are currently conducted, it asks how they *could* be structured if guided by shared physiological reasoning. The intent is to provide a reference that links measurement choices to underlying mechanisms, clarifies which contextual data are required for interpretation, and supports greater methodological consistency across building-scale experiments.

Across laboratory and field studies, a small set of physiological variables is consistently used to represent thermoregulatory function. These include internal temperature, surface temperature, cardiovascular activity, sudomotor responses, and, where relevant, respiration and metabolic heat production (ISO, 2004; Kenny, 2010; Parsons, 1993). Together, these signals offer complementary views of heat storage, heat transfer, and heat dissipation, and they can be obtained with established sensor technologies suitable for both controlled and applied protocols (Havenith, 2001; Parsons, 1993).

Although thermoregulation is multi-systemic, a small set of representative indicators is widely used because it captures key processes with acceptable burden and reliability. Core body temperature reflects internal heat storage and overall thermal strain (Romanovsky, 2014; Taylor, 2014). Skin temperature describes peripheral heat exchange at the body--environment interface and is closely associated with thermal sensation and comfort reports (Havenith, 2001; Zhang et al., 2010, 2004). Heart rate and heart rate variability index autonomic cardiovascular adjustments that support thermal balance and can indicate the stability of physiological regulation under load (Shaffer and Ginsberg, 2017). Measures of sweating, skin moisture, or electrodermal activity reflect sudomotor activation and the potential for evaporative heat loss (Boucsein, 2012; E. R. Nadel et al., 1971; Patterson et al., 1998; Stephenson et al., 1984). These variables are not redundant; each contributes a distinct but complementary perspective on the same thermoregulatory episode.

This paper therefore serves three aims: (i) to summarise the physiological meaning and standard measurement approaches of each variable; (ii) to identify participant, environmental, and procedural factors that modify these signals and should be documented for proper interpretation; and (iii) to outline common preprocessing and feature-extraction steps that enable comparability between studies. The purpose is not to prescribe new standards, but to re-articulate the established physiological basis of these measures within the methodological reality of building research.

The scope focuses on healthy adults under sedentary or light-activity conditions typical of buildings and similar environments. Evidence from exercise, clinical, and chronobiological studies is referenced where it clarifies mechanisms that also govern resting or mild-activity thermoregulation. Each section translates these mechanisms into practical guidance for experimental design for the experiments for the built environment; emphasizing how choices in sensor type, body site, timing, and data treatment shape the resulting signal.

Finally, because thermoregulation is inherently multi-systemic, many studies interpret it through several concurrent variables. A synthesis section therefore outlines how these indicators can be combined to describe the same physiological episode from complementary perspectives. The remainder of the paper is organised as follows: Section 2 presents, for each physiological signal, its mechanistic meaning (*why*), sensor options (*how*), and typical body sites (*where*), along with relevant modifiers and data-handling practices. Section 3 summarises common composite metrics and interpretive frameworks, and Section 4 discusses implications for documentation and comparability across research domains.

# PHYSIOLOGICAL SIGNALS

This chapter provides reference material for the physiological variables most relevant to thermal-environment studies. Each subsection follows a consistent structure: it explains the physiological mechanism represented by the signal, summarises typical sensor technologies and body sites, identifies known modifiers and confounders, and lists standard preprocessing or feature-extraction methods. The focus is on variables that together describe the main components of thermoregulation, internal heat storage, peripheral heat exchange, cardiovascular adjustment, and evaporative control -- mainly for the adult population under sedentary/light-activity conditions. The intent is not to introduce new measures but to assemble, in one place, the methodological knowledge required for transparent and physiologically grounded experimentation in the built environment.

## Core body temperature

### Why: the mechanistic reasons behind the measurement

Core body temperature (CBT) represents the most direct indicator of whole-body heat storage and internal thermal strain. It integrates metabolic heat production with convective, radiative, evaporative, and conductive losses, reflecting the net balance of the body's thermal budget (Werner, 2010). Even small CBT deviations can alter cardiovascular efficiency, neural conductivity, and endocrine signalling (Taylor, 2014).

Unlike skin temperature, which tracks environmental exchanges, CBT is actively defended near 36.5--37.5 °C in healthy adults through hypothalamic thermoregulatory circuits combining feedback and feed-forward control of vasomotion, sweating, and metabolic heat production (Romanovsky, 2007; Tan and Knight, 2018). During passive heat exposure, CBT increases linearly with cumulative heat storage and blood redistribution, serving as the primary input for effector activation thresholds

Because subjective thermal comfort or sensation can diverge from physiological strain, continuous CBT monitoring provides a quantitative index of thermal load, safety limits, and adaptation potential. Sustained CBT elevations ≥ 38.0--38.5 °C denote excessive physiological strain in occupational and environmental contexts (ISO, 2004), whereas levels ≥ 40.0--40.5 °C accompanied by central nervous system dysfunction define exertional heat stroke (Armstrong et al., 2007).

### How: sensor types for measurement 

A variety of sensors and techniques are used to estimate CBT, differing in anatomical site, thermal response time, invasiveness, and susceptibility to environmental error. Sensor types include thermal probes and thermocouples (measuring conductive heat transfer), infrared thermometers (radiative detection), thermistors with telemetry capability, and heat-flux capacitors (inferring deep temperature from surface gradients).

### Where: body sites of measurement

**Rectal thermometry.** Flexible thermistor probes inserted approximately 10--15 cm beyond the anal sphincter remain a laboratory reference. Insertion to near 15 cm minimises local gradient error and improves reproducibility (Miller et al., 2017). Rectal probes typically respond within 10--30 s and exhibit an accuracy of ±0.1 °C under quasi-steady conditions (Hymczak et al., 2021). Because of the surrounding tissue's thermal inertia, rectal temperature lags rapid internal shifts by 5--15 min, providing a time-integrated estimate of core heat content (Greenes and Fleisher, 2004).

**Oesophageal thermometry.** A lubricated thermistor or thermocouple is advanced \~35--45 cm through the nostril into the lower oesophagus, aligning with central blood temperature (Mekjavic and Rempel, 1990). Because of its proximity to large vessels, the oesophageal probe captures rapid changes in core blood temperature within \~10 s (Lee et al., 2000), and leads rectal measurements during both heating and cooling phases. Tolerance issues, probe displacement, and discomfort limit its use to short-term laboratory protocols.

**Gastrointestinal telemetry pills.** Ingestible capsules containing a precision thermistor and radio transmitter provide wireless measurements at 1--4 Hz sampling. Under controlled conditions, accuracy is ±0.1 °C (O'Brien et al., 1998). Transit time through the stomach and small intestine varies between 12 and 72 h, and measurements become invalid once the capsule enters the colon, typically marked by an abrupt temperature drop (Teunissen et al., 2012). Telemetry pills display intermediate dynamics, slower than oesophageal but faster than rectal responses (O'Brien et al., 1998).

**Tympanic thermometry.** Infrared tympanic devices estimate CBT from radiation emitted by the tympanic membrane, assuming equilibrium with carotid arterial blood. Accuracy depends strongly on probe orientation, ear-canal anatomy, and the absence of airflow or obstruction (Childs et al., 1999). Tympanic canal temperatures can diverge from oesophageal and rectal readings during exercise and recovery, particularly under convective airflow or incomplete sealing (Gagnon et al., 2010).

**Temporal-artery infrared and dual- or zero-heat-flux sensors.** Non-invasive infrared thermometers measure surface emission along the temporal artery, whereas dual-heat-flux (DHF) and zero-heat-flux (ZHF) sensors infer deep tissue temperature by combining paired heat-flux paths of different thermal resistances (Kitamura et al., 2010). These techniques are useful for ambulatory or field monitoring but require stable ambient conditions and careful calibration; drift can occur with sweating or variable skin perfusion (Bräuer et al., 2020).

**Pulmonary artery and bladder catheters.** Invasive thermistors located in the pulmonary artery directly measure mixed venous blood and remain the clinical *gold standard*. Bladder thermistors, integrated into urinary catheters, are less invasive and show small mean differences (≤ 0.2 °C) relative to pulmonary-artery temperature under stable hemodynamic conditions (Lefrant et al., 2003). Their use is restricted to medical or highly controlled research applications.

### Agreeability across sensor types

Inter-site comparisons show consistent but physiologically interpretable biases that depend on tissue depth, perfusion, and the rate of thermal change. Under steady conditions, rectal, intestinal, and oesophageal temperatures differ by less than 0.3 °C, but diverge during dynamic heating or cooling. Oesophageal readings track central blood temperature most closely, typically within ±0.2 °C of pulmonary-artery measurements and with the fastest response (≤10 s) (Lefrant et al., 2003; Robinson et al., 1998). Rectal temperature lags oesophageal by 10--25 min and averages 0.3--0.6 °C lower during heating phases (Lee et al., 2000). Intestinal or telemetry-pill temperatures are intermediate, initially 0.4--0.9 °C lower than rectal when the capsule remains in the stomach, but converging to ≤ 0.2 °C once it passes into the small intestine (Notley et al., 2021; Sparling et al., 1993; Teunissen et al., 2012).

Bladder thermistors agree well with pulmonary-artery temperature (bias ≤ 0.2 °C) under stable perfusion, but deviate during low urine flow or bypass (Lefrant et al., 2003). Rectal and oesophageal values remain within 0.4 °C of pulmonary-artery readings at rest, confirming their reliability as integrated estimates of body heat content (Robinson et al., 1998).

Non-invasive ear and forehead methods exhibit larger scatter. Infrared tympanic thermometers underestimate deep-core temperature by 0.3 °C at rest and by \~1 °C during exercise, with errors increasing to \>1.5 °C when rectal temperature exceeds 39 °C (Craig et al., 2002; Huggins et al., 2012). Even meta-analytic evidence across \>30 studies indicates wide limits of agreement (± 1.3 °C), making tympanic readings unreliable for precise monitoring (Craig et al., 2002). Temporal-artery infrared and axillary measures show similar variability (Robinson et al., 1998).

Zero-heat-flux (ZHF) thermometers show markedly improved accuracy, differing from pulmonary-artery temperature by only --0.06 °C (mean) with limits of agreement ± 0.89 °C (Verheyden et al., 2022). These perform comparably to oesophageal and bladder probes under anaesthesia when the forehead site remains perfused. Emerging dual-heat-flux and heart-rate-derived algorithms can estimate core temperature non-invasively with mean biases around 0.2--0.3 °C, but limits of agreement ± 0.6--0.7 °C (Agostinelli et al., 2023; Verdel et al., 2021). They remain sensitive to local perfusion and ambient conditions but hold promise for field and occupational studies.

Overall, oesophageal and pulmonary-artery sites provide the most responsive and accurate dynamic indicators of CBT, while rectal, intestinal, and bladder sensors yield stable integrated measures of stored heat. Infrared and heat-flux methods enable practical non-invasive alternatives when calibration and contextual metadata are explicitly documented.

### Known confounders and modifiers

Core body temperature is shaped by multiple intrinsic and extrinsic influences that must be measured, controlled, or statistically adjusted in experimental protocols. These factors act through metabolic, hormonal, neural, and environmental pathways that shift the thermoregulatory set-point or modify heat-exchange efficiency.

**Circadian influences.** CBT exhibits a robust endogenous oscillation of approximately 0.8--1.0 °C under normal entrainment, generated by the suprachiasmatic nucleus and peripheral clock gene networks (Kräuchi, 2002; Kräuchi and Wirz-Justice, 1994). The nadir occurs near 04:00--05:00 h, coinciding with peak melatonin and lowest alertness, while the acrophase appears around 16:00--18:00 h. This rhythm persists under constant posture and ambient conditions, confirming endogenous control, though masking by sleep, posture, and activity can shift observed CBT by ±0.3 °C (Kelly, 2006; Kräuchi, 2002; Refinetti, 1992). Ambient light exposure (Dijk et al., 1991; Elkounni et al., 2025) and recent travel may also alter phase and amplitude. Session timing, chronotype alignment, and relative phase (hours from habitual wake time or dim-light melatonin onset) should therefore be logged and, where possible, standardised across participants.

**Sex.** Generally, females exhibit higher core temperatures than males (Diamond et al., 2021; Waalen and Buxbaum, 2011). During exercise under heat stress, early observational studies suggested women experienced greater and more rapid increases in core temperature than men; however, these differences are largely explained by confounding factors such as a lower body mass, lower aerobic capacity, and a higher relative metabolic heat production in females (Debray et al., 2025; Dervis et al., 2016; Gagnon and Kenny, 2012a). When males and females are appropriately matched for physical characteristics and the biophysical requirement for heat loss, core temperature responses are generally similar, though women may experience slightly greater increases (0.2°C to 0.4°C) only during severe, uncompensable heat stress (Lei et al., 2017). This difference may be clinically insignificant (Giersch and Charkoudian, 2025).

**Sex hormones and reproductive status.** Progesterone elevates the hypothalamic thermoregulatory set-point, increasing resting core body temperature by approximately 0.3--0.5 °C during the luteal phase. In contrast, oestrogen facilitates peripheral heat dissipation through cutaneous vasodilation and enhanced skin perfusion (Charkoudian and Stachenfeld, 2016). Women using combined oral contraceptives exhibit a constant, mid-luteal-like CBT profile, typically 0.3--0.4 °C higher than naturally cycling follicular-phase values, with reduced circadian amplitude and phase stabilisation (Baker et al., 2001; Baker and Driver, 2007; Stephenson and Kolka, 1993). Accurate determination of menstrual or contraceptive phase is therefore essential in mixed-sex studies.

During perimenopause, fluctuating oestrogen levels destabilise hypothalamic feedback and narrow the thermoneutral zone, producing transient hyperthermic flushes (Freedman, 2014). Oestrogen therapy alone lowers the vasodilation and sweating thresholds, effectively narrowing the interthreshold zone (Freedman and Krell, 1999; Gupta et al., 2000), whereas the addition of progestin raises the defended temperature and CBT by \~ 0.3 °C, mirroring premenopausal luteal physiology (Baker et al., 2020; Stachenfeld et al., 2000). Exogenous sex hormones used in contraception, menopausal hormone therapy, or gender-affirming treatment likewise alter thermoregulatory set-point and amplitude: oestradiol-dominant regimens generally lower or stabilise CBT via enhanced vasodilation, while progestin-dominant or androgenic formulations elevate CBT and attenuate peripheral heat loss (Baker et al., 2020; Freedman and Blacker, 2002; Gombert-Labedens et al., 2025). Precise documentation of hormonal formulation, dosage, and treatment duration is essential for accurate cross-participant comparison.

**Age.** Advancing age reduces sweat-gland output and cutaneous vasodilation, slowing heat loss and increasing peak CBT during heat stress (Kenney and Munce, 2003). Under thermoneutral conditions, core temperature differences by age were found to be \~ 0.15 °C based on data from over 18.000 people (Waalen and Buxbaum, 2011).

**Fitness.** Aerobically trained individuals show slightly lower resting CBT (\~0.2 °C) and reduced heat-storage rates for a given metabolic load, owing to expanded plasma volume, earlier sweat onset, and efficient peripheral perfusion (Périard et al., 2021).

**Heat acclimation.** Repeated daily exposures, for even as few as 5 days, lower resting CBT by \~0.2--0.4 °C (Daanen et al., 2018; Taylor, 2014). Acclimated individuals maintain smaller CBT excursions and faster recovery under equivalent heat loads (Garrett et al., 2009). Acclimation adaptations partially reverse within 2--3 weeks of heat withdrawal; however, re-acclimation occurs quicker than initial acclimation (Daanen et al., 2018).

**Hydration and nutrition.** Dehydration ≥ 2 % body mass elevates CBT by 0.2--0.5 °C for a given workload due to plasma-volume reduction, impaired skin blood flow, and reduced sweat rate (Sawka et al., 2001). Diet-induced thermogenesis (DIT) transiently raises CBT by \~0.2--0.4 °C, peaking 1--3 h after eating, depending on macronutrient content (Westerterp, 2004), while the presence of diabetes mellitus, insulin resistance, obesity or thyroid disease alters the impacts (Tzeravini et al., 2024). Caffeine and capsaicin stimulate metabolic heat production, whereas alcohol depresses vasoconstriction, lowering CBT in cool conditions (Michlig et al., 2016; Romanovsky, 2007).

**Body composition.** Greater subcutaneous adiposity increases insulation and thermal inertia, lengthening CBT time constants by 20--30 % compared with lean individuals (Havenith, 2001). Conversely, higher muscle mass and surface-to-mass ratio facilitate faster heat dissipation.

**Posture.** Posture changes (supine to upright) can transiently alter CBT by \~0.1--0.4 °C through redistribution of blood volume and convective exchange (Donaldson et al., 1996; Tikuisis and Ducharme, 1996).

**Chronotype and sleep timing.** Interindividual differences in circadian phase shift CBT acrophase and amplitude (Taillard et al., 2003). Evening types (*owls*) exhibit delayed peaks and elevated nocturnal troughs, while morning types (*larks*) peak earlier by around 2 hours (Baehr et al., 2000; Kerkhof and Van Dongen, 1996). Sleep deprivation may blunt CBT amplitude, delay phase onset and lower overall CBT the following day during wake hours (Hibi et al., 2017).

**Neurodivergent** **populations.** Evidence from autism spectrum disorder (ASD), ADHD, and related neurodevelopmental conditions indicates altered autonomic balance and circadian regulation. Individuals with ASD frequently display attenuated CBT amplitude and increased day-to-day variability, suggesting weaker circadian entrainment (Dell'Osso et al., 2022). Melatonin secretion profiles in ASD are often delayed or reduced (Z. Wu et al., 2020), producing phase lags of 1--4 h relative to typically developing controls, with corresponding CBT delays of similar magnitude (Rossignol and Frye, 2011). ADHD is associated with delayed sleep onset, longer sleep latency, and a consistent eveningness preference (Snitselaar et al., 2017), all of which shift CBT acrophase later into the evening (Bijlenga et al., 2013).

**Underlying medical conditions and medications.** Fever and systemic inflammation raise the hypothalamic set-point via cytokine-mediated prostaglandin synthesis (Romanovsky, 2007). Thyroid dysfunctions, particularly hyperthyroidism, elevate basal metabolic rate and CBT, whereas hypothyroidism lowers it by a similar margin (Iwen et al., 2018). Autonomic neuropathy impairs thermoeffector control of skin blood flow and sweating, increasing vulnerability to heat and cold stress (Cheshire, 2016). Diabetes mellitus, through autonomic and microvascular dysfunction, reduces heat-dissipation capacity and alters core temperature responses (Kenny et al., 2016; Rutkove et al., 2009). Parkinson's patients have lower nighttime CBT following the severity of RSB symptoms (Zhong et al., 2013). Spinal cord injury, especially lesions at or above T6, interrupts sympathetic outflow and sweating/vasomotor control, leading to impaired thermoregulation (Handrakis et al., 2017; Karlsson, 2006). β-blockers, anticholinergics, sedatives, and SSRIs further modulate thermoregulatory control and should be screened (Romanovsky, 2007).

**Measurement artefacts**. Shallow rectal insertion, oral breathing/cold or hot fluids, or cerumen/misalignment in tympanic readings bias results; for ingestible pills, ingestion/timing, GI motility and device bias matter (Byrne and Lim, 2007; Childs et al., 1999; Hunt et al., 2017; ISO, 2004).

### Data handling methods

#### Sensor calibration

Sensor calibration is a critical step prior to data collection, particularly for ingestible telemetry pills and thermistors, to ensure measurement accuracy and correct for systematic bias. The standard approach involves evaluating each sensor individually against a certified, traceable reference thermometer in a circulated, heated water bath (Byrne and Lim, 2007). Calibration should be performed across a physiologically valid range of temperatures (typically three to five discrete points, such as 30 °C, 34 °C, 38 °C, and 42 °C). After allowing sufficient time for the sensor and water temperature to stabilise (e.g., \>4 minutes), simultaneous readings are recorded to establish a relationship (Hunt et al., 2017; Lee et al., 2000; O'Brien et al., 1998; Simpson et al., 2006).

Because individual sensors can exhibit systematic biases or offsets from the manufacturer\'s stated accuracy, the water bath data is used to generate an individualised linear regression equation for each sensor. This individual equation is then applied to correct the raw data collected during the actual experiment. Alternatively, a generalised linear correction equation can be applied to the raw data, provided that a single-point preliminary check confirms the sensor falls within an acceptable initial error margin (e.g., ±0.5 °C of the reference thermometer) (Hunt et al., 2017).

#### Data cleaning and correction

**Filtering for noise.** Practical approaches include low-pass or moving-average smoothing (e.g., 30--60 s windows) to suppress motion/respiratory artefacts while retaining thermoregulatory trends (Bongers et al., 2015; Byrne and Lim, 2007). For ingestible capsules, brief telemetry gaps (\< \~2 min) can be linearly interpolated; longer gaps (often caused by the sensor going temporarily out of range of the receiver) are excluded or spline-interpolated with caution (Bongers et al., 2015).

**Discarded data.** Artefact removal should target non-physiological discontinuities. Specific instances requiring data exclusion include:

\- Data points recorded before a sensor is properly affixed or ingested, or during known periods of temporary removal (e.g., bathing).

\- Sudden, transient depressions in gastrointestinal or oesophageal temperature are clearly associated with the ingestion of cold fluids or food, as these reflect local cooling rather than true core body temperature changes. To avoid these data blocks, several protocols provide food/drinks at around 36.5--37 °C (Byrne and Lim, 2007).

\- Data from the early phase of ingestible capsule transit; some protocols systematically erase data from the first several hours (e.g., 6 hours (Lee et al., 2000)) post-ingestion to avoid the instability and systematic errors associated with stomach transit.

**Typical ranges.** Normal resting core body temperature is tightly maintained between 36.0 -- 37.5 °C (Diamond et al., 2021; Mackowiak et al., 1992). Valid physiological data during severe thermal stress typically stays within the limits of clinical hypothermia (\< 35.0 °C) and severe hyperthermia or heat stroke (\> 40.0--40.5 °C). Readings falling significantly outside of these physiological extremes (such as sensor drops below 30 °C in ambulatory humans) are generally indicative of technical problems, equipment failure, cold food/drink ingestion, or the sensor expelled from the body.

#### Derived parameters

From the filtered signal, several derived parameters may be computed:

- [Baseline CBT (°C).]{.underline} Mean temperature during the final 10--15 min before exposure.

- [ΔCBT (°C).]{.underline} Difference between end- and start-exposure means; reflects net heat storage or dissipation.

- [Rate of rise (°C·h⁻¹).]{.underline} Linear slope of CBT during exposure; indicates the rate of uncompensated heat storage (Périard et al., 2021).

- [Peak CBT (°C).]{.underline} Maximum observed temperature during the protocol.

- [Area under the curve (AUC, °C·min).]{.underline} Integral of CBT above baseline across the session, often normalised by duration (°C·min) to quantify total thermal load (Datta et al., 2021).

- [Recovery slope (°C·h⁻¹).]{.underline} Rate of CBT decline post-exposure, used to assess heat-dissipation efficiency and vascular recovery kinetics.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Measure / Site           Sensor / Principle                       Response time   Accuracy        Advantages                                Limitations                           Approx. cost (€)\*
  ------------------------ ---------------------------------------- --------------- --------------- ----------------------------------------- ------------------------------------- ---------------------------------------------
  **Rectal**               Thermistor / thermocouple                10--30 s        ± 0.1 °C        Established reference, low noise          Invasive, slow dynamics               100--300

  **Oesophageal**          Thermistor (nasal insertion 35--45 cm)   5--10 s         ± 0.05 °C       Rapid response, tracks core blood temp.   Discomfort, motion artefact           150--400

  **Gastrointestinal**     Ingestible telemetry capsule/pill        5--15 s         ± 0.1 °C        Ambulatory, wireless                      Transit variability, cost             50--100 per capsule + receiver (1000--2000)

  **Tympanic**             Infrared thermopile                      \< 3 s          ± 0.2 °C        Non-invasive, rapid                       Position-dependent, earwax artefact   100--500

  **Dual-heat-flux**       Surface + heat-flux gradient             10--60 s        ± 0.1--0.2 °C   Continuous, wearable                      Calibration, ambient sensitivity      500--1500

  **Pulmonary/ Bladder**   Thermistor catheter                      1--2 s          ± 0.05 °C       Gold standard, high-frequency             Invasive, clinical only               \> 1000
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 1. Summary of core-temperature measurement techniques, signal properties, and practical considerations.

\* Costs represent approximate 2024 academic pricing; consumables not included.

## Skin temperature

### Why: the mechanistic reasons behind the measurement

Skin temperature (Tsk) represents the body's thermal interface with the environment. It reflects the dynamic balance between internal heat delivery via skin blood flow and external heat exchange through convection, radiation, and evaporation (Arens and Zhang, 2006; Havenith, 2001). Changes in skin temperature, therefore, serve as a direct indicator of cutaneous vasomotor adjustments that regulate core-to-environment heat transfer.

Unlike CBT, which changes slowly, skin temperature responds within seconds to alterations in air temperature, mean radiant temperature, air velocity, or clothing insulation. The spatial pattern of skin temperature provides insight into regional heat-loss pathways and thermoregulatory strategy: for example, distal (hand, foot) skin cooling denotes vasoconstriction, whereas proximal and facial warming mark vasodilation (Taylor, 2014).

At the whole-body level, mean skin temperature is a determinant of thermal comfort perception and autonomic heat-loss drive, forming part of the neural input that defines thermal sensation thresholds (Jacquot et al., 2014; Nadel et al., 1973; Zhang et al., 2004).

### How: sensor types for measurement 

**Contact sensors (thermistors, thermocouples).** Small, taped sensors measure surface temperature conductively. When properly mounted and shielded, both precision NTC thermistors and fine-wire copper--constantan thermocouples offer high accuracy and sub-second response; setup choices (contact pressure, tape, shielding, cable movement) are the dominant error sources rather than sensor physics (MacRae et al., 2018; Psikuta et al., 2014). Furthermore, hard-wired connections can hinder participant movement and are prone to detachment during movement, limiting their use in field settings (James et al., 2014)

**Wearable loggers (e.g., iButton®).** Compact thermochrones enable long-term field recordings (typically 1--60 s sampling). After two-point calibration, accuracy \~±0.1 °C is achievable. However, due to their larger mass and stainless-steel packaging, they exhibit high thermal inertia, resulting in slower response times, with a time constant () of approximately 19 seconds in water. Consequently, fast temperature transients are effectively low-pass filtered, which can introduce momentary errors of up to 1 °C during rapid environmental changes (Hasselberg et al., 2013; Smith et al., 2010; van Marken Lichtenbelt et al., 2006).

**Infrared thermometry.** Handheld infrared thermometers provide non-contact \"point and shoot\" spot measurements of thermal radiation emitted from the skin (Aaron J E Bach et al., 2015). These low-cost devices are highly valid and reliable for measuring skin temperature under stable, resting thermoneutral conditions (Buono et al., 2007). However, their accuracy significantly degrades in the presence of physical or environmental stressors. Specifically, sweat accumulation on the skin alters its radiant properties, leading infrared thermometers to substantially underestimate true skin temperature during exercise or in hot environments (Aaron J E Bach et al., 2015; James et al., 2014).

**Infrared thermography (IRT).** IRT provides non-contact regional/whole-body mapping. With emissivity set near human skin values (\~0.98), reflected temperature accounted for, and viewing distance/angle controlled, modern systems achieve ≲0.1--0.2 °C thermal resolution under static, controlled scenes (Almeida et al., 2022; Lahiri et al., 2012). Similar to infrared thermometers, moisture, sweat, or topical lotions act as physical barriers that lower apparent emissivity and can introduce massive temperature errors (Bernard et al., 2013).

### Where: body sites of measurement

Skin temperature exhibits large regional variation; typically smaller under thermoneutral and warm conditions, and potentially exceeding 10 °C across the body under cold exposure (Arens and Zhang, 2006; Hardy et al., 1938; E R Nadel et al., 1971). These differences arise from the heterogeneous distribution of skin blood flow, subcutaneous fat, and local exposure to environmental heat exchange. The choice of *where* to measure Tsk depends fundamentally on whether the aim is to obtain a representative whole-body mean or to probe regional mechanisms of thermoregulation.

- ![A full shot of a person and person AI-generated content may be incorrect.](C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git\_build_intermediate\media/media/image1.jpeg){width="5.5in" height="5.992346894138232in"}

Figure 1. Body sites for skin temperature measurement used across protocols.\
Anterior and posterior views show 18 anatomical regions grouped by head, torso, arms, and legs. Labels adopt a consistent left/right (L/R), anterior/posterior (A/P), and medial (M) notation (e.g., 13AL = left anterior wrist). The map aligns common measurement sites based on the meta reviews of (Choi et al., 1997; ISO, 2004; Kuwabara et al., 2006; Liu et al., 2011; Song et al., 2024; Winslow et al., 1936).

In mechanistic or circadian thermophysiology, averaging across sites can obscure key regional dynamics. Site-specific analysis, therefore, may be preferred when the objective is to characterise *where* and *how* heat exchange occurs.

- [Distal skin (hands/feet/ankle)]{.underline}. Sensitive marker of sympathetic vasomotor tone via AVA control; the distal--proximal gradient (DPG) predicts sleep-onset latency and comfort transitions (Kräuchi et al., 2000).

- [Proximal trunk (chest/back/thigh)]{.underline}. Tracks core-to-shell transfer and internal thermal load, with less susceptibility to local drafts than distal sites (ISO, 2004).

- [Face/neck.]{.underline} Rapidly responsive to both thermal and affective stimuli; facial thermal shifts of \~0.3--0.5 °C accompany social/affective manipulations (Ioannou et al., 2014).

- [Asymmetry and field studies.]{.underline} In non-uniform environments, anterior/posterior or left/right averages and region-specific weighting improve representativeness.

A wide range of formulas exists for integrating multiple site temperatures into a single representative mean. These computational approaches are described under *Data handling methods*, where the weighting systems and historical variants are consolidated in **Error! Reference source not found.** in **Error! Reference source not found.**.

### Agreeability across sensor types

Agreement among skin temperature systems depends on sensing principle (contact vs infrared), sensor packaging (mass, encapsulation material, backing), attachment method, sampling rate, firmware, and manufacturer calibration. Under steady conditions, co-located contact devices such as thermistors, thermocouples, and calibrated iButtons typically agree within ± 0.2--0.3 °C, although small systematic offsets may occur. Classic validations reported low bias (\~ --0.09 °C) and high precision (SD \~ 0.05 °C) for iButtons relative to reference thermistors, although brand- or model-specific differences of up to \~ 0.5 °C have also been noted, reflecting variation in encapsulation, adhesive insulation, and internal thermal time-constants (Kelechi et al., 2011; MacRae et al., 2018).

Attachment and packaging effects are among the largest practical error sources. Covering thermistors with foam or adhesive tape elevates readings by as much as +1.3 °C, particularly in thermoneutral air, due to reduced convective and evaporative loss (Buono and Ulrich, 1998). Manikin experiments confirm up to 2 °C under- or over-estimation depending on tape type, covering, and clothing insulation (Psikuta et al., 2014) while finite-element models demonstrate that low-conductivity foam backings trap heat around the probe (Boetcher et al., 2009). MacRae et al. (MacRae et al., 2018) review 21 contact-sensor studies and found measurement biases ranging from \< 0.5 °C to \> 0.5 °C, with 95 % limits of agreement often spanning ± 1 °C in vivo. They attribute most between-study spread to differences in sensor housing, attachment pressure, and environmental control, and noted that more than half of published experiments omit key metadata, e.g. sensor model, calibration procedure, attachment method, and shielding -- limiting reproducibility across laboratories.

Infrared modalities introduce additional sources of variability due to assumptions about emissivity, corrections for reflected radiation, and viewing geometry. Hand-held infrared thermometers and thermal cameras consistently overestimate skin temperature relative to contact probes, with mean biases of +0.8 to +1.9 °C during exercise or rapid thermal transitions (Aaron J E Bach et al., 2015; Buono et al., 2007; Maley et al., 2020; Matsukawa et al., 2000). A cold-exposure comparison reported a +1.8 °C bias (95 % LoA --0.46 to +4.07 °C) (Maley et al., 2020). The first systematic review of conductive versus infrared methods (Aaron J.E. Bach et al., 2015) found that 12 of 16 studies exceeded the commonly accepted ±0.5 °C bias and ±1 °C limits of agreement, particularly under exercise or radiant-load conditions. Subsequent reviews identified environmental and technical drivers, e.g. emissivity control, calibration-target temperature, and region-of-interest selection, as dominant determinants of variability (Fernández-Cuevas et al., 2015; Maniar et al., 2015; Moreira et al., 2017). Delphi consensus work (Moreira et al., 2017) now defines minimum reporting standards for infrared thermography, including emissivity = 0.97, fixed camera--subject distance, reference calibration targets, and ambient control.

Beyond the sensing principle, brand/model choice and setup variables (adhesive type, applied pressure, site curvature, shielding) can further shift readings. Across studies, inter-device spreads of \~ 0.5 °C are common even under controlled laboratory conditions, and ±1--2 °C differences appear under transient or asymmetric exposures (Aaron J.E. Bach et al., 2015; Boetcher et al., 2009; Buono and Ulrich, 1998; Cheung and Sweeney, 2001). While broad concordance between thermistor- and iButton (thermochron)-based systems is well established, brand-resolved benchmarking for skin-temperature loggers remains sparse.

### Known confounders and modifiers

Skin temperature is influenced by numerous physiological, environmental, and behavioural factors that interact across time scales. These modifiers must be carefully considered when interpreting or comparing measurements across individuals, sessions, or studies.

**Circadian influences.** Skin temperature follows a robust circadian rhythm orchestrated by the suprachiasmatic nucleus through sympathetic outflow and melatonin secretion. Distal regions such as the hands, wrists, and feet typically warm during the evening and reach their highest temperatures around the biological night, promoting heat dissipation and facilitating sleep onset. In contrast, proximal and facial regions tend to mirror the diurnal rhythm of core temperature, showing a mid-afternoon maximum and nocturnal decline (Kräuchi and Wirz-Justice, 2001). The distal--proximal gradient (DPG = Tsk distal − Tsk proximal) increases sharply before habitual sleep onset, often preceding the evening melatonin rise by about an hour, and has become a validated physiological marker of circadian phase (Abe and Kodama, 2015; Kräuchi et al., 1999, 1997).

**Chronotype and sleep timing.** Chronotype also modulates these temporal patterns: evening types exhibit delayed distal warming and smaller nocturnal DPG amplitudes relative to morning types (Brooks et al., 2023). Behavioural factors such as posture, recent activity, exposure to light, or use of screens with high blue light content before bedtime can attenuate distal vasodilation and blunt the nocturnal Tsk rhythm. Conversely, behaviours that promote peripheral vasodilation, such as foot bathing before sleep, accelerate distal warming and shorten sleep-onset latency (Liao et al., 2005). Because each measurement site expresses a distinct phase and amplitude of the daily temperature rhythm, cross-site comparisons should be interpreted in conjunction with the *2.2.3. Where: Body sites of measurement* Chapter.

**Sex.** Because women produce less metabolic heat and have a thicker layer of subcutaneous fat (which insulates the body core but leaves the skin cooler), men generally exhibit significantly higher average skin temperatures than women across most body regions at rest, particularly in the morning (Marins et al., 2015). A woman\'s skin temperature is significantly more affected by the exposure temperature than a man\'s: in cold exposure, the skin temperature drops faster and more in women, and the opposite is observable in warm exposure, mostly due to lower sweating thresholds and earlier onsets in men (Xu et al., 2024). Distal body parts show the greatest sex differences; for example, females\' foot temperatures are consistently much lower than males\' when resting in cool environments (Xu et al., 2025).

**Sex hormones and reproductive status.** Overall, females Sex steroid hormones strongly modulate cutaneous thermoeffector thresholds and baseline skin perfusion, thereby shaping skin-temperature patterns across the menstrual cycle and reproductive lifespan. Progesterone, elevated in the luteal phase, raises resting Tsk, increases vasoconstrictor responsiveness, and shifts the vasodilation threshold rightward, delaying heat dissipation under thermal load (Baker et al., 2020; Kirby et al., 2022; Wenner et al., 2011). In contrast, oestrogen enhances cutaneous vasodilation through both central autonomic pathways and peripheral nitric-oxide--mediated mechanisms (Charkoudian, 2010; Kellogg et al., 1999), promoting capillary recruitment and improving thermal conductance. Reduced oestrogen availability, whether in the late follicular phase, during menopause, or due to low-dose formulations, decreases skin perfusion and heightens thermal instability (Charkoudian and Stachenfeld, 2016).

Human microdialysis and local-heating studies further show that hormonal state alters nitric-oxide--dependent vasodilation, with combined oral contraceptive users exhibiting enhanced NO-mediated vasodilation compared with early-follicular measurements (Turner et al., 2023). These endocrine patterns underlie the well-known 24-h elevation in body temperature during the luteal or active-pill phase (Baker et al., 2001), as well as the lower vasodilation and sweating thresholds during oestrogen-dominant states (Charkoudian and Johnson, 1999).

Across reproductive stages, these mechanisms generate distinct regional and diurnal skin-temperature signatures. For example, women using combined oral contraceptives often show higher mean skin temperature but reduced diurnal amplitude, reflecting hormonal stabilisation and blunted cycling. During menopause, declining oestrogen produces marked vasomotor lability, with brief surges of facial and upper-body skin temperature (hot flashes) followed by rapid cooling (Freedman, 2014; Freedman and Blacker, 2002; Freedman and Krell, 1999). Because these hormonal influences vary by phase, formulation, and dosage, precise documentation of menstrual, contraceptive, or menopausal status is essential for meaningful cross-participant comparison.

**Age.** Ageing attenuates cutaneous vascular conductance and slows the temporal dynamics of local thermal responses. Older adults exhibit roughly half the reflex vasoconstriction capacity of young adults, with diminished neurotransmitter release, reduced nitric-oxide bioavailability, and slower vasodilatory recovery following temperature perturbations (Greaney et al., 2015; Holowatz and Kenney, 2010; Kenney et al., 2021, 2014). These alterations lead to smaller skin-temperature fluctuations, delayed distal warming, and blunted distal--proximal gradients, especially under thermal stress. Classic and contemporary studies confirm that older adults exhibit about half the reflex vasoconstrictor capacity of young adults and reduced active vasodilator responsiveness during heat stress (Greaney et al., 2015; Kenney and Munce, 2003; Van Someren et al., 2002).

**Fitness and acclimation.** Regular aerobic training or repeated heat exposure enhances cutaneous vascular sensitivity and thermoeffector gain. The threshold for vasodilation occurs at a lower internal temperature and the slope of the *skin temperature -- core body temperature* relationship steepens, producing faster surface warming and more efficient cooling under heat stress (Charkoudian, 2010). Heat-acclimated or physically fit individuals therefore display quicker Tsk recovery after thermal loads and smaller inter-regional gradients than sedentary participants, making fitness and acclimation history relevant covariates in comparative analyses.

**Body composition.** Subcutaneous adipose tissue functions as a thermal insulator, reducing conductive heat transfer to the surface and dampening rapid changes in Tsk. Individuals with greater total or regional adiposity exhibit lower mean and trunk Tsk, especially under cool ambient conditions (Livingstone et al., 1987; Neves, 2017). Modern infrared thermography has confirmed strong negative correlations between regional fat mass and surface temperature across the trunk and limbs, with correlation coefficients around --0.6 to --0.8 (Silva et al., 2024). Because adipose distribution varies regionally and between sexes, Tsk heterogeneity cannot be fully explained by body-mass index alone. Including direct body-composition measures (e.g., bioimpedance, DEXA) or at least anthropometric surrogates improves interpretability.

**Nutrition and hydration.** Skin perfusion depends on circulating plasma volume, metabolic rate, and vascular endothelial integrity. Even mild hypohydration equivalent to 2 % of body-mass loss reduces skin blood flow by approximately 15--20 % and lowers mean Tsk by about 0.3 °C at a given metabolic rate (Cheuvront and Kenefick, 2014; Sawka et al., 1998). Beyond hydration, postprandial metabolic and vasoactive processes substantially alter skin temperature, differently between sexes (Martinez-Tellez et al., 2019). Stimulant and psychoactive compounds further modify cutaneous thermoregulation: Caffeine intake (\~ 200 mg) lowers distal and mean Tsk for several hours through adrenergic vasoconstriction and can delay the nocturnal distal warming associated with sleep onset (Mchill et al., 2014). Alcohol, conversely, induces short-lived vasodilation and Tsk elevation followed by rebound cooling as core heat is lost.

**Neurophysiological and psychological factors.** Emotional and cognitive states rapidly influence skin temperature via autonomic control. Acute stress, anxiety, and cognitive load activate sympathetic vasoconstriction, particularly in glabrous regions such as the fingertips and face, producing brief (seconds-to-minutes) drops in local Tsk (Kistler et al., 1998). Relaxation and meditative states, conversely, enhance parasympathetic tone and promote peripheral warming. These rapid fluctuations mirror electrodermal and heart-rate changes, reflecting tight coupling between emotional arousal and thermoeffector output in hypothalamic and medullary circuits.

**Neurodivergent populations.** Neurodevelopmental conditions such as autism spectrum disorder (ASD) and attention-deficit/hyperactivity disorder (ADHD) show persistent circadian and autonomic dysregulation that modifies skin-temperature rhythms. Individuals with ASD exhibit reduced melatonin secretion, flattened nocturnal temperature amplitudes, and elevated sympathetic tone, yielding unstable distal--proximal gradients and irregular sleep--wake cycles (Dell'Osso et al., 2022; Tordjman et al., 2013; Z. Wu et al., 2020). Genetic variants in clock genes further link circadian misalignment with autistic traits (Tesfaye et al., 2022). Adults with ADHD display delayed and lower core and skin temperatures, greater day-to-day variability, and weaker nocturnal warming (Bijlenga et al., 2013).

**Underlying medical conditions.** Chronic diseases that impair autonomic or vascular function markedly alter skin-temperature dynamics. Type 2 diabetes mellitus elevates the internal-temperature threshold for active cutaneous vasodilation and reduces nitric-oxide-dependent vasodilatory capacity, reflecting both endothelial and neural impairments (Charkoudian, 2010; Wick et al., 2006). Baseline vasoconstrictor tone may be reduced, yet reflex responses to cold remain near-normal, suggesting selective deficits in active vasodilator pathways. Cardiovascular and thyroid disorders further modify basal perfusion and metabolic rate, shifting baseline mean skin temperature upward or downward depending on whether vasodilation or vasoconstriction predominates (Cohen et al., 2023; Safer, 2011; Weiss et al., 1993). Patients with hepatic cirrhosis show persistently elevated proximal and distal skin temperatures and fail to reach the near-zero distal--proximal gradient normally observed at sleep onset, indicating impaired nocturnal vasodilatory control (Garrido et al., 2017). Spinal cord injury disrupts sympathetic vasomotor and sudomotor control below the lesion, producing segmental anhidrosis and regionally fixed mean skin temperature profiles that vary little with ambient or internal temperature changes (Safer, 2011; Weiss et al., 1993).

**Measurement artefacts.** Measurement artefacts can rival or even surpass physiological variance in skin temperature. Contact sensors alter local heat exchange through poor adhesion, insulating tapes, or vessel compression, while emissivity errors, reflections, and viewing geometry affect infrared thermography (MacRae et al., 2018; Playà-Montmany and Tattersall, 2021; Ring and Ammer, 2012). Substances such as sweat, gels, or lotions can lower emissivity and increase reflected ambient radiation, introducing errors of \> 4 °C if uncorrected (Bernard et al., 2013). Standardised cleaning of both the sensor surfaces and the skin, low-insulating fixation, sensor equilibration, and calibration under controlled ambient conditions are essential for reproducibility (Fernández-Cuevas et al., 2015).

### Data handling methods

#### Sensor calibration

To ensure measurement accuracy, contact temperature sensors such as thermistors and thermocouples must undergo rigorous calibration prior to human application (Buono and Ulrich, 1998; Smith et al., 2010). A standard and highly reliable calibration method involves immersing the sensors in a temperature-controlled, stirred water bath across a physiologically relevant temperature range (e.g., 10 °C to 40 °C) alongside a high-precision, certified reference thermometer (Smith et al., 2010). Thermistors typically achieve post-calibration accuracy of ± 0.2 °C when verified against reference thermometers in stirred water baths (James et al., 2014; Taylor et al., 2014). Thermochrons provide high digital resolution (0.0625 °C; manufacturer specification) but factory accuracy of ± 0.5 °C, and inter-sensor offsets of \~0.2--0.4 °C are common when multiple devices are used simultaneously (MacRae et al., 2018; Maxim Integrated Products, 2015). After a post calibration by conducting individual linear regression analyses on each sensor to derive unique slope and intercept correction factors, the random error and systematic bias for both thermistors and iButtons can be reduced to negligible amounts (Smith et al., 2010; Su et al., 2025).

For infrared thermography, radiometric calibration using a blackbody or in-frame reference target, combined with emissivity correction (ε \~ 0.98), can control the drift under controlled laboratory conditions (Fernández-Cuevas et al., 2015; Ring and Ammer, 2012; Ul et al., 2023). However, even under controlled laboratory conditions, the expanded uncertainty of a calibrated thermal imager in practical use is approximately ±0.52 °C to ±0.6 °C, largely due to variations in ambient conditions, reflected background radiation, and distance effects (Ul et al., 2023).

#### Data cleaning and correction

**Filtering for noise.** Physiological sensors in contact with the human body often capture noise and random error during dynamic measurements (MacRae et al., 2018). Skin temperature data can be low-pass filtered at 0.05--0.1 Hz to remove high-frequency artefacts caused by movement or airflow, while preserving thermoregulatory fluctuations that occur over tens of seconds to minutes (Taylor et al., 2014). For 1 Hz wearable recordings, a moving-average or LOESS can balance temporal fidelity and noise reduction.

In infrared thermography, accurate emissivity and ambient control are critical. Human skin emissivity is \~0.98 ± 0.01 (Bernard et al., 2013); moisture, gels, or lotions lower apparent emissivity and can introduce temperature errors of several °C through increased ambient reflection (Fernández-Cuevas et al., 2015). Using ε = 0.97--0.98, perpendicular camera alignment, fixed distance, and controlled background temperature can minimise systematic bias to approximately ±0.3 °C under optimal laboratory conditions (Aaron J E Bach et al., 2015; Aaron J.E. Bach et al., 2015; Fernández-Cuevas et al., 2015; Ring and Ammer, 2012).

**Discarded data.** Sensor drift during long recordings should be corrected by cross-calibrating thermistors pre- and post-session (MacRae et al., 2018). Transient spikes (e.g., ±0.5 °C lasting \<10 s) from contact loss or cable movement should be removed or interpolated; periods of pressure or insulation should be flagged, as they may elevate local Tsk (James et al., 2014). Field and continuous physiological assessments are rarely free of artefacts caused by poor skin contact, loose tape, or sudden physical interference. To address this, automated artefact rejection procedures are implemented; a common non-parametric method involves calculating the rate of change (ROC) to remove fast temperature drops or rises exceeding one interquartile distance from the 25th or 75th percentiles, followed by removing implausibly low absolute temperatures and linearly interpolating the gaps e(van Marken Lichtenbelt et al., 2006). Periods where the sensor is subjected to excessive pressure or occlusion by heavy tape should also be flagged, as the insulating microenvironment impairs local heat dissipation and artificially elevates the localised skin temperature beneath the probe (MacRae et al., 2018). Additionally, some analysis protocols discard data from the initial acclimation/overshoot period (e.g., the first 10--30 minutes of room exposure) to ensure that only steady-state, thermally equilibrated temperatures are analysed (Ul et al., 2023).

**Typical ranges.** Skin temperature varies widely across body segments and in response to the ambient environment. In thermally neutral conditions at rest, the mean skin temperature generally ranges between 32.5 °C and 34.5 °C (Buono et al., 2007; Livingstone et al., 1987). Proximal core areas (e.g., chest and back) remain relatively stable, whereas distal regions, such as the hands and feet, exhibit the most significant fluctuations due to sympathetic vasoconstriction or vasodilation (Maniar et al., 2015; Xu et al., 2025). For instance, finger temperatures can rise to 37 °C during passive heating, but can drop to 24 °C or lower in cool ambient conditions (Matsukawa et al., 2000). Skin temperature readings falling drastically outside these physiologically expected bounds (i.e., below 16 °C without extreme cold water provocation, or above 40 °C without a severe heat source) are typically indicative of artifacts, sensor detachment, or painful thermal stress and are treated accordingly (Aaron J.E. Bach et al., 2015; Smith et al., 2010).

#### Derived parameters

Depending on study design and research aim, several key parameters are derived from the preprocessed Tsk signal:

- [Baseline Tsk (°C).]{.underline} The mean temperature over the final 5--10 minutes of the pre-exposure or neutral period; serves as a reference point for calculating subsequent changes.

- [ΔTsk (change, °C or K).]{.underline} The difference between end- and start-exposure means, indicating the magnitude of peripheral warming or cooling.

- [Rate of rise or fall (°C·h⁻¹).]{.underline} The slope of the linear regression fitted to the Tsk trajectory over the exposure period, describing the speed of thermal adaptation or recovery.

- [Distal--Proximal Gradient (DPG, °C).]{.underline}The mean of distal (hands, feet) minus proximal (chest, thigh) sites; a sensitive indicator of sympathetic vasomotor tone. Positive DPG values reflect vasodilation, whereas negative values indicate vasoconstriction.

- [Amplitude (diurnal or experimental, °C).]{.underline} The difference between maximum and minimum Tsk within a defined period, capturing circadian modulation or thermal variability.

[Mean skin temperature (°C).]{.underline} The weighted average across all measurement sites, representing overall shell temperature and used to estimate body heat storage. Since the 1930s, dozens of formulas have been proposed to estimate mean skin temperature from discrete site measurements. The earliest models used three to seven body sites, while later standards such as ISO 9886:2004 formalised four-, eight- and fourteen-site sets with equal or weighted contributions. Comparative analyses in the 2010s--2020s revealed between-formula spreads of up to 1 °C under non-uniform exposures (MacRae et al., 2018), underscoring the need to report both the included sites and their weighting coefficients explicitly. The principal historical and contemporary formulations are consolidated in Mean Skin Temperature Formulas.

Modified or hybrid mean skin temperature models are used when local conditions deviate from thermal uniformity or when higher spatial resolution is needed:

- [Cold exposure.]{.underline} Under cold air, formulas place disproportionately high weight on distal segments to capture extremity-driven heat loss. This reflects larger spatial non-uniformity in cool environments (Su et al., 2025).

- [Asymmetrical or radiant conditions.]{.underline} When exposures are non-uniform (e.g., radiant panels, drafts), it's appropriate to compute MST with region-specific subsets (e.g., anterior vs posterior) or adopt non-uniform comfort models that aggregate local states to whole-body sensation.

- [Brown Adipose Tissue (BAT) studies.]{.underline} High-resolution protocols use many sites (up to 26) to resolve regional thermogenesis and gradients; across-equation differences can be material (Martinez-Tellez et al., 2017).

- [Sleep physiology.]{.underline} Night-time studies re-evaluate daytime weighting factors, accounting for covered body areas and pressure artefacts from the supine posture (Lan et al., 2019; Xu and Lian, 2024).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Measure**                 **Sensor / Method**         **Sampling rate**   **Accuracy**   **Advantages**               **Limitations**                        **Approx. cost (€)\***
  --------------------------- --------------------------- ------------------- -------------- ---------------------------- -------------------------------------- ------------------------
  **Local Tsk**               Thermistor / thermocouple   0.1--1 Hz           ±0.1 °C        High precision, small size   Wired, local interference              50--300 per channel

  **Infrared thermography**   Calibrated IR camera        1--10 Hz            ±0.2 °C        Full-field spatial mapping   Sensitive to emissivity, reflections   5,000--20,000
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 2. Summary of skin-temperature measurement techniques and typical characteristics

\* Costs represent approximate 2024 academic prices for durable equipment; disposables, maintenance and analysis software are not included.

## Sweat, skin moisture and skin conductance

### Why: the mechanistic reasons 

Sweating is the body's principal avenue for evaporative heat loss during thermal stress. In warm, dry, and moving air, evaporation can provide 70--80 % of total heat dissipation, becoming the dominant term in the heat-balance equation when convective and radiant avenues are constrained (Havenith, 2001; E. R. Nadel et al., 1971; Stephenson et al., 1984). The onset, rate, and distribution of sweat secretion are governed by sympathetic cholinergic activation of eccrine glands, integrating both core- and skin-temperature drives (Arens and Zhang, 2006; Shibasaki and Crandall, 2010).

Local sweat rate (LSR) therefore represents the available evaporative capacity at a specific site, while the spatial recruitment pattern of active glands indicates how efficiently the body scales evaporative cooling during sustained or repeated heat loads (Havenith, 2001; Kondo et al., 1998).

Effective evaporation depends not only on secretion rate but also on skin wettedness, air velocity, humidity, and clothing permeability, which together determine the fraction of sweat that actually evaporates versus accumulates or drips (Havenith and van Middendorp, 1990; ISO, 2004).

Electrodermal activity (EDA), also termed galvanic skin response (GSR), provides an indirect index of sweat-duct filling and sudomotor nerve activity measured via small conductance changes. Because eccrine glands act as variable resistors when filled with electrolyte, EDA reflects both thermoregulatory sweating and non-thermal sympathetic arousal (Benedek and Kaernbach, 2010a; Boucsein, 2012). In thermal-physiology protocols, combining sweat-rate or skin-moisture measures with EDA links autonomic thermoeffector output to perceptual and emotional processes, allowing integrated assessment of heat strain, thermal comfort, and sympathetic load (Critchley, 2002; Gerrett et al., 2018).

### How: sensor types for measurement 

Quantifying sweating and skin conductance requires methods that differ in physical principle, temporal resolution, and calibration rigour. Each technique provides a different window onto evaporative heat loss or sudomotor activation, from direct local sweat flux to indirect indices of gland filling and surface moisture.

**Local sweat rate (LSR, ventilated-capsule method).** The gold-standard technique measures water-vapour flux from a small, sealed skin area ventilated with dry air. The vapour-density difference between inlet and outlet streams, determined using dew-point or infrared hygrometers, yields instantaneous LSR in mg·cm⁻²·min⁻¹ (Crawshaw et al., 1975; Havenith, 2001; Nadel et al., 1973). The system provides continuous, quantitative sweat-flux data, though it requires careful sealing and may slightly alter local evaporation.

**Near-skin humidity and skin moisture probes.** Simpler approaches employ miniature dew-point or capacitive (dielectric) sensors positioned a few mm above the surface to capture relative humidity in the skin microclimate (ISO, 2004). Readings are sensitive to contact pressure and ambient humidity drift, thus benefiting from standardised positioning and calibration against LSR.

**Absorbent-patch gravimetry and chemical analysis.** For integrated sweat-rate and composition data, absorbent pads or polymer films of known surface area are pre-weighed, applied for fixed intervals, and re-weighed post-collection; extracted sweat is analysed for electrolytes via ion chromatography (Baker et al., 2014, 2009). This method captures ionic composition and glandular adaptation but lacks temporal resolution.

**Colorimetric and microfluidic sweat patches.** Flexible polymer sensors containing hydrochromic dyes or serpentine microchannels visualise cumulative sweat volume and dynamics in real time (Koh et al., 2016; Madhu et al., 2025; Reeder et al., 2019; Yu and Sun, 2020). The colour intensity or length-of-fill correlates with sweat volume with latency of 1--3 s. These patches are inexpensive and well-suited for field or wearable applications, though quantitative use requires calibration against ventilated-capsule data and correction for evaporative loss beneath the patch.

**Whole-body sweat loss (WBSL).** Global evaporative water loss is determined gravimetrically from the change in nude body mass before and after exposure, corrected for fluid intake and urine output, and normalised to body-surface area (Cheuvront and Kenefick, 2014). Although WBSL integrates all regional fluxes, it lacks spatial or temporal resolution and is best interpreted alongside local measures.

**Electrodermal activity (EDA).** EDA quantifies sympathetic activation of eccrine sweat glands via changes in skin conductance between Ag/AgCl electrodes, typically at a constant 0.5 V DC and 4--32 Hz sampling (Benedek and Kaernbach, 2010a; Boucsein, 2012; Critchley, 2002). The signal comprises a slowly varying tonic component (skin-conductance level, SCL) and rapid phasic responses (skin-conductance responses, SCRs).

### Where: body sites of measurement

Sweating and electrodermal responses show strong topographical variation that reflects eccrine‐gland density, local skin temperature, and sympathetic innervation. Gland density ranges from fewer than 100 glands·cm⁻² on the trunk (e.g., \~64 on the back) to more than \~250--550 glands cm⁻² on palmar and plantar skin (Baker, 2019; Taylor and Machado-Moreira, 2013). During passive or low-metabolic heat exposures typical of sedentary laboratory studies, the highest thermoregulatory sweat rates occur on the forehead, upper back, chest, and thigh, whereas the distal limbs contribute less to total evaporative heat loss (Coull et al., 2021).

**Local sweat-rate sites**. Ventilated capsules and absorbent patches are most often applied to the forearm, chest, upper back, or thigh, which combine good attachment stability with representative thermoregulatory behaviour.\
Forearm placement remains the field standard due to historical comparability and low motion artefact, although biological variation between repeated trials can approach \~ 20--25 % CV (Kenefick et al., 2012). Trunk regions, particularly the back and chest, show higher reproducibility and smaller inter-individual variance than distal sites (CV \< 25 % under passive heating) when measured by the ventilated-capsule method (Rutherford et al., 2021). Technical-absorbent or polymer-patch methods produce equivalent steady-state flux estimates on these regions within \~10 % bias relative to capsule data (Morris et al., 2013).

**Skin-moisture and wettedness probes.** Capacitance or near-skin-humidity sensors are best mounted on flat, hairless surfaces such as the ventral forearm, upper arm, or upper chest, where contact pressure and curvature artefacts are minimal. These areas offer stable microclimates suitable for repeated recordings, whereas hair-bearing or curved surfaces (scalp, axillae, abdomen) introduce local humidity pockets that confound steady-state readings (Taylor and Machado-Moreira, 2013).

**Electrodermal-activity sites.** Electrodermal-activity electrodes detect sweat-duct filling and sympathetic activation. The palmar and plantar surfaces exhibit the highest gland densities and the largest phasic conductance responses but are also strongly influenced by emotional or cognitive stimuli (Hossain et al., 2022). For thermoregulatory studies, ventral forearm, upper arm, or upper chest placements are preferred, as they predominantly reflect thermal sympathetic drive rather than affective arousal.

**Confounding regions.** Certain regions, such as face, axillae, abdomen, and palms, may show sweating driven by non-thermal pathways (emotional (Harker, 2013; Wohlrab et al., 2023), gustatory (Laskawi et al., 1999), or visceral). Facial sweating contributes substantially to total evaporative heat loss (O'Brien and Cadarette, 2013) yet remains technically challenging to monitor continuously due to motion, airflow, and cosmetic interference (He et al., 2025).

### Agreeability across sensor types

Agreement between sweat-measurement systems depends on sensing principle, airflow characteristics, surface sealing, and temporal resolution. Comparative work shows that ventilated-capsule and technical-absorbent techniques yield closely matched steady-state local sweat rates under passive heating, with group-level bias typically \< 10 % and limits of agreement around ± 0.3 mg·cm⁻²·min⁻¹ (Morris et al., 2013). Reliability is region-specific: trunk sites (upper back/chest) show the highest repeatability (Intraclass Correlation Coefficient \~ 0.85), whereas forearm is lower (\~ 0.60) when measured during passive heating (Rutherford et al., 2021). Across repeated trials, analytical variance is dominated by biological variability plus subtle differences in capsule flow, seal integrity, and leak checks (Kenefick et al., 2012).

For near-skin humidity and skin-moisture probes, agreement improves when sensors are cross-calibrated against ventilated capsules under controlled, low-air-movement conditions and when pressure/occlusion are standardised. However, ambient air movement, condensation, and probe pressure can introduce appreciable error, so these systems are best treated as trend measures or calibrated surrogates of local sweat flux in sedentary laboratory settings (ISO, 2004).

Microfluidic/colorimetric patches show good concordance with capsule-derived flux once calibrated in situ during mild heat stress; typical absolute errors reported are on the order of RMSE \~ 0.2--0.4 mg·cm⁻²·min⁻(Koh et al., 2016; Reeder et al., 2019). Practical limitations include small air gaps or adhesive lift, which can under-collect sweat, and uncertainty from direct evaporation beneath the patch.

For electrodermal activity (EDA), signals recorded with constant-voltage or constant-current amplifiers are generally interchangeable when normalised within-subject and recorded with standardised electrode materials/placements; variability is driven more by electrode-skin interface (cleaning, gel/electrolyte, inter-electrode distance) than by the electronics themselves (Benedek and Kaernbach, 2010a, 2010b; Boucsein, 2012). Electrode-gel composition, surface cleaning, and inter-electrode distance contribute most measurement variability rather than electronics per se.

Overall, under controlled, sedentary laboratory conditions with careful calibration and placement, inter-method bias between established sweat-monitoring approaches (ventilated capsule, technical absorbent, calibrated microfluidics) is typically within \~ ± 10--15 %, with the remaining spread explained by biological variance and local setup details.

### Known confounders and modifiers

Sweat and electrodermal responses vary widely across individuals and conditions. Both are shaped by a combination of intrinsic physiological traits and extrinsic experimental factors that influence sudomotor drive, gland sensitivity, evaporative efficiency, or recording fidelity. The following modifiers should be considered when designing or comparing studies under sedentary or mild-activity thermal exposures.

**Circadian influences.** Sweating follows a diurnal rhythm coordinated with core body temperature and sympathetic tone. The onset and gain of the sweating response are lowest in the morning and highest in the late afternoon to early evening, paralleling the daily CBT maximum (Aoki et al., 1997; Stephenson et al., 1984). Under constant-routine conditions, local sweat rate and electrodermal activity both show afternoon elevations of \~15--25 %, attributed to circadian modulation of hypothalamic sympathetic output (Tayefeh et al., 1998). Sleep restriction or circadian misalignment dampens this rhythm, delaying sweating onset and reducing amplitude of both thermoregulatory and phasic EDA components (Timbal et al., 1975). Electrodermal and thermoeffector activity follow clear circadian organisation: EDA amplitude increases during sleep and exhibits a strong 24-h rhythm in controlled settings (Kim et al., 2018; Sano et al., 2014). Late-night light exposure or delayed chronotype shifts can attenuate the distal warming and sweating responses that normally precede sleep, altering both thermal comfort and circadian alignment (Czeisler et al., 1999; Kräuchi et al., 2000).

**Sex.** Men generally produce higher absolute sweat rates than women under the same heat load, mainly because of greater output per active gland rather than gland-number differences (Gagnon et al., 2013a, 2008; Gagnon and Kenny, 2012b, 2012a). Women, in turn, rely more heavily on cutaneous vasodilation for heat dissipation. This disparity is not due to an anatomical lack of sweat glands; in fact, because of their typically smaller body surface area, women actually possess a higher overall density of eccrine sweat glands than men. The reduced sweating response in females is driven by a significantly lower sweat output per individual gland and a reduced peripheral cholinergic responsiveness (Baker, 2019). Consequently, women are often characterized as more \"efficient\" sweaters during resting heat exposure (Yanovich et al., 2020). They tend to activate a higher percentage of their available sweat glands but secrete less overall fluid, which helps them avoid \"wasted sweating\", where excess sweat pools and drips off the skin without contributing to evaporative cooling, while still achieving effective thermal balance in moderately hot environments.

**Sex hormones and reproductive status.** Menstrual phase, oral-contraceptive use, and menopausal status primarily affect sweating by shifting the core-temperature threshold for activating heat-loss mechanisms (Lei et al., 2019; Smith and Havenith, 2012; Stachenfeld et al., 2000). Progesterone's thermogenic action elevates the hypothalamic set-point by roughly 0.4 °C in the luteal phase (Charkoudian and Stachenfeld, 2014; Israel and Schneller, 1950), reflected in higher oesophageal thresholds for sweating (38.0 ± 0.3 °C vs 37.3 ± 0.1 °C in the follicular phase) (Stachenfeld et al., 2000; Stephenson and Kolka, 1985).

Exogenous hormones exert similar effects. Combined OCPs raise the sweating threshold (Grucza et al., 1993; Sunderland and Nevill, 2003), consistent with progestin-mediated inhibition of warm-sensitive neurons (Nakayama et al., 1975). During the active high-hormone pill week, the oral-temperature threshold increases to \~ 37.15 ± 0.11 °C compared with the placebo week (Charkoudian and Johnson, 1997). Oestrogen counteracts this elevation: unopposed progestin yields a higher threshold (38.07 ± 0.17 °C), whereas combined oestrogen--progestin treatment lowers it (37.46 ± 0.18 °C), confirming oestrogen's cooling influence and antagonism to progestin (Stachenfeld et al., 2000; Stephenson and Kolka, 1999).

In postmenopausal women, oestrogen replacement similarly reduces sweating thresholds, while the addition of progestin abolishes this reduction (Brooks et al., 1997; Tankersley et al., 1992). Together, these findings demonstrate that progesterone elevates, and oestrogen lowers, the thermoregulatory operating point; an antagonistic interplay that underlies sex and hormonal differences in sudomotor control.

**Age.** Sweat-gland output and responsiveness decline progressively with ageing. Comparative studies report 30--40 % lower maximal sweat rates between 20 and 60 years, even under identical heat loads (Inoue et al., 2016, 1999). This reduction arises from atrophy of secretory coils, reduced cholinergic sensitivity, and impaired cutaneous vasodilation. Consequently, older adults show slower sweat onset and reduced regional uniformity, especially on the limbs and back. EDA amplitude and reactivity likewise diminish with age, reflecting lower sympathetic-skin response gain (Shibasaki and Crandall, 2010).

**Fitness and acclimation.** Aerobic training and repeated heat exposure both enhance sudomotor sensitivity and evaporative efficiency. Trained or acclimated individuals begin sweating at a lower core temperature and show steeper sweat rate--temperature slopes (Havenith and van Middendorp, 1990; Périard et al., 2015). Glandular recruitment expands, and the ionic composition of sweat (particularly Na⁺ and Cl⁻) shifts toward lower concentrations, reflecting ductal reabsorption adaptation. EDA studies show increased tonic levels during heat acclimation, consistent with heightened cholinergic activity (Gagnon and Kenny, 2012a).

**Body composition.** Subcutaneous adiposity insulates and increases heat storage requirements, typically delaying sweating and reducing heat-loss effectiveness under heat stress (Kenny et al., 2010; Morrissey et al., 2021).

**Hydration.** Around \~2% hypohydration, sweating and skin blood flow are reduced and evaporative heat loss becomes less effective, accelerating heat storage; functional impairments increase with greater deficits (Kenefick, 2018; Kenefick and Cheuvront, 2016; Sawka et al., 2015).

**Food intake and stimulants.** Postprandial thermogenesis modestly elevates metabolic heat production for several hours and can slightly raise core temperature, transiently lowering the load needed to trigger sweating (D'Alessio et al., 1988). Capsaicin (TRPV1 activation) elicits gustatory sweating via trigeminal sympathetic pathways (Drummond, 1995; Kawakami et al., 2016). Caffeine can modulate thermoregulatory responses in the heat, but effects on sweating and core temperature are heterogeneous across studies and doses (Hunt et al., 2021; Li et al., 2024). Nicotine increases sympathetic arousal, reflected in elevated EDA, while its effects on heat-evoked sweating remain less well characterised (Ho et al., 2020). Alcohol acutely increases skin perfusion and sweating with altered thermal sensation, followed by reduced core temperature and impaired thermoregulation (Yoda et al., 2005).

**Psychological and cognitive arousal**. Non-thermal sympathetic activation can strongly modulate EDA and palmar sweating. Mental workload, anxiety, or startle evoke rapid phasic conductance spikes and transient local sweating even under thermoneutral conditions (Boucsein, 2012; Critchley, 2002; Edelberg, 1972). These responses are most pronounced at glabrous sites such as the palms, soles, and forehead -- regions densely innervated by sympathetic cholinergic fibers (Taylor and Machado-Moreira, 2013), so they can obscure thermoregulatory signals if used for measurement. Non-glabrous placements (forearm, upper chest) minimise this interference.

**Neurodivergent populations.** Autonomic dysregulation in autism spectrum disorder (ASD) and attention-deficit/hyperactivity disorder (ADHD) can alter sudomotor profiles. In ASD, studies report elevated daytime tonic conductance, reduced nocturnal EDA amplitude, and weaker coupling between EDA and behavioural states, suggesting atypical sympathetic modulation (Chong et al., 2021; Schiltz et al., 2022). In adults with ADHD, there is evidence of delayed and altered circadian rhythms in body temperature and activity patterns (Bijlenga et al., 2013) and more broadly in neurophysiological responsiveness (Imeraj et al., 2012).

**Underlying medical conditions and medications.** Neurological and endocrine disorders can substantially alter thermoregulatory sweating by disrupting sympathetic cholinergic pathways or shifting central set-points. Autonomic neuropathies, classically in diabetes mellitus, Parkinson's disease, and after spinal-cord injury, damage postganglionic fibers innervating eccrine glands and produce regional hypohidrosis/anhidrosis, diminishing evaporative heat loss under environmental heat stress (Cheshire, 2016; Habek et al., 2022; Low, 2004; Reitz et al., 2002). Endocrine disorders likewise modify heat balance: thyroid excess increases metabolic heat production, while deficiency reduces it; changes that can raise or lower the threshold load required to trigger sweating (Cheshire, 2016; Iwen et al., 2018). Medications also modulate sudomotor activity: anticholinergics directly suppress eccrine secretion via muscarinic blockade; β-blockers and centrally acting agents (e.g., propranolol, clonidine) are used in selected hyperhidrosis or flushing contexts and can alter heat-loss responses -- hence essential careful medication screening in heat-stress studies (Glaser and Glaser, 2015).

**Measurement artefacts.** Measurement artefacts can rival physiological variance in magnitude. In sweat-rate systems, leaks or condensation within tubing alter humidity gradients; in EDA, variations in skin cleaning, electrode pressure, and gel conductivity produce drift and false phasic peaks (Boucsein, 2012). Skin cleaning with alcohol or abrasion can transiently increase local sweating by stimulating mechanoreceptors.

### Data handling methods

#### Sensor calibration

Accurate quantification of sweat and EDA signals requires pre- and post-session calibration to correct for drift and environmental bias.

**Ventilated-capsule systems**. Flow meters should be verified (0.5--1.0 L·min⁻¹) and dew-point sensors checked for linearity across 0--100 % RH. Zero-flow offsets are recorded at the start of each session to remove baseline drift (ISO, 2004). Capacitive or dielectric probes are calibrated against saturated-salt humidity standards to map raw voltage to relative humidity.

**Local sweat rate (LSR)**. Some wearables require a set stabilisation period within an environmental chamber prior to data collection. This period is used to assess an individual \"offset number\", which is later subtracted from the raw score during analysis to yield standardised LSR values (Relf et al., 2019). For colorimetric microfluidic (epifluidic) devices, calibration is integrated into the device hardware through the printing of reference markers (e.g., a white centree dot and four black crosses) (Koh et al., 2016). These markers enable software to perform automatic white balancing and position calibration, eliminating measurement errors caused by varying lighting conditions (daylight vs shadow) or device orientation (Choi et al., 2018; Koh et al., 2016).

**Sweat composition and biochemical analysis**. Calibration of analytical equipment is essential for quantifying sweat electrolytes. Handheld ion-selective electrode (ISE) analysers require frequent calibration (approximately every 10 measurements) to prevent instrument drift (Baker et al., 2014). A 2-point calibration is used for sodium with 150 ppm and 2000 ppm standard solutions, while a 1-point calibration (150 ppm) is used for potassium (Baker et al., 2014). Conductivity-based systems are calibrated using distilled cold water according to manufacturer guidelines before samples are processed (Relf et al., 2019). For patch-based collection, background sodium, chloride, and other electrolyte concentrations are determined from unexposed patches and used as correction factors (Klous et al., 2020). Colorimetric assays for biomarkers like chloride are calibrated by filling devices with known stock solutions (e.g., 25, 50, 75, and 100 mM) to produce a calibration curve or reference colour dial for image-based quantitation (Reeder et al., 2019).

**Electrodermal activity (EDA)**. Calibration for EDA involves electronic standardisation to manage the wide dynamic range of skin conductance. Wheatstone bridge circuits can be used to cancel out (or \"balance\") the large tonic skin conductance level so that small phasic responses can be resolved (Boucsein, 2012). Using adjustable resistors---such as a 10-turn potentiometer where each complete turn cancels out 10 μmhos---the experimenter balances the bridge to achieve an optimal amplifier sensitivity (e.g., 1 mV/cm) (Boucsein, 2012). Modern high-resolution analog-to-digital converters often bypass the need for this separate circuitry, instead using adaptive gain controls or high-pass filtering to compress the dynamic range and manage slow-varying baseline drift (Tronstad et al., 2022).

#### Data cleaning and correction

#### Local Sweat Rate (LSR)

**Filtering for noise.** Data integrity for LSR begins with rigorous skin preparation; sites are cleaned with alcohol and deionised water, then dried thoroughly to remove sebum and residual minerals (Akbar et al., 2023; Baker and Wolfe, 2020; Klous et al., 2020). To \"flush\" the sweat ducts of old sweat and surface contaminants, the first 20--30 minutes of sweat is often wiped away before actual collection begins. To filter out \"reactive error\" and prevent hidromeiosis (suppression of sweating caused by skin wettedness), ventilated capsules are supplied with dry air or nitrogen at flow rates typically between 0.4 and 2.0 L/min (Baker, 2019; Kondo et al., 1998; Lei et al., 2017; Morris et al., 2013; Mündel, 2020). In patch-based collection, noise from solid skin contaminants is filtered via centrifugation or a syringe compression method to isolate pure sweat fluid from the absorbent material (Akbar et al., 2023; Baker, 2019; Klous et al., 2020).

**Normalisation.** LSR is standardly normalised gravimetrically by calculating the mass of the sweat (wet patch minus dry patch mass) divided by the skin surface area and the duration of application, expressed as *mg·cm^-2^·min^-1^* (Klous et al., 2020; Smith and Havenith, 2011). To account for session-to-session variability, regional sweat rates may be standardised against the individual's Gross Sweat Loss (GSL) (Smith and Havenith, 2011). Furthermore, mathematical modelling uses sensitivity coefficients to weight skin areas based on their thermal sensor density (Havenith, 2001; Nadel et al., 1973).

**Discarded data.** In exercise physiology studies, data from the first and last 20 minutes of an exercise bout are often discarded in patch methods because they lack the temporal resolution to track the rapid onset and decay of sweating seen in continuous hygrometry (Morris et al., 2013; Taylor and Machado-Moreira, 2013). Additionally, some protocols discard the first 20--30 minutes of sweating to \"flush\" the sweat ducts of old sweat and contaminants (Akbar et al., 2023). Duplicate measurements showing a major variance are handled by discarding the outlier and retaining the value best representing the area activation (Baker, 2019; Poirier et al., 2016). In sedentary studies, the initial minutes may show an overshoot effect depending on the change in exposure from baseline; therefore, this could be a specific part of the analysis.

**Typical ranges.** Regional variations are significant: under passive heat exposure at rest, the forehead ranges from 0.99 to 1.71 mg·cm^-2^·min^-1^, the upper back from 0.59 to 1.20 mg·cm^-2^·min^-1^, and the limbs approximately 0.12 mg·cm^-2^·min^-1^ (Smith and Havenith, 2012; Taylor and Machado-Moreira, 2013).

#### Skin Wettedness (ω~max~)

**Filtering for noise.** Skin wettedness is a derived mathematical metric representing the proportion of the body surface covered by sweat. The noise is filtered by identifying the critical ambient vapour pressure inflection point from core temperature graphs during a humidity ramp protocol, which isolates the exact transition from compensable to uncompensable heat stress (Baker, 2019; Mündel, 2020; Ravanelli et al., 2018).

**Normalisation.** ω~max~ is expressed as a dimensionless ratio (0.00 to 1.00), where 1.00 represents a skin surface 100% saturated with sweat (Baker, 2019; Ravanelli et al., 2018).

**Discarded data.** Calculations focus on the upper physiological limit of evaporative heat loss; therefore, the mathematical derivation of ω~max~ requires identifying the specific inflection point where the body can no longer maintain thermal balance, rendering data below this threshold as strictly compensable baseline (Mündel, 2020).

**Typical ranges.** While traditional ISO models assume a ω~max~ of 0.85 for unacclimated individuals and 1.00 following successful heat acclimation , recent empirical data show values ranging from 0.72 in untrained/unacclimated individuals, to 0.84 in trained/unacclimated individuals, and up to 0.95 following aerobic training combined with heat acclimation (Candas et al., 1979; Périard et al., 2015).

#### Total Sweat Loss (Whole-Body Sweat Rate - WBSR)

**Normalisation.** WBSR is expressed in litres per hour (L/h) or grams per minute (g/min). It is rigorously normalised through corrections for mass errors, including fluid intake, urine voiding, and metabolic/respiratory mass loss due to gas exchange (Baker, 2019; Mündel, 2020).

**Typical ranges.** Rates typically range from \~0.2 to 0.4 L/h at rest or under mild conditions, up to 3.0 L/h across a wide range of activities, with strenuous endurance exercise in the heat occasionally eliciting maximal sustainable rates approaching 4.0 L/h (Baker and Wolfe, 2020; Kenefick and Cheuvront, 2016).

#### Electrodermal Activity (EDA)

**Filtering for noise.** EDA signals are resampled (e.g., at 8 Hz from 100 Hz) to improve processing efficiency (Hossain et al., 2022). Noise is filtered using low-pass Butterworth filters with cutoff frequencies between 0.6 Hz and 10 Hz to remove high-frequency artefacts (Boucsein, 2012; Hossain et al., 2022). High-pass filtering is applied to remove the slow-shifting tonic baseline (SCL) to isolate phasic responses (Braithwaite et al., 2015; Tronstad et al., 2022) (see 3.2.6.3 Derived parameters).

**Normalisation.** Logarithmic and square root transformations are used to address data skewness and Poisson distributions (Boucsein, 2012). Range correction scales data between an individual's minimum and maximum reactivity (0.0 to 1.0) to facilitate inter-individual comparison. Signals may also be detrended to eliminate slow shifts from thermoregulation (Boucsein, 2012).

**Discarded data.** The first and last 10 minutes of tasks are often discarded to eliminate the effects of physiological acclimatisation and anticipation anxiety (Boucsein, 2012). Any segments containing artefacts from movement, speech, or deep respiration (e.g., sighs) are rejected (Boucsein, 2012; Braithwaite et al., 2015; Tronstad et al., 2022).

**Typical ranges.** Tonic SCL generally falls between 2 and 20 µS (Boucsein et al., 2012). Phasic SCRs are registered using a detection criterion of 0.01 to 0.05 µS (Braithwaite et al., 2015), with frequencies typically ranging from 1 to over 20 SCRs/min, depending on the level of autonomic arousal (Boucsein et al., 2012; Braithwaite et al., 2015).

#### Derived parameters

Depending on study design and research aim, several key parameters are derived from the preprocessed sweat-rate and electrodermal signals. These parameters describe both the magnitude and temporal dynamics of sudomotor activity at local and whole-body levels.

For local and whole-body sweating, the following parameters are calculated:

- [Sweat-onset temperature (°C).]{.underline} The core or skin temperature at which sweat rate first rises above baseline by \> 0.01 mg·cm⁻²·min⁻¹, indicating activation of eccrine glands.

- [Maximum sweat rate (mg·cm⁻²·min⁻¹). The]{.underline} highest value reached during exposure; represents glandular output capacity.

- [Sweating sensitivity (mg·cm⁻²·min⁻¹·°C⁻¹).]{.underline} The slope of the sweat-rate--core-temperature relation after onset; reflects thermoeffector gain.

- [Total sweat output (mg·cm⁻²).]{.underline} The time-integrated area under the sweat-rate curve; quantifies cumulative evaporative loss for a given site or exposure period.

- Whole-body sweat loss (WBSL, kg·h⁻¹ or L·h⁻¹). Calculated as:

$$\text{WBSL} = (\text{Body mass}_{\text{pre}} - \text{Body mass}_{\text{post}}) + \text{Fluid intake} - \text{Urine volume}$$

The result is normalised by body-surface area using the Du Bois & Du Bois equation. Typical ranges are 0.2--0.6 kg·h⁻¹ at rest and \> 1 kg·h⁻¹ during moderate heat stress, depending on acclimation, clothing, and environment (Gagnon et al., 2013b; ISO, 2004).

EDA signals are decomposed into tonic (SCL) and phasic (SCR) components to separate baseline sympathetic tone from discrete bursts of sudomotor nerve activity (Benedek and Kaernbach, 2010a; Boucsein, 2012). Typical palmar conductance levels range 1--20 µS, with transient SCR amplitudes of 0.05--0.5 µS and 0--5 events·min⁻¹ under resting to mild-stress conditions.

- [Skin conductance level (SCL, µS).]{.underline} Mean tonic conductance over a defined period; represents baseline sympathetic drive.

- [ΔSCL (µS).]{.underline} Change in mean SCL between baseline and exposure; expresses magnitude of sympathetic shift.

- [Skin conductance response count (SCR·min⁻¹).]{.underline} Number of phasic responses exceeding a threshold (0.01--0.05 µS); reflects frequency of sudomotor bursts.

- [Mean SCR amplitude (ΔµS).]{.underline} Average height of detected SCRs; indicates intensity of individual sympathetic discharges.

- [Phasic driver / sudomotor-nerve activity (µS·s⁻¹).]{.underline} Output of non-negative deconvolution models (NeuroKit2 (Makowski et al., 2021) or Ledalab (Benedek and Kaernbach, 2010b)); provides a continuous index of sympathetic input.

- [Response latency (s).]{.underline} Interval between stimulus and SCR onset; reflects efferent conduction time and gland responsiveness.

- [EDA reactivity index (%).]{.underline} (ΔSCL / baseline SCL) × 100; normalised measure for inter-subject comparison.

For circadian or long-term recordings, additional descriptors can be extracted from smoothed SCL time series:

- [Amplitude (µS).]{.underline} Difference between daily maximum and minimum; expresses circadian modulation of sympathetic tone.

- [Mean level (µS).]{.underline} 24-h average; reflects overall autonomic balance.

- [Phase timing (h).]{.underline} Clock time of minimum SCL or maximum SCR frequency; aligns EDA rhythm with core-temperature phase (Vittrant et al., 2023).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Measure**                             **Sensor/Principle**                   **Sampling**         **Advantages**                        **Limitations**                         **Approx. Cost (€)\***
  --------------------------------------- -------------------------------------- -------------------- ------------------------------------- --------------------------------------- ------------------------
  **Local sweat rate (LSR)**              Ventilated capsule / dew-point         0.1--1 Hz            Gold-standard, continuous             Bulky setup, calibration required       2000--3000

  **Skin moisture / wettedness**          Capacitance / dielectric probe         1--10 Hz             Compact, non-invasive                 Indirect for rate, pressure sensitive   300--1500

  **Absorbent patch (REG)**               Filter pad gravimetry + ion analysis   Block (10--30 min)   Chemical analysis                     Discrete, no temporal resolution        Consumable + lab

  **Colorimetric / hydrochromic patch**   Color / length-of-fill microfluidic    Visual / photo       Low burden, field deployable          Calibration needed                      5--30 per patch

  **Whole-body sweat loss (WBSL)**        Body-mass scale (pre/post)             Block                Simple, global index                  No spatial or temporal resolution       \< 200

  **EDA\*\* (SCL/SCR)**                   Ag/AgCl electrodes (0.5 V)             4--32 Hz             Sensitive, continuous, non-invasive   Emotion confounds                       500--1500
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 3. Summary of sweat and electrodermal measurement techniques, typical signal characteristics, and practical considerations.\
  Sampling rates denote typical acquisition frequencies used for physiological data logging, not device limits.

\* Costs represent approximate 2024 academic prices for durable equipment; disposables, maintenance and analysis software are not included.\
\*\* EDA = electrodermal activity; SCL = skin conductance level; SCR = skin conductance response.

## Heart rate and heart rate variability

### Why: the mechanistic reasons behind the measurement

Heart rate (HR) is a primary indicator of the cardiovascular workload required to support metabolic demands and heat exchange. In resting humans, HR reflects the balance of sympathetic and parasympathetic outflow to the sinoatrial node, with vagal influences predominating under sedentary conditions (Berntson and Stowell, 1998; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). When the body is exposed to heat, this balance shifts markedly. Cutaneous vasodilation, required to transfer heat from the core to the skin, reduces total peripheral resistance, compelling the cardiovascular system to increase cardiac output to maintain arterial pressure (Crandall and González‐Alonso, 2010; Rowell, 1974). In healthy adults under passive heat stress, this increase in cardiac output is achieved primarily by raising HR rather than through substantial changes in stroke volume (Crandall and Wilson, 2015; Minson et al., 1998; Rowell et al., 1969; Rowell et al., 1967). Classic invasive studies demonstrate an approximately linear relationship between internal temperature and HR, typically showing increases of \~7 beats·min⁻¹ per 1 °C rise in core temperature (Crandall and Wilson, 2015; Jose and Collison, 1970), making HR a direct marker of combined thermal and circulatory strain.

Even in thermoneutral indoor environments, modest shifts in air temperature, mean radiant temperature, posture, or arousal elicit measurable autonomic adjustments that alter HR (Saul, 1990; Julian F. Thayer et al., 2010). Thus, HR functions as a continuous index of the chronotropic effort required to stabilise blood pressure while simultaneously supporting thermoregulation. When paired with core and skin temperatures, HR helps distinguish equivalent thermal states that are reached through different cardiovascular costs across individuals, times of day, or exposure histories.

Heart rate variability (HRV) quantifies the pattern and magnitude of beat-to-beat fluctuations around this mean rate. These fluctuations arise from baroreflex activity, respiratory sinus arrhythmia, vasomotor oscillations, and higher-order central autonomic regulation (Akselrod et al., 1981; Saul, 1990; Shaffer and Ginsberg, 2017). High resting HRV is associated with adaptive autonomic flexibility and strong vagal influence, whereas chronically reduced HRV reflects diminished baroreflex gain, reduced autonomic complexity, and elevated allostatic load (Shaffer et al., 2014; Julian F. Thayer et al., 2010).

HRV analysis is useful in thermal-environment studies because thermoregulation imposes rapid shifts in both sympathetic and parasympathetic outflow. Heat exposure usually induces withdrawal of vagal (parasympathetic) influence, leading to reductions in vagally mediated HRV indices, particularly in the high-frequency (HF) range linked to respiratory sinus arrhythmia: mean HR rises, HF-HRV decreases, and LF and LF/HF frequently increase (Bruce-Low et al., 2006; Crandall et al., 1999b; Niimi et al., 1997; Yamamoto et al., 2007). At the same time, moderate to pronounced heat stress is a strong sympathoexcitatory stimulus, increasing indices such as muscle sympathetic nerve activity (Crandall et al., 1999a; Cui et al., 2010, 2002; Low et al., 2011; Niimi et al., 1997). Together, these shifts alter time-domain and spectral HRV measures and can reveal how much autonomic effort is required to sustain thermal homeostasis.

Some frequency components of HRV have particular relevance for thermoregulation. Very-low-frequency (VLF) oscillations (\~0.003--0.04 Hz) have been linked to slow thermoregulatory and vasomotor processes, including modulation of peripheral arterial tone (Akselrod et al., 1981; Coenen et al., 1977; Myers et al., 2001; Rompelman et al., 1977; Thayer et al., 2012). This band likely reflects a mixture of mechanisms, but changes in VLF power during or after thermal perturbations can be informative about longer-timescale adjustments in vascular and thermal control. The HF band (\~0.15--0.4 Hz) predominantly indexes short-latency vagal modulation and is sensitive to both respiratory pattern and heat-induced vagal withdrawal. The LF band (\~0.04--0.15 Hz) reflects combined baroreflex and autonomic influences; although its interpretation as a direct marker of "sympathetic activity" is debated (Billman, 2013), LF and LF/HF often change systematically with thermal load and can still serve as descriptive markers if interpreted cautiously (Reyes del Paso et al., 2013).

In the context of indoor-environment research, HR and HRV provide complementary views of how the cardiovascular and autonomic systems maintain thermal balance. HR quantifies the overall cardiovascular effort required under a given environmental load; HRV describes the organisation, flexibility, and *cost* of that effort. When combined with core and skin temperatures, blood pressure, and sweating responses, these signals enable researchers to characterise not only the thermal state itself but the physiological work required to achieve and sustain it.

How: sensor types for measurement HR and HRV require a time series in which individual cardiac cycles can be identified with sufficient temporal precision to derive interbeat intervals. In practice, this is achieved via signals that capture either the electrical depolarisation of the heart (electrocardiography, ECG) or the peripheral pulse wave (photoplethysmography, PPG), as well as devices that embed these sensors in wearable formats.

**Laboratory electrocardiography (ECG).** The reference method for HR and HRV is multi- or single-lead ECG, which records cardiac depolarisation directly from the thorax (Task Force of the ESC/NASPE, 1996; Berntson et al., 1997). Short-term HRV is typically derived from 3--12 leads sampled at ≥250--500 Hz to resolve R peaks with millisecond precision and avoid aliasing in the HF band (Pinna et al., 2007; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). For building-scale experiments, a single modified lead II or a 3-lead configuration is usually sufficient, provided that R-waves are clearly distinguishable from noise. Higher sampling (500--1000 Hz) improves timing accuracy for nonlinear indices and ectopic-beat editing (Berntson and Stowell, 1998; Laborde et al., 2017). Research-grade ECG systems provide full waveforms, enabling visual inspection, manual or semi-automated artefact correction, and standardised time- and frequency-domain analysis (Shaffer and Ginsberg, 2017; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). The trade-offs are higher setup burden, the need for skin preparation and electrodes, and potential discomfort during long protocols.

**Holter monitors and ECG garments.** Holter recorders and ECG-integrated garments embed 1--3 leads in adhesive patches or textile electrodes and record continuously at 128--250 Hz over many hours (Catai et al., 2020). These systems are well suited to field or day-long laboratory protocols where HR/HRV must be tracked across changing indoor environments. When electrode contact is stable and R-wave amplitude is adequate, standard HRV indices from Holter recordings closely match those from conventional ECG in resting or light-activity conditions (Heilman and Porges, 2007; Kent et al., 2009; Umetani et al., 1998). Limitations include proprietary filtering pipelines, sometimes restricted access to raw ECG, and greater susceptibility to motion artefacts during free movement.

**Chest-strap heart rate monitors (single-lead ECG).** Chest straps use two or more dry electrodes on an elastic band to record a single-lead ECG from the lower thorax. Validated models show near-identical R--R intervals and HRV indices compared with reference ECG at rest and during low-to-moderate exercise (Giles et al., 2016; Schaffarczyk et al., 2022). Under these conditions, chest straps can serve as practical substitutes for wired ECG in seated or recumbent indoor studies, provided they export true beat-to-beat intervals rather than smoothed HR traces (Laborde et al., 2017; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). Their main limitations are dependence on correct strap tension and positioning, occasional contact loss from sweat or very dry skin, and device-to-device variation in internal preprocessing (Giles et al., 2016; Hinde et al., 2021; Huang et al., 2021; Schaffarczyk et al., 2022).

**Photoplethysmography (PPG).** PPG estimates HR from pulsatile changes in blood volume detected optically at the skin surface, typically at the finger pad or ear lobe (Akselrod et al., 1981; Lu et al., 2009). Pulse-to-pulse intervals derived from these signals yield pulse-rate variability (PRV), which can approximate ECG-HRV at rest in healthy adults: studies report strong correlations and small mean differences for mean HR, SDNN, RMSSD and HF power under warm, well-perfused conditions (Lu et al., 2009). However, PRV is more sensitive than ECG to local vasoconstriction, temperature-induced changes in perfusion, contact pressure, and movement (Kitney and Rompelman, 1980; Park and Park, 2022). Cooling the extremities, changing arm position, or applying pressure to the sensing site can distort pulse morphology or obscure beats, causing spurious variability or data loss (Kitney and Rompelman, 1980; Lu et al., 2009). In thermal-environment studies, these characteristics are particularly important: cooling of the extremities can reduce signal amplitude and distort interval estimates, while heating can change vascular tone and pulse transit time even if HRV at the heart remains unchanged. PRV should therefore be interpreted as a related but distinct signal, and its use for detailed frequency-domain HRV analyses, especially in protocols with large changes in local skin temperature, should be justified and ideally validated against ECG in a subset of participants.

**Wrist- and finger-worn wearables.** Commercial wearables (watches, wristbands, smart rings) use reflectance PPG to estimate HR and, in some cases, HRV. Systematic reviews show that many devices estimate mean HR accurately at rest but display highly variable and often poor agreement for HRV metrics, especially LF, HF and LF/HF (Georgiou et al., 2018; Stone et al., 2021). Finger-worn devices tend to outperform wrist wearables for nocturnal HR and HRV because of stronger pulsatile signals and reduced movement during sleep (Cao et al., 2022; Dial et al., 2025; Stone et al., 2021). Nonetheless, most wearables: (i) do not provide raw interbeat intervals; (ii) use dynamic, sometimes sparse sampling schemes; and (iii) apply proprietary filtering and artefact rejection that are undocumented and can change with firmware updates (Georgiou et al., 2018). As a result, wearable-derived indices are best treated as device-specific proxies of relative autonomic state (e.g. night-to-night changes in vagal tone) rather than as interchangeable replacements for ECG-based HRV in mechanistic thermal-physiology studies.

**[Implications for experimental design.]{.mark}** For mechanistic indoor-environment protocols where HRV is a primary outcome, research-grade ECG or validated chest-strap systems that output raw R--R intervals remain the preferred methods. PPG at finger or ear sites can be appropriate when electrical sensors are impractical, but its thermal sensitivity and site-specific artefacts must be considered in both design and analysis. Wrist and ring wearables can complement laboratory measurements for longer-term or field monitoring, but --unless device-specific validation is available-- HRV metrics derived from them should be used cautiously and primarily for descriptive or exploratory purposes rather than as a basis for quantitative autonomic modelling.

### Where: body sites of measurement

The anatomical site chosen to measure HR and HRV determines the quality of the physiological signal, the stability of beat detection, and the extent to which thermal manipulations influence the underlying waveform. Because HRV depends on millisecond-level precision, the placement of electrodes or optical sensors must minimise motion artefact, preserve waveform morphology, and avoid regions where thermoregulatory vasoconstriction or vasodilation can distort interbeat intervals.

**Thorax.** The anterior thorax is the most reliable site for capturing cardiac electrical activity, with consistently large and sharply defined R waves across individuals. Standard laboratory ECG positions electrodes along modified limb-lead vectors across the chest wall because this configuration maximises R-wave amplitude and minimises electromyographic interference (Berntson and Stowell, 1998; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). Thoracic placements also allow full waveform inspection for artefact detection and ectopic beat correction (Saul, 1990). Importantly for thermal studies, the thorax remains relatively stable in perfusion and skin temperature compared with peripheral sites, making it the preferred location for mechanistic HRV analysis.

**Lower thorax.** Chest-strap ECG sensors position electrodes circumferentially around the lower thorax, below the pectoral muscles. This site provides a stable electrical vector with high R-wave amplitude, yielding R--R intervals that closely match those from wired ECG during rest and mild activity (Giles et al., 2016; Schaffarczyk et al., 2022). The lower thorax is less affected by distal vasomotor changes induced by heating or cooling, making this location robust during indoor thermal exposures. Signal quality, however, depends on consistent strap tension and uninterrupted skin contact.

**Upper arm, flank, and rib cage.** Some adhesive ECG patches and ECG-integrated garments place electrodes along the upper arm, lateral thorax, or lower rib cage. These placements can produce interpretable cardiac vectors for estimating mean HR (Heilman and Porges, 2007), but R-wave amplitudes are typically smaller and more susceptible to movement than anterior chest sites. Thermal fluctuations that alter skin adhesion, such as sweating, localised heating, drafts, also degrade electrode stability. As a result, limb-adjacent electrode placements are generally unsuitable for high-precision HRV, particularly for frequency-domain or nonlinear analyses requiring stable, artefact-free R--R intervals (Catai et al., 2020).

**Fingertip.** Peripheral optical sensing introduces strong dependencies on local perfusion. Fingertip PPG is attractive because of its large pulsatile signal arising from the dense arteriolar network of the distal phalanx (Akselrod et al., 1981; Lu et al., 2009). Under warm, well-perfused conditions, fingertip pulse-wave intervals correlate closely with ECG-derived R--R intervals. However, the fingertip is one of the first sites to undergo thermoregulatory vasoconstriction during cooling, substantially reducing pulse amplitude and distorting beat detection (Kitney and Rompelman, 1980). Even modest thermal asymmetry across the hands, for example from radiant panels or drafts, can produce differences in waveform clarity. Fingertip PPG therefore requires strict control of hand position and local exposure in thermal-environment studies.

**Fingers.** Ring-based PPG sensors, positioned circumferentially at the base of the finger, offer more stable contact pressure and reduced motion relative to fingertip clips. These factors contribute to excellent nocturnal accuracy for both HR and HRV, with time-domain indices often approaching ECG agreement (Cao et al., 2022; Stone et al., 2021). Yet, the ring site remains physiologically peripheral: acral vasoconstriction during cooling, or asymmetrical hand exposure to airflow or radiant sources, can markedly affect beat detectability. Thus, although finger rings outperform wrist devices for HRV, the site is still susceptible to thermal confounding and requires careful monitoring of local conditions.

**Ear lobe.** The ear lobe provides a relatively well-perfused peripheral site with less thermal variability than the hands during mild cooling. PPG at the ear commonly retains adequate pulsatile amplitude even when finger signals deteriorate (Akselrod et al., 1981). Because head movement is limited during seated exposures, ear-lobe PPG experiences fewer motion artefacts than wrist sensors. However, clip pressure can distort the waveform, and local heating or cooling of the head, such as radiant warmers or ventilation jets, may influence perfusion (Park et al., 2022).

**Wrist.** Wrist-mounted PPG sensors sit over the radial and ulnar artery beds, where pulsatile signals are smaller, more variable, and more sensitive to motion than at the finger or ear. Numerous validation studies report accurate mean HR at rest but substantial variability in HRV metrics across wrist devices, driven by a combination of low peripheral perfusion, strap-pressure differences, and device-specific preprocessing (Georgiou et al., 2018; Stone et al., 2021). Wrist perfusion is also strongly influenced by thermoregulatory vasoconstriction, making HRV estimates particularly unreliable during cooling or asymmetric exposure (Lu et al., 2009). Wrist placement is therefore suitable for broad HR monitoring in field studies, but not for precise HRV interpretation in controlled thermal experiments.

### Agreeability across sensor types

Agreement between HR and HRV estimates varies substantially across sensor modalities. Multi-lead ECG is the reference standard for beat detection and all HRV metrics, and most validation studies interpret device performance relative to short artefact-free ECG segments.

Modern chest-strap monitors record a single ECG lead across the lower thorax and can reproduce RR intervals with very high fidelity. In controlled rest and orthostatic conditions, the Polar H10 or V800 shows extremely small bias and narrow limits of agreement, with ICC values above 0.99 for all standard HRV indices (Giles et al., 2016). Similar accuracy has been reported for earlier Polar models such as the S810, S810i, RS800, and RS800CX, provided that identical software is used to derive HRV metrics (Fuller et al., 2020; Gamelin et al., 2006; Hernández-Vicente et al., 2021; Hinde et al., 2021; Huang et al., 2021; Nunan et al., 2009; Schaffarczyk et al., 2022; Wallén et al., 2012). These findings indicate that chest-strap ECG is largely interchangeable with laboratory ECG for HRV at rest, although electrode--skin contact and strap tension remain critical sources of noise.

Peripheral PPG can approximate RR intervals when perfusion is stable. Several comparative studies show that fingertip or ear-lobe PPG produces HRV indices that correlate strongly with ECG under warm, motion-free conditions (Adams et al., 2022; Lu et al., 2009; Rogers et al., 2025). However, the PPG signal is strongly influenced by vasomotor tone: cold exposure, local vasoconstriction, or asymmetric radiant conditions degrade pulse amplitude and introduce jitter in beat-to-beat timing. As a result, mean HR remains accurate, but metrics sensitive to high-frequency variation, such as RMSSD, or HF power may deviate systematically from ECG estimates.

Smartwatch PPG signals, recorded at the wrist, show good accuracy for mean HR at rest but highly variable HRV agreement across devices. Systematic evaluations report wide limits of agreement, with many devices showing large errors in RMSSD, LF, and HF during even mild movement or thermal perturbation (Georgiou et al., 2018). Field validation studies consistently demonstrate that wrist PPG performance deteriorates under movement, mental workload, or low peripheral perfusion (Fuller et al., 2020; Hernando et al., 2018; Nelson and Allen, 2019; Schuurmans et al., 2020; Shumate et al., 2021; Stuyck et al., 2022). Because wrist perfusion is highly responsive to thermoregulatory vasoconstriction, HRV from these devices is not considered reliable in thermal-physiology contexts.

Finger-ring PPG sensors offer more stable contact pressure and stronger pulsatile amplitude than wrist devices. Comparative wearable studies show that ring-based devices outperform wrist PPG for nocturnal HRV and approach chest-strap ECG accuracy for RMSSD and SDNN (Cao et al., 2022; Dial et al., 2025; Fiore et al., 2024; Stone et al., 2021). However, the finger remains a thermally labile site, and perfusion changes during cooling or airflow can still degrade PRV accuracy relative to ECG.

A major source of disagreement across studies is not hardware but software. Several validation papers demonstrate that HRV values differ markedly across software packages, even when the [underlying RR intervals are identical]{.underline}, due to differences in artifact detection, ectopic correction, detrending, windowing, and spectral estimation (Nunan et al., 2009; Radespiel-Tröger et al., 2003; Wallén et al., 2012). HRV metrics are therefore not interchangeable across software ecosystems, and agreement must be assessed using identical analysis pipelines (see more in 3.5.5 Data handling methods).

Across all devices, a practical hierarchy emerges: Best agreement is between multi-lead ECG and chest-strap ECG, followed by fingertip and ear-lobe PPG under thermoneutral, stable conditions. Wrist-based PPG devices show variable to poor agreement, particularly for frequency-domain HRV. For thermal-physiology protocols, where peripheral perfusion can shift rapidly with temperature, radiant asymmetry, or airflow, ECG-based methods remain the preferred option for accurate HRV.

### Known confounders and modifiers

Heart rate and heart-rate variability are influenced by numerous physiological, behavioural, and environmental factors that act on overlapping time scales. Because HRV reflects the dynamic interplay of vagal and sympathetic outflow, and HR indexes net chronotropic demand, any factor that changes autonomic tone, baroreflex engagement, or peripheral perfusion can modulate these signals independently of thermal load. These modifiers must therefore be documented or controlled when HR/HRV are used to interpret thermoregulatory responses.

**Circadian and behavioural influences.** Cardiac autonomic activity shows a robust 24-h rhythm: vagal modulation (HF power, RMSSD) is highest during nocturnal sleep, while daytime wakefulness is characterised by relatively greater sympathetic predominance and reduced overall variability (Akselrod et al., 1981; Bonnemeier et al., 2003; Lipsitz et al., 1990; O'Brien et al., 1986; Otzenberger et al., 1998). Age-stratified population studies demonstrate that both HR and HRV exhibit clear diurnal patterns, with lowest resting HR and highest time-domain HRV parameters during the biological night, and progressive vagal withdrawal across the day (Umetani et al., 1998; Voss et al., 2012). Behavioural state strongly shapes these rhythms. Posture changes, spontaneous activity, cognitive load, and light exposure all shift sympathovagal balance: even low-level mental tasks or screen use can increase HR and reduce HF-HRV compared with quiet rest (Hjortskov et al., 2004; Vandewalle et al., 2007). Sleep restriction, social/occupational stress, and circadian misalignment (e.g. late chronotype in early schedules) reduce night-time vagal dominance and dampen the amplitude of day--night HRV variation (Jarczok et al., 2013; Seeman et al., 2001; Julian F. Thayer et al., 2010). Thermal protocols that compare "morning" and "afternoon" sessions or involve prolonged daytime exposure should therefore consider circadian phase, prior sleep, and behavioural context as important covariates.

**Sex.** Sex differences in HRV are well documented but depend strongly on age and hormonal status. Under resting, sedentary conditions, healthy women and men exhibit distinct heart rate variability (HRV) profiles; notably, women generally present with lower overall heart rate variability, as evidenced by a lower standard deviation of RR intervals (SD). However, the underlying autonomic balance differs between the sexes: women show a relative predominance of parasympathetic (vagal) modulation, while men display greater sympathetic dominance. This dynamic is clearly reflected in frequency-domain HRV measures, population studies show that women typically demonstrate lower low-frequency (LF) power, resulting in a lower LF/HF ratio than men, while absolute high-frequency (HF) power remains similar between the sexes (Sassi et al., 2015; Sinnreich et al., 1998; Sloan et al., 2008; Umetani et al., 1998). These sex-related differences in autonomic HRV balance are heavily influenced by aging and reproductive state, with distinct variations in autonomic modulation observed as women transition through menopause (Huikuri et al., 1996, 1990; Ramesh et al., 2022).

**Sex hormones and reproductive status.** Within women, menstrual-cycle--related variations in ovarian hormones modulate autonomic control. Experimental studies report enhanced vagal indices (HF, RMSSD) and lower LF/HF in oestrogen-dominant phases and greater sympathetic activity in the luteal phase, although effect sizes are small and not always consistent across metrics or protocols (Saeki et al., 1997; Sato et al., 1995; Yildirir et al., 2001). Detailed mapping of endogenous oestradiol, progesterone, FSH and LH across the cycle suggests that peak oestradiol is positively associated with absolute HRV power, supporting a cardioprotective, vagotonic effect of oestrogen (Leicht et al., 2003; Ramesh et al., 2022).

Interventional data reinforce this pattern: oestrogen replacement increases HRV and baroreflex sensitivity, whereas progesterone or combined oestrogen--progestin regimens can blunt vagal indices and shift LF/HF upward (Hirshoren et al., 2002; Liu et al., 2003). Oral contraceptives tend to flatten cyclical variation and modestly elevate resting HR, with subtle reductions in HF-HRV (Minson et al., 2000a, 2000b; Teixeira et al., 2015).

**Age.** Ageing has a pronounced and measure-dependent impact on HR and HRV. Cross-sectional and cohort studies from healthy populations show a progressive decline in SDNN, RMSSD, pNN50, HF and LF power from early adulthood onward, with the steepest reductions occurring between the third and seventh decades of life (O'Brien et al., 1986; Umetani et al., 1998; Voss et al., 2012). These age-related changes reflect declining vagal tone, impaired baroreflex sensitivity, and structural changes in both the sinus node and vasculature (Ingall et al., 1990; Yeh et al., 2022). Notably, older adults can exhibit HRV values that fall within the "high-risk" range for mortality even in the absence of overt disease (Kleiger et al., 1987; Umetani et al., 1998). Thermal studies therefore need to treat age as more than a descriptive characteristic: even in healthy cohorts, older groups will show reduced baseline HRV and potentially smaller autonomic responses to thermal perturbations, confounding comparisons if not accounted for.

**Fitness.** Aerobic fitness is strongly associated with higher resting HRV and lower resting HR. Systematic reviews and training studies consistently demonstrate that moderate-to-vigorous endurance training increases vagally mediated indices (RMSSD, HF) and total power, while lowering resting HR in previously sedentary adults (Aubert et al., 2003; Gregoire et al., 1996; Leicht et al., 2003; Melanson and Freedson, 2001). In older populations, long-term training and competitive endurance participation partly offset the age-related decline in HRV, yielding higher HF and LF power compared with sedentary peers (Aubert et al., 2003; Jensen-Urstad et al., 1997; Yataco et al., 1997).

**Acclimation.** Heat acclimation interacts with fitness by expanding plasma volume, improving cutaneous vasodilatory capacity, and reducing the HR increase required to sustain cardiac output at a given thermal load (González‐Alonso et al., 2008; Rowell, 1974). Acclimated individuals thus display lower HR at a given core temperature and more stable HRV under heat stress compared to unacclimated controls. Without explicit information on training status and recent acclimation (e.g. season, occupational exposure, climate), HR/HRV responses to thermal stimuli are difficult to attribute solely to environmental conditions.

**Body composition**. Body composition modifies autonomic regulation via altered metabolic load, inflammatory signalling, and haemodynamic demands. Increased body mass index and central adiposity are associated with elevated resting HR, reduced HF-HRV, and increased LF/HF ratio in otherwise healthy individuals, suggesting a shift toward sympathetic dominance (Michels et al., 2013; Tegegne et al., 2018; Windham et al., 2012). Obesity often co-occurs with reduced physical activity and subclinical cardiometabolic disease, further depressing HRV and blunting autonomic responsiveness. When comparing HR and HRV during thermal exposures, differences in BMI and fat distribution (e.g. android vs gynoid) should be treated as potential confounders, particularly in small samples.

**Hydration.** Hydration state critically influences cardiovascular control during heat stress. Classic physiological studies show that hypohydration of \~2 % body mass reduces stroke volume, elevates HR, and increases internal temperature thresholds for cutaneous vasodilation (Nadel et al., 1980). This combination increases cardiac strain and requires stronger sympathetic activation, reducing HRV even when environmental conditions are identical.

**Food intake and stimulants.** Food intake and macro-nutrient composition also modulate autonomic outflow. Postprandial thermogenesis and splanchnic vasodilation elevate HR and transiently reduce HF-HRV. Caffeine and nicotine acutely increase sympathetic tone and HR, lowering RMSSD and HF (Julian F. Thayer et al., 2010); alcohol has more complex, biphasic effects but is generally associated with lower short-term HRV in dependence and heavy use (Quintana et al., 2013). For resting thermal protocols, overnight fasting or standardised light meals and restrictions on caffeine, nicotine, and alcohol intake are therefore recommended.

**Psychological load and psychopathology.** Psychological stress is one of the most powerful non-thermal modifiers of HRV. Acute mental stress, anxiety, and negative affect produce rapid vagal withdrawal, increases in HR, and reductions in HF and RMSSD, while often increasing LF/HF. Meta-analyses show robust associations between reduced resting HRV and a range of psychiatric conditions including anxiety disorders, depression, alcohol dependence, bipolar disorder, and schizophrenia (Alvares et al., 2016; Beauchaine and Thayer, 2015; Chalmers et al., 2014; Faurholt-Jepsen et al., 2017; Henry et al., 2010; Holzman and Bridgett, 2017; Kemp et al., 2012, 2010). These effects are amplified by psychotropic medications, particularly tricyclic antidepressants, some SSRIs/SNRIs, and antipsychotics, which further reduce HRV (Alvares et al., 2016). Because low HRV can signal chronic stress or psychopathology rather than thermal strain per se, thermal experiments should at minimum screen for major psychiatric diagnoses, heavy alcohol use, and ongoing psychotropic treatment, or interpret HRV data with these factors explicitly in mind.

**Neurodivergent populations.** Neurodevelopmental conditions such as autism spectrum disorder (ASD) and attention-deficit/hyperactivity disorder (ADHD) are characterised by altered autonomic regulation, including atypical vagal tone, heightened sympathetic reactivity, and disrupted circadian patterns of HR and HRV (Bal et al., 2010; Beauchaine and Thayer, 2015). Individuals with ASD often show reduced HF-HRV at rest and diminished autonomic flexibility during social and cognitive challenges (Thapa et al., 2021; Tonhajzerova et al., 2021), while ADHD is associated with delayed HR/HRV rhythms and greater day-to-day variability. These baseline differences may shape both the magnitude and interpretation of HRV responses under thermal load and warrant documentation in inclusive or neurodivergent samples.

**Underlying medical conditions and medications**. Cardiometabolic and neurological diseases can profoundly depress HRV. Diabetes mellitus with cardiovascular autonomic neuropathy is associated with marked reductions in total power, HF, and time-domain indices, even after adjusting for age and disease duration (Masaoka et al., 1985; Spallone et al., 2011). Hypertension, coronary artery disease, and heart failure similarly reduce HRV and increase arrhythmic risk (Kleiger et al., 1987; Julian F Thayer et al., 2010).

Beyond disease, medications exert large and often directionally specific influences: β-blockers increase HF-HRV and reduce HR; anticholinergics blunt vagal modulation; some antidepressants and antipsychotics decrease HRV; and stimulants used for ADHD substantially elevate HR and LF/HF (Alvares et al., 2016; Julian F. Thayer et al., 2010). In many resting thermal protocols, the HRV effects of disease and medication exceed those of mild environmental heat or cold; careful screening and reporting are therefore essential.

**Respiration.** Because HF-HRV largely reflects respiratory sinus arrhythmia, any factor that alters respiratory frequency or tidal volume will affect HRV estimates (Brown et al., 1993; Hirsch and Bishop, 1981). Speaking, sighing, mask-wearing, slumped posture, and emotional arousal can all change breathing patterns; controlled metronome breathing, while standardising frequency, can itself act as a mild stressor and shift autonomic balance (Catai et al., 2020; Hoit and Lohmeier, 2000; Patwardhan et al., 1995; Vlemincx et al., 2013). Heat stress can modestly increase breathing rate, reducing HF power even without changes in autonomic drive (Rowell et al., 1969). Whenever HRV is used mechanistically, concurrent measurement or at least explicit consideration of respiration is recommended (Laborde et al., 2017).

**Measurement artefacts.** Finally, technical and preprocessing choices can generate "pseudo-variability" comparable in magnitude to physiological changes. Poor R-peak detection, motion artefacts, ectopic beats, missing data, and nonstationarity all distort time- and frequency-domain indices (Berntson and Stowell, 1998; Saul, 1990; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996; Voss et al., 2012). PPG-derived HRV is particularly sensitive to local vasoconstriction during cooling or airflow, which can degrade waveform quality and bias interval estimates (Georgiou et al., 2018; Stone et al., 2021).

### Data handling methods

The interpretability of HR and HRV in thermal-physiology experiments depends critically on rigorous data handling. Even small errors in beat detection or inconsistent preprocessing can obscure the relatively subtle autonomic changes typical of sedentary thermal exposures. Standard workflows therefore include (i) verifying sensor performance, (ii) cleaning RR intervals, and (iii) deriving a consistent set of indices using transparent and reproducible methods. As a well-established field outside thermophysiology, HRV research benefits from several methodological guidelines and reporting checklists (Agelink et al., 2001; Quintana et al., 2016; Shaffer and Ginsberg, 2017).

#### Sensor calibration

PPG-based/optical sensors rely on local perfusion and cannot be "calibrated" against a physical standard; instead, suitability is established via brief local validation against ECG under identical conditions (Gronwald et al., 2024; Lu et al., 2009).

#### Data cleaning and correction

Data cleaning is a vital stage in HRV analysis, as raw signals frequently contain technical noise, motion artifacts, and physiological anomalies (such as ectopic beats or arrhythmias) that can cause significant over- or under-estimation of HRV parameters (Berntson and Stowell, 1998; Catai et al., 2020; Laborde et al., 2017; Peltola, 2012; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996).

**Visual inspection and artefact detection.** Raw ECG or PPG waveforms and the RR tachogram should be inspected for:

- missed beats (single long RR \~2× local mean),

- double detections (two short RR),

- ectopic beats,

- saturated/flat segments (PPG contact loss),

- abrupt transients from movement.

Although automatic filters exist, visual inspection of flagged segments remains necessary in research settings. Following the GRAPH guidelines for transparent HRV reporting (Quintana et al., 2016), all preprocessing steps should be explicitly stated, including:

- the algorithm used for R-peak detection,

- criteria for identifying ectopic or artefactual beats,

- whether manual inspection was performed,

- beat-editing method (e.g., linear or cubic-spline interpolation),

- the percentage of corrected or removed beats per segment and per participant.

These elements are crucial because differences in artefact handling can generate variability comparable to physiological effects in short-term HRV.

**Correction strategies.** Common correction rules include:

- [Missed beat:]{.underline} divide a long RR into two interpolated intervals (Lipponen and Tarvainen, 2019).

- [Double detection:]{.underline} merge short intervals to approximate neighbouring RR.

- [Isolated ectopic beats:]{.underline} remove and replace with spline or linear interpolation (Catai et al., 2020; Peltola, 2012; Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). Simply deleting intervals is highly discouraged (especially for spectral analysis) because it shortens the waveform, introduces step-like discontinuities, and creates false frequency components (Peltola, 2012; Salo et al., 2001).

Methods papers recommend reporting the percentage of corrected beats, and excluding segments where \>3--5% of intervals were corrected (Jarrin et al., 2015; NUNAN et al., 2010; Radespiel-Tröger et al., 2003; Sandercock et al., 2005).

**Segment selection and stationarity.** Short-term HRV is conventionally derived from 5-min stationary segments, particularly for LF and HF spectral indices (Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996). Three-minute windows are sometimes used, especially for RMSSD or HF, but should be reported explicitly. For thermal protocols:

- segment lengths must be identical across conditions,

- transitions or posture changes are avoided,

- segments represent thermally stable phases (e.g., final 5 min of baseline, mid-exposure).

Time--frequency methods for nonstationary data exist (e.g., wavelets, adaptive Kalman smoother--based spectral estimation) (Sassi et al., 2015; Tarvainen et al., 2006), though these are generally unnecessary in stable, seated thermal exposures. Short-term HRV analysis should not be performed during the first minute following posture changes or sensor adjustment, and a period of acclimatization should precede the extraction of analysis windows to ensure signal stationarity (Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996).

**Detrending, resampling, and preprocessing.** Before spectral analysis, non-equidistant RR series are detrended, artefact-corrected, and resampled (typically at 2--4 Hz) using cubic spline interpolation to create an equidistant time series. Simple polynomial detrending may be insufficient; the smoothness-priors detrending method acts as an advanced time-varying high-pass filter that effectively reduces slow drift and improves LF/HF estimates in short windows by removing VLF distortions reduces slow drift and improves LF/HF estimates in short windows (Jarrin et al., 2012; Lipponen and Tarvainen, 2019; Tarvainen et al., 2002).

- Reporting should include:

- detrending method,

- interpolation method and resampling frequency,

- spectral method (FFT vs autoregressive),

- LF/HF normalisation (absolute vs normalised vs log-transformed),

- software and version.

The pipeline dependence of spectral HRV indices is well documented (Jarrin et al., 2012; Kalinkov et al., 2020; Quintana et al., 2016). Explicit reporting of software and parameter settings is essential for reproducibility, because different toolchains and analytical choices can produce systematically different outputs for the exact same raw data.

**Typical ranges.** Normative physiological ranges exhibit massive inter-individual variation and are heavily dependent on factors such as age, sex, and recording duration. In large-scale studies of healthy adults, common time-domain HRV indices show the following typical profiles:

- [SDNN (Standard Deviation of NN intervals)]{.underline} Depending on the specific age cohort, normal physiological limits for 24-hour recordings generally span from roughly 63 to 219 ms (Umetani et al., 1998). Other population samples report mean daytime SDNN values clustering broadly between 50 and 150 ms (Windham et al., 2012).

- [RMSSD.]{.underline} Mean values for resting healthy adults in short-term studies are frequently observed between 35 and 41 ms (NUNAN et al., 2010), while other cohorts report average night-time RMSSD values clustering between 20 and 60 ms (Windham et al., 2012).

#### Derived parameters

From the cleaned NN series, several HR and HRV parameters are derived. Their interpretation in thermoregulation depends on how autonomic outflow adapts to changes in skin blood flow, venous return, baroreflex engagement, and metabolic load.

Time-domain indices:

- [Mean HR / Mean NN]{.underline}**.** Indicates total cardiovascular effort. HR rises in heat (cutaneous vasodilation reduces vascular resistance) and may decrease slightly in mild cooling.

- [SDNN.]{.underline} Reflects total variability, incorporating slow vasomotor and baroreflex rhythms. Often decreases under heat, may increase modestly in non-shivering cold.

- [RMSSD *(primary vagal marker).*]{.underline} Robust index of parasympathetic modulation. Decreases reliably in heat via vagal withdrawal; stable or slightly increased in mild cold. Most reliable HRV feature in wearable validation studies (Giles et al., 2016; Nunan et al., 2009).

- [pNN50.]{.underline} Similar to RMSSD but noisier; less commonly interpreted.

Frequency-domain indices:

- [VLF (0.003--0.04 Hz).]{.underline} Associated with slow thermoregulatory and vasomotor oscillations. Difficult to estimate reliably in 5-min recordings but often suppressed under heat and increased in mild peripheral cooling.

- [LF (0.04--0.15 Hz).]{.underline} Reflects baroreflex-mediated blood-pressure modulation. Often decreases in heat (reduced baroreflex gain), increases in cooling with stronger sympathetic vasoconstrictor oscillations.

- [HF (0.15--0.4 Hz).]{.underline} Respiratory sinus arrhythmia; vagally mediated. Decreases in heat, stable in mild cooling. Strongly dependent on breathing rate → breathing should be recorded or controlled.

- [LF/HF ratio.]{.underline} Sensitive to breathing, baroreflex gain, and total power; not a reliable index of "sympathovagal balance," especially in thermal studies where baroreflex modulation and respiratory patterns change simultaneously (Billman, 2013; Goldstein et al., 2011).

Non-linear indices:

- [SD1, SD2 (Poincaré plot).]{.underline} SD1 tracks vagal modulation (RMSSD-like), SD2 reflects long-term variability including baroreflex activity. Both tend to decrease during passive heat; SD2 may increase slightly in cold.

- [Entropy (ApEn, SampEn).]{.underline} Captures pattern irregularity. Can decrease in heat (reduced autonomic flexibility), remain stable or increase in cold. Sensitive to artefacts and requires carefully selected stationary windows.

- [DFA α1 (fractal scaling).]{.underline} Represents a fractal-like structure of HR dynamics. Sometimes decreases toward randomness (α1 → 0.5) during strong heat load, indicating constrained regulatory adaptability. Intermediate cold exposures sometimes preserve fractal structure.

For building-scale thermal studies, a recommended practical minimal reporting subset includes: mean HR, RMSSD, HF power (with breathing rate), and SD1/SD2 when longer stationary windows are available. Reporting window length, breathing conditions, and % of corrected beats is essential for comparability. GRAPH further recommends reporting absolute (ms²) LF and HF power in addition to any log-transformed or normalised units, as absolute values convey the true magnitude of autonomic fluctuations and facilitate cross-study comparability.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Measure**                               **Sensor**                                                  **Sampling**                                **Advantages**                                                                                                                 **Limitations**                                                                                             **Approx. Cost (€)**
  ----------------------------------------- ----------------------------------------------------------- ------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------- ----------------------
  **HR + HRV (reference method)**           Multi-lead ECG (3--12 leads)                                250--1000 Hz                                Gold standard for HRV; full waveforms; best R-peak precision; robust to peripheral vasomotor changes                           Requires electrodes & prep; reduced comfort for long protocols; higher setup burden                         3000--10,000

  **HR + HRV**                              Single-lead chest-strap ECG (e.g., Polar H10/V800)          130--1000 Hz                                Very high agreement with ECG (ICC \>0.99 at rest); low burden; stable thoracic vector; suitable for long indoor protocols      Dependent on strap tension & moisture; raw IBI export varies by model                                       80--150

  **HR + PRV (ECG-approximation)**          Finger or ear-lobe PPG                                      25--200 Hz                                  Strong pulsatile signal; good agreement with ECG under warm, motion-free conditions; compatible with seated indoor protocols   Highly sensitive to perfusion changes, local cooling, and contact pressure; limited reliability for LF/HF   200--800

  **HR + PRV (limited HRV accuracy)**       Wrist-worn PPG (smartwatches)                               Dynamic (typically 25--100 Hz equivalent)   Convenient, low burden; good continuous HR; useful for field monitoring                                                        Poor LF/HF accuracy; no raw IBIs on many devices; strong dependence on motion and vasoconstriction          150--500

  **HR + PRV \*\* (improved over wrist)**   Finger-ring PPG (smart rings)                               Dynamic (\~20--250 Hz equivalent)           Stable contact, strong pulsatile amplitude; excellent nocturnal HRV; better than wrist devices                                 Still peripheral --susceptible to cooling and airflow; proprietary preprocessing                            250--600

  **HR (limited HRV)**                      Upper-arm / rib-cage ECG patches                            128--256 Hz                                 Wearable over many hours; simple setup                                                                                         Smaller R-waves; motion artefacts; thermal effects on adhesion; limited spectral HRV                        200--500

  **HR only**                               Commercial activity trackers (accelerometer + PPG fusion)   Device-specific                             Very low burden; contextual behaviour data                                                                                     Not suitable for HRV; heavy proprietary filtering                                                           50--300
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 4. Summary of HR and HRV measurement techniques, typical signal characteristics, and practical considerations.\
  Sampling rates denote common acquisition frequencies used for physiological data logging, not device limits.

\* Cost estimates reflect approximate 2024 academic/research purchasing ranges.\
\*\* PRV = pulse-rate variability, derived from PPG. Approximates ECG-HRV only when perfusion and contact are stable.

## Blood pressure

### Why: the mechanistic reasons behind the measurement

Arterial blood pressure (BP) indexes the perfusion pressure delivered to organs and the load against which the heart pumps; in shorthand, it reflects the interaction of cardiac output with total peripheral resistance and arterial compliance. Under warm indoor exposures, cutaneous vasodilation redistributes blood to the skin, lowers peripheral resistance, and requires compensatory adjustments in cardiac output to maintain BP; documenting BP therefore links thermal vasomotion to central hemodynamics in sedentary protocols (Crandall, 2008).

Short-latency baroreflex and autonomic responses stabilise BP on the order of seconds to minutes, while vascular/renal mechanisms govern longer horizons; even small BP shifts (e.g., diastolic or MAP) during passive heating or cooling provide a hemodynamic context for concurrent changes in skin blood flow, skin temperature, and heart-rate--derived metrics (Mukkamala et al., 2022).

Because thermal manipulations in seated participants alter vascular tone without large metabolic changes, BP serves as the concise readout of whether perfusion pressure is preserved as skin blood flow increases, and whether autonomic buffering remains intact across time-of-day or exposure blocks (Rowell, 1974).

### How: sensor types for measurement 

**Upper-arm cuff (oscillometric or auscultatory).** Automated oscillometric cuffs are the default for intermittent BP at rest in laboratory and field studies; the device infers systolic/diastolic values from the cuff-pressure oscillation envelope during deflation, while auscultatory methods detect Korotkoff sounds. Validation statements and technique details are consolidated by the American Heart Association (Muntner et al., 2019); modelling/limits of oscillometry are reviewed with open-access summaries (Chandrasekhar et al., 2019). Under sedentary, thermally perturbed conditions, accuracy can vary with arterial compliance and waveform shape; worth noting when vasodilation is substantial (Alpert et al., 2014).

**Ambulatory/automated repeated cuffs.** For longer indoor protocols, ambulatory or scheduled automated measurements extend intermittent monitoring without continuous inflation, retaining the oscillometric principle and standard validation constraints (Muntner et al., 2019).

**Non-invasive continuous methods (beat-to-beat).** A range of systems provide continuous or near--beat-to-beat BP estimation without arterial cannulation, typically by tracking arterial volume or wall motion at a peripheral site and then reconstructing arterial pressure from the waveform plus calibration (Meidert and Saugel, 2018).

- [Volume-clamp (vascular unloading) finger cuff,]{.underline} A pneumatic cuff around the finger adjusts pressure to maintain constant arterial volume; the servo-controlled cuff pressure approximates the intra-arterial waveform. This "Penáz method" underlies several commercial systems and has been evaluated against invasive reference measurements in perioperative and intensive-care cohorts (Fortin et al., 2021; Saugel et al., 2020; Wagner et al., 2015).

- [Applanation/arterial tonometry.]{.underline} A flat sensor positioned over a superficial artery (typically radial) partially flattens the vessel and records the pressure waveform, which is then calibrated to brachial cuff values. Technical descriptions and comparative performance data are summarised in reviews of non-invasive arterial pressure monitoring (Athaya and Choi, 2022; Meidert and Saugel, 2018); see also Salvi et al. for radial tonometry and central pressure estimation (Salvi et al., 2015).

- [Cuffless timing methods (PTT/PAT)]{.underline}. Pulse transit time (PTT) and pulse arrival time (PAT) approaches estimate BP changes from the delay between a proximal signal (e.g., ECG or phonocardiogram) and a distal photoplethysmogram (PPG) or similar waveform. Reviews highlight their promise and the need for individual calibration and careful validation (Ding and Zhang, 2019; Mukkamala et al., 2022). A recent example is the cuffless real-time device by Choi et al., which uses ECG electrodes and a microphone at the wrist to derive PTT and estimate BP (Choi et al., 2023).

- [Wearable cuffless devices (wrist/arm/ring).]{.underline} Newer devices embed optical, electrical or mechanical sensors into wristbands, upper-arm bands or rings, and estimate BP using pulse-wave features and machine-learning models. Systematic and narrative reviews summarise available devices, sensing principles and validation status (Islam et al., 2022; Kumar et al., 2024; Zhao et al., 2023). These systems are still typically calibrated to brachial cuff measurements and their performance under different thermal and perfusion states remains an active research area.

**Invasive arterial line.** Direct intra-arterial monitoring via an arterial catheter connected to a fluid-filled transducer remains the reference standard for waveform fidelity and absolute pressure measurement, particularly in critically ill or high-risk surgical patients (Athaya and Choi, 2022; Meidert and Saugel, 2018; Romagnoli et al., 2014). It is, however, restricted to clinical or highly controlled physiological settings and is not typical for sedentary built-environment experiments, where the non-invasive alternatives above are preferred.

### Where: body sites of measurement

Blood pressure in sedentary thermophysiology studies is most commonly measured at the upper arm, wrist, finger, or much less frequently the radial or a central artery. The choice of site determines which arterial segment is sampled (brachial vs radial vs digital), the hydrostatic relation to the heart, and how strongly local vasomotor changes (e.g., thermal vasodilation in the hand) influence the signal (Muntner et al., 2019).

**Upper-arm (brachial) measurements.** The standard location for non-invasive sphygmomanometry is the upper arm with the cuff encircling the brachial artery at heart level in the seated position (Muntner et al., 2019). This site is preferred because the brachial artery is relatively large, easily occluded, and lies at a similar hydrostatic level to the aorta when the arm is supported; brachial pressures are also the reference against which alternative sites (wrist, finger, tonometry) are usually validated (Pickering T et al., 2005). In indoor sedentary experiments, cuffs are typically placed on the non-dominant upper arm to minimise movement and interference with tasks.

**Wrist (radial/ulnar) cuff devices.** Oscillometric wrist monitors place the cuff over the radial and ulnar arteries proximal to the carpus. They are used when upper-arm placement is impractical (e.g., very large arm circumference or arm instrumentation), but wrist readings are more sensitive to arm and wrist position relative to the heart and to local vasomotor tone (Casiglia et al., 2016; Palatini, 2025). Comparative work and clinical guidance generally regard upper-arm (brachial) measurement as the reference and treat wrist devices as secondary options that require careful positioning and validation (Melville et al., 2018).

**Finger (digital) measurements.** Finger cuffs used in volume-clamp systems enclose the middle phalanx and maintain constant arterial volume via a servo-controlled pressure adjustment; the cuff pressure then approximates the finger arterial pressure waveform. This site enables beat-to-beat recording and is widely used for continuous BP and derived hemodynamic variables in research (Fortin et al., 2021; Żyliński and Cybulski, 2022). Meta-analyses comparing finger-cuff arterial pressure with invasive reference show acceptable mean bias but wide limits of agreement, with accuracy reduced when peripheral vasoconstriction, low perfusion or rapid hemodynamic changes are present (Andriessen et al., 2008; Saugel et al., 2020). In thermal studies, the finger site is therefore attractive for continuous monitoring but more vulnerable to local temperature and vasomotor changes than the brachial site.

**Radial artery (wrist/forearm) applanation tonometry.** Applanation tonometry at the radial artery records the local pulse waveform by gently flattening (applanating) the artery against underlying bone with a flat sensor. The waveform is subsequently calibrated to brachial cuff systolic and diastolic pressures to estimate peripheral and, via transfer functions, central pressures (Salvi et al., 2015; Sharman et al., 2017).

**Central and invasive sites (reference).** Invasive catheters placed in central arteries (e.g., radial, femoral, or directly the aorta) provide reference waveforms and absolute pressures for validation studies but are almost never used in sedentary built-environment experiments. They mainly appear in perioperative or intensive-care research, where they serve as the comparison standard for finger-cuff, radial-tonometry or cuffless methods (Meidert and Saugel, 2018; Romagnoli et al., 2014).

### Agreeability across sensor types

Brachial upper-arm oscillometric devices are generally treated as the non-invasive reference in adults at rest (Muntner et al., 2019). Method-comparison studies and meta-analyses report small mean differences versus invasive arterial pressure for mean arterial pressure, alongside wide individual limits of agreement (Nedel et al., 2022; Schutte et al., 2022). These devices are therefore suitable for group-level analyses and trend tracking, but not strictly interchangeable with intra-arterial measurements at the individual level (Nedel et al., 2022).

Within non-invasive techniques, correctly sized upper-arm cuffs typically perform better than wrist cuffs (Casiglia et al., 2016; Irving et al., 2016). Wrist devices show larger bias and scatter and require careful positioning at heart level and, ideally, device-specific validation against brachial measurements (Melville et al., 2018).

Finger volume-clamp systems provide beat-to-beat waveforms and track brachial or intra-arterial pressures reasonably at rest (Fortin et al., 2021). However, individual limits of agreement on the order of \~10--20 mmHg and sensitivity to local vasoconstriction or low perfusion are commonly reported (Saugel et al., 2020).

For cuffless wearable systems, current evidence indicates modest mean bias versus cuff-based reference in seated or ambulatory users (Islam et al., 2022). Between-device and between-study heterogeneity is high, and limits of agreement often exceed usual interchangeability criteria (Mukkamala et al., 2022; Proença et al., 2023). When reporting BP outcomes, it is therefore useful to specify device type, body site, calibration procedure and posture, and to treat different sensor types as related but non-equivalent measures unless equivalence has been demonstrated for the protocol in question.

### Known confounders and modifiers

Blood pressure is sensitive to intrinsic regulatory rhythms and to experimental conditions that affect vascular tone, volume status, or measurement technique.

**Circadian influences.** Blood pressure exhibits a pronounced 24-h rhythm, with daytime values typically 10--20 % higher than nighttime pressures ("dipping") and a characteristic morning surge after waking (Bankir et al., 2008; Filippone et al., 2023; Hermida et al., 2007). Abnormal dipping patterns (non-dipping, reverse dipping) are associated with increased cardiovascular risk, even when mean 24-h BP is similar (Cuspidi et al., 2017; Pierdomenico et al., 2016). Irregular sleep--wake schedules, naps, and shift work can blunt or distort these profiles (Hinderliter et al., 2013; Kakaletsis et al., 2023). Behaviour immediately before measurement (recent walking, posture changes, talking, screen use, cognitive tasks) adds short-term fluctuations on top of the circadian pattern; aligning recording windows to habitual sleep--wake timing and standardising pre-measurement behaviour reduces this variance.

**Sex.** Across adulthood, women generally show lower BP than age-matched men until midlife, with convergence or reversal around menopause, reflecting sex-specific trajectories in vascular stiffness, autonomic balance, and the renin--angiotensin--aldosterone system (Tasić et al., 2022).

**Sex hormones and reproductive status.** Oestrogen tends to promote vasodilation and lower BP via endothelial nitric oxide and neurohumoral modulation, whereas progestins and androgens can favour higher vascular tone (Drury et al., 2024). Combined oral contraceptive use is associated with modest but significant elevations in BP and a higher risk of developing hypertension in meta-analyses and large cohort studies (Cameron et al., 2023; de Souza et al., 2024). Around menopause, declining oestrogen and increasing arterial stiffness contribute to steeper age-related rises in systolic and pulse pressure in women than in men (Drury et al., 2024). Accurate documentation of sex, menstrual or menopausal status, and hormonal contraception type and duration is therefore essential for cross-participant comparisons.

**Age.** Ageing increases large-artery stiffness, widens pulse pressure, and attenuates baroreflex sensitivity, leading to higher systolic and pulse pressures and less efficient buffering of acute BP changes (Kim, 2023; Laurent and Boutouyrie, 2020). Older adults exhibit greater seasonal and thermal influences on BP and are more prone to orthostatic instability compared with young adults (Monahan, 2007). Age group and vascular risk profile thus shape both baseline levels and responses to thermal or postural perturbations.

**Fitness and acclimation.** Regular aerobic training modestly lowers resting BP and reduces BP reactivity to physical and mental stressors, partly through improved endothelial function and autonomic regulation (Mariano et al., 2023). Higher cardiorespiratory fitness is associated with more favourable heart-rate variability and baroreflex indices, indicating greater buffering capacity against acute challenges. Although specific data on heat-acclimation and resting BP in sedentary indoor conditions are limited, training status and recent exercise can shift absolute pressures and should be recorded when comparing groups.

**Body composition.** Higher BMI, central adiposity and visceral fat are consistently associated with higher BP and increased hypertension risk across age groups (Chandra et al., 2014; Leite et al., 2021). Network meta-analyses show a graded increase in hypertension incidence with higher or rising adiposity trajectories (Tan et al., 2023). Differences in fat distribution (e.g., android vs gynoid) further modulate BP, so anthropometry and, where possible, direct body-composition measures improve interpretability of between-participant differences.

**Nutrition and hydration.** Hydration status influences BP by altering plasma volume and autonomic--hormonal responses. Experimental work shows that hypohydration can modify baroreflex control, vascular resistance and BP variability, sometimes lowering resting BP but increasing susceptibility to orthostatic or heat-induced instability (Watso and Farquhar, 2019).\
Caffeine induces a small but significant transient rise in systolic and diastolic BP (\~2--4 mmHg) over several hours, particularly in non-habitual consumers and in individuals with hypertension (Abbas-Hashemi et al., 2023; Mesas et al., 2011; Xu et al., 2021). Energy drinks combining caffeine with other stimulants elicit somewhat larger short-term BP increases (Benjo et al., 2019; Gualberto et al., 2024) Meal timing and composition (e.g., large carbohydrate loads) can also induce postprandial hypotension or variability, especially in older or autonomically impaired individuals. Standardising or documenting recent fluid intake, meals, and stimulant use is therefore important.

**Neurophysiological and psychological factors.** Acute psychological stress, time pressure and emotional arousal typically raise BP via sympathetic activation and vasoconstriction. Laboratory studies show substantial inter-individual differences in BP reactivity to mental-stress tasks, and exaggerated reactivity predicts incident hypertension and cardiovascular events (Ginty et al., 2022; Matthews et al., 2004). Everyday cognitive load (e.g., demanding tasks during measurement) and affective state can therefore modulate BP independently of the thermal environment.

**Neurodivergent populations.** Neurodevelopmental conditions such as autism spectrum disorder (ASD) and ADHD are associated with atypical cardiovascular autonomic regulation. In ASD, autonomic-clinic cohorts report intermittent neuro-cardiovascular dysfunction affecting both heart rate and blood pressure, including postural tachycardia, vasovagal syncope and orthostatic hypotension, indicating impaired sympathetic vasoconstriction and baroreflex control (Owens et al., 2021; Tonhajzerova et al., 2021). In ADHD, ambulatory blood-pressure monitoring studies and stimulant-treatment trials show small but consistent increases in daytime systolic BP and heart rate, and a higher prevalence of elevated BP or hypertension compared with peers (Buitelaar et al., 2022; Grisaru et al., 2013). While detailed circadian BP profiles in neurodivergent adults remain limited, these findings suggest that both baseline BP and its responses to posture, stress or medication may diverge from neurotypical patterns and should be explicitly reported.

**Underlying medical conditions.** Chronic kidney disease, diabetes, obstructive sleep apnoea and established hypertension all alter BP regulation, often disrupting normal dipping patterns and increasing BP variability (Luo et al., 2023; Pierdomenico et al., 2016) . Autonomic neuropathies and neurodegenerative disorders can produce orthostatic hypotension or labile BP through impaired baroreflex and sympathetic control (Kim, 2023). Recording major cardiovascular and autonomic diagnoses, and keeping medication regimens stable where possible, is important for interpretation.

**Measurement artefacts.** Procedural factors and device characteristics can introduce variability comparable to physiological effects. Common issues include incorrect cuff size, cuff placement over clothing, arm not supported at heart level, talking during measurement, insufficient seated rest, and recent activity (Muntner et al., 2019). Device-specific calibration, repeated readings after a standardised rest period, and consistent posture and arm support are essential to reduce artefactual variance. Reporting device type, measurement protocol and quality-control steps alongside BP outcomes improves reproducibility and cross-study comparison.

### Data handling methods

#### Sensor calibration

Modern aneroid and oscillometric sphygmomanometers are calibrated against reference manometers. When correctly calibrated and maintained, an accuracy within ±3 mmHg is expected, with digital devices often calibrated against a reference manometer having a strict accuracy of ±0.1 mmHg (Kumar et al., 2021). At the device/clinical level, the AAMI/ESH/ISO Universal Standard (ISO 81060-2 (ISO, 2019)) specifies accuracy criteria and validation procedures for non-invasive intermittent BP devices, forming the basis for most commercial upper-arm and wrist monitors and their periodic verification against reference methods (Stergiou et al., 2018). Continuous finger volume-clamp systems and radial applanation tonometry require calibration to brachial SBP/DBP at baseline, along with hydrostatic (height) correction between the heart and measurement site, as differences in arm position significantly alter pressures (Fortin et al., 2021; Salvi et al., 2015; Saugel et al., 2020). Cuffless and wearable devices generally depend on one or more reference measurements with a validated brachial cuff to initialize the mapping between pulse-wave features (such as pulse transit time) and absolute BP (Mukkamala et al., 2022). Because of continuous physiological changes and vascular aging, this calibration must be repeated at defined intervals for the device to accurately track BP over time (Henry et al., 2024; Hu et al., 2023; Schutte et al., 2022).

#### Data cleaning and correction

For intermittent brachial measurements, BP is typically recorded as three consecutive readings, spaced 1 to 2 minutes apart, following at least 5 minutes of seated rest (Stergiou et al., 2021). The arm must be supported at heart level, and both the patient and observer must refrain from talking. Because the first reading is often the highest, the patient\'s BP is usually recorded as the average of the last two readings; additional measurements are recommended if the first two readings differ by more than 10 mmH (Williams et al., 2019). Readings taken with incorrect cuff size, over clothing, during posture changes, or within 30 min of caffeine or smoking should be excluded or repeated under standardised conditions (Pickering et al., 2005).

**Filtering for noise.** Because raw blood pressure and biosignals like photoplethysmograms are highly susceptible to baseline wandering, motion artefacts, and external high-frequency interference, rigorous filtering is essential. Butterworth filters are extensively used; for instance, applying a low-pass Butterworth filter (e.g., 0.5 to 30 Hz, or specifically a 10 Hz cutoff) effectively removes high-frequency noise and movement artefacts (Boschi et al., 2023; Maqsood et al., 2025). Other common filters include bandpass Equiripple FIR filters (e.g., 0.5--8 Hz) for PPG signals and Savitzky--Golay filters for arterial blood pressure (ABP) signals (Athaya and Choi, 2022). To eliminate baseline offsets, nonlinear Median filters (MF) are frequently applied, with more complex noise, advanced signal processing techniques such as Wavelet Transforms (WT) (using basis functions like Daubechies or sym8), Hilbert-Huang Transforms (HHT), and Independent Component Analysis (ICA) are utilized (Deng et al., 2020). Additionally, adaptive filters (like Least Mean Squares \[LMS\] or Normalized Least Mean Squares \[NLMS\]) can dynamically subtract motion artifacts by using an accelerometer\'s signal norm as a reference (Boschi et al., 2023; Choi et al., 2008).

**Normalisation.** Normalisation is a crucial processing step that eliminates scale and range differences across biosignals, enabling accurate algorithm training and robust monitoring (Mukkamala et al., 2022). In optical measurements like PPG, data-driven feature extraction is performed only after normalising the pulsatile alternating current (AC) component relative to the non-pulsatile direct current (DC) component; this specific normalisation mitigates the effects of ambient lighting, temperature variations, and skin pigmentation (Mukkamala et al., 2022). In machine learning, input and output signal segments are routinely scaled using mathematical normalisations, most commonly Z-score, mean, and Min-Max normalisations (Maqsood et al., 2025).

**Discarded data.** To maintain the integrity of BP measurements and algorithm training datasets, data containing severe artefacts, protocol violations, or physiological impossibilities must be systematically discarded. In digital signal processing, segments with unacceptably fast heartbeats, long discontinuities, or missing values are removed. Algorithms often use double derivation thresholding (e.g., excluding segments with high standard derivations beyond a cutoff) or deploy specific Convolutional Neural Networks (CNNs) to automatically flag and discard erroneous PPG and ABP signals. Furthermore, \"peak cleaning\" mechanisms use acceleration norms to identify and discard specific time windows heavily corrupted by motion artefacts (Athaya and Choi, 2022). In clinical validation and practice, readings are excluded if independent human observers disagree on a systolic or diastolic measurement by more than 4 mmHg (ISO, 2019), or if the required Korotkoff sounds (K1 or K5) cannot be clearly heard (Stergiou et al., 2018).

**Typical ranges.** Typical blood pressure ranges serve dual purposes: diagnosing patient health in clinical settings and establishing strict algorithmic thresholds for data cleaning. Clinically, a healthy individual\'s normal BP is widely defined as having a systolic BP (SBP) \< 120 mmHg and a diastolic BP (DBP) \< 80 mmHg (Baik et al., 2023; Muntner et al., 2019; Williams et al., 2019). Hypertension thresholds vary slightly by clinical guidelines but are generally defined as 130/80 mmHg (ACC/AHA guidelines (Muntner et al., 2019)) or 140/90 mmHg (ESC/ESH guidelines (Montalescot et al., 2013)) for office readings. For signal processing and deep learning applications, algorithms define erroneous or \"irregular\" signals based on extreme physiological limits. Datasets frequently flag and discard reading segments if the DBP falls below 50--60 mmHg or exceeds 130 mmHg, and if the SBP falls below 80 mmHg or exceeds 180--200 mmHg (Rishi Vardhan et al., 2021).

#### Derived parameters

Depending on study design and research aim, several key parameters are derived from the preprocessed BP signal. These metrics describe both the magnitude and temporal dynamics of cardiovascular responses.

- [Baseline BP (mmHg).]{.underline} Mean SBP, DBP and/or MAP over the final 3--10 min of the pre-exposure or neutral period; used as a reference for subsequent changes (Stergiou et al., 2021)[.]{.underline} When devices do not provide MAP directly, it is usually estimated as:

  MAP = DBP + ⅓(SBP − DBP)

  Alternative weightings such as DBP + 0.4(SBP − DBP) or DBP + 0.412(SBP − DBP) have been proposed to better approximate time-averaged pressure and show slightly stronger associations with target-organ indices; comparisons of seven different formulas report systematic between-formula differences of a few mmHg (Papaioannou et al., 2016). Studies comparing measured oscillometric MAP with values recalculated from SBP and DBP similarly conclude that measured and calculated MAP cannot be used interchangeably in individual subjects (Kiers et al., 2008). Using a single, explicitly stated formula within a study avoids internal inconsistencies.

- [ΔBP (change, mmHg).]{.underline} Difference between end- and start-exposure means, or between condition means, indicating the magnitude of pressor or depressor responses to thermal, postural, or behavioural manipulations.

- [Rate of change (mmHg·min⁻¹).]{.underline} Slope of a linear regression fitted to SBP, DBP or MAP over a specified interval (e.g., first 20--30 min of exposure), describing the speed of adjustment or recovery.

- [Short-term variability (SD, CV).]{.underline} For continuous recordings, variability within a segment (e.g., 5--30 min) is summarised as the standard deviation (SD) or coefficient of variation (CV = SD/mean × 100 %) of SBP, DBP or MAP (Parati et al., 2018).

- [Average real variability (ARV).]{.underline} Mean absolute difference between consecutive values over a given period; ARV is less influenced by extreme values than SD and is increasingly used in BP-variability research (Parati et al., 2018).

For extended or ambulatory recordings, additional descriptors are often used:

- [Daytime and nighttime means (mmHg).]{.underline} Mean BP during predefined wake and sleep windows, typically based on diaries or fixed clock-time bands.

- Dipping percentage (%). Calculated as:

- $100\  \times \ (daytime\ mean\  - \ nighttime\ mean)\ /\ daytime\ mean$

  used to classify individuals as "dippers", "non-dippers", "extreme dippers", or "risers" based on established cut-offs (Cuspidi et al., 2017; Pierdomenico et al., 2016).

- [BP load / area-under-curve (AUC).]{.underline} Proportion of readings above guideline thresholds (e.g., ≥135/85 mmHg daytime) or time integral of BP above baseline or clinical cut-offs; these indices capture cumulative exposure to elevated pressure beyond simple means.

Across repeated sessions or time blocks, visit- or period-level variability can be summarised as the SD or ARV of mean BP values, reflecting intra-individual lability over hours to weeks and showing independent associations with cardiovascular risk (Schutte et al., 2022; Vidal-Petiot et al., 2017).

Table 5. Summary of blood-pressure measurement techniques, typical signal characteristics, and practical considerations\
Sampling rates denote typical acquisition frequencies used for physiological data logging, not device limits.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Measure**                                 **Sensor / Principle**                            **Sampling rate**               **Advantages**                               **Limitations**                                                                     **Approx. cost (€)\***
  ------------------------------------------- ------------------------------------------------- ------------------------------- -------------------------------------------- ----------------------------------------------------------------------------------- ------------------------
  **Brachial BP**                             Upper-arm oscillometric cuff                      Block (2--3 readings / point)   Standard method; widely validated; simple    Intermittent; sensitive to cuff size, posture, talking, recent intake               100--1000

  **Ambulatory BP**                           Automated upper-arm oscillometric (24 h)          Block (15--60 min intervals)    Day--night pattern; real-world environment   No beat-to-beat detail; cuff inflation may disturb sleep                            150--2000

  **Wrist BP**                                Wrist oscillometric cuff (radial/ulnar)           Block                           Compact; option when arm cuffs impractical   Requires strict heart-level positioning; generally less accurate than arm           100--800

  **Continuous finger BP**                    Volume-clamp finger cuff                          100--250 Hz (beat-to-beat)      Beat-to-beat waveform; hemodynamic indices   Needs calibration to brachial BP; sensitive to vasoconstriction, hand temperature   5,000--25,000

  **Radial waveform / derived BP**            Applanation tonometry at radial artery            128--1000 Hz                    Central BP estimation; waveform morphology   Operator dependent; calibration and probe placement critical                        5,000--20,000

  **Cuffless wearable BP (wrist/arm/ring)**   Optical / impedance / pressure sensors + PTT/ML   1--10 Hz                        Low burden; potential long-term monitoring   Requires calibration; device- and state-dependent accuracy; evolving validation     200--1500

  **Invasive arterial BP \*\***               Fluid-filled or solid-state arterial catheter     100--250 Hz                     Gold-standard reference; high fidelity       Invasive; clinical use only; not used in typical sedentary experiments              Per-use clinical
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\* Costs represent approximate 2024 academic prices for durable equipment; disposables, maintenance and analysis software are not included.\
\*\* Included as reference method; rarely used outside clinical or highly controlled physiological studies.

## Other physiological indicators

A number of additional physiological measures are occasionally incorporated into built-environment studies to address specific questions or to connect protocols with neighbouring literatures. They are less commonly used than core temperature, skin temperature, cardiovascular indices, sweating and electrodermal activity, and their analytical standards largely come from fields such as neuroscience, vascular physiology, endocrinology, and exercise science. This section briefly summarises why these signals are measured, how they are typically acquired, and where on the body they are recorded.

### Electroencephalography (EEG)

**Why.** EEG can be used to index dynamics related to arousal, sleep--wake state, and cognitive or mental workload. In thermophysiological research, nocturnal EEG is used to quantify sleep architecture and continuity under different thermal or environmental conditions, while daytime EEG is increasingly used to assess how indoor temperature, ventilation, noise or lighting influences attention, fatigue, and task performance. Changes in band-limited power (e.g. theta, alpha, beta) and event-related potentials are sensitive to cognitive load and vigilance, making EEG a useful complement to heart rate, EDA, and behavioural performance measures when cognitive state is of interest (Chikhi et al., 2022; Wascher et al., 2023).

**How.** EEG measures voltage differences at the scalp using multiple electrodes referenced to a common or linked reference. Conventional laboratory systems use gel-based caps with 32--64 or more channels, high input-impedance amplifiers, and wired acquisition. Recent mobile systems employ 5--14 dry or semi-dry electrodes integrated into headsets or headbands, with wireless transmission and embedded amplifiers. These devices trade spatial resolution and artefact robustness for reduced setup time and higher acceptability in field-like environments (Ladouce et al., 2024; Swerdloff and Hargrove, 2023).

**Where.** Electrode placement follows reduced versions of the international 10--20 system. Full-cap setups cover frontal, central, temporal, parietal, and occipital regions; portable environmental setups often concentrate on frontal and central leads, which are informative for vigilance and workload and easier to accommodate with everyday headwear (Chikhi et al., 2022). Some commercial systems embed electrodes into headphone bands or in-ear devices, further lowering intrusiveness at the cost of more constrained spatial sampling.

### Skin blood flow (SBF)

**Why.** Skin blood flow provides a more direct measure of cutaneous vasomotor responses than skin temperature alone. It reflects the balance between sympathetic vasoconstrictor and active vasodilator outflow and is central to controlling dry heat exchange at the body surface (Charkoudian, 2003). SBF measurements are used to characterise reflex thermoregulatory responses to whole-body heating and cooling, local thermal control mechanisms, and age- or disease-related changes in microvascular function that may modify thermal tolerance (Johnson and Kellogg, 2010; Low et al., 2020).

**How.** SBF is commonly assessed using laser Doppler flowmetry, which estimates red blood cell flux in superficial capillary beds, or by optical photoplethysmography, which infers perfusion from pulsatile changes in light absorption. These techniques provide continuous time series in arbitrary perfusion units rather than absolute flow. For mechanistic studies, local heating or cooling protocols can be applied to the measurement site to probe reflex and local control mechanisms (Johnson and Kellogg, 2010).

**Where.** Probes are taped or strapped to the skin over regions of interest, typically the ventral forearm, dorsal hand, fingertip, calf, or foot. Sites are chosen to match the research question: for example, distal extremities to study arteriovenous anastomoses, or forearm and calf to examine non-glabrous skin responses (Charkoudian, 2003). Probes are usually shielded from direct drafts and radiative sources to minimise local environmental artefacts. In built-environment studies, SBF remains more common in small mechanistic protocols than in larger field deployments because of its sensitivity to motion and the need for site-specific preparation.

### Endocrine and biochemical markers

**Why.** Hormonal and biochemical markers provide an integrative view of stress, circadian phase, inflammation, and metabolic status that can modulate or contextualise thermophysiological responses. Cortisol profiles are used to index hypothalamic--pituitary--adrenal (HPA) axis activity and its circadian rhythm or response to environmental and psychosocial stressors (El-Farhan et al., 2017; Paragliola et al., 2021). Melatonin timing, especially dim-light melatonin onset (DLMO), serves as a robust circadian phase marker that can anchor interpretation of temperature, sleep, and autonomic rhythms (Kennaway, 2023; Pandi-Perumal et al., 2007). Inflammatory markers or endothelial indicators are sometimes measured in studies linking environmental exposures to vascular or metabolic risk.

**How.** These markers are sampled discretely rather than continuously. Cortisol can be assayed from serum, saliva, urine, hair, or interstitial fluid; salivary and urinary cortisol are particularly useful for repeated sampling over the day and for capturing circadian patterns (El-Farhan et al., 2017; Juliana et al., 2025). Melatonin is typically measured from saliva or plasma samples collected at regular intervals in the evening to determine DLMO (Glacet et al., 2023; Lewy and Sack, 1989). Inflammatory and endothelial markers, lipids and other biochemical measures are generally obtained from venous blood and analysed in batches.

**Where.** Blood samples are drawn from peripheral veins (usually in the arm), saliva is collected via oral swabs or passive drool, and urine is collected either as spot samples or over defined intervals. In many environmental or field studies, saliva and urine are preferred for logistical reasons, with serum used when clinical or more detailed biochemical profiling is required (El-Farhan et al., 2017). Interpretation focuses on systemic or whole-day patterns rather than local tissue concentrations.

### Movement and activity (accelerometry)

**Why.** Movement and posture influence convective and evaporative heat loss and shape the context in which physiological signals are recorded. Accelerometry provides an objective record of whether a participant is sitting, standing, walking, or engaging in more vigorous activity, and is often used to distinguish low-level activity from true rest, to flag motion artefacts in other signals, and to interpret differences in thermal responses between sessions or participants. In sedentary built-environment studies, activity data are typically used as contextual covariates rather than primary outcomes (Yang and Hsu, 2010).

**How.** Accelerometers measure tri-axial linear acceleration, and sometimes angular velocity, at sampling rates from a few Hz to several hundred Hz. Many optical heart-rate, ECG and smartwatch devices include embedded accelerometers, so movement data are often available without additional hardware. Dedicated activity monitors provide higher configurability and may include posture classification algorithms. Raw acceleration can be processed into step counts, activity counts, posture labels, or simple metrics such as time spent sitting vs standing and number of sit-to-stand transitions (Lugade et al., 2014; Yang and Hsu, 2010).

**Where.** Sensors are typically worn on the wrist, chest, waist, or thigh. Wrist-worn accelerometry is convenient and aligns with common wearable devices but is less precise for posture discrimination; thigh- or waist-mounted sensors provide better separation of sitting, standing and stepping at the cost of slightly higher burden (Foerster et al., 1999; Franzese et al., 2025). In built-environment protocols, wrist or chest placements are often chosen to co-locate accelerometry with HR or ECG sensors.

### Respiratory and metabolic measures

**Why.** Ventilation and metabolic rate determine internal heat production and influence gas exchange, which can interact with indoor air quality and thermal comfort. In some laboratory-based thermophysiology studies, respiratory and metabolic measurements are used to quantify resting energy expenditure, the metabolic cost of tasks, or the effect of temperature on ventilatory patterns. These data help separate changes in heat storage due to altered environmental heat loss from those caused by shifts in metabolic rate (Delsoglio et al., 2019).

**How.** Metabolic rate is most commonly measured by indirect calorimetry, which estimates oxygen consumption (VO₂) and carbon dioxide production (VCO₂) by analysing inspired and expired gases. From these, resting or task-related energy expenditure can be calculated (Delsoglio et al., 2019; Mora et al., 2021). Gas exchange is recorded breath-by-breath or averaged over short windows; several methods exist for processing VO₂/VCO₂ time series for steady-state or maximal values (Martin-Rincon and Calbet, 2020; Robergs and Burnett, 2003). Ventilation and respiratory pattern can also be monitored using respiratory inductance plethysmography belts, nasal thermistors, or pressure sensors, providing information on breathing frequency and tidal volume without full calorimetry.

**Where.** Indirect calorimetry typically uses a mouthpiece with a nose clip, or a tight-fitting face mask, connected to a metabolic cart or a portable gas analyser. Respiratory belts are placed around the thorax and abdomen, while nasal thermistors or pressure transducers are positioned near the nostrils. These setups are more intrusive than most other signals discussed in this paper and are therefore mainly used in short, controlled laboratory exposures rather than long-duration building field studies (Delsoglio et al., 2019). In the context of built-environment research, respiratory and metabolic measures remain specialised tools for selected protocols where heat production is a primary outcome.

# TERMINOLOGICAL ALIGNMENT 

This chapter establishes a shared conceptual and terminological foundation for human thermal physiology research in built environment studies. While the previous chapter address measurement logic and signal-specific methodology, the present chapter operates at a cross-cutting level: it examines how variables are represented, defined, derived, and named across the field.

Considerable variability exists in symbolic notation, composite metric formulation, anatomical labelling, and semantic usage. Such inconsistencies impede reproducibility, hinder cross-study comparison, and complicate structured metadata reporting. Rather than imposing a new standard, this chapter documents the prevailing conventions and organizes them into a coherent framework.

The material is structured across four layers of abstraction:

1.  Symbolic notation and variable conventions,

2.  Harmonization challenges in derived and composite metrics,

3.  Anatomical reference and measurement site taxonomy, and

4.  Controlled vocabulary and glossary of terms.

## Symbolic notation and variable conventions

+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| **Metric family**                                             | **Specific variable / measure** | **Unit**                       | **Common aliases / symbols**                                              | **Notes**                                                                                             |
+===============================================================+=================================+================================+===========================================================================+=======================================================================================================+
| Core body temperature (CBT, T~core,~ T~CORE~, t~core,~ t~cr~) | Rectal temperature              | °C                             | trect, trec, tr, *t*~re~, tre, Trect, Trec, Tr, T~re~, Tre, T~REC~        | *t*~re~ in ISO 9886                                                                                   |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Oesophageal temperature         | °C                             | *t*~eso~, tes, *t*~es~, Teso, Tes, T~es~                                  | *t*~es~ in ISO 9886                                                                                   |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Gastrointestinal telemetry      | °C                             | *t*~ab~, *t*~gi~, *t*~pill~, *t*~GI~, T~PILL~                             | *t*~ab~ in ISO 9886                                                                                   |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Tympanic temperature            | °C                             | *t*~ty~, T~ty~, Tear                                                      | *t*~ty~ in ISO 9886                                                                                   |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Aural canal temperature         | °C                             | *t*~ac~, T~AUR~                                                           | *t*~ac~ in ISO 9886                                                                                   |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Oral temperature                | °C                             | *t*~or~, Tor                                                              | *t*~or~ in ISO 9886                                                                                   |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Skin temperature                                              | Local skin temperature          | °C                             | *t*~sk~, T~sk~, Tsk, Tskin, Tsk~i~                                        | *t*~sk~; index i denotes site (e.g., *t*~sk,chest~); Tsk or Tskin more commonly found in publications |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Mean skin temperature           | °C                             | *t*~sk~, T̄sk, MST, Tmean~skin~, Tsk~mean~                                 | Also *t*~sk~ in ISO 9886; MST common in building studies.                                             |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Gradients                       | °C, K                          | ΔTcore--skin, ΔTneck--ankle, ΔTprox--dist, DPG (Distal-Proximal Gradient) | Greek Δ denotes difference; both orders (core--skin / skin--core) appear, need to clarify.            |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Sweat / skin moisture                                         | Local sweat rate                | mg·cm⁻²·min⁻¹, mL·min⁻¹, g⋅h⁻¹ | *S*~W~, ṁsw, SRlocal, SR                                                  | *S*~W~ in ISO 9886                                                                                    |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Whole-body sweat loss           | mL, % body mass                | ∆m~sw~,WBSL, Δm                                                           | ∆m~sw~ in ISO 9886; WBSL common in sports; Δm used in ergonomics.                                     |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Skin wettedness                 | --                             | w                                                                         |                                                                                                       |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Electrodermal activity (family) | mS                             | EDA, SC, GSR                                                              | EDA preferred; GSR deprecated; SC sometimes confuses with sweat chloride.                             |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Tonic component (level)         | mS                             | SCL, EDA Tonic, SC                                                        | SCL (skin conductance level) standard.                                                                |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Phasic component (response)     | µS                             | SCR, SL, EDA Phasic                                                       | SCR (skin conductance response); SL used in psychophysiology.                                         |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Cardiovascular                                                | Heart rate                      | beats·min⁻¹                    | HR, bpm                                                                   |                                                                                                       |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Inter-beat interval             | ms                             | IBI, RR, RRi                                                              | RR from ECG R-wave interval; IBI preferred for PPG data.                                              |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Systolic pressure               | mmHg                           | SBP, Ps                                                                   | Ps legacy                                                                                             |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Diastolic pressure              | mmHg                           | DBP, Pd                                                                   | Pd legacy                                                                                             |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Mean arterial pressure          | mmHg                           | MAP, Pm                                                                   | Pm legacy                                                                                             |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Stroke volume                   | mL                             | SV                                                                        |                                                                                                       |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Cardiac output                  | L·min⁻¹                        | Q̇, CO                                                                     | Dot on Q indicates flow; CO older clinical style.                                                     |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Autonomic modulation (HRV)                                    | Time-domain indices             | ms                             | RMSSD, SDNN, pNN50, NNmean                                                | All-caps abbreviations fixed by HRV Task Force (1996).                                                |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Frequency-domain indices        | ms² or n.u.                    | LF, HF, LF/HF, TP                                                         | LF/HF ratio not dimensioned; n.u. = normalised units.                                                 |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Nonlinear indices               | --                             | SD1, SD2, SampEn, ApEn                                                    | Case-sensitive                                                                                        |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Vascular control                                              | Skin blood flow                 | PU, % max                      | SkBF, SBF, Flux                                                           | Flux shorthand from LDF; PU = perfusion units.                                                        |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Cutaneous vascular conductance  | PU·mmHg⁻¹, % max               | CVC, CVC~norm~                                                            | CVC = SkBF / MAP; subscript norm if normalised.                                                       |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Forearm blood flow              | mL·min⁻¹·100 mL⁻¹              | FBF                                                                       | Fixed abbreviation; capitalisation consistent.                                                        |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Metabolic / systemic                                          | Oxygen consumption              | mL·kg⁻¹·min⁻¹                  | VO₂, V̇O₂, VO2abs                                                          | Dot indicates rate; VO₂ standardised by physiology journals.                                          |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Carbon dioxide production       | mL·kg⁻¹·min⁻¹                  | VCO₂, V̇CO₂                                                                | Analogous to VO₂; VCO₂ plain text acceptable.                                                         |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Metabolic rate                  | W·m⁻², Met                     | M, Met, qmet                                                              | Met capitalised when unit, lower-case when variable.                                                  |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Respiratory exchange ratio      | --                             | RER, RQ                                                                   | RER = short-term, RQ = steady-state.                                                                  |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Heat storage rate               | °C·h⁻¹, kJ·kg⁻¹                | S, ΔH                                                                     | ΔH = enthalpy change.                                                                                 |
|                                                               +---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|                                                               | Body surface area               | m²                             | BSA                                                                       | Unambiguous; constants differ by formula (Du Bois vs Mosteller).                                      |
+---------------------------------------------------------------+---------------------------------+--------------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

: Table 6. Physiological variable naming conventions in thermal physiology studies

## Standardization challenges in derived metrics

Derived physiological metrics often exhibit substantial variability in weighting schemes, anatomical site selection, and reporting conventions. Mean skin temperature (MST) provides a paradigmatic example of such fragmentation, with multiple competing formulae and inconsistent site definitions across disciplines.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pts       A       B       C       D          E       F       G      H        I        J        K        L        M           N        O             P        Q        R        S        T        U      by                    Year   Ref
  ----- --- ------- ------- ------- ---------- ------- ------- ------ -------- -------- -------- -------- -------- ----------- -------- ------------- -------- -------- -------- -------- -------- ------ --------------------- ------ ------------------------------------
  3     a                                              0.14                                      0.50                                                          0.36                                       Burton                1935   (Mitchell and Wyndham, 1969)

  3     b                                              0.14                                      0.50                                                                   0.36                              Olesen                1984   (Olesen, 1984)

  3     c   0.25                                       0.50                                                                                                                      0.25                     Cho et al.            1996   (Cho et al., 1996)

  3     d                                              0.30                                      0.35                                                          0.35                                       Wu et al.             2020   (Y. Wu et al., 2020)

  4     a                                              0.15                                      0.34                                   0.33                   0.18                                       Newburgh & Spealman   1943   (Teichner, 1958)

  4     b                           0.30                                                         0.30                                   0.20                   0.20                                       Ramanathan            1964   (Ramanathan, 1964)

  4     c                   0.28                                      0.16              0.28                                                                   0.28                                       ? +                   1992   (ISO, 2004)

  4     d                                              0.14                                      0.35                                   0.26                   0.25                                       Wu et al.             2020   (Y. Wu et al., 2020)

  5     a   0.07                                                      0.05                       0.50                                   0.18                   0.20                                       Ouyang                1985   (Ouyang, 1985)

  5     b           0.07            0.19 (a)                                                              0.175    0.175                              0.39                                                Houdas                1982   (Houdas and Ring, 1982)

  5     c   0.07                                                      0.05                       0.42                                   0.26                   0.20                                       Wu et al.             2020   (Y. Wu et al., 2020)

  5     d   0.20                    0.18                              0.05              0.50                                            0.07                                                              Wang et al.           2013   (Wang et al., 2013)

  6     a           0.14                               0.11    0.05                     0.19     0.19                                   0.32                                                              Ouyang                1985   (Ouyang, 1985)

  6     b           0.149           0.107                                                        0.186    0.186                         0.186         0.186                                               Teichner              1958   (Teichner, 1958)

  6     c   0.10                                       0.05           0.05                       0.40                                   0.20                   0.20                                       Miura et al           ?      (Mochida, 1983)

  6     d   0.11                    0.1                0.13                                      0.28                                   0.21                   0.20                                       Mochida               1983   (Mochida, 1983)

  6     e           0.14                               0.11           0.05                       0.19     0.19                          0.32                                                              Palmes & Park         1947   (Palmes and Park, 1947)

  7     a   0.07                                       0.14    0.05                              0.35                                   0.19                   0.13                                0.07   Hardy & DuBois        1938   (Hardy et al., 1938)

  7     b                                              0.14           0.14              0.07     0.07                                   0.14                            0.14     0.14                     Park                  1988   (Park et al., 1988)

  7     c   0.21                    0.12               0.06                                      0.21              0.17                 0.15                   0.08                                       Nadel                 ?      (Mochida, 1983)

  7     d                   0.098   0.082              0.114                            0.162    0.166                                  0.182                  0.206                                      Ouyang                1985   (Ouyang, 1985)

  7     e   0.066                   0.149              0.151                                     0.153             0.153                0.163                  0.183                                      Mochida               1983   (Mochida, 1983)

  7     f   0.198                   0.138              0.076                                     0.179             0.145                0.153                  0.092                                      Mochida               1983   (Mochida, 1983)

  8     a                           0.085              0.09                             0.11     0.11     0.11     0.11                 0.23                   0.16                                       Ouyang                1985   (Ouyang, 1985)

  8     b   0.07                    0.07               0.07           0.05              0.175    0.175                                  0.19                   0.20                                       Gagge & Nishi +       1977   (Gagge and Nishi, 1977; ISO, 2004)

  8     c   0.21                    0.12               0.06                             0.11     0.10              0.17                 0.15                   0.08                                       Nadel                 1973   (Nadel et al., 1973)

  8     d   0.07                    0.13               0.12                             0.09     0.09              0.18                 0.16                   0.16                                       Nadel                 1973   (Nadel et al., 1973)

  8     e   0.19                    0.13               0.12                             0.09     0.08              0.12                 0.12                   0.15                                       Crawshaw              1975   (Crawshaw et al., 1975)

  9     a   0.07                    0.07               0.07           0.05              0.18     0.18                                   0.19                   0.13                       0.06            Ouyang                1985   (Ouyang, 1985)

  9     b   0.12                    0.18               0.05           0.04                       0.18              0.16                 0.18                   0.11                       0.08            Neuroth               ?      (Houdas and Ring, 1982)

  10    a           0.10            0.07               0.07           0.06              0.125    0.13                                   0.125\*                0.15                       0.05            Teichner ++           1943   (Teichner, 1958)

  10    b   0.06                    0.09               0.06           0.05              0.19     0.10              0.095                0.19                   0.12                                0.06   Ouyang                1985   (Ouyang, 1985)

  10    c   0.06                    0.08               0.06           0.05              0.12     0.12              0.12                 0.19                   0.13                       0.07            Colin & Houdas        1982   (Colin et al., 1971)

  10    d           0.20            0.05\*\*           0.05                             0.20     0.05              0.125 (r)            0.125\*\*\*            0.075    0.075                             Houdas & Ring         1982   (Colin et al., 1971)

  10    e           0.10            0.07               0.07           0.06              0.13     0.13                                   0.125\*\*              0.15                       0.05            Omrec                 ?      (Houdas and Ring, 1982)

  10    f   0.031           0.043   0.082              0.06           0.05              0.17                       0.081       0.081    0.17                            0.134             0.07            Kurata & Funazu       ?      (Mochida, 1983)

  10    g   0.10                    0.10                              0.10              0.10     0.10              0.10                 0.10          0.10              0.10              0.10            Stolwijk & Hardy      1966   (Gagge et al., 1967)

  11        0.06                    0.07               0.07           0.05              0.09     0.09     0.09     0.09                 0.19                   0.13                       0.07            Ouyang                1985   (Ouyang, 1985)

  12        0.07                                       0.14           0.05              0.0875   0.0875   0.0875   0.0875               0.095         0.095    0.065    0.065             0.07            Hardy & DuBois        1938   (Hardy et al., 1938)

  13        0.077           0.077   0.077              0.077          0.077             0.077    0.077    0.077    0.077                0.077                  0.077                      0.077           Nielsen               1984   (Nielsen and Nielsen, 1984)

  14        0.071           0.071   0.071      0.071                  0.071             0.071    0.071    0.071    0.071 (r)            0.071 (r)     0.071    0.071    0.071             0.071           Olesen +              1992   (ISO, 2004; Olesen, 1984)

  15    a   0.06                    0.035              0.025          0.0225   0.0225   0.18     0.20                                   0.1025        0.1025   0.0625   0.0625   0.325    0.325           Ouyang                1985   (Ouyang, 1985)

  15    b   0.07            0.07    0.07               0.07           0.07              0.07     0.07     0.07     0.07                 0.07\*        0.07     0.07     0.07              0.07            Mitchell & Wyndham    1969   (Mitchell and Wyndham, 1969)

  17        0.037   0.037           0.075              0.075          0.025    0.025    0.0625   0.0625   0.0625   0.0625      0.0625   0.0875        0.0875   0.0875   0.0875   0.0305   0.0305          Ouyang                1985   (Ouyang, 1985)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 7. Measurement sites and weighting factors for mean skin temperature formulas.\
  A: Forehead, B: Left cheek, C: Left neck\
  D: Right upper arm, E: Left elbow, F: Left forearm, G: Left palm, H: Right hand, I: Left hand\
  J: Left back, K: left chest, L: Left lumbar, M: Abdomen, N: Left buttocks\
  O: Anterior thigh, P: Left posterior thigh, Q: Right anterior calf, R: Left posterior calf, S: Left foot, T: Right foot, U: Left sole

+----------------------------+-------------------------------------------------------------------------------+------------------------------+
| \(a\) Measured anteriorly\ | \* Measured on anterior thigh and antero-medial thigh, same weighting factor  | \+ Adopted by ISO 9886:2004\ |
| (r) Measured on the right  |                                                                               | ++ Adopted by QREC           |
|                            | \*\* Measured on two locations, anterior and posterior, same weighting factor |                              |
|                            |                                                                               |                              |
|                            | \*\*\* Measured on antero-medial thigh                                        |                              |
+============================+===============================================================================+==============================+

## 

## Anatomical reference taxonomy

This section compiles the anatomical sites used for skin-temperature measurement, standardised into 19 body regions. Each site may include left/right or anterior/posterior counterparts; these are only specified when relevant.\
Letters A--U from the previous chapter, 4.2 Mean skin temperature formulas are retained solely to map historical formulas to the standardised regions shown in Table 8 and Figure 2.

![Figure 2. Skin temperature measurement sites. Letter annotations refer to the matching measurement regions in Mean Skin Temperature calculation formulas. Regions correspond to Table 8. Each may be subdivided by side (L/R) or aspect (A = anterior, P = posterior, M = midline).\
Black points indicate specific aspects of measurement sites as per MST formulas. Pink points indicate other possible sites, as seen in current practices.](C:\Users\kobas\00_Repos\2511_WhyWeMeasureWhat_Git\_build_intermediate\media/media/image2.jpeg){alt="A full shot of a person and person AI-generated content may be incorrect." width="6.627777777777778in" height="7.220833333333333in"}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  MST Formula Code   MST Formula Laterality\                   Region Code      Common Aliases / Variants                                     Notes
                     /Aspect                                                                                                                  
  ------------------ ----------------------------------------- ---------------- ------------------------------------------------------------- -------------------------------------------------------------------------------
  A                  Anterior midline                          1 Forehead       Brow, temple                                                  

  --                 --                                        2 Nose           Nasal dorsum, alar region                                     Facial IRT extension; captures respiratory heat exchange

  B                  Left                                      3 Cheek          Malar region, zygomatic arch                                  Common in IRT; not in older MST sets

  C                  Left                                      4 Neck           Sternocleidomastoid, nape, lateral neck, nuchal area          

  K                  Left                                      5 Chest          Pectoral region, forebreast, sternum, thorax                  

  M                  --                                        6 Abdomen        Umbilical region, epigastric, central abdomen, lower thorax   

  J                  Left                                      7 Back           Scapular, interscapular, upper thoracic region                Frequent confusion with lumbar; mapped here

  L                  Left                                      8 Lumbar         Lumbar, flank, lumbosacral region                             

  N                  Left                                      9 Buttocks       Gluteal region                                                Included in extended body-surface formulas

  D                  Right                                     10 Upper arm     Biceps, triceps, deltoid region                               

  E                  Left                                      11 Elbow         Cubital fossa (front), olecranon (back)                       

  F                  Left                                      12 Forearm       Antebrachial region                                           Widely used due to accessibility

  --                 --                                        13 Wrist         Carpal region, radial wrist                                   Optional distal proxy for forearm, got popular with new wearables

  G, H, I            Left palm, Right dorsum, Left dorsum      14 Hand          Hand: Dorsum of hand, back of hand                            

  --                 --                                        15 Finger        Digital area, fingertip, phalanx                              Sensitive to sympathetic vasoconstriction, also used with new wearables

  O, P               Anterior, Posterior                       16 Thigh         Quadriceps (front), hamstring (back)                          

  Q, R               Anterior, Posterior                       17 Lower leg     Anterior: Anterior tibia, shin\                               Differentiated anterior/posterior in formulas -- calf vs shin often conflated
                                                                                Posterior: Gastrocnemius, calf                                

  --                 --                                        18 Ankle         Malleolar area, lateral ankle, Achilles tendon                Added for distal gradient analysis

  S, T, U            Left dorsum, Right dorsum, Left plantar   19 Foot / Sole   Foot: Instep, dorsal foot\                                    
                                                                                Sole: Plantar surface, sole                                   
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Table 8. Canonical body regions for skin-temperature measurement, with MST formula mappings, common aliases, and notes

## Controlled vocabulary and glossary

# SAMPLE CHECKLISTS & SCHEMAS

This appendix illustrates one practical way to structure experiment-, participant-, and session-level documentation for human thermal physiology studies. The goal is not to prescribe a new field-wide standard, but to make our own approach transparent and to provide concrete examples that other groups can adapt and share. By circulating comparable schemas, the field can gradually converge on common reporting practices and enable more reproducible, interoperable datasets.

The structure mirrors other established data standards for human studies, such as the Brain Imaging Data Structure (BIDS) (Gorgolewski et al., 2016), which separates participants.tsv and sessions.tsv files, and the ISA-Tab framework (Sansone et al., 2012), which distinguishes investigation, study, and assay metadata. Our schema follows a similar logic: clean separation of persistent attributes, per-experiment descriptors, and per-visit variables.

We distinguish three levels:

- Experiment metadata: one record per study or protocol. Stores high-level information: title, lab, institute, recruitment window, primary endpoints, general exposure types (lab vs field, heat vs cold vs neutral), and ethics approval identifiers.

- Participant metadata: one record per person, containing attributes that change slowly or not at all during the study. Stores demographics, morphology, health and diagnoses, hormonal status, lifestyle, sleep and chronotype, thermal sensitivity, and (optionally) built-environment context.

- Session metadata: one record per visit or experimental condition per person. Stores per-visit timing, condition labels, acute state (sleep, illness, recent behaviour), clothing and activity, and key protocol deviations.

- 

- This separation reflects how physiological data are actually generated: experiments define the protocol; participants bring stable individual characteristics; and sessions capture the day-to-day variability that strongly shapes thermoregulatory responses.

Device inventories (sensor IDs, firmware versions, calibration logs) are stored in separate tables and linked to specific sessions and experiments. Separating device metadata helps manage multi-sensor setups, facilitates troubleshooting, and supports later data harmonisation.

## Experiment-level metadata

Experiment-level metadata capture the high-level characteristics of a study: where and when it was conducted, by whom, under which ethical approvals, and what its overall design and planned exposures were. These fields describe the protocol as a whole, independently of any particular participant or session, and form the top level of the metadata hierarchy.

To make the schema easier to reuse across different laboratories and study types, fields are grouped by topic and are assigned to three informal tiers:

- [Tier 1 -- Core experiment descriptors:]{.underline} Essential information needed to interpret or reuse a study, including experiment identifiers, institutional affiliation, ethics approval, study design and environment, recruitment window, and the main exposure/intervention categories.

- [Tier 2 -- Recommended descriptors:]{.underline} Information that improves reproducibility and interpretability but may not always be available, such as randomisation method, blinding, standardised behavioural instructions, number and naming of conditions, and detailed environmental or HVAC descriptions.

- [Tier 3 -- Specialised descriptors:]{.underline} More specific contextual information that is useful for certain study types or advanced meta-analyses, including room geometry, calibration summaries, or detailed equipment notes. These fields are optional but help achieve FAIR-level documentation when available.

To aid cross-study comparison, we also include a concise PICOT summary for each experiment. PICOT provides a high-level, non-redundant synopsis of the Population, Intervention, Comparison, Outcomes, and Time frame, complementing (but not duplicating) the detailed metadata fields.

+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| **Group**                                  | **Field name**                       | **Tier** | **Typical answers / coding**                                                                | **Notes / considerations**                                                                        |
+============================================+======================================+==========+=============================================================================================+===================================================================================================+
| Core IDs                                   | Experiment ID                        | 1        | Unique alphanumeric code                                                                    | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Experiment name                      | 1        | Descriptive title                                                                           | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Principal investigator/s             | 1        | Name/s or initials                                                                          | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Researcher/s                         | 1        | Name/s or initials                                                                          | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Contact person                       | 1        | Single designated contact                                                                   | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Contact information                  | 1        | Email                                                                                       | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Lab/s                                | 1        | Lab or unit name                                                                            | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Institute/s                          | 1        | Organisational affiliation                                                                  | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Location/s                           | 1        | City, country, optionally coordinates or street address                                     | High-resolution location info helps with automated climate data and time zone                     |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Ethics & governance                        | Ethics committee                     | 1        | Full name                                                                                   | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Ethics approval ID/Code              | 1        | Approval number                                                                             | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Approval date                        | 2        | YYYY-MM-DD                                                                                  | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Amendments/versions                  | 2        | Yes/No; brief notes                                                                         | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Data protection compliance           | 1        | GDPR, HIPAA, other                                                                          | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Preregistration ID                   | 2--3     | OSF/clinicaltrials.gov link                                                                 | --                                                                                                |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Study type                                 | Study environment                    | 1        | Laboratory, Field, Hybrid                                                                   | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Study design                         | 1        | Controlled/Observational/Interventional                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Experimental structure               | 2        | Between-subjects, Within-subjects, Repeated measures, Crossover, Pre-Post, etc.             | Multiple can apply                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Randomisation                        | 2        | Yes/No; method (simple, block, Latin square)                                                | Links to randomisation table                                                                      |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Blinding                             | 1        | None/Single-blind/Double-blind                                                              | If None, a short description nice to have                                                         |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Timing & Schedule                          | Start date of the experiment         | 1        | YYYY-MM-DD                                                                                  | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | End date of the experiment           | 1        | YYYY-MM-DD                                                                                  | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Typical session duration             | 1        | Minutes or hours                                                                            | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Standard session start time          | 1        | hh:mm, 24 h time                                                                            | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Standard session end time            | 1        | hh:mm, 24 h time                                                                            | --                                                                                                |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Study population                           | Target sample size                   | 1        | Integer                                                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Achieved sample size                 | 1        | Integer                                                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Male participants                    | 1        | Integer                                                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Female participants                  | 1        | Integer                                                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Intersex participants                | 1        | Integer                                                                                     | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Age range                            | 1        | Minimum-maximum                                                                             | "21--35 years"                                                                                    |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Population description               | 1        | Free text                                                                                   | e.g., "Healthy university students", "Sedentary adults aged 20--40"                               |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Inclusion criteria                   | 1        | Free text or list                                                                           | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Exclusion criteria                   | 1        | Free text or list                                                                           | --                                                                                                |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Intervention                               | Study domain/s                       | 1        | Thermal / Humidity / Air velocity / Lighting / Air quality / Noise                          | Multiple allowed                                                                                  |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Intervention description             | 1        | Free text                                                                                   | Describe all manipulated variables                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Number of conditions                 | 2        |                                                                                             | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Condition labels                     | 2        |                                                                                             | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Standardised behaviour rules         | 1        | Resting, sitting, acclimatisation/normalisation, movement, eating, drinking protocols, etc. | --                                                                                                |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Environment & equipment (experiment-level) | Spatial typology                     | 1        | Office / Residential / Educational / Public / etc.                                          | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | HVAC system description              | 2        | AC model, radiant panel specs, air velocity sources                                         | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Room dimensions                      | 3        | m² or m³                                                                                    | --                                                                                                |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Baseline environmental control       | 1        | Air temperature, radiant temperature, humidity, lighting ranges, etc.                       | Multiple allowed                                                                                  |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Primary instruments used             | 1        | Names + IDs                                                                                 | Linked to external Sensors table if exists                                                        |
|                                            +--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | Instrument calibration notes         | 3        | Summary + links to logs                                                                     | Linked to external Sensors table if exists                                                        |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| PICOT Summary                              | P -- Population                      | 1        | Short description of target group and key eligibility criteria                              | "Healthy adults 18--35, BMI 18--25, non-smokers; no CV/metabolic disease; regular sleep schedule" |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | I -- Intervention / exposure         | 1        | Summary of main exposure(s) or experimental condition(s)                                    | "14-day heat acclimation: AC at 26 °C vs free-running apartment (summer conditions)"              |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | C -- Comparison / control conditions | 1        | Description of comparator condition(s)                                                      | "Free-running cooling vs constant AC; within-subject crossover" or "Neutral 24 °C control"        |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | O -- Primary outcome(s               | 1        | List main endpoints and how they are quantified                                             | "Core body temperature, neck/ankle skin temp, HR, BP, HRV (RMSSD), thermal sensation"             |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | O -- Secondary outcomes              | 2        | Additional exploratory endpoints (no units or detail)                                       | "Sleep onset latency, actigraphy-based sleep efficiency, melatonin AUC"                           |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                            | T -- Time frame                      | 1        | Time horizon for the effect and measurement                                                 | "Pre--post mild heat stress test before and after 14-day exposure; tests between 09:00--16:00"    |
+--------------------------------------------+--------------------------------------+----------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

: Table 9. Experiment-level metadata schema, organised by group and tier.

## Participant-level metadata

Participant-level metadata capture characteristics that are stable or slowly changing across the duration of a study. These variables describe each individual taking part in the experiment and provide the context needed to interpret physiological responses, account for relevant modifiers, and enable subgroup or meta-analytic work.

Each participant is represented by one row in a dedicated metadata table, with one column per field. As in the experiment-level schema, fields are grouped by topic (e.g., Demographics & Morphology, Health & Diagnoses, Lifestyle, Reproductive & Hormonal) and assigned to informal tiers indicating their importance:

- [Tier 1 -- Core:]{.underline} Minimal information required in any thermal physiology experiment (e.g., age, sex at birth, height, weight, BMI, basic health status, habitual physical activity, key hormonal status).

- [Tier 2 -- Recommended:]{.underline} Variables that strongly influence thermoregulation and improve interpretability, including body surface area, thermal history, smoking and alcohol use, typical sleep timing, menstrual cycle characteristics, hormone therapies, thermosensitivity, and selected built-environment descriptors.

- [Tier 3 -- Specialised:]{.underline} More detailed or study-specific attributes, such as body composition, occupation, education, sensory-sensitivity or psychological scales, quality-of-life instruments, or vision/colour-vision assessments. These fields are optional but useful for specialised analyses or targeted protocols.

The participant metadata table can be implemented in a spreadsheet, REDCap form, or as structured CSV/TSV with accompanying JSON (e.g., a participants.tsv + participants.json pair following BIDS conventions).

+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Group**                                               | **Field name**                               | **Tier** | **Typical answers / coding**                                                                  | **Example instruments / tools**                                                                                                                                                                       |
+=========================================================+==============================================+==========+===============================================================================================+=======================================================================================================================================================================================================+
| Core IDs                                                | Participant ID                               | 1        | Text ID (e.g. P01, SL23_001)                                                                  | -- (lab-defined)                                                                                                                                                                                      |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Study / cohort                               | 1        | Text (e.g. PMV05 -- Red, ACvsFR -- AC)                                                        | -- (lab-defined)                                                                                                                                                                                      |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Demographics & morphology                               | Age                                          | 1        | Numeric (years at first session)                                                              | Direct (derived from DOB if stored). If ethics committees do not allow, then age group according to a medically agreed on standard (Diaz et al., 2021)                                                |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Sex                                          | 1        | Categorical: female / male / trans f2m/ trans m2f                                             | Trans categories only for active transitioning at the time of the experiment                                                                                                                          |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Gender identity (optional)                   | 2        | Categorical or free text                                                                      | -- (lab-defined wording)                                                                                                                                                                              |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Height                                       | 1        | Numeric (cm), self-reported or measured (flag which)                                          | Stadiometer; self-report                                                                                                                                                                              |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Weight                                       | 1        | Numeric (kg), self-reported or measured                                                       | Scale or self-report. If measured, note the method (e.g., in nude, in underwear, fasting morning, etc.)                                                                                               |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | BMI                                          | 1        | Numeric (kg·m⁻²), derived                                                                     | Calculation from height & weight                                                                                                                                                                      |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Body surface area (BSA)                      | 2        | Numeric (m²)                                                                                  | DuBois & DuBois, Mosteller, etc. (formula documented)                                                                                                                                                 |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Body fat %                                   | 2        | Numeric (%)                                                                                   | BIA, DXA, skinfolds, BodPod, etc.                                                                                                                                                                     |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Ethnic background / nationality              | 3        | Categorical or free text; optional                                                            | -- (decide based on ethics & purpose)                                                                                                                                                                 |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thermal history & occupation                            | Thermal history / acclimation background     | 2        | Free text or categories (e.g. "\>5 y in hot climate", "recently relocated from cold climate") | -- (short structured items)                                                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Occupation / profession                      | 3        | Categorical / free text (e.g. student, office worker, outdoor labour)                         | -- (decide based on ethics & purpose)                                                                                                                                                                 |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Education level                              | 3        | Categorical (e.g. secondary / bachelor / master / PhD)                                        | -- (decide based on ethics & purpose)                                                                                                                                                                 |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lifestyle & exposure                                    | Smoking status                               | 1        | Never / former / current; pack-years if known                                                 | Can be taken from PAR-Q+ or simple lab form                                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Alcohol use (habitual)                       | 2        | Units per week or categories (none / occasional / regular)                                    | AUDIT-C (Lawford et al., 2012) or simple frequency question                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Regular caffeine intake                      | 2        | Cups per day or categories (low / moderate / high)                                            | Simple frequency question                                                                                                                                                                             |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Physical activity / fitness level (habitual) | 1--2     | MET-min/week + category (low / moderate / high)                                               | IPAQ-SF, IPAQ-LF (Lee et al., 2011), or GPAQ (WHO) (Bull et al., 2009)                                                                                                                                |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Health & diagnoses                                      | Overall health status                        | 1        | Healthy / controlled condition(s) / other + notes                                             | Summary from screening; may combine PAR-Q+ (Warburton et al., 2011) + brief medical history                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Cardiovascular diagnoses                     | 1        | Yes/No per condition (hypertension, arrhythmia, CAD, HF, etc.)                                | PAR-Q+, Charlson comorbidity list (Charlson et al., 2022), or tailored checklist                                                                                                                      |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Endocrine / metabolic diagnoses              | 1        | Yes/No per condition (diabetes, thyroid disease, obesity, CKD, etc.)                          | PAR-Q+, Charlson-based checklist                                                                                                                                                                      |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Neurological / autonomic disorders           | 1        | Yes/No per condition (POTS, autonomic neuropathy, Parkinson's, SCI, etc.)                     | Screening form referencing medical history                                                                                                                                                            |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | History of syncope / orthostatic intolerance | 2--3     | Yes/No + short description                                                                    | PAR-Q+ style yes/no item(s)                                                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Diagnosed sleep disorder                     | 2--3     | None / OSA / insomnia / restless legs / other                                                 | PSQI/ISI + STOP-Bang / Berlin / Epworth, or clinical history                                                                                                                                          |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Neurodivergent diagnosis                     | 2--3     | None / ASD / ADHD / other / prefer not to say                                                 | Self-report; may link to ASD/ADHD screening tools if used                                                                                                                                             |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Other diagnoses relevant to thermoregulation | 2--3     | Free text + coded categories                                                                  | Examples: autoimmune disease, large burns/grafts, chronic infection, etc.                                                                                                                             |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Medication                                              | Chronic medications (by class)               | 1        | Yes/No per class (β-blockers, antihypertensives, anticholinergics, SSRIs, stimulants, etc.)   | Simple class checklist; optionally ATC codes                                                                                                                                                          |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Thermally relevant medication notes          | 2        | Free text (drug names, dose, duration)                                                        | -- (structured notes)                                                                                                                                                                                 |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reproductive & hormonal                                 | Menstrual / reproductive status              | 1        | Eumenorrheic / perimenopausal / postmenopausal / amenorrheic / pregnant / lactating           | Simple categorical items                                                                                                                                                                              |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Cycle length & regularity                    | 2        | Numeric (days) + regular / irregular                                                          | Short structured questions                                                                                                                                                                            |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Hormonal contraception                       | 1        | Type (combined pill, progestin-only, IUD, implant, injection, none) + duration                | Short structured questions                                                                                                                                                                            |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | HRT (hormone replacement therapy)            | 1        | Regimen (oestrogen, oestrogen+progestin, other) + duration                                    | Medical history question                                                                                                                                                                              |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | GAHT (gender-affirming hormone therapy)      | 1        | Yes/No; regimen (e.g. oestradiol, testosterone, blockers) + duration                          | Medical history; optional and ethics-dependent                                                                                                                                                        |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thermal sensitivity / preference & psychological traits | Thermal sensitivity / preference             | 1--2     | Scores + groupings (e.g. cold / neutral / warm-preferring)                                    | ETSRS (Van Someren et al., 2016) or similar                                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Personality traits                           | 3        | Scores on Big Five, BIS/BAS, etc.                                                             | Big Five (e.g. BFI, NEO-FFI), BIS/BAS scales, etc.                                                                                                                                                    |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | General sensory / emotional sensitivity      | 3        | Score(s)                                                                                      | Highly Sensitive Person Scale (HSPS) or similar, if used                                                                                                                                              |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Psychological / psychiatric scales           | 2--3     | Scores, cut-offs for depression, anxiety, etc.                                                | e.g. PHQ-9, GAD-7, DASS-21                                                                                                                                                                            |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sleep & chronobiology                                   | Chronotype                                   | 1        | Continuous score + category (morning / intermediate / evening)                                | Morningness--Eveningness Questionnaire (MEQ) (Horne and Ostberg, 1976), Composite Scale of Morningness (CSM) (Smith et al., 2011), and/or Munich Chronotype Questionnaire (Roenneberg et al., 2015).\ |
|                                                         |                                              |          |                                                                                               | Store instrument name + score/category                                                                                                                                                                |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Habitual bedtime                             | 1--2     | Typical bed and wake times (work days vs free days)                                           | Often comes with MCTQ; or simple timing questions                                                                                                                                                     |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Habitual sleep quality                       | 2--3     | Global score, and optionally "good vs poor sleeper"                                           | Pittsburgh Sleep Quality Index (PSQI) for overall sleep quality (Buysse et al., 1989)                                                                                                                 |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Built-environment context (optional)                    | Main dwelling type                           | 3        | Detached house / apartment / dorm / informal etc.                                             | Simple categorical question                                                                                                                                                                           |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Home and/or office heating/cooling systems   | 2        | Multi-select: central heating, floor heating, AC, fans, none, etc.                            | Simple checklist                                                                                                                                                                                      |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Typical bedroom temperature                  | 3        | °C or cool/neutral/warm category                                                              | Self-estimate question                                                                                                                                                                                |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vision & sensory (for light/EEG-heavy protocols)        | Vision status                                | 3        | Normal with/without correction / impaired                                                     | Snellen or LogMAR chart; self-report of correction                                                                                                                                                    |
|                                                         +----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Colour vision                                | 3        | Normal / red--green deficiency / other                                                        | Ishihara plates or equivalent test                                                                                                                                                                    |
+---------------------------------------------------------+----------------------------------------------+----------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10. Example participant-level metadata schema, including groups, field definitions, tiers, typical coding formats, and references to relevant standards or screening tools.

Note. Some questions may be redundant when already used as an exclusion criterion, e.g., if having any CV history is an exclusion reason, then no need to repeat it in participant metadata.

## Session-level metadata

Session-level metadata captures all information that varies from one visit or experimental condition to the next for a given participant. Many of the acute modifiers discussed in Section 2---such as last night's sleep, time since waking, recent illness, caffeine or meal timing, and daily hormonal fluctuations---change from day to day and therefore must be recorded at the session rather than participant level.

Each session is represented by one row in a dedicated metadata table, with one column per session field. As with the experiment- and participant-level schemas, fields are grouped by topic (e.g., Identifiers & Timing, Devices & Logistics, Protocol Adherence, Acute Health State) and assigned to informal tiers:

- [Tier 1 -- Core:]{.underline} Essential variables recorded for every visit (e.g., session ID, date and time, condition code, clothing, sleep duration, pre-session restrictions, acute illness indicators).

- [Tier 2 -- Recommended:]{.underline} Factors that meaningfully influence thermophysiological responses but may not always be collected (e.g., researchers present, acclimation period, night-shift work, time since exercise).

- [Tier 3 -- Specialised:]{.underline} Detailed or study-specific variables, such as exact bathroom break volumes, caloric intake calculations, event logs, or fine-grained environmental contextualisation.

Individual studies may extend this table with experiment-specific columns, such as time points for discrete measurements, cognitive task blocks, stepwise heating/cooling adjustments, water-intake increments, or protocol deviations. The core fields remain comparable across studies, facilitating harmonisation and meta-analysis.

Session metadata can be recorded via paper logs, REDCap/Qualtrics forms, or digital forms directly linked to the underlying session table.

+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| **Group**                                  | **Field name**                             | **Tier** | **Typical answers / coding**                                                                                                                                     | **Example instruments / tools**                                                                         |
+============================================+============================================+==========+==================================================================================================================================================================+=========================================================================================================+
| Identifiers & timing                       | Session ID                                 | 1        | Unique ID per visit/condition (e.g. P01_S1, P03_C01_Armchair)                                                                                                    | Lab-defined                                                                                             |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Participant ID                             | 1        | Unique participant code linked to master table (P01, SL23_001, etc.)                                                                                             | Lab-defined                                                                                             |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Date                                       | 1        | Calendar date                                                                                                                                                    | -- YYYY-MM-DD or format noted                                                                           |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Session start time                         | 1        | 24-h clock time or UNIX timestamp                                                                                                                                | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Session end time                           | 1        | 24-h clock time or UNIX timestamp                                                                                                                                | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Condition / scenario code                  | 1        | Text label for assigned condition (e.g. C01_01, Heat_26C, Night_Armchair)                                                                                        | Lab-defined                                                                                             |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Location / room                            | 1        | Room or laboratory code                                                                                                                                          | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Researchers present                        | 2        | Initials or staff codes                                                                                                                                          | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Devices & protocol logistics               | Device IDs used                            | 1        | ID numbers for all devices applied to this participant                                                                                                           | Internal device inventory                                                                               |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Device attachment / ingestion times        | 1        | Clock times per device (e.g., "CBT pill ingested 17:50", "Sensors attached 17:55")                                                                               | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Device attachment type                     | 1        | Attachment type per device, when relevant (e.g., "Skin temperature sensor IDXXXXX: Medical tape")                                                                | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Condition order / randomisation code       | 1        | Randomisation sequence label (e.g., "Sequence A: warm → neutral → cool")                                                                                         | Study randomisation plan                                                                                |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Calibration / zeroing performed            | 2        | Yes/No + short note (e.g., "BP device calibrated 2025-06-01")                                                                                                    | Device calibration logs                                                                                 |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Environment & exposure (session context)   | Clothing description                       | 1        | Free text description (e.g. "T-shirt, jeans, socks")                                                                                                             | --                                                                                                      |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Clothing insulation (clo)                  | 1        | Numeric clo value (approx. 0.5--1.5 etc.)                                                                                                                        | Estimation based on ISO 9920 tables; or lab-specific lookup                                             |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Outdoor weather context                    | 2--3     | Simple categories: "cold spell", "typical", "heatwave", or link to local weather series                                                                          | Researcher notes -- weather data assumed to be measured or obtained from nearest meteorological station |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Use of additional personal conditioning    | 2--3     | Yes/No; type (fan, blanket, personal heater, etc.)                                                                                                               | Observed + logged when allowed by protocol                                                              |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Protocol adherence                         | Pre-session restriction compliance         | 1--2     | Yes/No; if No: short description (e.g. "coffee 2 h before", "ran to lab")                                                                                        | Checklist based on study instructions (no alcohol, no caffeine, etc.)                                   |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Arrival time to lab                        | 2        | Clock time                                                                                                                                                       | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Waiting / acclimation period               | 2        | Minutes from arrival to session start (numeric)                                                                                                                  | Derived from times, duration should be standardised                                                     |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Scheduling & circadian context             | Sleep-wake times                           | 1--2     | Clock time, 24 h                                                                                                                                                 | Sleep log / app                                                                                         |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Sleep duration last night                  | 1        | Numeric (hours slept; e.g. 6.8)                                                                                                                                  | Derived from log                                                                                        |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Sleep quality last night                   | 1--2     | 0--10 scale or 1--5 Likert                                                                                                                                       | Subjective rating                                                                                       |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Recent night-shift work                    | 2        | Yes/No; description (e.g. "3 consecutive night shifts in last week")                                                                                             | Sleep log / app                                                                                         |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Acute health state (today / last few days) | Recent acute illness (last 7 days)         | 1--2     | Yes/No; short description ("URI with fever", "GI infection")                                                                                                     | PAR-Q+ style yes/no items; brief medical history                                                        |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Fever symptoms in last 48 h                | 2        | Yes/No; peak temperature if known                                                                                                                                | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Antipyretic use (last 48 h)                | 2        | Yes/No; drug name and approximate time (free text)                                                                                                               | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | New medications since previous session     | 2        | Yes/No; if Yes: names and doses (free text)                                                                                                                      | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Behaviour since waking (session-day)       | Time since last meal at start              | 1--2     | Numeric (hours); optional category (light / normal / heavy); Yes/No if a specific fasting time was instructed (e.g. "Did not eat in the last 12 hours")          | --                                                                                                      |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Time since last caffeine                   | 1--2     | Numeric (hours); type (coffee / tea / energy drink / other); Yes/No if a specific fasting time was instructed (e.g. "Did not drink coffee in the last 12 hours") | --                                                                                                      |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Time since last moderate/vigorous exercise | 2        | Numeric (hours); or category (\<4 h, 4--12 h, \>12 h); Yes/No if a specific fasting time was instructed (e.g. "Did not exercise in the last 12 hours")           | Short structured item; can echo IPAQ intensity definitions                                              |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Alcohol intake in last 24 h                | 2        | Yes/No; rough units or category (none / 1--2 / 3--5 / \>5)                                                                                                       | AUDIT-C wording if more structure needed; alternatively an alcohol test can be done before each session |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Smoking / vaping today                     | 2--3     | Yes/No; approximate cigarettes/vapes since waking                                                                                                                | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Hormonal & reproductive (per session info) | Menstrual phase at session                 | 1        | Categorical (e.g. early follicular, late follicular, mid-luteal, perimenopausal, postmenopausal, unknown)                                                        | Derived from self-reported menstrual dates; optionally hormone assays                                   |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Pregnancy / breastfeeding status           | 2        | Yes/No; if Yes: notes                                                                                                                                            | Pregnancy tests can be done before each experiment/session when needed                                  |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Events & deviations                        | Acute events during session                | 1--2     | Free text (e.g. "felt faint at 20:10, paused", "strong emotional phone call at 21:00")                                                                           | End-of-session log entry                                                                                |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Bathroom visits                            | 2--3     | Times or time ranges; optional volume where measured                                                                                                             | Manually logged, useful for future detection of outside-lab/uncontrolled exposure times                 |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Food / drink provided                      | 2--3     | Type and energy content (kcal) if standardised                                                                                                                   | Study-specific (e.g. Huel Liquid Drink)                                                                 |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Required calories                          | 2--3     | Calculated kcal requirement via BMR equations                                                                                                                    | Formulas St. Jeor-Mifflin (Mifflin et al., 1990) or similar                                             |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Food / drink consumed                      | 2--3     | Estimated intake (kcal or %) + timing                                                                                                                            | Participant-specific                                                                                    |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Major protocol deviations                  | 1--2     | Free text (e.g. "session ended early", "CBT probe dislodged", "BP failed for 30 min")                                                                            | Protocol deviation form                                                                                 |
|                                            +--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                            | Free-text notes                            | 2        | Any other remarks that help interpret data                                                                                                                       | --                                                                                                      |
+--------------------------------------------+--------------------------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

: Table 11. Example session-level metadata schema, organised by group, tier, and typical data formats, with optional references to instruments or logging tools.

# CONTRIBUTION

## Community and community roles

This is the first version of the wiki. In future versions, the community structure and roles will be:

Author

Editor

Contributor

Reviewer

## List of contributors

**Bilge Kobas**

Bilge is a research associate...

**Someone Someone**

## Governance

The website will be updated every xx months

## How to cite

You can cite this work using the Zenodo doi xxx

We also have a methods paper xxx

## Contact

For collaboration requests, contact Bilge at bilge.kobas@tum.de.

# REFERENCES

Abbas-Hashemi, S.A., Hosseininasab, D., Rastgoo, S., Shiraseb, F., Asbaghi, O., 2023. The effects of caffeine supplementation on blood pressure in adults: A systematic review and dose-response meta-analysis. Clin. Nutr. ESPEN 58, 165--177. https://doi.org/10.1016/j.clnesp.2023.09.923

Abe, N., Kodama, H., 2015. Distal-proximal skin temperature gradient prior to sleep onset in infants for clinical use. Pediatrics International 57, 227--233. https://doi.org/10.1111/ped.12473

Adams, T., Wagner, S., Baldinger, M., Zellhuber, I., Weber, M., Nass, D., Surges, R., 2022. Accurate detection of heart rate using in-ear photoplethysmography in a clinical setting. Front. Digit. Health 4, 1--10. https://doi.org/10.3389/fdgth.2022.909519

Agelink, M.W., Majewski, T., Akila, F., Zeit, T., Ziegler, D., 2001. Standardized tests of Heart Rate Variability. Clinical Autonomic Research 11, 99--108.

Agostinelli, P.J., Linder, B.A., Frick, K.A., Bordonie, N.C., Neal, F.K., Sefton, J.E.M., 2023. Validity of heart rate derived core temperature estimation during simulated firefighting tasks. Sci. Rep. 13, 1--11. https://doi.org/10.1038/s41598-023-49929-x

Akbar, M., Wandy, A., Soraya, G.V., Goysal, Y., Lotisna, M., Basri, M.I., 2023. Sudomotor dysfunction in diabetic peripheral neuropathy (DPN) and its testing modalities: A literature review. Heliyon 9, e18184. https://doi.org/10.1016/j.heliyon.2023.e18184

Akselrod, S., Gordon, D., Ubel, F.A., Shannon, D.C., Berger, A.C., Cohen, R.J., 1981. Power Spectrum Analysis of Heart Rate Fluctuation: A Quantitative Probe of Beat-to-Beat Cardiovascular Control. Science (1979). 213, 220--222. https://doi.org/10.1126/science.6166045

Almeida, R.M.S.F., Barreira, E., Simões, M.L., Sousa, T.S.F., 2022. Infrared Thermography to Evaluate Thermal Comfort under Controlled Ambient Conditions. Applied Sciences (Switzerland) 12. https://doi.org/10.3390/app122312105

Alpert, B.S., Quinn, D., Gallick, D., 2014. Oscillometric blood pressure: A review for clinicians. Journal of the American Society of Hypertension 8, 930--938. https://doi.org/10.1016/j.jash.2014.08.014

Alvares, G.A., Quintana, D.S., Hickie, I.B., Guastella, A.J., 2016. Autonomic nervous system dysfunction in psychiatric disorders and the impact of psychotropic medications: A systematic review and meta-analysis. Journal of Psychiatry and Neuroscience 41, 89--104. https://doi.org/10.1503/jpn.140217

Andriessen, P., Schraa, O., van den Bosch-Ruis, W., Jan Ten Harkel, D., Settels, J.J., Oetomo, S.B., Blanco, C.E., 2008. Feasibility of Noninvasive Continuous Finger Arterial Blood Pressure Measurements in Very Young Children, Aged 0--4 Years. Pediatr. Res. 63, 691--696. https://doi.org/10.1203/PDR.0b013e31816c8fe3

Aoki, K., Kondo, N., Shibasaki, M., Takano, S., Tominaga, H., Katsuura, T., 1997. Circadian variation of sweating responses to passive heat stress. Acta Physiol. Scand. 161, 397--402. https://doi.org/10.1046/j.1365-201X.1997.d01-1981.x

Arens, E., Zhang, H., 2006. The skin's role in human thermoregulation and comfort, in: Thermal and Moisture Transport in Fibrous Materials. Elsevier, pp. 560--602. https://doi.org/10.1533/9781845692261.3.560

Armstrong, L.E., Casa, D.J., Millard-Stafford, M., Moran, D.S., Pyne, S.W., Roberts, W.O., 2007. Exertional heat illness during training and competition. Med. Sci. Sports Exerc. 39, 556--572. https://doi.org/10.1249/MSS.0b013e31802fa199

Athaya, T., Choi, S., 2022. A Review of Noninvasive Methodologies to Estimate the Blood Pressure Waveform. Sensors 22, 3953. https://doi.org/10.3390/s22103953

Aubert, A.E., Seps, B., Beckers, F., 2003. Heart Rate Variability in Athletes. Sports Medicine 33, 889--919. https://doi.org/10.2165/00007256-200333120-00003

Bach, Aaron J E, Stewart, I.B., Disher, A.E., Costello, J.T., 2015. A comparison between conductive and infrared devices for measuring mean skin temperature at rest, during exercise in the heat, and recovery. PLoS One 10, e0117907. https://doi.org/10.1371/journal.pone.0117907

Bach, Aaron J.E., Stewart, I.B., Minett, G.M., Costello, J.T., 2015. Does the technique employed for skin temperature assessment alter outcomes? A systematic review. Physiol. Meas. 36, R27--R51. https://doi.org/10.1088/0967-3334/36/9/R27

Baehr, E.K., Revelle, W., Eastman, C.I., 2000. Individual differences in the phase and amplitude of the human circadian temperature rhythm: with an emphasis on morningness--eveningness. J. Sleep Res. 9, 117--127. https://doi.org/10.1046/j.1365-2869.2000.00196.x

Baik, I., Kim, N.H., Kim, S.H., Shin, C., 2023. Association of blood pressure measurements in sitting, supine, and standing positions with the 10-year risk of mortality in Korean adults. Epidemiol. Health 45, e2023055. https://doi.org/10.4178/epih.e2023055

Baker, F.C., Driver, H.S., 2007. Circadian rhythms, sleep, and the menstrual cycle. Sleep Med. 8, 613--622. https://doi.org/10.1016/j.sleep.2006.09.011

Baker, F.C., Mitchell, D., Driver, H.S., 2001. Oral contraceptives alter sleep and raise body temperature in young women. Pflugers Arch. 442, 729--737. https://doi.org/10.1007/s004240100582

Baker, F.C., Siboza, F., Fuller, A., 2020a. Temperature regulation in women: Effects of the menstrual cycle. Temperature 7, 226--262. https://doi.org/10.1080/23328940.2020.1735927

Baker, L.B., 2019. Physiology of sweat gland function: The roles of sweating and sweat composition in human health. Temperature 6, 211--259. https://doi.org/10.1080/23328940.2019.1632145

Baker, L.B., Stofan, J.R., Hamilton, A.A., Horswill, C.A., 2009. Comparison of regional patch collection vs. whole body washdown for measuring sweat sodium and potassium loss during exercise. J. Appl. Physiol. 107, 887--895. https://doi.org/10.1152/japplphysiol.00197.2009

Baker, L.B., Ungaro, C.T., Barnes, K.A., Nuccio, R.P., Reimel, A.J., Stofan, J.R., 2014. Validity and reliability of a field technique for sweat Na+ and K+ analysis during exercise in a hot-humid environment. Physiol. Rep. 2. https://doi.org/10.14814/phy2.12007

Baker, L.B., Wolfe, A.S., 2020. Physiological mechanisms determining eccrine sweat composition. Eur. J. Appl. Physiol. 120, 719--752. https://doi.org/10.1007/s00421-020-04323-7

Bal, E., Harden, E., Lamb, D., Van Hecke, A.V., Denver, J.W., Porges, S.W., 2010. Emotion recognition in children with autism spectrum disorders: Relations to eye gaze and autonomic state. J. Autism Dev. Disord. 40, 358--370. https://doi.org/10.1007/s10803-009-0884-3

Bankir, L., Bochud, M., Maillard, M., Bovet, P., Gabriel, A., Burnier, M., 2008. Nighttime blood pressure and nocturnal dipping are associated with daytime urinary sodium excretion in African subjects. Hypertension 51, 891--898. https://doi.org/10.1161/HYPERTENSIONAHA.107.105510

Beauchaine, T.P., Thayer, J.F., 2015. Heart rate variability as a transdiagnostic biomarker of psychopathology. International Journal of Psychophysiology 98, 338--350. https://doi.org/10.1016/j.ijpsycho.2015.08.004

Benedek, M., Kaernbach, C., 2010a. A continuous measure of phasic electrodermal activity. J. Neurosci. Methods 190, 80--91. https://doi.org/10.1016/j.jneumeth.2010.04.028

Benedek, M., Kaernbach, C., 2010b. Decomposition of skin conductance data by means of nonnegative deconvolution. Psychophysiology 47, 647--658. https://doi.org/10.1111/j.1469-8986.2009.00972.x

Benjo, A.M., Jaramillo, V., Atassi, F., Nascimento, F., Benjo, J., Mahtta, D., Alviar, C., 2019. Acute Cardiovascular Effects of Energy Drinks in Healthy Subjects: a Meta-Analysis of Randomized Trials. J. Am. Coll. Cardiol. 73, 1883. https://doi.org/10.1016/s0735-1097(19)32489-1

Bernard, V., Staffa, E., Mornstein, V., Bourek, A., 2013. Infrared camera assessment of skin surface temperature - Effect of emissivity. Physica Medica 29, 583--591. https://doi.org/10.1016/j.ejmp.2012.09.003

Berntson, G.G., Stowell, J.R., 1998. ECG artifacts and heart period variability: Don't miss a beat! Psychophysiology 35, 127--132. https://doi.org/10.1017/S0048577298001541

Bijlenga, D., Van Someren, E.J.W., Gruber, R., Bron, T.I., Kruithof, I.F., Spanbroek, E.C.A., Kooij, J.J.S., 2013. Body temperature, activity and melatonin profiles in adults with attention-deficit/hyperactivity disorder and delayed sleep: A case-control study. J. Sleep Res. 22, 607--616. https://doi.org/10.1111/jsr.12075

Billman, G.E., 2013. The LF/HF ratio does not accurately measure cardiac sympatho-vagal balance. Front. Physiol. 4 FEB, 1--5. https://doi.org/10.3389/fphys.2013.00026

Boetcher, S.K.S., Sparrow, E.M., Dugay, M. V., 2009. Characteristics of direct-contact, skin-surface temperature sensors. Int. J. Heat Mass Transf. 52, 3799--3804. https://doi.org/10.1016/j.ijheatmasstransfer.2009.02.011

Bongers, C.C.W.G., Hopman, M.T.E., Eijsvogels, T.M.H., 2015. Using an ingestible telemetric temperature pill to assess gastrointestinal temperature during exercise. Journal of Visualized Experiments 2015, 1--9. https://doi.org/10.3791/53258

Bonnemeier, H., Wiegand, U.K.H., Brandes, A., Kluge, N., Katus, H.A., Richardt, G., Potratz, J., 2003. Circadian profile of cardiac autonomic nervous modulation in healthy subjects: Differing effects of aging and gender on heart rate variability. J. Cardiovasc. Electrophysiol. 14, 791--799. https://doi.org/10.1046/j.1540-8167.2003.03078.x

Boschi, F., Figini, V., Pagana, G., Visintin, M., Scholar, G., 2023. Optimized Cuffless Blood Pressure Measurement Using ECG , PPG and Linear Regression. https://doi.org/10.20944/preprints202312.0273.v1

Boucsein, W., 2012. Electrodermal Activity, 2nd ed. Springer US, Boston, MA. https://doi.org/10.1007/978-1-4614-1126-0

Boucsein, W., Fowles, D.C., Grimnes, S., Ben-Shakhar, G., Roth, W.T., Dawson, M.E., Filion, D.L., 2012. Publication recommendations for electrodermal measurements. Psychophysiology 49, 1017--1034. https://doi.org/10.1111/j.1469-8986.2012.01384.x

Braithwaite, J.J., Derrick, W.G., Jones, R., Rowe, M., 2015. A Guide for Analysing Electrodermal Activity (EDA) &amp; Skin Conductance Responses (SCRs) for Psychological Experiments. Birmingham, UK.

Bräuer, A., Fazliu, A., Perl, T., Heise, D., Meissner, K., Brandes, I.F., 2020. Accuracy of zero-heat-flux thermometry and bladder temperature measurement in critically ill patients. Sci. Rep. 10, 1--7. https://doi.org/10.1038/s41598-020-78753-w

Brooks, E.M., Morgan, A.L., Pierzga, J.M., Wladkowski, S.L., O'Gorman, J.T., Derr, J.A., Kenney, W.L., 1997. Chronic hormone replacement therapy alters thermoregulatory and vasomotor function in postmenopausal women. J. Appl. Physiol. 83, 477--484. https://doi.org/10.1152/jappl.1997.83.2.477

Brooks, T.G., Lahens, N.F., Grant, G.R., Sheline, Y.I., FitzGerald, G.A., Skarke, C., 2023. Diurnal rhythms of wrist temperature are associated with future disease risk in the UK Biobank. Nat. Commun. 14, 5172. https://doi.org/10.1038/s41467-023-40977-5

Brown, T.E., Beightol, L.A., Koh, J., Eckberg, D.L., 1993. Important influence of respiration on human R-R interval power spectra is largely ignored. J. Appl. Physiol. 75, 2310--2317. https://doi.org/10.1152/jappl.1993.75.5.2310

Bruce-Low, S.S., Cotterrell, D., Jones, G.E., 2006. Heart rate variability during high ambient heat exposure. Aviat. Space Environ. Med. 77, 915--20.

Buitelaar, J.K., van de Loo-Neus, G.H.H., Hennissen, L., Greven, C.U., Hoekstra, P.J., Nagy, P., Ramos-Quiroga, A., Rosenthal, E., Kabir, S., Man, K.K.C., IC, W., Coghill, D., Häge, A., Banaschewski, T., Inglis, S.K., Carucci, S., Danckaerts, M., Dittmann, R.W., Falissard, B., Garas, P., Hollis, C., Konrad, K., Kovshoff, H., Liddle, E., McCarthy, S., Neubert, A., Sonuga-Barke, E.J.S., Zuddas, A., 2022. Long-term methylphenidate exposure and 24-hours blood pressure and left ventricular mass in adolescents and young adults with attention deficit hyperactivity disorder. European Neuropsychopharmacology 64, 63--71. https://doi.org/10.1016/j.euroneuro.2022.09.001

Bull, F.C., Maslin, T.S., Armstrong, T., 2009. Global physical activity questionnaire (GPAQ): Nine country reliability and validity study. J. Phys. Act. Health 6, 790--804. https://doi.org/10.1123/jpah.6.6.790

Buono, M.J., Jechort, A., Marques, R., Smith, C., Welch, J., 2007. Comparison of infrared versus contact thermometry for measuring skin temperature during exercise in the heat. Physiol. Meas. 28, 855--859. https://doi.org/10.1088/0967-3334/28/8/008

Buono, M.J., Ulrich, R.L., 1998. Comparison of mean skin temperature using "covered" versus "uncovered" contact thermistors. Physiol. Meas. 19, 297--300. https://doi.org/10.1088/0967-3334/19/2/016

Buysse, D.J., Reynolds, C.F., Monk, T.H., Berman, S.R., Kupfer, D.J., 1989. The Pittsburgh sleep quality index: A new instrument for psychiatric practice and research. Psychiatry Res. 28, 193--213. https://doi.org/10.1016/0165-1781(89)90047-4

Byrne, C., Lim, C.L., 2007. The ingestible telemetric body core temperature sensor: A review of validity and exercise applications. Br. J. Sports Med. 41, 126--133. https://doi.org/10.1136/bjsm.2006.026344

Cameron, N.A., Blyler, C.A., Bello, N.A., 2023. Oral Contraceptive Pills and Hypertension: A Review of Current Evidence and Recommendations. Hypertension 80, 924--935. https://doi.org/10.1161/HYPERTENSIONAHA.122.20018

Candas, V., Libert, J.P., Vogt, J.J., 1979. Human skin wettedness and evaporative efficiency of sweating. J. Appl. Physiol. 46, 522--528. https://doi.org/10.1152/jappl.1979.46.3.522

Cao, R., Azimi, I., Sarhaddi, F., Niela-Vilen, H., Axelin, A., Liljeberg, P., Rahmani, A.M., 2022. Accuracy Assessment of Oura Ring Nocturnal Heart Rate and Heart Rate Variability in Comparison With Electrocardiography in Time and Frequency Domains: Comprehensive Analysis. J. Med. Internet Res. 24, 1--16. https://doi.org/10.2196/27487

Casiglia, E., Tikhonoff, V., Albertini, F., Palatini, P., 2016. Poor Reliability of Wrist Blood Pressure Self-Measurement at Home: A Population-Based Study. Hypertension 68, 896--903. https://doi.org/10.1161/HYPERTENSIONAHA.116.07961

Catai, A.M., Pastre, C.M., Godoy, M.F. de, Silva, E. da, Takahashi, A.C. de M., Vanderlei, L.C.M., 2020. Heart rate variability: are you using it properly? Standardisation checklist of procedures. Braz. J. Phys. Ther. 24, 91--102. https://doi.org/10.1016/j.bjpt.2019.02.006

Chalmers, J.A., Quintana, D.S., Abbott, M.J.A., Kemp, A.H., 2014. Anxiety disorders are associated with reduced heart rate variability: A meta-analysis. Front. Psychiatry 5, 1--11. https://doi.org/10.3389/fpsyt.2014.00080

Chandra, A., Neeland, I.J., Berry, J.D., Ayers, C.R., Rohatgi, A., Das, S.R., Khera, A., McGuire, D.K., De Lemos, J.A., Turer, A.T., 2014. The relationship of body mass and fat distribution with incident hypertension: Observations from the dallas heart study. J. Am. Coll. Cardiol. 64, 997--1002. https://doi.org/10.1016/j.jacc.2014.05.057

Chandrasekhar, A., Yavarimanesh, M., Hahn, J.O., Sung, S.H., Chen, C.H., Cheng, H.M., Mukkamala, R., 2019. Formulas to Explain Popular Oscillometric Blood Pressure Estimation Algorithms. Front. Physiol. 10, 1--14. https://doi.org/10.3389/fphys.2019.01415

Charkoudian, N., 2010. Mechanisms and modifiers of reflex induced cutaneous vasodilation and vasoconstriction in humans. J. Appl. Physiol. 109, 1221--1228. https://doi.org/10.1152/japplphysiol.00298.2010

Charkoudian, N., 2003. Skin blood flow in adult human thermoregulation: How it works, when it does not, and why. Mayo Clin. Proc. 78, 603--612. https://doi.org/10.4065/78.5.603

Charkoudian, N., Johnson, J.M., 1999. Reflex control of cutaneous vasoconstrictor system is reset by exogenous female reproductive hormones. J. Appl. Physiol. 87, 381--385. https://doi.org/10.1152/jappl.1999.87.1.381

Charkoudian, N., Johnson, J.M., 1997. Modification of active cutaneous vasodilation by oral contraceptive hormones. J. Appl. Physiol. 83, 2012--2018. https://doi.org/10.1152/jappl.1997.83.6.2012

Charkoudian, N., Stachenfeld, N., 2016. Sex hormone effects on autonomic mechanisms of thermoregulation in humans. Auton. Neurosci. 196, 75--80. https://doi.org/10.1016/j.autneu.2015.11.004

Charkoudian, N., Stachenfeld, N.S., 2014. Reproductive Hormone Influences on Thermoregulation in Women, in: Comprehensive Physiology. Wiley, pp. 793--804. https://doi.org/10.1002/cphy.c130029

Charlson, M.E., Carrozzino, D., Guidi, J., Patierno, C., 2022. Charlson Comorbidity Index: A Critical Review of Clinimetric Properties. Psychother. Psychosom. 91, 8--35. https://doi.org/10.1159/000521288

Cheshire, W.P., 2016. Thermoregulatory disorders and illness related to heat and cold stress. Auton. Neurosci. 196, 91--104. https://doi.org/10.1016/j.autneu.2016.01.001

Cheung, S.S., Sweeney, D.H., 2001. Influence of attachment method and clothing on skin temperature sensor accuracy. Med. Sci. Sports Exerc. 33, S161.

Cheuvront, S.N., Kenefick, R.W., 2014. Dehydration: Physiology, Assessment, and Performance Effects. Compr. Physiol. 4, 257--285. https://doi.org/10.1002/j.2040-4603.2014.tb00543.x

Chikhi, S., Matton, N., Blanchet, S., 2022. EEG power spectral measures of cognitive workload: A meta-analysis. Psychophysiology 59, 1--24. https://doi.org/10.1111/psyp.14009

Childs, C., Harrison, R., Hodkinson, C., 1999. Tympanic membrane temperature as a measure of core temperature. Arch. Dis. Child. 80, 262--266. https://doi.org/10.1136/adc.80.3.262

Cho, C.K., Lee, H.M., Yun, M.H., Lee, M.W., 1996. Development of a temperature control procedure for a room air-conditioner using the concept of just noticeable difference (JND) on thermal sensation, in: Proceedings of the Human Factors and Ergonomics Society Annual Meeting. pp. 473--477. https://doi.org/10.1177/154193129604000901

Choi, H.S., Myoung, H.S., Lee, H.K., Park, H.D., Lee, K.J., 2008. A new noise reduction method for oscillometric blood pressure measurement. Proceedings of the 30th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS'08 - "Personalized Healthcare through Technology" 5, 270--272. https://doi.org/10.1109/iembs.2008.4649142

Choi, J., Ghaffari, R., Baker, L.B., Rogers, J.A., 2018. Skin-interfaced systems for sweat collection and analytics. Sci. Adv. 4, 1--9. https://doi.org/10.1126/sciadv.aar3921

Choi, J., Kang, Y., Park, J., Joung, Y., Koo, C., 2023. Development of Real-Time Cuffless Blood Pressure Measurement Systems with ECG Electrodes and a Microphone Using Pulse Transit Time (PTT). Sensors 23, 1684. https://doi.org/10.3390/s23031684

Choi, J.K., Miki, K., Sagawa, S., Shiraki, K., 1997. Evaluation of mean skin temperature formulas by infrared thermography. Int. J. Biometeorol. 41, 68--75. https://doi.org/10.1007/s004840050056

Chong, P.L.H., Abel, E., Pao, R., McCormick, C.E.B., Schwichtenberg, A.J., 2021. Sleep Dysregulation and Daytime Electrodermal Patterns in Children With Autism: A Descriptive Study. Journal of Genetic Psychology 182, 335--347. https://doi.org/10.1080/00221325.2021.1911919

Coenen, A.J.R.M., Rompelman, O., Kitney, R.I., 1977. Measurement of heart-rate variability: Part 2-hardware digital device for the assessment of heart-rate variability. Med. Biol. Eng. Comput. 15, 423--430. https://doi.org/10.1007/BF02457997

Cohen, B., Cadesky, A., Jaggi, S., 2023. Dermatologic manifestations of thyroid disease: a literature review. Front. Endocrinol. (Lausanne). 14, 1--20. https://doi.org/10.3389/fendo.2023.1167890

Colin, J., Timbal, J., Houdas, Y., Boutelier, C., Guieu, J.D., 1971. Computation of mean body temperature from rectal and skin temperatures. J. Appl. Physiol. 31, 484--489. https://doi.org/10.1152/jappl.1971.31.3.484

Coull, N.A., West, A.M., Hodder, S.G., Wheeler, P., Havenith, G., 2021. Body mapping of regional sweat distribution in young and older males. Eur. J. Appl. Physiol. 121, 109--125. https://doi.org/10.1007/s00421-020-04503-5

Craig, J. V., Lancaster, G.A., Taylor, S., Williamson, P.R., Smyth, R.L., 2002. Infrared ear thermometry compared with rectal thermometry in children: A systematic review. Lancet 360, 603--609. https://doi.org/10.1016/S0140-6736(02)09783-0

Crandall, C.G., 2008. Heat stress and baroreflex regulation ofblood pressure. Med. Sci. Sports Exerc. 40, 2063--2070. https://doi.org/10.1249/MSS.0b013e318180bc98

Crandall, C.G., Etzel, R.A., Farr, D.B., 1999a. Cardiopulmonary baroreceptor control of muscle sympathetic nerve activity in heat-stressed humans. American Journal of Physiology-Heart and Circulatory Physiology 277, H2348--H2352. https://doi.org/10.1152/ajpheart.1999.277.6.H2348

Crandall, C.G., González‐Alonso, J., 2010. Cardiovascular function in the heat‐stressed human. Acta Physiologica 199, 407--423. https://doi.org/10.1111/j.1748-1716.2010.02119.x

Crandall, C.G., Levine, B.D., Etzel, R.A., 1999b. Effect of increasing central venous pressure during passive heating on skin blood flow. J. Appl. Physiol. 86, 605--610. https://doi.org/10.1152/jappl.1999.86.2.605

Crandall, C.G., Wilson, T.E., 2015. Human cardiovascular responses to passive heat stress. Compr. Physiol. https://doi.org/10.1002/cphy.c140015

Crawshaw, L.I., Nadel, E.R., Stolwijk, J.A.J., Stamford, B.A., 1975. Effect of local cooling on sweating rate and cold sensation. Pflugers Arch. 354, 19--27. https://doi.org/10.1007/BF00584500

Critchley, H.D., 2002. Review: Electrodermal Responses: What Happens in the Brain. The Neuroscientist 8, 132--142. https://doi.org/10.1177/107385840200800209

Cui, J., Shibasaki, M., Low, D.A., Keller, D.M., Davis, S.L., Crandall, C.G., 2010. Heat stress attenuates the increase in arterial blood pressure during the cold pressor test. J. Appl. Physiol. 109, 1354--1359. https://doi.org/10.1152/japplphysiol.00292.2010

Cui, J., Wilson, T.E., Crandall, C.G., 2002. Phenylephrine-induced elevations in arterial blood pressure are attenuated in heat-stressed humans. Am. J. Physiol. Regul. Integr. Comp. Physiol. 283, 1221--1226. https://doi.org/10.1152/ajpregu.00195.2002

Cuspidi, C., Sala, C., Tadic, M., Gherbesi, E., De Giorgi, A., Grassi, G., Mancia, G., 2017. Clinical and prognostic significance of a reverse dipping pattern on ambulatory monitoring: An updated review. J. Clin. Hypertens. 19, 713--721. https://doi.org/10.1111/jch.13023

Czeisler, C.A., Duffy, J.F., Shanahan, T.L., Brown, E.N., Mitchell, J.F., Rimmer, D.W., Ronda, J.M., Silva, E.J., Allan, J.S., Emens, J.S., Dijk, D.J., Kronauer, R.E., 1999. Stability, precision, and near-24-hour period of the human circadian pacemaker. Science (1979). 284, 2177--2181. https://doi.org/10.1126/science.284.5423.2177

Daanen, H.A.M., Racinais, S., Périard, J.D., 2018. Heat Acclimation Decay and Re-Induction: A Systematic Review and Meta-Analysis. Sports Medicine 48, 409--430. https://doi.org/10.1007/s40279-017-0808-x

D'Alessio, D.A., Kavle, E.C., Mozzoli, M.A., Smalley, K.J., Polansky, M., Kendrick, Z. V., Owen, L.R., Bushman, M.C., Boden, G., Owen, O.E., 1988. Thermic effect of food in lean and obese men. Journal of Clinical Investigation 81, 1781--1789. https://doi.org/10.1172/JCI113520

Datta, N.R., Marder, D., Datta, S., Meister, A., Puric, E., Stutz, E., Rogers, S., Eberle, B., Timm, O., Staruch, M., Riesterer, O., Bodis, S., 2021. Quantification of thermal dose in moderate clinical hyperthermia with radiotherapy: a relook using temperature--time area under the curve (AUC). International Journal of Hyperthermia 38, 296--307. https://doi.org/10.1080/02656736.2021.1875060

de Souza, I.S., Laporta, G.Z., Zangirolami-Raimundo, J., Sorpreso, I.C.E., Silva dos Santos, H.C.L., Soares Júnior, J.M., Raimundo, R.D., 2024. Association between the use of oral contraceptives and the occurrence of systemic hypertension: A systematic review with statistical comparison between randomized clinical trial interventions. Eur. J. Obstet. Gynecol. Reprod. Biol. X 22, 100307. https://doi.org/10.1016/j.eurox.2024.100307

Debray, A., Sardar, S., Deshayes, T.A., Mornas, A., Oubouchou, K., Ouazaa, Y., Gagnon, D., 2025. Sex-related differences in temperature regulation during heat stress from childhood to older age. Autonomic Neuroscience 260, 103294. https://doi.org/10.1016/j.autneu.2025.103294

Dell'Osso, L., Massoni, L., Battaglini, S., Cremone, I.M., Carmassi, C., Carpita, B., 2022. Biological correlates of altered circadian rhythms, autonomic functions and sleep problems in autism spectrum disorder. Ann. Gen. Psychiatry 21, 1--28. https://doi.org/10.1186/s12991-022-00390-6

Delsoglio, M., Achamrah, N., Berger, M.M., Pichard, C., 2019. Indirect calorimetry in clinical practice. J. Clin. Med. 8, 1--19. https://doi.org/10.3390/jcm8091387

Deng, F., Zhang, J., Jia, Y., 2020. A denoising strategy for the improvements of PPGi's signal-to-noise-ratio. J. Phys. Conf. Ser. 1607. https://doi.org/10.1088/1742-6596/1607/1/012088

Dervis, S., Coombs, G.B., Chaseling, G.K., Filingeri, D., Smoljanic, J., Jay, O., 2016. A comparison of thermoregulatory responses to exercise between mass-matched groups with large differences in body fat. J. Appl. Physiol. 120, 615--623. https://doi.org/10.1152/japplphysiol.00906.2015

Dial, M.B., Hollander, M.E., Vatne, E.A., Emerson, A.M., Edwards, N.A., Hagen, J.A., 2025. Validation of nocturnal resting heart rate and heart rate variability in consumer wearables. Physiol. Rep. 13, 1--13. https://doi.org/10.14814/phy2.70527

Diamond, A., Lye, C.T., Prasad, D., Abbott, D., 2021. One size does not fit all: Assuming the same normal body temperature for everyone is not justified. PLoS One 16, 1--13. https://doi.org/10.1371/journal.pone.0245257

Diaz, T., Strong, K.L., Cao, B., Guthold, R., Moran, A.C., Moller, A.B., Requejo, J., Sadana, R., Thiyagarajan, J.A., Adebayo, E., Akwara, E., Amouzou, A., Aponte Varon, J.J., Azzopardi, P.S., Boschi-Pinto, C., Carvajal, L., Chandra-Mouli, V., Crofts, S., Dastgiri, S., Dery, J.S., Elnakib, S., Fagan, L., Jane Ferguson, B., Fitzner, J., Friedman, H.S., Hagell, A., Jongstra, E., Kann, L., Chatterji, S., English, M., Glaziou, P., Hanson, C., Hosseinpoor, A.R., Marsh, A., Morgan, A.P., Munos, M.K., Noor, A., Pavlin, B.I., Pereira, R., Porth, T.A., Schellenberg, J., Siddique, R., You, D., Vaz, L.M.E., Banerjee, A., 2021. A call for standardised age-disaggregated health data. Lancet Healthy Longev. 2, e436--e443. https://doi.org/10.1016/S2666-7568(21)00115-X

Dijk, D.-J., Cajochen, C., Borbély, A.A., 1991. Effect of a single 3-hour exposure to bright light on core body temperature and sleep in humans. Neurosci. Lett. 121, 59--62. https://doi.org/10.1016/0304-3940(91)90649-E

Ding, X., Zhang, Y.-T., 2019. Pulse transit time technique for cuffless unobtrusive blood pressure measurement: from theory to algorithm. Biomed. Eng. Lett. 9, 37--52. https://doi.org/10.1007/s13534-019-00096-x

Donaldson, G.C., Scarborough, M., Mridha, K., Whelan, L., Caunce, M., Keatinge, W.R., 1996. Effect of posture on body temperature of young men in cold air. Eur. J. Appl. Physiol. Occup. Physiol. 73, 326--331. https://doi.org/10.1007/BF02425494

Drummond, P.D., 1995. Mechanisms of physiological gustatory sweating and flushing in the face. J. Auton. Nerv. Syst. 52, 117--124. https://doi.org/10.1016/0165-1838(94)00151-9

Drury, E.R., Wu, J., Gigliotti, J.C., Le, T.H., 2024. Sex differences in blood pressure regulation and hypertension: renal, hemodynamic, and hormonal mechanisms. Physiol. Rev. 104, 199--251. https://doi.org/10.1152/physrev.00041.2022

Edelberg, R., 1972. Electrical activity of the skin: Its measurement and uses in psychophysiology, in: Greenfield, N.S., Sternbach, R.A. (Eds.), Handbook of Psychophysiology. Holt, Rinehart & Winston, New York, p. 1011.

El-Farhan, N., Rees, D.A., Evans, C., 2017. Measuring cortisol in serum, urine and saliva -- are our assays good enough? Ann. Clin. Biochem. 54, 308--322. https://doi.org/10.1177/0004563216687335

Elkounni, A., Vellei, M., Le Dréau, J., Schweiker, M., Inard, C., 2025. Acute effect of light and time of day on thermal physiology, perception, and behavior. Sci. Rep. 15, 38640. https://doi.org/10.1038/s41598-025-22542-w

Faurholt-Jepsen, M., Kessing, L.V., Munkholm, K., 2017. Heart rate variability in bipolar disorder: A systematic review and meta-analysis. Neurosci. Biobehav. Rev. 73, 68--80. https://doi.org/10.1016/j.neubiorev.2016.12.007

Fernández-Cuevas, I., Bouzas Marins, J.C., Arnáiz Lastras, J., Gómez Carmona, P.M., Piñonosa Cano, S., García-Concepción, M.Á., Sillero-Quintana, M., 2015. Classification of factors influencing the use of infrared thermography in humans: A review. Infrared Phys. Technol. 71, 28--55. https://doi.org/10.1016/j.infrared.2015.02.007

Filippone, E.J., Foy, A.J., Naccarelli, G. V., 2023. Controversies in Hypertension III: Dipping, Nocturnal Hypertension, and the Morning Surge. American Journal of Medicine 136, 629--637. https://doi.org/10.1016/j.amjmed.2023.02.018

Fiore, M., Bianconi, A., Sicari, G., Conni, A., Lenzi, J., Tomaiuolo, G., Zito, F., Golinelli, D., Sanmarchi, F., 2024. The Use of Smart Rings in Health Monitoring---A Meta-Analysis. Applied Sciences (Switzerland) 14, 1--18. https://doi.org/10.3390/app142310778

Foerster, F., Smeja, M., Fahrenberg, J., 1999. Detection of posture and motion by accelerometry: a validation study in ambulatory monitoring. Comput. Human Behav. 15, 571--583. https://doi.org/10.1016/S0747-5632(99)00037-0

Fortin, J., Rogge, D.E., Fellner, C., Flotzinger, D., Grond, J., Lerche, K., Saugel, B., 2021. A novel art of continuous noninvasive blood pressure measurement. Nat. Commun. 12, 1387. https://doi.org/10.1038/s41467-021-21271-8

Franzese, F., Hettiarachchi, P., Holtermann, A., Ahmadi, M., Johansson, P.J., 2025. Comparing Physical Activity Metrics From Different Placements of Thigh-Worn Accelerometers. J. Meas. Phys. Behav. 8, 1--15. https://doi.org/10.1123/jmpb.2024-0043

Freedman, R.R., 2014. Menopausal Related Hot flashes: Mechanisms, Endocrinology and Treatment. J Steroid Biochem Mol Biol 142, 115--120. https://doi.org/10.1016/j.jsbmb.2013.08.010.MENOPAUSAL

Freedman, R.R., Blacker, C.M., 2002. Estrogen raises the sweating threshold in postmenopausal women with hot flashes. Fertil. Steril. 77, 487--490. https://doi.org/10.1016/S0015-0282(01)03009-6

Freedman, R.R., Krell, W., 1999. Reduced thermoregulatory null zone in postmenopausal women with hot flashes. Am. J. Obstet. Gynecol. 181, 66--70. https://doi.org/10.1016/S0002-9378(99)70437-0

Fuller, D., Colwell, E., Low, J., Orychock, K., Ann Tobin, M., Simango, B., Buote, R., van Heerden, D., Luan, H., Cullen, K., Slade, L., Taylor, N.G.A., 2020. Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review. JMIR Mhealth Uhealth 8, 1--23. https://doi.org/10.2196/18694

Gagge, A.P., Nishi, Y., 1977. Heat Exchange Between Human Skin Surface and Thermal Environment, in: Comprehensive Physiology. Wiley, pp. 69--92. https://doi.org/10.1002/cphy.cp090105

Gagge, A.P., Stolwijk, J.A.J., Hardy, J.D., 1967. Comfort and thermal sensations and associated physiological responses at various ambient temperatures. Environ. Res. 1, 1--20. https://doi.org/10.1016/0013-9351(67)90002-3

Gagnon, D., Crandall, C.G., Kenny, G.P., 2013a. Sex differences in postsynaptic sweating and cutaneous vasodilation. J. Appl. Physiol. 114, 394--401. https://doi.org/10.1152/japplphysiol.00877.2012

Gagnon, D., Jay, O., Kenny, G.P., 2013b. The evaporative requirement for heat balance determines whole‐body sweat rate during exercise under conditions permitting full evaporation. J. Physiol. 591, 2925--2935. https://doi.org/10.1113/jphysiol.2012.248823

Gagnon, D., Jay, O., Lemire, B., Kenny, G.P., 2008. Sex-related differences in evaporative heat loss: The importance of metabolic heat production. Eur. J. Appl. Physiol. 104, 821--829. https://doi.org/10.1007/s00421-008-0837-0

Gagnon, D., Kenny, G.P., 2012a. Sex differences in thermoeffector responses during exercise at fixed requirements for heat loss. J. Appl. Physiol. 113, 746--757. https://doi.org/10.1152/japplphysiol.00637.2012

Gagnon, D., Kenny, G.P., 2012b. Does sex have an independent effect on thermoeffector responses during exercise in the heat? Journal of Physiology 590, 5963--5973. https://doi.org/10.1113/jphysiol.2012.240739

Gagnon, D., Lemire, B.B., Jay, O., Kenny, G.P., 2010. Aural canal, esophageal, and rectal temperatures during exertional heat stress and the subsequent recovery period. J. Athl. Train. 45, 157--163. https://doi.org/10.4085/1062-6050-45.2.157

Gamelin, F.X., Berthoin, S., Bosquet, L., 2006. Validity of the polar S810 Heart rate monitor to measure R-R intervals at rest. Med. Sci. Sports Exerc. 38, 887--893. https://doi.org/10.1249/01.mss.0000218135.79476.9c

Garrett, A.T., Goosens, N.G., Rehrer, N.G., Patterson, M.J., Cotter, J.D., 2009. Induction and decay of short-term heat acclimation. Eur. J. Appl. Physiol. 107, 659--670. https://doi.org/10.1007/s00421-009-1182-7

Garrido, M., Saccardo, D., De Rui, M., Vettore, E., Verardo, A., Carraro, P., Di Vitofrancesco, N., Mani, A.R., Angeli, P., Bolognesi, M., Montagnese, S., 2017. Abnormalities in the 24-hour rhythm of skin temperature in cirrhosis: Sleep-wake and general clinical implications. Liver International 37, 1833--1842. https://doi.org/10.1111/liv.13525

Georgiou, K., Larentzakis, A. V., Khamis, N.N., Alsuhaibani, G.I., Alaska, Y.A., Giallafos, E.J., 2018. Can Wearable Devices Accurately Measure Heart Rate Variability? A Systematic Review. Folia Med. (Plovdiv). 60, 7--20. https://doi.org/10.2478/folmed-2018-0012

Gerrett, N., Griggs, K., Redortier, B., Voelcker, T., Kondo, N., Havenith, G., 2018. Sweat from gland to skin surface: production, transport, and skin absorption. J. Appl. Physiol. 125, 459--469. https://doi.org/10.1152/japplphysiol.00872.2017

Giersch, G.E.W., Charkoudian, N., 2025. Regulation of body temperature and blood pressure in women: Mechanisms and implications for heat illness risk. Exp. Physiol. 110, 196--199. https://doi.org/10.1113/EP091455

Giles, D., Draper, N., Neil, W., 2016. Validity of the Polar V800 heart rate monitor to measure RR intervals at rest. Eur. J. Appl. Physiol. 116, 563--571. https://doi.org/10.1007/s00421-015-3303-9

Ginty, A.T., Tyra, A.T., Young, D.A., Brindle, R.C., de Rooij, S.R., Williams, S.E., 2022. Cardiovascular reactions to acute psychological stress and academic achievement. Psychophysiology 59, 1--14. https://doi.org/10.1111/psyp.14064

Glacet, R., Reynaud, E., Robin-Choteau, L., Reix, N., Hugueny, L., Ruppert, E., Geoffroy, P.A., Kilic-Huck, Ü., Comtet, H., Bourgin, P., 2023. A comparison of four methods to estimate dim light melatonin onset: a repeatability and agreement study. Chronobiol. Int. 40, 123--131. https://doi.org/10.1080/07420528.2022.2150554

Glaser, D.A. nna, Glaser, K., 2015. Use of Systemic Therapies to Manage Focal Hyperhidrosis. Mo. Med. 112, 287--291.

Goldstein, D.S., Bentho, O., Park, M.Y., Sharabi, Y., 2011. Low-frequency power of heart rate variability is not a measure of cardiac sympathetic tone but may be a measure of modulation of cardiac autonomic outflows by baroreflexes. Exp. Physiol. 96, 1255--1261. https://doi.org/10.1113/expphysiol.2010.056259

Gombert-Labedens, M., Vesterdorf, K., Fuller, A., Maloney, S.K., Baker, F.C., 2025. Effects of menopause on temperature regulation. Temperature 12, 92--132. https://doi.org/10.1080/23328940.2025.2484499

González‐Alonso, J., Crandall, C.G., Johnson, J.M., 2008. The cardiovascular challenge of exercising in the heat. J. Physiol. 586, 45--53. https://doi.org/10.1113/jphysiol.2007.142158

Gorgolewski, K.J., Auer, T., Calhoun, V.D., Craddock, R.C., Das, S., Duff, E.P., Flandin, G., Ghosh, S.S., Glatard, T., Halchenko, Y.O., Handwerker, D.A., Hanke, M., Keator, D., Li, X., Michael, Z., Maumet, C., Nichols, B.N., Nichols, T.E., Pellman, J., Poline, J.-B., Rokem, A., Schaefer, G., Sochat, V., Triplett, W., Turner, J.A., Varoquaux, G., Poldrack, R.A., 2016. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. Sci. Data 3, 160044. https://doi.org/10.1038/sdata.2016.44

Greaney, J.L., Alexander, L.M., Kenney, W.L., 2015. Sympathetic control of reflex cutaneous vasoconstriction in human aging. J. Appl. Physiol. 119, 771--782. https://doi.org/10.1152/japplphysiol.00527.2015

Greenes, D.S., Fleisher, G.R., 2004. When body temperature changes, does rectal temperature lag? Journal of Pediatrics 144, 824--826. https://doi.org/10.1016/j.jpeds.2004.02.037

Gregoire, J., Tuck, S., Yamamoto, Y., Hughson, R.L., 1996. Heart Rate Variability at Rest and Exercise: Influence of Age, Gender, and Physical Training. Canadian Journal of Applied Physiology 21, 455--470. https://doi.org/10.1139/h96-040

Grisaru, S., Yue, M.W., Mah, J.C., Hamiwka, L.A., 2013. Ambulatory blood pressure monitoring in a cohort of children referred with suspected hypertension: Characteristics of children with and without attention deficit hyperactivity disorder. Int. J. Hypertens. 2013. https://doi.org/10.1155/2013/419208

Gronwald, T., Schaffarczyk, M., Reinsberger, C., Hoos, O., 2024. Heart Rate Variability -- Methods and Analysis in Sports Medicine and Exercise Science. Dtsch. Z. Sportmed. 75, 113--118. https://doi.org/10.5960/dzsm.2024.595

Grucza, R., Pekkarinen, H., Titov, E.-K., Kononoff, A., Haenninen, O., 1993. Influence of the menstrual cycle and oral contraceptives on thermoregulatory responses to exercise in young women. Eur. J. Appl. Physiol. Occup. Physiol. 67, 279--285. https://doi.org/10.1007/BF00864229

Gualberto, P.I.B., Benvindo, V. V, Waclawovsky, G., Deresz, L.F., 2024. Acute effects of energy drink consumption on cardiovascular parameters in healthy adults: a systematic review and meta-analysis of randomized clinical trials. Nutr. Rev. 82, 1028--1045. https://doi.org/10.1093/nutrit/nuad112

Gupta, N., Frank, S.M., Ghoneim, N., El-Rahmany, H.K., Talamini, M.A., Zacur, H.A., Raja, S.N., 2000. Thermoregulation and hormone replacement in postmenopausal women. J. Therm. Biol. 25, 165--169. https://doi.org/10.1016/S0306-4565(99)00053-4

Habek, M., Andabaka, M., Fanciulli, A., Brecl Jakob, G., Drulović, J., Leys, F., Di Pauli, F., Hegen, H., Auer, M., Pekmezović, T., Mesaroš, Š., Jovičević, V., Junaković, A., Wenning, G.K., Deisenhammer, F., Gabelić, T., Barun, B., Adamec, I., Krbot Skorić, M., 2022. Sudomotor dysfunction in people with neuromyelitis optica spectrum disorders. Eur. J. Neurol. 29, 2772--2780. https://doi.org/10.1111/ene.15413

Handrakis, J.P., Trbovich, M., Hagen, E.M., Price, M., 2017. Thermodysregulation in persons with spinal cord injury: case series on use of the autonomic standards. Spinal Cord 3, 1--7. https://doi.org/10.1038/S41394-017-0026-7

Hardy, J.D., Du Bois, E.F., Soderstrom, G.F., 1938. The Technic of Measuring Radiation and Convection. J. Nutr. 15, 461--475. https://doi.org/10.1093/jn/15.5.461

Harker, M., 2013. Psychological Sweating: A Systematic Review Focused on Aetiology and Cutaneous Response. Skin Pharmacol. Physiol. 26, 92--100. https://doi.org/10.1159/000346930

Hasselberg, M.J., McMahon, J., Parker, K., 2013. The validity, reliability, and utility of the iButton® for measurement of body temperature circadian rhythms in sleep/wake research. Sleep Med. 14, 5--11. https://doi.org/10.1016/j.sleep.2010.12.011

Havenith, G., 2001. Individualized model of human thermoregulation for the simulation of heat stress response. J. Appl. Physiol. 90, 1943--1954. https://doi.org/10.1152/jappl.2001.90.5.1943

Havenith, G., van Middendorp, H., 1990. The relative influence of physical fitness, acclimatization state, anthropometric measures and gender on individual reactions to heat stress. Eur. J. Appl. Physiol. Occup. Physiol. 61, 419--427. https://doi.org/10.1007/BF00236062

He, J., Liu, Yanchen, Wu, H., Liu, Yanni, 2025. Association of Facial Infrared Thermography with Thermal Comfort and Cognitive Performance in Summer Indoor Environments. Energy and Built Environment. https://doi.org/10.1016/j.enbenv.2025.10.003

Heilman, K.J., Porges, S.W., 2007. Accuracy of the LifeShirt® (Vivometrics) in the detection of cardiac rhythms. Biol. Psychol. 75, 300--305. https://doi.org/10.1016/j.biopsycho.2007.04.001

Henry, B., Merz, M., Hoang, H., Abdulkarim, G., Wosik, J., Schoettker, P., 2024. Cuffless Blood Pressure in clinical practice: challenges, opportunities and current limits. Blood Press. 33. https://doi.org/10.1080/08037051.2024.2304190

Henry, B.L., Minassian, A., Paulus, M.P., Geyer, M.A., Perry, W., 2010. Heart rate variability in bipolar mania and schizophrenia. J. Psychiatr. Res. 44, 168--176. https://doi.org/10.1016/j.jpsychires.2009.07.011

Hermida, R.C., Ayala, D.E., Portaluppi, F., 2007. Circadian variation of blood pressure: The basis for the chronotherapy of hypertension. Adv. Drug Deliv. Rev. 59, 904--922. https://doi.org/10.1016/j.addr.2006.08.003

Hernández-Vicente, A., Hernando, D., Marín-Puyalto, J., Vicente-Rodríguez, G., Garatachea, N., Pueyo, E., Bailón, R., 2021. Validity of the Polar H7 Heart Rate Sensor for Heart Rate Variability Analysis during Exercise in Different Age, Body Composition and Fitness Level Groups. Sensors 21, 902. https://doi.org/10.3390/s21030902

Hernando, D., Roca, S., Sancho, J., Alesanco, Á., Bailón, R., 2018. Validation of the Apple Watch for Heart Rate Variability Measurements during Relax and Mental Stress in Healthy Subjects. Sensors 18, 2619. https://doi.org/10.3390/s18082619

Hibi, M., Kubota, C., Mizuno, T., Aritake, S., Mitsui, Y., Katashima, M., Uchida, S., 2017. Effect of shortened sleep on energy expenditure, core body temperature, and appetite: a human randomised crossover trial. Sci. Rep. 7, 39640. https://doi.org/10.1038/srep39640

Hinde, K., White, G., Armstrong, N., 2021. Wearable devices suitable for monitoring twenty four hour heart rate variability in military populations. Sensors (Switzerland) 21, 1--20. https://doi.org/10.3390/s21041061

Hinderliter, A.L., Routledge, F.S., Blumenthal, J.A., Koch, G., Hussey, M.A., Wohlgemuth, W.K., Sherwood, A., 2013. Reproducibility of blood pressure dipping: Relation to day-to-day variability in sleep quality. Journal of the American Society of Hypertension 7, 432--439. https://doi.org/10.1016/j.jash.2013.06.001

Hirsch, J.A., Bishop, B., 1981. Respiratory sinus arrhythmia in humans: How breathing pattern modulates heart rate. Am. J. Physiol. Heart Circ. Physiol. 10, 620--629. https://doi.org/10.1152/ajpheart.1981.241.4.h620

Hirshoren, N., Tzoran, I., Makrienko, I., Edoute, Y., Plawner, M.M., Itskovitz-Eldor, J., Jacob, G., Center, R.M., 2002. Menstrual cycle effects on the neurohumoral and autonomic nervous systems regulating the cardiovascular system. Journal of Clinical Endocrinology and Metabolism 87, 1569--1575. https://doi.org/10.1210/jcem.87.4.8406

Hjortskov, N., Rissen, D., Blangsted, A.K., Fallentin, N., Lundberg, U., Sogaard, K., 2004. The effect of mental stress on heart rate variability and blood pressure during computer work. Eur. J. Appl. Physiol. 92, 84--89. https://doi.org/10.1007/s00421-004-1055-z

Ho, A.V.T., Toska, K., Wesche, J., 2020. Rapid, Large, and Synchronous Sweat and Cardiovascular Responses Upon Minor Stimuli in Healthy Subjects. Dynamics and Reproducibility. Front. Neurol. 11, 1--10. https://doi.org/10.3389/fneur.2020.00051

Hoit, J.D., Lohmeier, H.L., 2000. Influence of Continuous Speaking on Ventilation. Journal of Speech, Language, and Hearing Research 43, 1240--1251. https://doi.org/10.1044/jslhr.4305.1240

Holowatz, L.A., Kenney, W.L., 2010. Peripheral mechanisms of thermoregulatory control of skin blood flow in aged humans. J. Appl. Physiol. 109, 1538--1544. https://doi.org/10.1152/japplphysiol.00338.2010

Holzman, J.B., Bridgett, D.J., 2017. Heart rate variability indices as bio-markers of top-down self-regulatory mechanisms: A meta-analytic review. Neurosci. Biobehav. Rev. 74, 233--255. https://doi.org/10.1016/j.neubiorev.2016.12.032

Horne, J.A., Ostberg, O., 1976. A self-assessment questionnaire to determine morningness-eveningness in human circadian rhythms. Int. J. Chronobiol. 4, 97--110.

Hossain, M.-B., Kong, Y., Posada-Quintero, H.F., Chon, K.H., 2022. Comparison of Electrodermal Activity from Multiple Body Locations Based on Standard EDA Indices' Quality and Robustness against Motion Artifact. Sensors 22, 3177. https://doi.org/10.3390/s22093177

Houdas, Y., Ring, E.F.J., 1982. Temperature Distribution, in: Houdas, Y., Ring, E.F.J. (Eds.), Human Body Temperature. Springer US, Boston, MA, pp. 81--103. https://doi.org/10.1007/978-1-4899-0345-7_5

Hu, J.R., Martin, G., Iyengar, S., Kovell, L.C., Plante, T.B., Helmond, N. van, Dart, R.A., Brady, T.M., Turkson-Ocran, R.A.N., Juraschek, S.P., 2023. Validating cuffless continuous blood pressure monitoring devices. Cardiovasc. Digit. Health J. 4, 9--20. https://doi.org/10.1016/j.cvdhj.2023.01.001

Huang, C.J., Chan, H.L., Chang, Y.J., Chen, S.M., Hsu, M.J., 2021. Validity of the polar v800 monitor for assessing heart rate variability in elderly adults under mental stress and dual task conditions. Int. J. Environ. Res. Public Health 18, 1--12. https://doi.org/10.3390/ijerph18030869

Huggins, R., Glaviano, N., Negishi, N., Casa, D.J., Hertel, J., 2012. Comparison of rectal and aural core body temperature thermometry in hyperthermic, exercising individuals: A meta-analysis. J. Athl. Train. 47, 329--338. https://doi.org/10.4085/1062-6050-47.3.09

Huikuri, H. V., Kessler, K.M., Terracall, E., Castellanos, A., Linnaluoto, M.K., Myerburg, R.J., 1990. Reproducibility and circadian rhythm of heart rate variability in healthy subjects. Am. J. Cardiol. 65, 391--393. https://doi.org/10.1016/0002-9149(90)90308-N

Huikuri, H. V., Pikkuja¨msa¨, S.M., Airaksinen, K.E.J., Ika¨heimo, M.J., Rantala, A.O., Kauma, H., Lilja, M., Kesa¨niemi, Y.A., 1996. Sex-Related Differences in Autonomic Modulation of Heart Rate in Middle-aged Subjects. Circulation 94, 122--125. https://doi.org/10.1161/01.CIR.94.2.122

Hunt, A.P., Bach, A.J.E., Borg, D.N., Costello, J.T., Stewart, I.B., 2017. The Systematic Bias of Ingestible Core Temperature Sensors Requires a Correction by Linear Regression. Front. Physiol. 8, 1--7. https://doi.org/10.3389/fphys.2017.00260

Hunt, L.A., Hospers, L., Smallcombe, J.W., Mavros, Y., Jay, O., 2021. Caffeine alters thermoregulatory responses to exercise in the heat only in caffeine-habituated individuals: A double-blind placebo-controlled trial. J. Appl. Physiol. 131, 1300--1310. https://doi.org/10.1152/japplphysiol.00172.2021

Hymczak, H., Gołąb, A., Mendrala, K., Plicner, D., Darocha, T., Podsiadło, P., Hudziak, D., Gocoł, R., Kosiński, S., 2021. Core temperature measurement---principles of correct measurement, problems, and complications. Int. J. Environ. Res. Public Health 18. https://doi.org/10.3390/ijerph182010606

Imeraj, L., Sonuga-Barke, E., Antrop, I., Roeyers, H., Wiersema, R., Bal, S., Deboutte, D., 2012. Altered circadian profiles in attention-deficit/hyperactivity disorder: An integrative review and theoretical framework for future studies. Neurosci. Biobehav. Rev. 36, 1897--1919. https://doi.org/10.1016/j.neubiorev.2012.04.007

Ingall, T.J., McLeod, J.G., O'Brien, P.C., 1990. The effect of ageing on autonomic nervous system function. Aust. N. Z. J. Med. 20, 570--577. https://doi.org/10.1111/j.1445-5994.1990.tb01315.x

Inoue, Y., Gerrett, N., Ichinose-Kuwahara, T., Umino, Y., Kiuchi, S., Amano, T., Ueda, H., Havenith, G., Kondo, N., 2016. Sex differences in age-related changes on peripheral warm and cold innocuous thermal sensitivity. Physiol. Behav. 164, 86--92. https://doi.org/10.1016/j.physbeh.2016.05.045

Inoue, Y., Havenith, G., Kenney, W.L., Loomis, J.L., Buskirk, E.R., 1999. Exercise- and methylcholine-induced sweating responses in older and younger men: Effect of heat acclimation and aerobic fitness. Int. J. Biometeorol. 42, 210--216. https://doi.org/10.1007/s004840050107

Ioannou, S., Morris, P., Mercer, H., Baker, M., Gallese, V., Reddy, V., 2014. Proximity and gaze influences facial temperature: A thermal infrared imaging study. Front. Psychol. 5, 1--12. https://doi.org/10.3389/fpsyg.2014.00845

Irving, G., Holden, J., Stevens, R., McManus, R.J., 2016. Which cuff should I use? Indirect blood pressure measurement for the diagnosis of hypertension in patients with obesity: a diagnostic accuracy review. BMJ Open 6, e012429. https://doi.org/10.1136/bmjopen-2016-012429

Islam, S.M.S., Chow, C.K., Daryabeygikhotbehsara, R., Subedi, N., Rawstorn, J., Tegegne, T., Karmakar, C., Siddiqui, M.U., Lambert, G., Maddison, R., 2022. Wearable cuffless blood pressure monitoring devices: A systematic review and meta-Analysis. European Heart Journal - Digital Health 3, 323--337. https://doi.org/10.1093/ehjdh/ztac021

ISO, 2019. Non-invasive sphygmomanometers---Part 2: Clinical investigation of the intermittent automated measurement type. AAMI. https://doi.org/10.2345/9781570207228.ch1

ISO, 2004. ISO 9886:2004 Ergonomics --- Evaluation of thermal strain by physiological measurements. Geneva.

Israel, S.L., Schneller, O., 1950. The Thermogenic Property of Progesterone. Fertil. Steril. https://doi.org/10.1016/s0015-0282(16)30066-8

Iwen, K.A., Oelkrug, R., Brabant, G., 2018. Effects of thyroid hormones on thermogenesis and energy partitioning. J. Mol. Endocrinol. 60, R157--R170. https://doi.org/10.1530/JME-17-0319

Jacquot, C.M.C., Schellen, L., Kingma, B.R., van Baak, M.A., Van Marken Lichtenbelt, W.D., 2014. Influence of thermophysiology on thermal behavior: The essentials of categorization. Physiol. Behav. 128, 180--187. https://doi.org/10.1016/j.physbeh.2014.01.025

James, C.A., Richardson, A.J., Watt, P.W., Maxwell, N.S., 2014. Reliability and validity of skin temperature measurement by telemetry thermistors and a thermal camera during exercise in the heat. J. Therm. Biol. 45, 141--149. https://doi.org/10.1016/j.jtherbio.2014.08.010

Jarczok, M.N., Jarczok, M., Mauss, D., Koenig, J., Li, J., Herr, R.M., Thayer, J.F., 2013. Autonomic nervous system activity and workplace stressors---A systematic review. Neurosci. Biobehav. Rev. 37, 1810--1823. https://doi.org/10.1016/j.neubiorev.2013.07.004

Jarrin, D.C., Gv, Q.C., Mcgrath, J.J., West, S.S., Hb, Q.C., Poirier, P., Séguin, L., Tremblay, R.E., Ste-justine, D.R.C.H.U., 2015. Short-Term Heart Rate Variability in a Population-Based Sample of 10-Year-Old Children. Pediatr. Cardiol. 36, 41--48. https://doi.org/10.1007/s00246-014-0962-y.Short-Term

Jarrin, D.C., McGrath, J.J., Giovanniello, S., Poirier, P., Lambert, M., 2012. Measurement fidelity of heart rate variability signal processing: The devil is in the details. International Journal of Psychophysiology 86, 88--97. https://doi.org/10.1016/j.ijpsycho.2012.07.004

Jensen-Urstad, K., Storck, N., Bouvier, F., Ericson, M., Lindblad, L.E., Jensen-Urstad, M., 1997. Heart rate variability in healthy subjects is related to age and gender. Acta Physiol. Scand. 160, 235--241. https://doi.org/10.1046/j.1365-201X.1997.00142.x

Johnson, J.M., Kellogg, D.L., 2010. Local thermal control of the human cutaneous circulation. J. Appl. Physiol. 109, 1229--1238. https://doi.org/10.1152/japplphysiol.00407.2010

Jose, A.D., Collison, D., 1970. The normal range and determinants of the intrinsic heart rate in man. Cardiovasc. Res. 4, 160--167. https://doi.org/10.1093/cvr/4.2.160

Juliana, N., Maluin, S.M., Effendy, N.M., Abu, I.F., Azmani, S., 2025. Cortisol Detection Methods and the Hormone's Role in Evaluating Circadian Rhythm Disruption. Int. J. Mol. Sci. 26, 1--17. https://doi.org/10.3390/ijms26189141

Kakaletsis, N., Ntaios, G., Milionis, H., Karagiannaki, A., Chouvarda, I., Dourliou, V., Ladakis, I., Kaiafa, G., Vemmos, K., Savopoulos, C., 2023. Midday Dipping and Circadian Blood Pressure Patterns in Acute Ischemic Stroke. J. Clin. Med. 12. https://doi.org/10.3390/jcm12144816

Kalinkov, K., Markova, V., Ganchev, T., 2020. Heart Rate Variability calculation methods, in: Proceedings of the International Conference on Biomedical Innovations and Applications, BIA 2020. pp. 97--100. https://doi.org/10.1109/BIA50171.2020.9244285

Karlsson, A.K., 2006. Autonomic dysfunction in spinal cord injury: Clinical presentation of symptoms and signs. Prog. Brain Res. 152, 1--8. https://doi.org/10.1016/S0079-6123(05)52034-X

Kawakami, S., Sato, H., Sasaki, A.T., Tanabe, H.C., Yoshida, Y., Saito, M., Toyoda, H., Sadato, N., Kang, Y., 2016. The brain mechanisms underlying the perception of pungent taste of capsaicin and the subsequent autonomic responses. Front. Hum. Neurosci. 9, 1--16. https://doi.org/10.3389/fnhum.2015.00720

Kelechi, T.J., Good, A., Mueller, M., 2011. Agreement and repeatability of an infrared thermometer. J. Nurs. Meas. 19, 55--64. https://doi.org/10.1891/1061-3749.19.1.55

Kellogg, D.L., Liu, Y., Kosiba, I.F., O'Donnell, D., 1999. Role of nitric oxide in the vascular effects of local warming of the skin in humans. J. Appl. Physiol. 86, 1185--1190. https://doi.org/10.1152/jappl.1999.86.4.1185

Kelly, G., 2006. Body temperature variability (Part 1): a review of the history of body temperature and its variability due to site selection, biological rhythms, fitness, and aging. Alternative Medicine Review 11, 278--293.

Kemp, A.H., Quintana, D.S., Felmingham, K.L., Matthews, S., Jelinek, H.F., 2012. Depression, comorbid anxiety disorders, and heart rate variability in physically healthy, unmedicated patients: Implications for cardiovascular risk. PLoS One 7, 1--8. https://doi.org/10.1371/journal.pone.0030777

Kemp, A.H., Quintana, D.S., Gray, M.A., Felmingham, K.L., Brown, K., Gatt, J.M., 2010. Impact of Depression and Antidepressant Treatment on Heart Rate Variability: A Review and Meta-Analysis. Biol. Psychiatry 67, 1067--1074. https://doi.org/10.1016/j.biopsych.2009.12.012

Kenefick, R.W., 2018. Drinking Strategies: Planned Drinking Versus Drinking to Thirst. Sports Medicine 48, 31--37. https://doi.org/10.1007/s40279-017-0844-6

Kenefick, R.W., Cheuvront, S.N., 2016. Physiological adjustments to hypohydration: Impact on thermoregulation. Auton. Neurosci. 196, 47--51. https://doi.org/10.1016/j.autneu.2016.02.003

Kenefick, R.W., Cheuvront, S.N., Elliott, L.D., Ely, B.R., Sawka, M.N., 2012. Biological and analytical variation of the human sweating response: Implications for study design and analysis. Am. J. Physiol. Regul. Integr. Comp. Physiol. 302, 252--258. https://doi.org/10.1152/ajpregu.00456.2011

Kennaway, D.J., 2023. The dim light melatonin onset across ages, methodologies, and sex and its relationship with morningness/eveningness. Sleep 46, 1--14. https://doi.org/10.1093/sleep/zsad033

Kenney, W.L., Craighead, D.H., Alexander, L.M., 2014. Heat Waves, Aging, and Human Cardiovascular Health. Med. Sci. Sports Exerc. 46, 1891--1899. https://doi.org/10.1249/MSS.0000000000000325

Kenney, W.L., Munce, T.A., 2003. Aging and human temperature regulation. J. Appl. Physiol. 95, 2598--2603. https://doi.org/10.1152/japplphysiol.00202.2003

Kenney, W.L., Wolf, S.T., Dillon, G.A., Berry, C.W., Alexander, L.M., 2021. Temperature regulation during exercise in the heat: Insights for the aging athlete. J. Sci. Med. Sport 24, 739--746. https://doi.org/10.1016/j.jsams.2020.12.007

Kenny, G.P., 2010. Human thermoregulation: separating thermal and nonthermal effects on heat loss. Frontiers in Bioscience 15, 259. https://doi.org/10.2741/3620

Kenny, G.P., Sigal, R.J., McGinn, R., 2016. Body temperature regulation in diabetes. Temperature 3, 119--145. https://doi.org/10.1080/23328940.2015.1131506

Kenny, G.P., Yardley, J., Brown, C., Sigal, R.J., Jay, O., 2010. Heat stress in older individuals and patients with common chronic diseases. CMAJ. Canadian Medical Association Journal 182, 1053--1060. https://doi.org/10.1503/cmaj.081050

Kent, L., O'Neill, B., Davison, G., Nevill, A., Stuart Elborn, J., Bradley, J.M., 2009. Validity and reliability of cardiorespiratory measurements recorded by the LifeShirt during exercise tests. Respir. Physiol. Neurobiol. 167, 162--167. https://doi.org/10.1016/j.resp.2009.03.013

Kerkhof, G.A., Van Dongen, H.P.A., 1996. Morning-type and evening-type individuals differ in the phase position of their endogenous circadian oscillator. Neurosci. Lett. 218, 153--156. https://doi.org/10.1016/S0304-3940(96)13140-2

Kiers, H.D., Hofstra, J.M., Wetzels, J.F.M., 2008. Oscillometric blood pressure measurements: Differences between measured and calculated mean arterial pressure. Netherlands Journal of Medicine 66, 474--479.

Kim, H.-L., 2023. Arterial stiffness and hypertension. Clin. Hypertens. 29, 1--9. https://doi.org/10.1186/s40885-023-00258-1

Kim, J., Ku, B., Bae, J.H., Han, G.C., Kim, J.U., 2018. Contrast in the circadian behaviors of an electrodermal activity and bioimpedance spectroscopy. Chronobiol. Int. https://doi.org/10.1080/07420528.2018.1486852

Kirby, N. V., Notley, S.R., Meade, R.D., Richards, B.J., Kenny, G.P., 2022. Menstrual Cycle Modulates the Contribution of Dry Heat Loss to Total Heat Loss During Exercise in Warm‐Dry Conditions in Young, Recreationally Active Females: Preliminary Findings. The FASEB Journal 36. https://doi.org/10.1096/fasebj.2022.36.S1.R5592

Kistler, A., Mariauzouls, C., Von Berlepsch, K., 1998. Fingertip temperature as an indicator for sympathetic responses. International Journal of Psychophysiology 29, 35--41. https://doi.org/10.1016/S0167-8760(97)00087-1

Kitamura, K.I., Zhu, X., Chen, W., Nemoto, T., 2010. Development of a new method for the noninvasive measurement of deep body temperature without a heater. Med. Eng. Phys. 32, 1--6. https://doi.org/10.1016/j.medengphy.2009.09.004

Kitney, R.I.;, Rompelman, O., 1980. The Study of heart-rate variability. Clarendon Press, Oxford.

Kleiger, R.E., Miller, J.P., Bigger, J.T., Moss, A.J., 1987. Decreased heart rate variability and its association with increased mortality after acute myocardial infarction. Am. J. Cardiol. 59, 256--262. https://doi.org/10.1016/0002-9149(87)90795-8

Klous, L., De Ruiter, C., Alkemade, P., Daanen, H., Gerrett, N., 2020. Sweat rate and sweat composition during heat acclimation. J. Therm. Biol. 93, 102697. https://doi.org/10.1016/j.jtherbio.2020.102697

Koh, A., Kang, D., Xue, Y., Lee, S., Pielak, R.M., Kim, J., Hwang, T., Min, S., Banks, A., Bastien, P., Manco, M.C., Wang, L., Ammann, K.R., Jang, K., Won, P., Han, S., Ghaffari, R., Paik, U., Slepian, M.J., Balooch, G., Huang, Y., Rogers, J.A., 2016. A soft, wearable microfluidic device for the capture, storage, and colorimetric sensing of sweat. Sci. Transl. Med. 8. https://doi.org/10.1126/scitranslmed.aaf2593

Kondo, N., Takano, S., Aoki, K., Shibasaki, M., Tominaga, H., Inoue, Y., 1998. Regional differences in the effect of exercise intensity on thermoregulatory sweating and cutaneous vasodilation. Acta Physiol. Scand. 164, 71--78. https://doi.org/10.1046/j.1365-201X.1998.00407.x

Kräuchi, K., 2002. How is the circadian rhythm of core body temperature regulated? Clinical Autonomic Research 12, 147--149. https://doi.org/10.1007/s10286-002-0043-9

Kräuchi, K., Cajochen, C., Werth, E., Wirz-Justice, A., 2000. Functional link between distal vasodilation and sleep-onset latency? Am. J. Physiol. Regul. Integr. Comp. Physiol. 278, 741--748. https://doi.org/10.1152/ajpregu.2000.278.3.r741

Kräuchi, K., Cajochen, C., Werth, E., Wirz-Justice, A., 1999. Warm feet promote the rapid onset of sleep. Nature 401, 36--37. https://doi.org/10.1038/43366

Kräuchi, K., Cajochen, C., Wirz-Justice, A., 1997. A relationship between heat loss and sleepiness: Effects of postural change and melatonin administration. J. Appl. Physiol. 83, 134--139. https://doi.org/10.1152/jappl.1997.83.1.134

Kräuchi, K., Wirz-Justice, A., 2001. Circadian clues to sleep onset mechanisms. Neuropsychopharmacology 25, S92--S96. https://doi.org/10.1016/S0893-133X(01)00315-3

Kräuchi, K., Wirz-Justice, A., 1994. Circadian rhythm of heat production, heart rate , and skin and core temperature under unmasking conditions in men. Am. J. Physiol. 267, R819-29. https://doi.org/http://dx.doi.org/10.1152/ajpregu.1994.267.3.R819

Kumar, R., Dubey, P.K., Zafer, A., Kumar, A., Yadav, S., 2021. Past, present and future of blood pressure measuring instruments and their calibration. Measurement (Lond). 172, 108845. https://doi.org/10.1016/j.measurement.2020.108845

Kumar, S., Yadav, S., Kumar, A., 2024. Blood pressure measurement techniques, standards, technologies, and the latest futuristic wearable cuff-less know-how. Sensors & Diagnostics 3, 181--202. https://doi.org/10.1039/D3SD00201B

Kuwabara, K., Mochida, T., Nagano, K., Shimakura, K., 2006. Fundamental Study of Weighting Factors for Calculating Mean Skin Temperature. J. Hum. Environ. Syst. 9, 35--42. https://doi.org/10.1618/jhes.9.35

Laborde, S., Mosley, E., Thayer, J.F., 2017. Heart Rate Variability and Cardiac Vagal Tone in Psychophysiological Research -- Recommendations for Experiment Planning, Data Analysis, and Data Reporting. Front. Psychol. 08, 1--18. https://doi.org/10.3389/fpsyg.2017.00213

Ladouce, S., Pietzker, M., Manzey, D., Dehais, F., 2024. Evaluation of a headphones-fitted EEG system for the recording of auditory evoked potentials and mental workload assessment. Behavioural Brain Research 460, 114827. https://doi.org/10.1016/j.bbr.2023.114827

Lahiri, B.B., Bagavathiappan, S., Jayakumar, T., Philip, J., 2012. Medical applications of infrared thermography: A review. Infrared Phys. Technol. 55, 221--235. https://doi.org/10.1016/j.infrared.2012.03.007

Lan, L., Xia, L., Tang, J., Wyon, D.P., Liu, H., 2019. Mean skin temperature estimated from 3 measuring points can predict sleeping thermal sensation. Build. Environ. 162, 106292. https://doi.org/10.1016/j.buildenv.2019.106292

Laskawi, R., Ellies, M., Röodel, R., Schoenebeck, C., 1999. Gustatory sweating: Clinical implications and etiologic aspects. Journal of Oral and Maxillofacial Surgery 57, 642--648. https://doi.org/10.1016/S0278-2391(99)90420-2

Laurent, S., Boutouyrie, P., 2020. Arterial Stiffness and Hypertension in the Elderly. Front. Cardiovasc. Med. 7, 1--13. https://doi.org/10.3389/fcvm.2020.544302

Lawford, B.R., Barnes, M., Connor, J.P., Heslop, K., Nyst, P., Young, R.M.D., 2012. Alcohol use disorders identification test (AUDIT) scores are elevated in antipsychotic-induced hyperprolactinaemia. Journal of Psychopharmacology 26, 324--329. https://doi.org/10.1177/0269881110393051

Lee, P.H., Macfarlane, D.J., Lam, T., Stewart, S.M., 2011. Validity of the international physical activity questionnaire short form (IPAQ-SF): A systematic review. International Journal of Behavioral Nutrition and Physical Activity 8, 115. https://doi.org/10.1186/1479-5868-8-115

Lee, S.M.C., Jon Williams, W., Fortney Schneider, S.M., 2000. Core temperature measurement during supine exercise: Esophageal, rectal, and intestinal temperatures. Aviat. Space Environ. Med. 71, 939--945.

Lefrant, J.Y., Muller, L., Emmanuel Coussaye, J., Benbabaali, M., Lebris, C., Zeitoun, N., Mari, C., Saïssi, G., Ripart, J., Eledjam, J.J., 2003. Temperature measurement in intensive care patients: Comparison of urinary bladder, oesophageal, rectal, axillary, and inguinal methods versus pulmonary artery core method. Intensive Care Med. 29, 414--418. https://doi.org/10.1007/s00134-002-1619-5

Lei, T.H., Cotter, J.D., Schlader, Z.J., Stannard, S.R., Perry, B.G., Barnes, M.J., Mündel, T., 2019. On exercise thermoregulation in females: interaction of endogenous and exogenous ovarian hormones. Journal of Physiology 597, 71--88. https://doi.org/10.1113/JP276233

Lei, T.H., Stannard, S.R., Perry, B.G., Schlader, Z.J., Cotter, J.D., Mündel, T., 2017. Influence of menstrual phase and arid vs. humid heat stress on autonomic and behavioural thermoregulation during exercise in trained but unacclimated women. Journal of Physiology 595, 2823--2837. https://doi.org/10.1113/JP273176

Leicht, A.S., Hirning, D.A., Allen, G.D., 2003. Heart rate variability and endogenous sex hormones during the menstrual cycle in young women. Exp. Physiol. 88, 441--446. https://doi.org/10.1113/eph8802535

Leite, N.N., Cota, B.C., Gotine, A.R.E.M., Rocha, D.M.U.P., Pereira, P.F., Hermsdorff, H.H.M., 2021. Visceral adiposity index is positively associated with blood pressure: A systematic review. Obes. Res. Clin. Pract. 15, 546--556. https://doi.org/10.1016/j.orcp.2021.10.001

Lewy, A.J., Sack, R.L., 1989. The dim light melatonin onset as a marker for orcadian phase position. Chronobiol. Int. 6, 93--102. https://doi.org/10.3109/07420528909059144

Li, H., Yang, Y., Liu, Q., Liu, L., Zhang, G., Zhang, X., Yin, M., Cao, Y., 2024. The Effects of Caffeine on Exercise in Hot Environments: A Bibliometric Study. Nutrients 16. https://doi.org/10.3390/nu16213692

Liao, W.-C., Landis, C.A., Lentz, M.J., Chiu, M.-J., 2005. Effect of foot bathing on distal-proximal skin temperature gradient in elders. Int. J. Nurs. Stud. 42, 717--722. https://doi.org/10.1016/j.ijnurstu.2004.11.011

Lipponen, J.A., Tarvainen, M.P., 2019. A robust algorithm for heart rate variability time series artefact correction using novel beat classification. J. Med. Eng. Technol. 43, 173--181. https://doi.org/10.1080/03091902.2019.1640306

Lipsitz, L.A., Mietus, J., Moody, G.B., Goldberger, A.L., 1990. Spectral characteristics of heart rate variability before and during postural tilt: Relations to aging and risk of syncope. Circulation 81, 1803--1810. https://doi.org/10.1161/01.cir.81.6.1803

Liu, C.C., Kuo, T.B.J., Yang, C.C.H., 2003. Effects of estrogen on gender-related autonomic differences in humans. Am. J. Physiol. Heart Circ. Physiol. 285, 2188--2193. https://doi.org/10.1152/ajpheart.00256.2003

Liu, W., Lian, Z., Deng, Q., Liu, Y., 2011. Evaluation of calculation methods of mean skin temperature for use in thermal comfort study. Build. Environ. 46, 478--488. https://doi.org/10.1016/j.buildenv.2010.08.011

Livingstone, S.D., Nolan, R.W., Frim, J., Reed, L.D., Limmer, R.E., 1987. A thermographic study of the effect of body composition and ambient temperature on the accuracy of mean skin temperature calculations. Eur. J. Appl. Physiol. Occup. Physiol. 56, 120--125. https://doi.org/10.1007/BF00696387

Low, D.A., Jones, H., Cable, N.T., Alexander, L.M., Kenney, W.L., 2020. Historical reviews of the assessment of human cardiovascular function: interrogation and understanding of the control of skin blood flow. Eur. J. Appl. Physiol. 120, 1--16. https://doi.org/10.1007/s00421-019-04246-y

Low, D.A., Keller, D.M., Wingo, J.E., Brothers, R.M., Crandall, C.G., 2011. Sympathetic nerve activity and whole body heat stress in humans. J. Appl. Physiol. https://doi.org/10.1152/japplphysiol.00498.2011

Low, P.A., 2004. Evaluation of sudomotor function. Clinical Neurophysiology 115, 1506--1513. https://doi.org/10.1016/j.clinph.2004.01.023

Lu, G., Yang, F., Taylor, J.A., Stein, J.F., 2009. A comparison of photoplethysmography and ECG recording to analyse heart rate variability in healthy subjects. J. Med. Eng. Technol. 33, 634--641. https://doi.org/10.3109/03091900903150998

Lugade, V., Fortune, E., Morrow, M., Kaufman, K., 2014. Validity of using tri-axial accelerometers to measure human movement-Part I: Posture and movement detection. Med. Eng. Phys. 36, 169--176. https://doi.org/10.1016/j.medengphy.2013.06.005

Luo, Q., Li, N., Zhu, Q., Yao, X., Wang, M., Heizhati, M., Cai, X., Hu, J., Abulimiti, A., Yao, L., Li, X., Gan, L., 2023. Non-dipping blood pressure pattern is associated with higher risk of new-onset diabetes in hypertensive patients with obstructive sleep apnea: UROSAH data. Front. Endocrinol. (Lausanne). 14, 1--13. https://doi.org/10.3389/fendo.2023.1083179

Mackowiak, P.A., Wasserman, S.S., Levine, M.M., 1992. A Critical Appraisal of 98.6°F, the Upper Limit of the Normal Body Temperature, and Other Legacies of Carl Reinhold August Wunderlich. JAMA: The Journal of the American Medical Association 268, 1578--1580. https://doi.org/10.1001/jama.1992.03490120092034

MacRae, B.A., Annaheim, S., Spengler, C.M., Rossi, R.M., 2018. Skin temperature measurement using contact thermometry: A systematic review of setup variables and their effects on measured values. Front. Physiol. 9, 1--24. https://doi.org/10.3389/fphys.2018.00029

Madhu, S., Alam, M.S., Ramasamy, S., Choi, J., 2025. Wearable, fabric-based microfluidic systems with integrated electrochemical and colorimetric sensing array for multiplex sweat analysis. Chemical Engineering Journal 504, 158979. https://doi.org/10.1016/j.cej.2024.158979

Makowski, D., Pham, T., Lau, Z.J., Brammer, J.C., Lespinasse, F., Pham, H., Schölzel, C., Chen, S.H.A., 2021. NeuroKit2: A Python toolbox for neurophysiological signal processing. Behav. Res. Methods 53, 1689--1696. https://doi.org/10.3758/s13428-020-01516-y

Maley, M.J., Hunt, A.P., Bach, A.J., Eglin, C.M., Costello, J.T., 2020. Infrared cameras overestimate skin temperature during rewarming from cold exposure. J. Therm. Biol. 91, 102614. https://doi.org/10.1016/j.jtherbio.2020.102614

Maniar, N., Bach, A.J.E., Stewart, I.B., Costello, J.T., 2015. The effect of using different regions of interest on local and mean skin temperature. J. Therm. Biol. 49--50, 33--38. https://doi.org/10.1016/j.jtherbio.2015.01.008

Maqsood, S., Xu, S., Springer, M., Mohawesh, R., Salameh, H.B., Gheewala, S., 2025. Temporal attention to estimate continuous blood pressure using photoplethysmography signals. Cluster Comput. 28. https://doi.org/10.1007/s10586-025-05185-4

Mariano, I.M., Amaral, A.L., Ribeiro, P.A.B., Puga, G.M., 2023. Exercise training improves blood pressure reactivity to stress: a systematic review and meta-analysis. Sci. Rep. 13, 10962. https://doi.org/10.1038/s41598-023-38041-9

Marins, J.C.B., Formenti, D., Costa, C.M.A., De Andrade Fernandes, A., Sillero-Quintana, M., 2015. Circadian and gender differences in skin temperature in militaries by thermography. Infrared Phys. Technol. 71, 322--328. https://doi.org/10.1016/j.infrared.2015.05.008

Martinez-Tellez, B., Ortiz-Alvarez, L., Sanchez-Delgado, G., Xu, H., Acosta, F.M., Merchan-Ramirez, E., Muñoz-Hernandez, V., Martinez-Avila, W.D., Contreras-Gomez, M.A., Gil, A., Labayen, I., Ruiz, J.R., 2019. Skin temperature response to a liquid meal intake is different in men than in women. Clinical Nutrition 38, 1339--1347. https://doi.org/10.1016/j.clnu.2018.05.026

Martinez-Tellez, B., Sanchez-Delgado, G., Acosta, F.M., Alcantara, J.M.A., Boon, M.R., Rensen, P.C.N., Ruiz, J.R., 2017. Differences between the most used equations in BAT-human studies to estimate parameters of skin temperature in young lean men. Sci. Rep. 7, 1--12. https://doi.org/10.1038/s41598-017-10444-5

Martin-Rincon, M., Calbet, J.A.L., 2020. Progress Update and Challenges on VO2max Testing and Interpretation. Front. Physiol. 11, 1--8. https://doi.org/10.3389/fphys.2020.01070

Masaoka, S., Lev-Ran, A., Hill, L.R., Vakil, G., Hon, E.H., 1985. Heart rate variability in diabetes: Relationship to age and duration of the disease. Diabetes Care 8, 64--68. https://doi.org/10.2337/diacare.8.1.64

Matsukawa, T., Ozaki, M., Nishiyama, T., Imamura, M., Kumazawa, T., 2000. Comparison of infrared thermometer with thermocouple for monitoring skin temperature. Crit. Care Med. 28, 532--536. https://doi.org/10.1097/00003246-200002000-00041

Matthews, K.A., Katholi, C.R., McCreath, H., Whooley, M.A., Williams, D.R., Zhu, S., Markovitz, J.H., 2004. Blood pressure reactivity to psychological stress predicts hypertension in the CARDIA study. Circulation 110, 74--78. https://doi.org/10.1161/01.CIR.0000133415.37578.E4

Maxim Integrated Products, 2015. DS1922L DS1922T iButton Temperature Loggers with 8KB Datalog Memory DS1922L / DS1922T iButton Temperature Loggers with 8KB Datalog Memory Absolute Maximum Ratings.

Mchill, A.W., Smith, B.J., Wright, K.P., 2014. Effects of caffeine on skin and core temperatures, alertness, and recovery sleep during circadian misalignment. J. Biol. Rhythms 29, 131--143. https://doi.org/10.1177/0748730414523078

Meidert, A.S., Saugel, B., 2018. Techniques for Non-Invasive Monitoring of Arterial Blood Pressure. Front. Med. (Lausanne). 4, 1--6. https://doi.org/10.3389/fmed.2017.00231

Mekjavic, I.B., Rempel, M.E., 1990. Determination of esophageal probe insertion length based on standing and sitting height. J. Appl. Physiol. 69, 376--379. https://doi.org/10.1152/jappl.1990.69.1.376

Melanson, E.L., Freedson, P.S., 2001. The effect of endurance training on resting heart rate variability in sedentary adult males. Eur. J. Appl. Physiol. 85, 442--449. https://doi.org/10.1007/s004210100479

Melville, S., Teskey, R., Philip, S., Simpson, J.A., Lutchmedial, S., Brunt, K.R., 2018. A comparison and calibration of a wrist-worn blood pressure monitor for patient management: Assessing the reliability of innovative blood pressure devices. J. Med. Internet Res. 20, 1--13. https://doi.org/10.2196/jmir.8009

Mesas, A.E., Leon-Muñoz, L.M., Rodriguez-Artalejo, F., Lopez-Garcia, E., 2011. The effect of coffee on blood pressure and cardiovascular disease in hypertensive individuals: A systematic review and meta-analysis. American Journal of Clinical Nutrition 94, 1113--1126. https://doi.org/10.3945/ajcn.111.016667

Michels, N., Clays, E., De Buyzere, M., Huybrechts, I., Marild, S., Vanaelst, B., De Henauw, S., Sioen, I., 2013. Determinants and reference values of short-term heart rate variability in children. Eur. J. Appl. Physiol. 113, 1477--1488. https://doi.org/10.1007/s00421-012-2572-9

Michlig, S., Merlini, J.M., Beaumont, M., Ledda, M., Tavenard, A., Mukherjee, R., Camacho, S., Le Coutre, J., 2016. Effects of TRP channel agonist ingestion on metabolism and autonomic nervous system in a randomized clinical trial of healthy subjects. Sci. Rep. 6, 1--12. https://doi.org/10.1038/srep20795

Mifflin, M., St Jeor, S., Hill, L., Scott, B., Daugherty, S., Koh, Y., 1990. A new predictive equation for resting energy expenditure in healthy individuals. Am. J. Clin. Nutr. 51, 241--247. https://doi.org/10.1093/ajcn/51.2.241

Miller, K.C., Hughes, L.E., Long, B.C., Adams, W.M., Casa, D.J., 2017. Validity of core temperature measurements at 3 rectal depths during rest, exercise, cold-water immersion, and recovery. J. Athl. Train. 52, 332--338. https://doi.org/10.4085/1062-6050-52.2.10

Minson, C.T., Halliwill, J.R., Young, T.M., Joyner, M.J., 2000a. Influence of the menstrual cycle on sympathetic activity, baroreflex sensitivity, and vascular transduction in young women. Circulation 101, 862--868. https://doi.org/10.1161/01.CIR.101.8.862

Minson, C.T., Halliwill, J.R., Young, T.M., Joyner, M.J., 2000b. Sympathetic activity and baroreflex sensitivity in young women taking oral contraceptives. Circulation 102, 1473--1476. https://doi.org/10.1161/01.CIR.102.13.1473

Minson, C.T., Wladkowski, S.L., Cardell, A.F., Pawelczyk, J.A., Kenney, W.L., 1998. Age alters the cardiovascular response to direct passive heating. J. Appl. Physiol. 84, 1323--1332. https://doi.org/10.1152/jappl.1998.84.4.1323

Mitchell, D., Wyndham, C.H., 1969. Comparison of weighting formulas for calculating mean skin temperature. J. Appl. Physiol. 26, 616--622. https://doi.org/10.1152/jappl.1969.26.5.616

Mochida, T., 1983. Mean Skin Temperature Weighted by Skin Area, Heat Transfer Coefficients and Thermal Sensitivity. Bulletin of the Faculty of Engineering Hokkaido University 115.

Monahan, K.D., 2007. Effect of aging on baroreflex function in humans. Am. J. Physiol. Regul. Integr. Comp. Physiol. 293. https://doi.org/10.1152/ajpregu.00031.2007

Montalescot, G., Sechtem, U., Achenbach, S., Andreotti, F., Arden, C., Budaj, A., Bugiardini, R., Crea, F., Cuisset, T., Di Mario, C., Ferreira, J.R., Gersh, B.J., Gitt, A.K., Hulot, J.S., Marx, N., Opie, L.H., Pfisterer, M., Prescott, E., Ruschitzka, F., Sabaté, M., Senior, R., Taggart, D.P., Van Der Wall, E.E., Vrints, C.J.M., Zamorano, J.L., Baumgartner, H., Bax, J.J., Bueno, H., Dean, V., Deaton, C., Erol, C., Fagard, R., Ferrari, R., Hasdai, D., Hoes, A.W., Kirchhof, P., Knuuti, J., Kolh, P., Lancellotti, P., Linhart, A., Nihoyannopoulos, P., Piepoli, M.F., Ponikowski, P., Sirnes, P.A., Tamargo, J.L., Tendera, M., Torbicki, A., Wijns, W., Windecker, S., Valgimigli, M., Claeys, M.J., Donner-Banzhoff, N., Frank, H., Funck-Brentano, C., Gaemperli, O., Gonzalez-Juanatey, J.R., Hamilos, M., Husted, S., James, S.K., Kervinen, K., Kristensen, S.D., Maggioni, A. Pietro, Romeo, F., Rydén, L., Simoons, M.L., Steg, P.G., Timmis, A., Yildirir, A., 2013. 2013 ESC guidelines on the management of stable coronary artery disease. Eur. Heart J. 34, 2949--3003. https://doi.org/10.1093/eurheartj/eht296

Mora, S.J., Sprowls, M., Tipparaju, V. V., Wheatley-Guy, C.M., Kulick, D., Johnson, B., Xiaojun, X., Forzani, E., 2021. Comparative study of a novel portable indirect calorimeter to a reference breath-by-breath instrument and its use in telemedicine settings. Clin. Nutr. ESPEN 46, 361--366. https://doi.org/10.1016/j.clnesp.2021.09.731

Moreira, D.G., Costello, J.T., Brito, C.J., Adamczyk, J.G., Ammer, K., Bach, A.J.E., Costa, C.M.A., Eglin, C., Fernandes, A.A., Fernández-Cuevas, I., Ferreira, J.J.A., Formenti, D., Fournet, D., Havenith, G., Howell, K., Jung, A., Kenny, G.P., Kolosovas-Machuca, E.S., Maley, M.J., Merla, A., Pascoe, D.D., Priego Quesada, J.I., Schwartz, R.G., Seixas, A.R.D., Selfe, J., Vainer, B.G., Sillero-Quintana, M., 2017. Thermographic imaging in sports and exercise medicine: A Delphi study and consensus statement on the measurement of human skin temperature. J. Therm. Biol. 69, 155--162. https://doi.org/10.1016/j.jtherbio.2017.07.006

Morris, N.B., Cramer, M.N., Hodder, S.G., Havenith, G., Jay, O., 2013. A comparison between the technical absorbent and ventilated capsule methods for measuring local sweat rate. J. Appl. Physiol. 114, 816--823. https://doi.org/10.1152/japplphysiol.01088.2012

Morrissey, M.C., Wu, Y., Zuk, E.F., Livingston, J., Casa, D.J., Pescatello, L.S., 2021. The impact of body fat on thermoregulation during exercise in the heat: A systematic review and meta-analysis. J. Sci. Med. Sport 24, 843--850. https://doi.org/10.1016/j.jsams.2021.06.004

Mukkamala, R., Stergiou, G.S., Avolio, A.P., 2022. Cuffless Blood Pressure Measurement. Annu. Rev. Biomed. Eng. 24, 203--230. https://doi.org/10.1146/annurev-bioeng-110220-014644

Mündel, T., 2020. Thermoregulatory sweating and evaporative heat loss during exercise: is the whole greater than the sum of its parts? Journal of Physiology 598, 2535--2536. https://doi.org/10.1113/JP279944

Muntner, P., Shimbo, D., Carey, R.M., Charleston, J.B., Gaillard, T., Misra, S., Myers, M.G., Ogedegbe, G., Schwartz, J.E., Townsend, R.R., Urbina, E.M., Viera, A.J., White, W.B., Wright, J.T., 2019. Measurement of Blood Pressure in Humans: A Scientific Statement From the American Heart Association. Hypertension 73, E35--E66. https://doi.org/10.1161/HYP.0000000000000087

Myers, C.W., Cohen, M.A., Eckberg, D.L., Taylor, J.A., 2001. A model for the genesis of arterial pressure Mayer waves from heart rate and sympathetic activity. Autonomic Neuroscience 91, 62--75. https://doi.org/10.1016/S1566-0702(01)00289-2

Nadel, E R, Bullard, R.W., Stolwijk, J.A., 1971. Importance of skin temperature in the regulation of sweating. J. Appl. Physiol. 31, 80--87. https://doi.org/10.1152/jappl.1971.31.1.80

Nadel, E.R., Fortney, S.M., Wenger, C.B., 1980. Effect of hydration state on circulatory and thermal regulations. J. Appl. Physiol. Respir. Environ. Exerc. Physiol. 49, 715--721. https://doi.org/10.1152/jappl.1980.49.4.715

Nadel, E. R., Mitchell, J.W., Saltin, B., Stolwijk, J.A., 1971. Peripheral modifications to the central drive for sweating. J. Appl. Physiol. 31, 828--833. https://doi.org/10.1152/jappl.1971.31.6.828

Nadel, E.R., Mitchell, J.W., Stolwijk, J.A.J., 1973. Differential thermal sensitivity in the human skin. Pflugers Arch. 340, 71--76. https://doi.org/10.1007/BF00592198

Nakayama, T., Suzuki, M., Ishizuka, N., 1975. Action of progesterone on preoptic thermosensitive neurones. Nature 258, 80. https://doi.org/10.1038/258080a0

Nedel, W.L., Vasconcellos, A.T., Gunsch, K.A., Rigotti Soares, P.H., 2022. Accuracy and precision of oscillometric noninvasive blood pressure measurement in critically ill patients: systematic review and meta-analysis. Anaesthesiol. Intensive Ther. 54, 425--431. https://doi.org/10.5114/ait.2022.123120

Nelson, B.W., Allen, N.B., 2019. Accuracy of consumer wearable heart rate measurement during an ecologically valid 24-hour period: Intraindividual validation study. JMIR Mhealth Uhealth 7, 1--16. https://doi.org/10.2196/10828

Neves, E.B., 2017. The effect of body fat percentage and body fat distribution on skin surface temperature with infrared thermography. J. Therm. Biol. 66, 1--9. https://doi.org/10.1016/j.jtherbio.2017.03.006

Nielsen, R., Nielsen, B., 1984. Measurement of mean skin temperature of clothed persons in cool environments. Eur. J. Appl. Physiol. Occup. Physiol. 53, 231--236. https://doi.org/10.1007/BF00776595

Niimi, Y., Matsukawa, T., Sugiyama, Y., Shamsuzzaman, A.S.M., Ito, H., Sobue, G., Mano, T., 1997. Effect of heat stress on muscle sympathetic nerve activity in humans. J. Auton. Nerv. Syst. 63, 61--67. https://doi.org/10.1016/S0165-1838(96)00134-8

Notley, S.R., Meade, R.D., Kenny, G.P., 2021. Time following ingestion does not influence the validity of telemetry pill measurements of core temperature during exercise-heat stress: The journal Temperature toolbox. Temperature 8, 12--20. https://doi.org/10.1080/23328940.2020.1801119

Nunan, D., Gay, D., Jakovljevic, D.G., Hodges, L.D., Sandercock, G.R.H., Brodie, D.A., 2009. Validity and reliability of short-term heart-rate variability from the Polar S810. Med. Sci. Sports Exerc. 41, 243--250. https://doi.org/10.1249/MSS.0b013e318184a4b1

NUNAN, D., SANDERCOCK, G.R.H., BRODIE, D.A., 2010. A Quantitative Systematic Review of Normal Values for Short-Term Heart Rate Variability in Healthy Adults. Pacing and Clinical Electrophysiology 33, 1407--1417. https://doi.org/10.1111/j.1540-8159.2010.02841.x

O'Brien, C., Cadarette, B.S., 2013. Quantification of head sweating during rest and exercise in the heat. Eur. J. Appl. Physiol. 113, 735--741. https://doi.org/10.1007/s00421-012-2482-x

O'Brien, C., Hoyt, R.W., Buller, M.J., Castellani, J.W., Young, A.J., 1998. Telemetry pill measurement of core temperature in humans during active heating and cooling. Med. Sci. Sports Exerc. 30, 468--472. https://doi.org/10.1097/00005768-199803000-00020

O'Brien, I.A., O'Hare, P., Corrall, R.J., 1986. Heart rate variability in healthy subjects: effect of age and the derivation of normal ranges for tests of autonomic function. Heart 55, 348--354. https://doi.org/10.1136/hrt.55.4.348

Olesen, B.W., 1984. How many sites are necessary to estimate a mean skin temperature. Thermal physiology 34--38.

Otzenberger, H., Gronfier, C., Simon, C., Charloux, A., Ehrhart, J., Piquard, F., Brandenberger, G., 1998. Dynamic heart rate variability: A tool for exploring sympathovagal balance continuously during sleep in men. Am. J. Physiol. Heart Circ. Physiol. 275. https://doi.org/10.1152/ajpheart.1998.275.3.h946

Ouyang, H., 1985. Clothes hygiene. People's Military Medicine Press, Beijing.

Owens, A.P., Mathias, C.J., Iodice, V., 2021. Autonomic Dysfunction in Autism Spectrum Disorder. Front. Integr. Neurosci. 15, 1--10. https://doi.org/10.3389/fnint.2021.787037

Palatini, P., 2025. Challenges and pitfalls of cuff oscillometric blood pressure measurement. Hypertension Research 48, 1993--1996. https://doi.org/10.1038/s41440-025-02207-x

Palmes, E.D., Park, C.R., 1947. Thermocouples for the measurement of the surface temperature of the skin. Fed. Proc. 6, 175.

Pandi-Perumal, S.R., Smits, M., Spence, W., Srinivasan, V., Cardinali, D.P., Lowe, A.D., Kayumov, L., 2007. Dim light melatonin onset (DLMO): A tool for the analysis of circadian phase in human sleep and chronobiological disorders. Prog. Neuropsychopharmacol. Biol. Psychiatry 31, 1--11. https://doi.org/10.1016/j.pnpbp.2006.06.020

Papaioannou, T.G., Protogerou, A.D., Vrachatis, D., Konstantonis, G., Aissopou, E., Argyris, A., Nasothimiou, E., Gialafos, E.J., Karamanou, M., Tousoulis, D., Sfikakis, P.P., 2016. Mean arterial pressure values calculated using seven different methods and their associations with target organ deterioration in a single-center study of 1878 individuals. Hypertension Research 39, 640--647. https://doi.org/10.1038/hr.2016.41

Paragliola, R.M., Corsello, A., Troiani, E., Locantore, P., Papi, G., Donnini, G., Pontecorvi, A., Corsello, S.M., Carrozza, C., 2021. Cortisol circadian rhythm and jet-lag syndrome: evaluation of salivary cortisol rhythm in a group of eastward travelers. Endocrine 73, 424--430. https://doi.org/10.1007/s12020-021-02621-4

Parati, G., Stergiou, G.S., Dolan, E., Bilo, G., 2018. Blood pressure variability: clinical relevance and application. The Journal of Clinical Hypertension 20, 1133--1137. https://doi.org/10.1111/jch.13304

Park, H., Park, D.Y., 2022. Prediction of individual thermal comfort based on ensemble transfer learning method using wearable and environmental sensors. Build. Environ. 207, 108492. https://doi.org/10.1016/j.buildenv.2021.108492

Park, J., Seok, H.S., Kim, S.-S., Shin, H., 2022. Photoplethysmogram Analysis and Applications: An Integrative Review. Front. Physiol. 12, 1--23. https://doi.org/10.3389/fphys.2021.808451

Park, Y.H., Iwamoto, J., Tajima, F., Miki, K., Park, Y.S., Shiraki, K., 1988. Effect of pressure on thermal insulation in humans wearing wet suits. J. Appl. Physiol. 64, 1916--1922. https://doi.org/10.1152/jappl.1988.64.5.1916

Parsons, K., 1993. Human thermal environments, in: Human Thermal Environments. CRC Press, pp. 22--49. https://doi.org/10.1201/9780203302620-10

Patterson, M.J., Cotter, J.D., Taylor, N.A.S., 1998. Human sudomotor responses to heating and cooling upper-body skin surfaces: Cutaneous thermal sensitivity. Acta Physiol. Scand. 163, 289--296. https://doi.org/10.1046/j.1365-201x.1998.00379.x

Patwardhan, A.R., Vallurupalli, S., Evans, J.M., Bruce, E.N., Knapp, C.F., 1995. Override of spontaneous respiratory pattern generator reduces cardiovascular parasympathetic influence. J. Appl. Physiol. 79, 1048--1054. https://doi.org/10.1152/jappl.1995.79.3.1048

Peltola, M.A., 2012. Role of editing of R-R intervals in the analysis of heart rate variability. Front. Physiol. 3 MAY, 1--10. https://doi.org/10.3389/fphys.2012.00148

Périard, J.D., Eijsvogels, T.M.H., Daanen, H.A.M., 2021. Exercise under heat stress: Thermoregulation, hydration, performance implications, and mitigation strategies. Physiol. Rev. https://doi.org/10.1152/physrev.00038.2020

Périard, J.D., Racinais, S., Sawka, M.N., 2015. Adaptations and mechanisms of human heat acclimation: Applications for competitive athletes and sports. Scand. J. Med. Sci. Sports 25, 20--38. https://doi.org/10.1111/sms.12408

Pickering T, Hall J, Appel L, Falkner B, Graves J, Hill M, Jones D, Kurtz T, Sheps S, Edward J. Roccella E, 2005. Recommendations for Bloods Pressure Measurements in Humans. The Journal of Clinical Hypertension 7, 102--109.

Pickering, T.G., Hall, J.E., Appel, L.J., Falkner, B.E., Graves, J.W., Hill, M.N., Jones, D.W., Kurtz, T., Sheps, S.G., Roccella, E.J., 2005. Recommendations for Blood Pressure Measurement in Humans: An AHA Scientific Statement from the Council on High Blood Pressure Research Professional and Public Education Subcommittee. The Journal of Clinical Hypertension 7, 102--109. https://doi.org/10.1111/j.1524-6175.2005.04377.x

Pierdomenico, S.D., Pierdomenico, A.M., Coccina, F., Lapenna, D., Porreca, E., 2016. Circadian blood pressure changes and cardiovascular risk in elderly-treated hypertensive patients. Hypertension Research 39, 805--811. https://doi.org/10.1038/hr.2016.74

Pinna, G.D., Maestri, R., Torunski, A., Danilowicz-Szymanowicz, L., Szwoch, M., La Rovere, M.T., Raczak, G., 2007. Heart rate variability measures: A fresh look at reliability. Clin. Sci. 113, 131--140. https://doi.org/10.1042/CS20070055

Playà-Montmany, N., Tattersall, G.J., 2021. Spot size, distance and emissivity errors in field applications of infrared thermography. Methods Ecol. Evol. 12, 828--840. https://doi.org/10.1111/2041-210X.13563

Poirier, M.P., Gagnon, D., Kenny, G.P., 2016. Local versus whole-body sweating adaptations following 14 days of traditional heat acclimation. Applied Physiology, Nutrition and Metabolism 41, 816--824. https://doi.org/10.1139/apnm-2015-0698

Proença, M., Ambühl, J., Bonnier, G., Meister, T.A., Valentin, J., Soria, R., Ferrario, D., Lemay, M., Rexhaj, E., 2023. Method-comparison study between a watch-like sensor and a cuff-based device for 24-h ambulatory blood pressure monitoring. Sci. Rep. 13, 1--10. https://doi.org/10.1038/s41598-023-33205-z

Psikuta, A., Niedermann, R., Rossi, R.M., 2014. Effect of ambient temperature and attachment method on surface temperature measurements. Int. J. Biometeorol. 58, 877--885. https://doi.org/10.1007/s00484-013-0669-4

Quintana, D.S., Alvares, G.A., Heathers, J.A.J., 2016. Guidelines for Reporting Articles on Psychiatry and Heart rate variability (GRAPH): recommendations to advance research communication. Transl. Psychiatry 6. https://doi.org/10.1038/TP.2016.73

Quintana, D.S., Guastella, A.J., Mcgregor, I.S., Hickie, I.B., Kemp, A.H., 2013. Moderate alcohol intake is related to increased heart rate variability in young adults: Implications for health and well-being. Psychophysiology 50, 1202--1208. https://doi.org/10.1111/psyp.12134

Radespiel-Tröger, M., Rauh, R., Mahlke, C., Gottschalk, T., Mück-Weymann, M., 2003. Agreement of two different methods for measurement of heart rate variability. Clinical Autonomic Research 13, 99--102. https://doi.org/10.1007/s10286-003-0085-7

Ramanathan, N.L., 1964. A new weighting system for mean surface temperature of the human body. J. Appl. Physiol. 19, 531--533. https://doi.org/10.1152/jappl.1964.19.3.531

Ramesh, S., James, M.T., Holroyd-Leduc, J.M., Wilton, S.B., Sola, D.Y., Ahmed, S.B., 2022. Heart rate variability as a function of menopausal status, menstrual cycle phase, and estradiol level. Physiol. Rep. 10, 1--10. https://doi.org/10.14814/phy2.15298

Ravanelli, N., Coombs, G.B., Imbeault, P., Jay, O., 2018. Maximum skin wettedness after aerobic training with and without heat acclimation. Med. Sci. Sports Exerc. 50, 299--307. https://doi.org/10.1249/MSS.0000000000001439

Reeder, J.T., Choi, J., Xue, Y., Gutruf, P., Hanson, J., Liu, M., Ray, T., Bandodkar, A.J., Avila, R., Xia, W., Krishnan, S., Xu, S., Barnes, K., Pahnke, M., Ghaffari, R., Huang, Y., Rogers, J.A., 2019. Waterproof, electronics-enabled, epidermal microfluidic devices for sweat collection, biomarker analysis, and thermography in aquatic settings. Sci. Adv. 5. https://doi.org/10.1126/sciadv.aau6356

Refinetti, R., 1992. Analysis of the circadian rhythm of body temperature. Behavior Research Methods, Instruments, & Computers 24, 28--36. https://doi.org/10.3758/BF03203466

Reitz, A., Schmid, D.M., Curt, A., Knapp, P.A., Schurch, B., 2002. Sympathetic sudomotor skin activity in human after complete spinal cord injury. Auton. Neurosci. 102, 78--84. https://doi.org/10.1016/S1566-0702(02)00207-2

Relf, R., Willmott, A., Flint, M.S., Beale, L., Maxwell, N., 2019. Reliability of a wearable sweat rate monitor and routine sweat analysis techniques under heat stress in females. J. Therm. Biol. 79, 209--217. https://doi.org/10.1016/j.jtherbio.2018.12.019

Reyes del Paso, G.A., Langewitz, W., Mulder, L.J.M., van Roon, A., Duschek, S., 2013. The utility of low frequency heart rate variability as an index of sympathetic cardiac tone: A review with emphasis on a reanalysis of previous studies. Psychophysiology 50, 477--487. https://doi.org/10.1111/psyp.12027

Ring, E.F.J., Ammer, K., 2012. Infrared thermal imaging in medicine. Physiol. Meas. 33. https://doi.org/10.1088/0967-3334/33/3/R33

Rishi Vardhan, K., Vedanth, S., Poojah, G., Abhishek, K., Nitish Kumar, M., Vijayaraghavan, V., 2021. BP-Net: Efficient Deep Learning for Continuous Arterial Blood Pressure Estimation using Photoplethysmogram. Proceedings - 20th IEEE International Conference on Machine Learning and Applications, ICMLA 2021 1495--1500. https://doi.org/10.1109/ICMLA52953.2021.00241

Robergs, R.A., Burnett, A.F., 2003. Methods Used to Process Data from Indirect Calorimetry and their Application to VO2Max. Journal of Exercise Physiology 6, 44--57.

Robinson, J., Charlton, J., Seal, R., Spady, D., Joffres, M.R., 1998. Oesophageal, rectal, axillary, tympanic and pulmonary artery temperatures during cardiac surgery. Canadian Journal of Anaesthesia 45, 317--323. https://doi.org/10.1007/BF03012021

Roenneberg, T., Keller, L.K., Fischer, D., Matera, J.L., Vetter, C., Winnebeck, E.C., 2015. Human activity and rest in situ. Methods Enzymol. 552, 257--283. https://doi.org/10.1016/bs.mie.2014.11.028

Rogers, D.W., Himariotis, A.T., Sherriff, T.J., Proulx, Q.J., Duong, M.T., Noel, S.E., Cornell, D.J., 2025. Test--Retest Reliability and Concurrent Validity of Photoplethysmography Finger Sensor to Collect Measures of Heart Rate Variability. Sports 13, 29. https://doi.org/10.3390/sports13020029

Romagnoli, S., Ricci, Z., Quattrone, D., Tofani, L., Tujjar, O., Villa, G., Romano, S.M., De Gaudio, A.R., 2014. Accuracy of invasive arterial pressure monitoring in cardiovascular patients: an observational study. Crit. Care 18, 644. https://doi.org/10.1186/s13054-014-0644-4

Romanovsky, A.A., 2014. Skin temperature: its role in thermoregulation. Acta Physiologica 210, 498--507. https://doi.org/10.1111/apha.12231

Romanovsky, A.A., 2007. Thermoregulation: Some concepts have changed. Functional architecture of the thermoregulatory system. Am. J. Physiol. Regul. Integr. Comp. Physiol. 292, 64--66. https://doi.org/10.1152/ajpregu.00668.2006

Rompelman, O., Coenen, A.J.R.M., Kitney, R.I., 1977. Measurement of heart-rate variability: Part 1---Comparative study of heart-rate variability analysis methods. Med. Biol. Eng. Comput. 15, 233--239. https://doi.org/10.1007/BF02441043

Rossignol, D.A., Frye, R.E., 2011. Melatonin in autism spectrum disorders: A systematic review and meta-analysis. Dev. Med. Child Neurol. 53, 783--792. https://doi.org/10.1111/j.1469-8749.2011.03980.x

Rowell, L.B., 1974. Human cardiovascular adjustments to exercise and thermal stress. Physiol. Rev. 54, 75--159. https://doi.org/10.1152/physrev.1974.54.1.75

Rowell, L.B., Brengelmann, G.L., Murray, J.A., 1969. Cardiovascular responses to sustained high skin temperature in resting man. J. Appl. Physiol. 27, 673--680. https://doi.org/10.1152/jappl.1969.27.5.673

Rowell, L.B., Kraning, K.K., Kennedy, J.W., Evans, T.O., 1967. Central circulatory responses to work in dry heat before and after acclimatization. J. Appl. Physiol. 22, 509--518. https://doi.org/10.1152/jappl.1967.22.3.509

Rowell , L.B., Murray, J.A., Brengelmann, G.L., Kraning, K.K., 1969. Human Cardiovascular Adjustments to Rapid Changes in Skin Temperature during Exercise. Circ. Res. 24, 711--724. https://doi.org/10.1161/01.RES.24.5.711

Rutherford, M.M., Akerman, A.P., Notley, S.R., Meade, R.D., Schmidt, M.D., Kenny, G.P., 2021. Regional variation in the reliability of sweat rate measured via the ventilated capsule technique during passive heating. Exp. Physiol. 106, 615--633. https://doi.org/10.1113/EP089074

Rutkove, S.B., Veves, A., Mitsa, T., Nie, R., Fogerson, P.M., Garmirian, L.P., Nardin, R.A., 2009. Impaired distal thermoregulation in diabetes and diabetic polyneuropathy. Diabetes Care 32, 671--676. https://doi.org/10.2337/dc08-1844

Saeki, Y., Atogami, F., Takahashi, K., Yoshizawa, T., 1997. Reflex control of autonomic function induced by posture change during the menstrual cycle. J. Auton. Nerv. Syst. 66, 69--74. https://doi.org/10.1016/S0165-1838(97)00067-2

Safer, J.D., 2011. Thyroid hormone action on skin. Dermatoendocrinol. 3, 211--215. https://doi.org/https://doi.org/10.4161/derm.3.3.17027

Salo, M.A., Huikuri, H. V., Seppanen, T., 2001. Ectopic beats in heart rate variability analysis: Effects of editing on time and frequency domain measures. Annals of Noninvasive Electrocardiology 6, 5--17. https://doi.org/10.1111/j.1542-474X.2001.tb00080.x

Salvi, P., Grillo, A., Parati, G., 2015. Noninvasive estimation of central blood pressure and analysis of pulse waves by applanation tonometry. Hypertension Research 38, 646--648. https://doi.org/10.1038/hr.2015.78

Sandercock, G.R.H., Bromley, P.D., Brodie, D.A., 2005. The reliability of short-term measurements of heart rate variability. Int. J. Cardiol. 103, 238--247. https://doi.org/10.1016/j.ijcard.2004.09.013

Sano, A., Picard, R.W., Stickgold, R., 2014. Quantitative analysis of wrist electrodermal activity during sleep. International Journal of Psychophysiology 94, 382--389. https://doi.org/10.1016/j.ijpsycho.2014.09.011

Sansone, S.-A., Rocca-Serra, P., Field, D., Maguire, E., Taylor, C., Hofmann, O., Fang, H., Neumann, S., Tong, W., Amaral-Zettler, L., Begley, K., Booth, T., Bougueleret, L., Burns, G., Chapman, B., Clark, T., Coleman, L.-A., Copeland, J., Das, S., de Daruvar, A., de Matos, P., Dix, I., Edmunds, S., Evelo, C.T., Forster, M.J., Gaudet, P., Gilbert, J., Goble, C., Griffin, J.L., Jacob, D., Kleinjans, J., Harland, L., Haug, K., Hermjakob, H., Sui, S.J.H., Laederach, A., Liang, S., Marshall, S., McGrath, A., Merrill, E., Reilly, D., Roux, M., Shamu, C.E., Shang, C.A., Steinbeck, C., Trefethen, A., Williams-Jones, B., Wolstencroft, K., Xenarios, I., Hide, W., 2012. Toward interoperable bioscience data. Nat. Genet. 44, 121--126. https://doi.org/10.1038/ng.1054

Sassi, R., Cerutti, S., Lombardi, F., Malik, M., Huikuri, H. V., Peng, C.K., Schmidt, G., Yamamoto, Y., 2015. Advances in heart rate variability signal analysis: Joint position statement by the e-Cardiology ESC Working Group and the European Heart Rhythm Association co-endorsed by the Asia Pacific Heart Rhythm Society. Europace 17, 1341--1353. https://doi.org/10.1093/europace/euv015

Sato, N., Miyake, S., Akatsu, J., Kumashiro, M., 1995. Power spectral analysis of heart rate variability in healthy young women during the normal menstrual cycle. Psychosom. Med. 57, 331--335. https://doi.org/10.1097/00006842-199507000-00004

Saugel, B., Hoppe, P., Nicklas, J.Y., Kouz, K., Körner, A., Hempel, J.C., Vos, J.J., Schön, G., Scheeren, T.W.L., 2020. Continuous noninvasive pulse wave analysis using finger cuff technologies for arterial blood pressure and cardiac output monitoring in perioperative and intensive care medicine: a systematic review and meta-analysis. Br. J. Anaesth. 125, 25--37. https://doi.org/10.1016/j.bja.2020.03.013

Saul, J., 1990. Beat-To-Beat Variations of Heart Rate Reflect Modulation of Cardiac Autonomic Outflow. Physiology 5, 32--37. https://doi.org/10.1152/physiologyonline.1990.5.1.32

Sawka, M., Latzka, W., Matott, R., Montain, S., 1998. Hydration Effects on Temperature Regulation. Int. J. Sports Med. 19, S108--S110. https://doi.org/10.1055/s-2007-971971

Sawka, M.N., Cheuvront, S.N., Kenefick, R.W., 2015. Hypohydration and Human Performance: Impact of Environment and Physiological Mechanisms. Sports Medicine 45, 51--60. https://doi.org/10.1007/s40279-015-0395-7

Sawka, M.N., Montain, S.J., Latzka, W.A., 2001. Hydration effects on thermoregulation and performance in the heat. Comparative Biochemistry and Physiology - A Molecular and Integrative Physiology 128, 679--690. https://doi.org/10.1016/S1095-6433(01)00274-4

Schaffarczyk, M., Rogers, B., Reer, R., Gronwald, T., 2022. Validity of the Polar H10 Sensor for Heart Rate Variability Analysis during Resting State and Incremental Exercise in Recreational Men and Women. Sensors 22, 6536. https://doi.org/10.3390/s22176536

Schiltz, H.K., Fenning, R.M., Erath, S.A., Baucom, B.R.W., Baker, J.K., 2022. Electrodermal Activity Moderates Sleep-Behavior Associations in Children with Autism Spectrum Disorder. Res. Child Adolesc. Psychopathol. 50, 823--835. https://doi.org/10.1007/s10802-022-00900-w

Schutte, A.E., Kollias, A., Stergiou, G.S., 2022. Blood pressure and its variability: classic and novel measurement techniques. Nat. Rev. Cardiol. 19, 643--654. https://doi.org/10.1038/s41569-022-00690-0

Schuurmans, A.A.T.T., de Looff, P., Nijhof, K.S., Rosada, C., Scholte, R.H.J.J., Popma, A., Otten, R., 2020. Validity of the Empatica E4 Wristband to Measure Heart Rate Variability (HRV) Parameters: a Comparison to Electrocardiography (ECG). J. Med. Syst. 44, 190. https://doi.org/10.1007/s10916-020-01648-w

Seeman, T.E., McEwen, B.S., Rowe, J.W., Singer, B.H., 2001. Allostatic load as a marker of cumulative biological risk: MacArthur studies of successful aging, in: Proceedings of the National Academy of Sciences of the United States of America. pp. 4770--4775. https://doi.org/10.1073/pnas.081072698

Shaffer, F., Ginsberg, J.P., 2017. An Overview of Heart Rate Variability Metrics and Norms. Front. Public Health 5, 1--17. https://doi.org/10.3389/fpubh.2017.00258

Shaffer, F., McCraty, R., Zerr, C.L., 2014. A healthy heart is not a metronome: an integrative review of the heart's anatomy and heart rate variability. Front. Psychol. 5, 1--19. https://doi.org/10.3389/fpsyg.2014.01040

Sharman, J.E., Avolio, A.P., Baulmann, J., Benetos, A., Blacher, J., Blizzard, C.L., Boutouyrie, P., Chen, C.H., Chowienczyk, P., Cockcroft, J.R., Cruickshank, J.K., Ferreira, I., Ghiadoni, L., Hughes, A., Jankowski, P., Laurent, S., McDonnell, B.J., McEniery, C., Millasseau, S.C., Papaioannou, T.G., Parati, G., Park, J.B., Protogerou, A.D., Roman, M.J., Schillaci, G., Segers, P., Stergiou, G.S., Tomiyama, H., Townsend, R.R., Van Bortel, L.M., Wang, J., Wassertheurer, S., Weber, T., Wilkinson, I.B., Vlachopoulos, C., 2017. Validation of non-invasive central blood pressure devices: ARTERY Society task force consensus statement on protocol standardization. Eur. Heart J. 38, 2805--2812. https://doi.org/10.1093/eurheartj/ehw632

Shibasaki, M., Crandall, C.G., 2010. Mechanisms and controllers of eccrine sweating in humans. Frontiers in Bioscience S2, 94. https://doi.org/10.2741/s94

Shumate, T., Link, M., Furness, J., Kemp-Smith, K., Simas, V., Climstein, M., 2021. Validity of the Polar Vantage M watch when measuring heart rate at different exercise intensities. PeerJ 9, e10893. https://doi.org/10.7717/peerj.10893

Silva, R.K. do N., Matias, F.L., Gonçalves, A.F., dos Santos, F.N.A., Eduardo, G.N., Andrade, P.R. de, 2024. RELATIONSHIO BETWEEN SKIN TEMPERATURE AND BODY COMPOSITION WOMEN. Braz. J. Phys. Ther. 28, 100969. https://doi.org/10.1016/j.bjpt.2024.100969

Simpson, R., Machin, G., McEvoy, H., Rusby, R., 2006. Traceability and calibration in temperature measurement: a clinical necessity. J. Med. Eng. Technol. 30, 212--217. https://doi.org/10.1080/03091900600711530

Sinnreich, R., Kark, J.D., Friedlander, Y., Sapoznikov, D., Luria, M.H., 1998. Five minute recordings of heart rate variability for population studies: Repeatability and age-sex characteristics. Heart 80, 156--162. https://doi.org/10.1136/hrt.80.2.156

Sloan, R.P., Huang, M.-H., McCreath, H., Sidney, S., Liu, K., Dale Williams, O., Seeman, T., 2008. Cardiac autonomic control and the effects of age, race, and sex: The CARDIA study. Autonomic Neuroscience 139, 78--85. https://doi.org/10.1016/j.autneu.2008.01.006

Smith, A.D.H., Crabtree, D.R., Bilzon, J.L.J., Walsh, N.P., 2010. The validity of wireless iButtons® and thermistors for human skin temperature measurement. Physiol. Meas. 31, 95--114. https://doi.org/10.1088/0967-3334/31/1/007

Smith, C.J., Havenith, G., 2012. Body Mapping of Sweating Patterns in Athletes. Med. Sci. Sports Exerc. 44, 2350--2361. https://doi.org/10.1249/MSS.0b013e318267b0c4

Smith, C.J., Havenith, G., 2011. Body mapping of sweating patterns in male athletes in mild exercise-induced hyperthermia. Eur. J. Appl. Physiol. 111, 1391--1404. https://doi.org/10.1007/s00421-010-1744-8

Smith, C.S., Reilly, C., Midkiff, K., 2011. Composite Scale of Morningness. PsycTESTS Dataset. https://doi.org/10.1037/t07216-000

Snitselaar, M.A., Smits, M.G., van der Heijden, K.B., Spijker, J., 2017. Sleep and Circadian Rhythmicity in Adult ADHD and the Effect of Stimulants: A Review of the Current Literature. J. Atten. Disord. 21, 14--26. https://doi.org/10.1177/1087054713479663

Song, W., Zhong, F., Calautit, J.K., Li, J., 2024. Exploring the role of skin temperature in thermal sensation and thermal comfort: A comprehensive review. Energy and Built Environment. https://doi.org/10.1016/j.enbenv.2024.03.002

Spallone, V., Ziegler, D., Freeman, R., Bernardi, L., Frontoni, S., Pop‐Busui, R., Stevens, M., Kempler, P., Hilsted, J., Tesfaye, S., Low, P., Valensi, P., 2011. Cardiovascular autonomic neuropathy in diabetes: clinical impact, assessment, diagnosis, and management. Diabetes. Metab. Res. Rev. 27, 639--653. https://doi.org/10.1002/dmrr.1239

Sparling, P.B., Snow, T.K., Millard-Stafford, M.L., 1993. Monitoring core temperature during exercise: Ingestible sensor vs. rectal thermistor. Aviat. Space Environ. Med. 64, 760--763.

Stachenfeld, N.S., Silva, C., Keefe, D.L., 2000. Estrogen modifies the temperature effects of progesterone. J. Appl. Physiol. 88, 1643--1649. https://doi.org/10.1152/jappl.2000.88.5.1643

Stephenson, L.A., Kolka, M.A., 1999. Esophageal temperature threshold for sweating decreases before ovulation in premenopausal women. J. Appl. Physiol. 86, 22--28. https://doi.org/10.1152/jappl.1999.86.1.22

Stephenson, L.A., Kolka, M.A., 1993. Thermoregulation in Women. Exerc. Sport Sci. Rev. 21, 231???262. https://doi.org/10.1249/00003677-199301000-00008

Stephenson, L.A., Kolka, M.A., 1985. Menstrual cycle phase and time of day alter reference signal controlling arm blood flow and sweating. Am. J. Physiol. Regul. Integr. Comp. Physiol. 18. https://doi.org/10.1152/ajpregu.1985.249.2.r186

Stephenson, L.A., Wenger, C.B., O'Donovan, B.H., Nadel, E.R., 1984. Circadian rhythm in sweating and cutaneous blood flow. Am. J. Physiol. Regul. Integr. Comp. Physiol. 15, 321--324. https://doi.org/10.1152/ajpregu.1984.246.3.r321

Stergiou, G.S., Alpert, B., Mieke, S., Asmar, R., Atkins, N., Eckert, S., Frick, G., Friedman, B., Graßl, T., Ichikawa, T., Ioannidis, J.P., Lacy, P., McManus, R., Murray, A., Myers, M., Palatini, P., Parati, G., Quinn, D., Sarkis, J., Shennan, A., Usuda, T., Wang, J., Wu, C.O., O'Brien, E., 2018. A universal standard for the validation of blood pressure measuring devices: Association for the Advancement of Medical Instrumentation/European Society of Hypertension/International Organization for Standardization (AAMI/ESH/ISO) Collaboration Statement. Hypertension 71, 368--374. https://doi.org/10.1161/HYPERTENSIONAHA.117.10237

Stergiou, G.S., Palatini, P., Parati, G., O'Brien, E., Januszewicz, A., Lurbe, E., Persu, A., Mancia, G., Kreutz, R., 2021. 2021 European Society of Hypertension practice guidelines for office and out-of-office blood pressure measurement. J. Hypertens. 39, 1293--1302. https://doi.org/10.1097/HJH.0000000000002843

Stone, J.D., Ulman, H.K., Tran, K., Thompson, A.G., Halter, M.D., Ramadan, J.H., Stephenson, M., Finomore, V.S., Galster, S.M., Rezai, A.R., Hagen, J.A., 2021. Assessing the Accuracy of Popular Commercial Technologies That Measure Resting Heart Rate and Heart Rate Variability. Front. Sports Act. Living 3. https://doi.org/10.3389/fspor.2021.585870

Stuyck, H., Dalla Costa, L., Cleeremans, A., Van den Bussche, E., 2022. Validity of the Empatica E4 wristband to estimate resting-state heart rate variability in a lab-based context. International Journal of Psychophysiology 182, 105--118. https://doi.org/10.1016/j.ijpsycho.2022.10.003

Su, X., Kazanci, O.B., Olesen, B.W., Sun, L., Yuan, Y., 2025. A novel method of calculating mean skin temperature with high thermal sensitivity for thermal sensation evaluation. Energy Build. 340. https://doi.org/10.1016/j.enbuild.2025.115809

Sunderland, C., Nevill, M., 2003. Effect of the menstrual cycle on performance of intermittent, high-intensity shuttle running in a hot environment. Eur. J. Appl. Physiol. 88, 345--352. https://doi.org/10.1007/s00421-002-0722-1

Swerdloff, M.M., Hargrove, L.J., 2023. Dry EEG measurement of P3 to evaluate cognitive load during sitting, standing, and walking. PLoS One 18, 1--16. https://doi.org/10.1371/journal.pone.0287885

Taillard, J., Philip, P., Coste, O., Sagaspe, P., Bioulac, B., 2003. The circadian and homeostatic modulation of sleep pressure during wakefulness differs between morning and evening chronotypes. J. Sleep Res. 12, 275--282. https://doi.org/10.1046/j.0962-1105.2003.00369.x

Tan, C.L., Knight, Z.A., 2018. Regulation of Body Temperature by the Nervous System. Neuron 98, 31--48. https://doi.org/10.1016/j.neuron.2018.02.022

Tan, L., Long, L., Ma, X., Yang, W., Liao, F., Peng, Y., Lu, J., Shen, A., An, D., Qu, H., Fu, C., 2023. Association of body mass index trajectory and hypertension risk: A systematic review of cohort studies and network meta-analysis of 89,094 participants. Front. Cardiovasc. Med. 9. https://doi.org/10.3389/fcvm.2022.941341

Tankersley, C.G., Nicholas, W.C., Deaver, D.R., Mikita, D., Kenney, W.L., 1992. Estrogen replacement in middle-aged women: Thermoregulatory responses to exercise in the heat. J. Appl. Physiol. 73, 1238--1245. https://doi.org/10.1152/jappl.1992.73.4.1238

Tarvainen, M.P., Georgiadis, S.D., Ranta-Aho, P.O., Karjalainen, P.A., 2006. Time-varying analysis of heart rate variability signals with a Kalman smoother algorithm. Physiol. Meas. 27, 225--239. https://doi.org/10.1088/0967-3334/27/3/002

Tarvainen, M.P., Ranta-aho, P.O., Karjalainen, P.A., 2002. An advanced detrending method with application to HRV analysis. IEEE Trans. Biomed. Eng. 49, 172--175. https://doi.org/10.1109/10.979357

Tasić, T., Tadić, M., Lozić, M., 2022. Hypertension in Women. Front. Cardiovasc. Med. 9, 1--7. https://doi.org/10.3389/fcvm.2022.905504

Task Force of the European Society of Cardiology the North American Society of Pacing Electrophysiology, 1996. Heart Rate Variability: Standards of Measurement, Physiological Interpretation, and Clinical Use. Circulation 93, 1043--1065. https://doi.org/10.1161/01.CIR.93.5.1043

Tayefeh, F., Plattner, O., Sessler, D.I., Ikeda, T., Marder, D., 1998. Circadian changes in the sweating-to-vasoconstriction interthreshold range. Pflugers Arch. 435, 402--406. https://doi.org/10.1007/s004240050530

Taylor, N.A.S., 2014. Human Heat Adaptation. Compr. Physiol. 4, 325--365. https://doi.org/10.1002/j.2040-4603.2014.tb00547.x

Taylor, N.A.S., Machado-Moreira, C.A., 2013. Regional variations in transepidermal water loss, eccrine sweat gland density, sweat secretion rates and electrolyte composition in resting and exercising humans. Extrem. Physiol. Med. 2, 1. https://doi.org/10.1186/2046-7648-2-4

Taylor, N.A.S., Tipton, M.J., Kenny, G.P., 2014. Considerations for the measurement of core, skin and mean body temperatures. J. Therm. Biol. 46, 72--101. https://doi.org/10.1016/j.jtherbio.2014.10.006

Tegegne, B.S., Man, T., van Roon, A.M., Riese, H., Snieder, H., 2018. Determinants of heart rate variability in the general population: The Lifelines Cohort Study. Heart Rhythm 15, 1552--1558. https://doi.org/10.1016/j.hrthm.2018.05.006

Teichner, W.H., 1958. Assessment of Mean Body Surface Temperature. J. Appl. Physiol. 12, 169--176. https://doi.org/10.1152/jappl.1958.12.2.169

Teixeira, A.L., Ramos, P.S., Vianna, L.C., Ricardo, D.R., 2015. Heart rate variability across the menstrual cycle in young women taking oral contraceptives. Psychophysiology 52, 1451--1455. https://doi.org/10.1111/psyp.12510

Tesfaye, R., Huguet, G., Schmilovich, Z., Renne, T., Loum, M.A., Douard, E., Saci, Z., Jean-Louis, M., Martineau, J.L., Whelan, R., Desrivieres, S., Heinz, A., Schumann, G., Hayward, C., Elsabbagh, M., Jacquemont, S., 2022. Investigating the contributions of circadian pathway and insomnia risk genes to autism and sleep disturbances. Transl. Psychiatry 12. https://doi.org/10.1038/s41398-022-02188-2

Teunissen, L.P.J., De Haan, A., De Koning, J.J., Daanen, H.A.M., 2012. Telemetry pill versus rectal and esophageal temperature during extreme rates of exercise-induced core temperature change. Physiol. Meas. 33, 915--924. https://doi.org/10.1088/0967-3334/33/6/915

Thapa, R., Pokorski, I., Ambarchi, Z., Thomas, E., Demayo, M., Boulton, K., Matthews, S., Patel, S., Sedeli, I., Hickie, I.B., Guastella, A.J., 2021. Heart Rate Variability in Children With Autism Spectrum Disorder and Associations With Medication and Symptom Severity. Autism Research 14, 75--85. https://doi.org/10.1002/aur.2437

Thayer, J.F., Åhs, F., Fredrikson, M., Sollers, J.J., Wager, T.D., 2012. A meta-analysis of heart rate variability and neuroimaging studies: Implications for heart rate variability as a marker of stress and health. Neurosci. Biobehav. Rev. 36, 747--756. https://doi.org/10.1016/j.neubiorev.2011.11.009

Thayer, Julian F, Hansen, A.L., Johnsen, B.H., Balance, A., Medicine, B., 2010. Handbook of Behavioral Medicine, Handbook of Behavioral Medicine. Springer New York, New York, NY. https://doi.org/10.1007/978-0-387-09488-5

Thayer, Julian F., Yamamoto, S.S., Brosschot, J.F., 2010. The relationship of autonomic imbalance, heart rate variability and cardiovascular disease risk factors. Int. J. Cardiol. 141, 122--131. https://doi.org/10.1016/j.ijcard.2009.09.543

Tikuisis, P., Ducharme, M.B., 1996. The effect of postural changes on body temperatures and heat balance. Eur. J. Appl. Physiol. Occup. Physiol. 72--72, 451--459. https://doi.org/10.1007/BF00242275

Timbal, J., Colin, J., Boutelier, C., 1975. Circadian variations in the sweating mechanism. J. Appl. Physiol. 39, 226--230. https://doi.org/https://doi.org/10.1152/jappl.1975.39.2.226

Tonhajzerova, I., Ondrejka, I., Ferencova, N., Bujnakova, I., Grendar, M., Olexova, L.B., Hrtanek, I., Visnovcova, Z., 2021. Alternations in the Cardiovascular Autonomic Regulation and Growth Factors in Autism. Physiol. Res. 70, 551--561. https://doi.org/10.33549/physiolres.934662

Tordjman, S., Najjar, I., Bellissant, E., Anderson, G., Barburoth, M., Cohen, D., Jaafari, N., Schischmanoff, O., Fagard, R., Lagdas, E., Kermarrec, S., Ribardiere, S., Botbol, M., Fougerou, C., Bronsard, G., Vernay-Leconte, J., 2013. Advances in the Research of Melatonin in Autism Spectrum Disorders: Literature Review and New Perspectives. Int. J. Mol. Sci. 14, 20508--20542. https://doi.org/10.3390/ijms141020508

Tronstad, C., Amini, M., Bach, D.R., Martinsen, Ø.G., 2022. Current trends and opportunities in the methodology of electrodermal activity measurement. Physiol. Meas. 43, 02TR01. https://doi.org/10.1088/1361-6579/ac5007

Turner, C.G., Stanhewicz, A.E., Nielsen, K.E., Otis, J.S., Feresin, R.G., Wong, B.J., 2023. Effects of biological sex and oral contraceptive pill use on cutaneous microvascular endothelial function and nitric oxide-dependent vasodilation in humans. J. Appl. Physiol. 134, 858--867. https://doi.org/10.1152/japplphysiol.00586.2022

Tzeravini, E., Tentolouris, A., Kokkinos, A., Tentolouris, N., Katsilambros, N., 2024. Diet induced thermogenesis, older and newer data with emphasis on obesity and diabetes mellitus - A narrative review. Metabol. Open 22, 100291. https://doi.org/10.1016/j.metop.2024.100291

Ul, I.P., Msl, P.S., Zealand, N., Inrim, G., Cmi, L.K., Republic, C., Npl, S., Npl, G.M., Garcia, D.C., Fda, Q.W., Inmetro, K.K., Cnam, M.S., Tubİtak, Ö.P.Y., 2023. Best Practice Guide Use Of Thermal Imagers To Perform Traceable Non- Contact Screening Of Human Body Temperature Version 3, July 2023.

Umetani, K., Singer, D.H., McCraty, R., Atkinson, M., 1998. Twenty-four hour time domain heart rate variability and heart rate: Relations to age and gender over nine decades. J. Am. Coll. Cardiol. 31, 593--601. https://doi.org/10.1016/S0735-1097(97)00554-8

van Marken Lichtenbelt, W.D., Daanen, H.A.M., Wouters, L., Fronczek, R., Raymann, R.J.E.M., Severens, N.M.W., Van Someren, E.J.W., 2006. Evaluation of wireless determination of skin temperature using iButtons. Physiol. Behav. 88, 489--497. https://doi.org/10.1016/j.physbeh.2006.04.026

Van Someren, E.J.W., Dekker, K., Te Lindert, B.H.W., Benjamins, J.S., Moens, S., Migliorati, F., Aarts, E., van der Sluis, S., 2016. The experienced temperature sensitivity and regulation survey. Temperature 3, 59--76. https://doi.org/10.1080/23328940.2015.1130519

Van Someren, E.J.W., Raymann, R.J.E.M., Scherder, E.J.A., Daanen, H.A.M., Swaab, D.F., 2002. Circadian and age-related modulation of thermoreception and temperature regulation: Mechanisms and functional implications. Ageing Res. Rev. 1, 721--778. https://doi.org/10.1016/S1568-1637(02)00030-2

Vandewalle, G., Middleton, B., Rajaratnam, S.M.W., Stone, B.M., Thorleifsdottir, B., Arendt, J., Dijk, D.J., 2007. Robust circadian rhythm in heart rate and its variability: Influence of exogenous melatonin and photoperiod. J. Sleep Res. 16, 148--155. https://doi.org/10.1111/j.1365-2869.2007.00581.x

Verdel, N., Podlogar, T., Ciuha, U., Holmberg, H.C., Debevec, T., Supej, M., 2021. Reliability and validity of the core sensor to assess core body temperature during cycling exercise. Sensors 21, 1--13. https://doi.org/10.3390/s21175932

Verheyden, C., Neyrinck, A., Laenen, A., Rex, S., Van Gerven, E., 2022. Clinical evaluation of a cutaneous zero-heat-flux thermometer during cardiac surgery. J. Clin. Monit. Comput. 36, 1279--1287. https://doi.org/10.1007/s10877-021-00758-1

Vidal-Petiot, E., Stebbins, A., Chiswell, K., Ardissino, D., Aylward, P.E., Cannon, C.P., Ramos Corrales, M.A., Held, C., López-Sendón, J.L., Stewart, R.A.H., Wallentin, L., White, H.D., Steg, P.G., 2017. Visit-to-visit variability of blood pressure and cardiovascular outcomes in patients with stable coronary heart disease. Insights from the STABILITY trial. Eur. Heart J. 38, 2813--2822. https://doi.org/10.1093/eurheartj/ehx250

Vittrant, B., Courrier, V., Yang, R.Y., de Villèle, P., Tebeka, S., Mauries, S., Geoffroy, P.A., 2023. Circadian-like patterns in electrochemical skin conductance measured from home-based devices: a retrospective study. Front. Neurol. 14, 1--8. https://doi.org/10.3389/fneur.2023.1249170

Vlemincx, E., Abelson, J.L., Lehrer, P.M., Davenport, P.W., Van Diest, I., Van Den Bergh, O., 2013. Respiratory variability and sighing: A psychophysiological reset model. Biol. Psychol. 93, 24--32. https://doi.org/10.1016/j.biopsycho.2012.12.001

Voss, A., Heitmann, A., Schroeder, R., Peters, A., Perz, S., 2012. Short-term heart rate variability - Age dependence in healthy subjects. Physiol. Meas. 33, 1289--1311. https://doi.org/10.1088/0967-3334/33/8/1289

Waalen, J., Buxbaum, J.N., 2011. Is Older Colder or Colder Older? The Association of Age With Body Temperature in 18,630 Individuals. J. Gerontol. A Biol. Sci. Med. Sci. 66A, 487--492. https://doi.org/10.1093/gerona/glr001

Wagner, J.Y., Negulescu, I., Schöfthaler, M., Hapfelmeier, A., Meidert, A.S., Huber, W., Schmid, R.M., Saugel, B., 2015. Continuous noninvasive arterial pressure measurement using the volume clamp method: an evaluation of the CNAP device in intensive care unit patients. J. Clin. Monit. Comput. 29, 807--813. https://doi.org/10.1007/s10877-015-9670-2

Wallén, M.B., Hasson, D., Theorell, T., Canlon, B., Osika, W., Ward, S.A., 2012. Possibilities and limitations of the polar RS800 in measuring heart rate variability at rest. Eur. J. Appl. Physiol. 112, 1153--1165. https://doi.org/10.1007/s00421-011-2079-9

Wang, Z., He, Y., Hou, J., Jiang, L., 2013. Human skin temperature and thermal responses in asymmetrical cold radiation environments. Build. Environ. 67, 217--223. https://doi.org/10.1016/j.buildenv.2013.05.020

Warburton, D.E.R., Bredin, S.S.D., Jamnik, V.K., Gledhill, N., 2011. Validation of the PAR-Q+ and ePARmed-X+. Health & Fitness Journal of Canada 4, 1920--6216. https://doi.org/10.14288/hfjc.v4i2.151

Wascher, E., Reiser, J., Rinkenauer, G., Larrá, M., Dreger, F.A., Schneider, D., Karthaus, M., Getzmann, S., Gutberlet, M., Arnau, S., 2023. Neuroergonomics on the Go: An Evaluation of the Potential of Mobile EEG for Workplace Assessment and Design. Hum. Factors 65, 86--106. https://doi.org/10.1177/00187208211007707

Watso, J.C., Farquhar, W.B., 2019. Hydration status and cardiovascular function. Nutrients 11. https://doi.org/10.3390/nu11081866

Weiss, M., Milman, B., Rosen, B., Zimlichman, R., 1993. Quantitation of thyroid hormone effect on skin perfusion by laser Doppler flowmetry. Journal of Clinical Endocrinology and Metabolism 76, 680--682. https://doi.org/10.1210/jcem.76.3.8445026

Wenner, M.M., Taylor, H.S., Stachenfeld, N.S., 2011. Progesterone enhances adrenergic control of skin blood flow in women with high but not low orthostatic tolerance. Journal of Physiology 589, 975--986. https://doi.org/10.1113/jphysiol.2010.194563

Werner, J., 2010. System properties, feedback control and effector coordination of human temperature regulation. Eur. J. Appl. Physiol. 109, 13--25. https://doi.org/10.1007/s00421-009-1216-1

Westerterp, K.R., 2004. Diet induced thermogenesis. Nutr. Metab. (Lond). 1, 1--5. https://doi.org/10.1186/1743-7075-1-5

Wick, D.E., Roberts, S.K., Basu, A., Sandroni, P., Fealey, R.D., Sletten, D., Charkoudian, N., 2006. Delayed threshold for active cutaneous vasodilation in patients with Type 2 diabetes mellitus. J. Appl. Physiol. 100, 637--641. https://doi.org/10.1152/japplphysiol.00943.2005

Williams, B., Mancia, G., Spiering, W., Rosei, E.A., Azizi, M., Burnier, M., Clement, D.L., Coca, A., De Simone, G., Dominiczak, A., Kahan, T., Mahfoud, F., Redon, J., Ruilope, L., Zanchetti, A., Kerins, M., Kjeldsen, S.E., Kreutz, R., Laurent, S., Lip, G.Y.H., McManus, R., Narkiewicz, K., Ruschitzka, F., Schmieder, R.E., Shlyakhto, E., Tsioufis, C., Aboyans, V., Desormais, I., 2019. 2018 ESC/ESH Guidelines for the management of arterial hypertension. Kardiol. Pol. 77, 71--159. https://doi.org/10.5603/KP.2019.0018

Windham, B.G., Fumagalli, S., Ble, A., Sollers, J.J., Thayer, J.F., Najjar, S.S., Griswold, M.E., Ferrucci, L., 2012. The relationship between heart rate variability and adiposity differs for central and overall adiposity. J. Obes. 2012. https://doi.org/10.1155/2012/149516

Winslow, C.-E.A., Herrington, L.P., Gagge, A.P., 1936. A NEW METHOD OF PARTITIONAL CALORIMETRY. American Journal of Physiology-Legacy Content 116, 641--655. https://doi.org/10.1152/ajplegacy.1936.116.3.641

Wohlrab, J., Bechara, F.G., Schick, C., Naumann, M., 2023. Hyperhidrosis: A Central Nervous Dysfunction of Sweat Secretion. Dermatol. Ther. (Heidelb). 13, 453--463. https://doi.org/10.1007/s13555-022-00885-w

Wu, Y., Liu, H., Li, B., Jokisalo, J., Kosonen, R., Cheng, Y., Zhao, W., Yuan, X., 2020. Evaluation and modification of the weighting formulas for mean skin temperature of human body in winter conditions. Energy Build. 229. https://doi.org/10.1016/j.enbuild.2020.110390

Wu, Z., Huang, S., Zou, J., Wang, Q., Naveed, M., Bao, H., Wang, W., Fukunaga, K., Han, F., 2020. Autism spectrum disorder (ASD): Disturbance of the melatonin system and its implications. Biomedicine & Pharmacotherapy 130, 110496. https://doi.org/10.1016/j.biopha.2020.110496

Xu, X., Lian, Z., 2024. Rethinking the calculation method of mean skin temperature in sleep research: Different formulas apply to different purposes. Build. Environ. 251, 111231. https://doi.org/10.1016/j.buildenv.2024.111231

Xu, X., Zhang, H., Lian, Z., Xu, H., 2025. Sex difference in body temperature and thermal perception during nighttime sleep: A time series analysis. Energy Build. 344, 115995. https://doi.org/10.1016/j.enbuild.2025.115995

Xu, X., Zhang, H., Wu, G., Lian, Z., Xu, H., 2024. Sex differences in body temperature and thermal perception under stable and transient thermal environments: A comparative study. Science of The Total Environment 951, 175323. https://doi.org/10.1016/j.scitotenv.2024.175323

Xu, Z., Meng, Q., Ge, X., Zhuang, R., Liu, J., Liang, X., Fan, H., Yu, P., Zheng, L., Zhou, X., 2021. A short-term effect of caffeinated beverages on blood pressure: A meta-analysis of randomized controlled trails. J. Funct. Foods 81, 104482. https://doi.org/10.1016/j.jff.2021.104482

Yamamoto, S., Iwamoto, M., Inoue, M., Harada, N., 2007. Evaluation of the effect of heat exposure on the autonomic nervous system by heart rate variability and urinary catecholamines. J. Occup. Health 49, 199--204. https://doi.org/10.1539/joh.49.199

Yang, C.C., Hsu, Y.L., 2010. A review of accelerometry-based wearable motion detectors for physical activity monitoring. Sensors 10, 7772--7788. https://doi.org/10.3390/s100807772

Yanovich, R., Ketko, I., Charkoudian, N., 2020. Sex differences in human thermoregulation: Relevance for 2020 and beyond. Physiology 35, 177--184. https://doi.org/10.1152/physiol.00035.2019

Yataco, A.R., Fleisher, L.A., Katzel, L.I., 1997. Heart rate variability and cardiovascular fitness in senior athletes. American Journal of Cardiology 80, 1389--1391. https://doi.org/10.1016/S0002-9149(97)00697-8

Yeh, C.-H., Kuo, T.B.J., Li, J.-Y., Kuo, K.-L., Chern, C.-M., Yang, C.C.H., Huang, H.-Y., 2022. Effects of age and sex on vasomotor activity and baroreflex sensitivity during the sleep--wake cycle. Sci. Rep. 12, 22424. https://doi.org/10.1038/s41598-022-26440-3

Yildirir, A., Kabakci, G., Akgul, E., Tokgozoglu, L., Oto, A., 2001. Effects of menstrual cycle on cardiac autonomic innervation as assessed by heart rate variability. Annals of Noninvasive Electrocardiology 7, 60--63. https://doi.org/10.1111/j.1542-474x.2001.tb00140.x

Yoda, T., Crawshaw, L.I., Nakamura, M., Saito, K., Konishi, A., Nagashima, K., Uchida, S., Kanosue, K., 2005. Effects of alcohol on thermoregulation during mild heat exposure in humans. Alcohol 36, 195--200. https://doi.org/10.1016/j.alcohol.2005.09.002

Yu, H., Sun, J., 2020. Sweat detection theory and fluid driven methods: A review. Nanotechnology and Precision Engineering 3, 126--140. https://doi.org/10.1016/j.npe.2020.08.003

Zhang, H., Arens, E., Huizenga, C., Han, T., 2010. Thermal sensation and comfort models for non-uniform and transient environments, part III: Whole-body sensation and comfort. Build. Environ. 45, 399--410. https://doi.org/10.1016/j.buildenv.2009.06.020

Zhang, H., Huizenga, C., Arenas, E., Wang, D., 2004. Thermal sensation and comfort in transient non-uniform thermal environments. Eur. J. Appl. Physiol. 92, 728--733. https://doi.org/10.1007/s00421-004-1137-y

Zhao, L., Liang, C., Huang, Y., Zhou, G., Xiao, Y., Ji, N., Zhang, Y.T., Zhao, N., 2023. Emerging sensing and modeling technologies for wearable and cuffless blood pressure monitoring. NPJ Digit. Med. 6, 1--15. https://doi.org/10.1038/s41746-023-00835-6

Zhong, G., Bolitho, S., Grunstein, R., Naismith, S.L., Lewis, S.J.G., 2013. The Relationship between Thermoregulation and REM Sleep Behaviour Disorder in Parkinson's Disease. PLoS One 8, e72661. https://doi.org/10.1371/journal.pone.0072661

Żyliński, M., Cybulski, G., 2022. Verification of the Assumptions of Volume-Clamp Method for Continuous Blood Pressure Measurement in a Silicone Phantom, in: 2022 Computing in Cardiology (CinC). Tampere, Finland, pp. 1--4. https://doi.org/10.22489/CinC.2022.215
