# INTRODUCTION

Physiological measurements describe how the human body responds to its thermal environment. They translate the abstract language of building conditions — air temperature, radiant heat, humidity, air movement — into the biological processes that determine whether a space supports health, performance, and well-being. A century of thermophysiology research has produced precise methods for measuring these processes: what sensors to use, where on the body to place them, how to calibrate and process the signals, and how to interpret the results. That knowledge exists. The problem is that it is scattered across disciplines — thermophysiology, sports science, psychophysiology, chronobiology, clinical monitoring — and is not consistently applied in building research.

This resource exists to bridge that gap.

## What this resource is

*Why We Measure What, How and Where* is an open, version-controlled reference for physiological signal measurement in indoor thermal environment studies. It is aimed at researchers who measure human physiological responses in building experiments — whether in controlled climate chambers, living labs, or occupied field settings — and who want their work to be grounded in established physiological reasoning and comparable with other studies.

The resource documents five commonly used physiological signals:

- [Core body temperature](../physiological-signals/core-body-temperature)
- [Skin temperature](../physiological-signals/skin-temperature)
- [Heart rate and heart rate variability](../physiological-signals/heart-rate-and-heart-rate-variability)
- [Blood pressure](../physiological-signals/blood-pressure)
- [Sweat, skin moisture, and skin conductance](../physiological-signals/sweat-skin-moisture-and-skin-conductance)

For each signal, the same six-layer template is applied: *why* we measure it (mechanistic rationale), *how* it is measured (sensing principles and technologies), *where* on the body it is measured (anatomical site considerations), *how well* different methods agree (cross-method validation), *what else shapes it* (confounders and modifiers), and *how raw data become reported outcomes* (data handling and processing).

Beyond the signal chapters, the resource provides:

- [Terminological alignment](../terminological-alignment/index) — a harmonised notation table, standardisation challenges in derived metrics, an anatomical reference taxonomy, and a controlled vocabulary and glossary
- [Sample checklists and schemas](../sample-checklists-schemas/index) — structured metadata templates at the experiment, participant, and session level

## Why this resource exists

Building science and indoor environmental research have increasingly incorporated physiological measurements over the past decade. Advances in wearable sensing have made it practical to monitor core temperature, heart rate variability, skin conductance, and skin temperature in sedentary participants over long durations. But as the number of studies has grown, so has the heterogeneity of how those measurements are made, described, and reported.

The same variable — mean skin temperature, say, or heart rate variability — can mean different things depending on how many body sites were used, which formula was applied, which sensor was chosen, and which preprocessing steps were taken. When these decisions are not documented, studies that appear to measure the same thing cannot reliably be compared or combined.

This heterogeneity has three layers:

**Interpretive fragmentation** — physiological signals are selected and described without an explicit connection to the thermoregulatory mechanism they are supposed to represent. Heart rate goes up in a warm room: is that a marker of cardiovascular strain, autonomic adjustment, dehydration, or postural change? Without a stated mechanistic rationale, the measurement is ambiguous.

**Measurement fragmentation** — different sensing technologies target related but non-identical constructs. ECG-derived and PPG-derived heart rate variability are not interchangeable under thermal stress. Rectal and tympanic temperature track the same biological quantity but respond at different speeds. These distinctions are well understood within their source disciplines but are not always carried into building research.

**Descriptive fragmentation** — terminology, anatomical site names, and variable notation vary across publications. The same body location may be called 'chest', 'sternum', 'thorax', or 'pectoral region'. HRV indices are reported in different units with different preprocessing pipelines. Mean skin temperature formulas from three-site to seventeen-site variants are used without specifying which.

These three layers compound each other. A signal selected without mechanistic clarity, measured with an undocumented device, and described with inconsistent terminology is very difficult to interpret or reuse. This is not a problem of bad science — most studies are individually rigorous. It is a problem of missing connective tissue: the shared language and documentation practices that allow individual studies to accumulate into population-level evidence.

## What this resource does not do

This resource does not prescribe a single correct method for any measurement. It does not tell you which sensor to buy or which formula to use. It documents the options, their properties, their limits of agreement, and the decisions that need to be made and reported.

It also does not replace the existing standards that govern individual measurements — ISO 9886, the IUPS Thermal Physiology Glossary, ISO 7726, the Task Force HRV guidelines {cite:p}`noauthor_iso_2004,IUPSThermalCommission2001,ISO7726,electrophysiology_heart_1996` — but complements them by assembling their methodological knowledge in one place, in the context of sedentary indoor experiments.

The current scope is intentionally bounded: **healthy adults, sedentary or light-activity conditions, controlled or semi-controlled indoor environments**. Field studies, exercise physiology, clinical populations, and outdoor exposures involve additional considerations that will be addressed in future versions.

## How to use this resource

**If you are designing a new study**, start with the signal chapters for the variables you plan to measure. The *Why* section will help you connect your measurement choice to your research question. The *Confounders and modifiers* section will tell you which participant characteristics to screen for and document. The *Data handling* section will tell you what preprocessing decisions to make explicit. The [sample schemas](../sample-checklists-schemas/index) give you a ready-made documentation structure.

**If you are reporting or writing up a study**, the [notation table](../terminological-alignment/symbolic-notation-and-variable-conventions) and [glossary](../terminological-alignment/controlled-vocabulary-and-glossary) will help you use consistent terminology. The [anatomical taxonomy](../terminological-alignment/anatomical-reference-taxonomy) provides standard site names. The [derived metrics chapter](../terminological-alignment/standardization-challenges-in-derived-metrics) documents which MST formulas and mean body temperature weightings have been used historically, so you can report yours in context.

**If you are reviewing a paper or building a meta-analysis**, the agreeability sections and the empirical metadata analysis in the accompanying paper describe what is typically documented and what is typically missing, giving you a basis for systematic quality assessment.

## How this resource is maintained

The resource is maintained as a living document: it will be updated as sensing technologies develop, as new evidence on modifier effects becomes available, and as community contributions expand its scope. Changes are tracked through the project repository so that earlier versions remain accessible. When significant revisions occur, a new version identifier is assigned.

If you use this resource in published work, please cite the specific version to ensure that your methods can be linked to a stable reference. Citation guidance is available [here](../contribution/how-to-cite).

Contributions are welcome. See [how to contribute](../contribution/how-to-contribute) for guidance on proposing additions, corrections, or new content.

## About this resource

This resource was developed at the Chair of Building Technology and Climate Responsive Design, Technical University of Munich. It accompanies a peer-reviewed methods paper that describes the framework in detail, provides empirical evidence for the fragmentation problem from a metadata analysis of 250 indoor thermal physiology studies, and positions the resource within the broader landscape of reproducibility infrastructure in environmental research.

The underlying literature corpus integrates publications spanning thermophysiology, psychophysiology, sports and exercise science, chronobiology, clinical monitoring, and indoor environmental research. Priority was given to meta-analyses, systematic reviews, international standards, and methodological position papers.

The resource is published under an open licence. Version history and contribution records are maintained at [GitHub](https://github.com/bilgekobas/WhyWeMeasureWhat).
