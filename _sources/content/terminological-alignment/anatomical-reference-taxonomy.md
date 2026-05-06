# Anatomical reference taxonomy

This section compiles the anatomical sites used for skin-temperature measurement, standardised into 26 body regions. Each site may include left/right or anterior/{ref}`posterior <label-spatial-orientation>` counterparts; these are only specified when relevant.\
Letters A--U from the previous chapter, 4.2 Mean skin temperature formulas are retained solely to map historical formulas to the standardised regions shown in the below Figure and Table.

```{figure} C:/Users/kobas/00_Repos/2511_WhyWeMeasureWhat_Git/book/assets/figures/skin-temp-sites.jpeg
:name: fig-skin-temp-sites
:width: 90%
:alt: Body sites for skin temperature measurement

Skin temperature measurement sites. Skin temperature measurement sites. Letter annotations refer to the matching measurement regions in {ref}`Mean Skin Temperature calculation formulas <mean-skin-temperature-formulas>`. Regions correspond to {numref}`tab-mst-formulas`. Each may be subdivided by side (L/R) or aspect (A = anterior, P = posterior, M = midline).\
Black points indicate specific aspects of measurement sites as per MST formulas. Pink points indicate other possible sites, as seen in current practices.`.
```


### Surface measurement sites

:::{table} General anatomical reference taxonomy for surface physiological measurements, grouped by anatomical region and aligned with legacy mean skin temperature (MST) formula codes where applicable.
| **Body domain** | **Region code** | **Site / region** | **{ref}`Laterality <label-laterality>`** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Head** | 1 | Forehead | Midline | Anterior | Brow, temple | Skin temperature, IRT, zero-heat-flux CBT | A | Common in MST and facial thermography |
|  | 2 | Nose | Midline | Anterior | Nasal dorsum, alar region | IRT, facial temperature | — | Relevant for respiratory heat exchange |
|  | 3 | Cheek | Left / right | Anterior | Malar region, zygomatic arch | Skin temperature, IRT | B | Common in IRT; not always included in older MST sets |
|  | 4 | Neck | Left / right / midline | Anterior / posterior / lateral | Sternocleidomastoid, nape, lateral neck, nuchal area | Skin temperature, IRT | C | Exact placement should be specified |
|  | 5 | Earlobe | Left / right | Inferior / lateral | Auricular lobe | PPG, pulse oximetry, temperature | — | Sometimes preferred over finger because of local perfusion stability |
| **Trunk** | 6 | Back | Left / right / midline | Posterior | Scapular, interscapular, upper thoracic region | Skin temperature, IRT | J | Should be distinguished from lumbar |
|  | 7 | Lumbar | Left / right / midline | Posterior | Lumbar, flank, lumbosacral region | Skin temperature, IRT | L | Lower posterior trunk; often merged with “back” |
|  | 8 | Abdomen | Midline / left / right | Anterior | Umbilical region, epigastric, central abdomen | Skin temperature, IRT | M | Surface abdomen is distinct from gastrointestinal internal sites |
|  | 9 | Buttocks | Left / right | Posterior | Gluteal region | Skin temperature | N | Included in extended body-surface formulas |
|  | 10 | Chest | Midline / left / right | Anterior | Pectoral region, sternum, thorax | Skin temperature, ECG, respiration, accelerometry | K | Must distinguish sternum from lateral chest |
| **Upper limb** | 11 | Upper arm | Left / right | Anterior / posterior / lateral | Biceps, triceps, deltoid region | Skin temperature, cuff BP, PPG | D | Distinguish upper arm skin from brachial cuff site |
|  | 12 | Elbow | Left / right | Anterior / posterior | Cubital fossa, olecranon | Skin temperature | E | Anterior and posterior elbow are not equivalent |
|  | 13 | Forearm | Left / right | Anterior / posterior / lateral | Antebrachial region | Skin temperature, PPG, EDA, IRT | F | Widely used due to accessibility |
|  | 14 | Wrist | Left / right | Volar / dorsal | Carpal region, radial wrist, volar wrist | PPG, skin temperature, cuffless BP, EDA | — | Exact side and surface should be specified |
|  | 15 | Hand | Left / right | Palmar / dorsal | Palm, volar hand, dorsum of hand, back of hand | Skin temperature, EDA, IRT | G, H, I | Palmar and dorsal surfaces are physiologically distinct |
|  | 16 | Finger | Left / right | Digit-specific / distal | Fingertip, phalanx, digital area | PPG, SpO₂, skin temperature, EDA | — | Highly vasomotor-sensitive; digit and side should be reported |
| **Lower limb** | 17 | Thigh | Left / right | Anterior / posterior | Quadriceps, hamstring | Skin temperature, IRT | O, P | Anterior and posterior thigh should be distinguished |
|  | 18 | Lower leg | Left / right | Anterior / posterior | Shin, tibial region, calf, gastrocnemius | Skin temperature, IRT | Q, R | Calf and shin are often conflated in the literature |
|  | 19 | Ankle | Left / right | Medial / lateral / posterior | Malleolar area, Achilles region | Skin temperature | — | Exact aspect matters substantially |
|  | 20 | Foot | Left / right | Dorsal | Foot dorsum, instep | Skin temperature, IRT | S, T | Dorsal foot should be distinguished from plantar foot |
|  | 21 | Foot | Left / right | Plantar | Sole, plantar foot | Skin temperature, pressure, sweat | U | Plantar surface is not equivalent to dorsal foot |
:::

### Cavity-based measurement sites

:::{table} Anatomical reference taxonomy for cavity-based physiological measurements.
| **Body domain** | **Region code** | **Site / region** | **Laterality** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Head** | 22 | Ear canal / tympanic site | Left / right | — | Aural canal, tympanic canal | Core body temperature proxy | — | Distinguish ear canal measurement from true tympanic measurement |
| **Head** | 23 | Oral cavity | — | Sublingual / oral | Sublingual, oral temperature | Core body temperature proxy | — | Should distinguish oral from sublingual |
| **Trunk** | 24 | Rectum | — | — | Rectal site | Core body temperature | — | Depth of insertion strongly affects comparability |
:::

### Internal measurement sites

:::{table} Anatomical reference taxonomy for invasive internal physiological measurements.
| **Body domain** | **Region code** | **Site / region** | **Laterality** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Trunk** | 25 | Gastrointestinal tract | — | — | GI lumen, intestinal site | CBT pill / ingestible telemetry | — | Internal site; not anatomically equivalent to surface abdomen |
| **Trunk** | 26 | Oesophagus | — | — | Esophageal site | Core body temperature | — | Insertion depth should always be reported |
| **Trunk** | 27 | Bladder | — | — | Vesical site | Core body temperature | — | Mostly clinical / catheter-based |
| **Trunk** | 28 | Pulmonary artery | — | — | PA catheter site | Core body temperature | — | Clinical gold standard; highly invasive |
:::