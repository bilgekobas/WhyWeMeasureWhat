# Anatomical reference taxonomy

This section compiles anatomical sites used for surface and internal physiological measurements, standardised into body regions and sub-regions where appropriate. Certain modalities, particularly facial infrared thermography (IRT) and brown-adipose-tissue-related supraclavicular measurements, require finer anatomical subdivision than traditional mean skin temperature (MST) formulations. Each site may include left/right or anterior/{ref}`posterior <label-spatial-orientation>` counterparts; these are only specified when relevant.  

Letters A--U from the previous chapter, {ref}`Mean Skin Temperature formulas <mean-skin-temperature-formulas>` are retained solely to map historical formulas to the standardised regions shown in the below Figure and Table.

```{figure} C:/Users/kobas/00_Repos/2511_WhyWeMeasureWhat_Git/book/assets/figures/anatomical-taxonomy.jpg
:name: fig-anatomical-taxonomy
:width: 90%
:alt: Body sites for surface measurements

Surface sites for typical physiological signal measurements. Letter annotations refer to the matching measurement regions in {ref}`Mean Skin Temperature calculation formulas <mean-skin-temperature-formulas>`. Regions correspond to {numref}`tab-mst-formulas`. Each may be subdivided by side (L/R) or aspect (A = anterior, P = posterior, M = midline).  
Black points indicate site aspects explicitly represented in historical MST formulations. Pink points indicate additional anatomical sub-sites commonly used in current physiological, wearable, and infrared thermography (IRT) research.
```

### Surface measurement sites

:::{table} General anatomical reference taxonomy for surface physiological measurements, grouped by anatomical region and aligned with legacy mean skin temperature (MST) formula codes where applicable.
:name: tab-anatomical-taxonomy-surface

| **Body domain** | **Region code** | **Site / region** | **{ref}`Laterality <label-laterality>`** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Head** | 1 | Forehead | Midline | Anterior | Frontal region, brow | Skin temperature, IRT, zero-heat-flux CBT | A | Common in MST and facial thermography |
|  | 2 | Temple | Left, Right | Lateral | Temporal region | IRT, facial temperature | — | Often analysed separately from forehead in facial thermography |
|  | 3 | Nose | Midline | Anterior | Nasal dorsum, nasal tip, alar region | IRT, facial temperature | — | Relevant for respiratory heat exchange and facial thermography |
|  | 4 | Cheek | Left, Right | Anterior | Malar region, zygomatic arch | Skin temperature, IRT | B | Common in facial thermography |
|  | 5 | Earlobe | Left, Right | Inferior, Lateral | Auricular lobe | PPG, pulse oximetry, temperature | — | Sometimes preferred over finger because of local perfusion stability |
|  | 6 | Neck | Midline, Left, Right | Anterior, Posterior, Lateral | Sternocleidomastoid, nape, nuchal area | Skin temperature, IRT | C | Exact placement should be specified |
|  | 7 | Clavicular / supraclavicular region | Left, Right | Superior, Anterior | Supraclavicular fossa, clavicular region, over-the-shoulder region | IRT, skin temperature | — | Frequently used in BAT-related thermography studies |
| **Trunk** | 8 | Chest | Midline, Left, Right | Anterior | Pectoral region, sternum, thorax | Skin temperature, ECG, respiration, accelerometry | K | Must distinguish sternum from lateral chest |
|  | 9 | Back | Midline, Left, Right | Posterior | Scapular, interscapular, upper thoracic region | Skin temperature, IRT | J | Should be distinguished from lumbar |
|  | 10 | Upper arm | Left, Right | Anterior, Posterior, Lateral | Biceps, triceps, deltoid region | Skin temperature, cuff BP, PPG | D | Distinguish upper-arm skin from brachial cuff site |
|  | 11 | Elbow | Left, Right | Anterior, Posterior | Cubital fossa, olecranon | Skin temperature | E | Anterior and posterior elbow are not equivalent |
|  | 12 | Abdomen | Midline, Left, Right | Anterior | Umbilical region, epigastric, central abdomen | Skin temperature, IRT | M | Surface abdomen is distinct from gastrointestinal internal sites |
|  | 13 | Lumbar | Midline, Left, Right | Posterior | Lumbar, flank, lumbosacral region | Skin temperature, IRT | L | Lower posterior trunk; often merged with “back” |
|  | 14 | Forearm | Left, Right | Anterior, Posterior, Lateral | Antebrachial region | Skin temperature, PPG, EDA, IRT | F | Widely used due to accessibility |
|  | 15 | Buttocks | Left, Right | Posterior | Gluteal region | Skin temperature | N | Included in extended body-surface formulas |
|  | 16 | Wrist | Left, Right | Volar, Dorsal | Carpal region, radial wrist, volar wrist | PPG, skin temperature, cuffless BP, EDA | — | Exact side and surface should be specified |
|  | 17 | Hand/Palm | Left, Right | Dorsal, Palmar | Hand: Dorsum of the hand; Palm: Volar hand | EDA, skin temperature | G, H, I | Palmar skin has distinct sudomotor properties |
|  | 18 | Finger | Left, Right | Dorsal, Palmar | Fingertip, phalanx, digital area | PPG, SpO₂, skin temperature, EDA | — | Highly vasomotor-sensitive; digit and side should be reported |
| **Lower limb** | 19 | Thigh | Midline, Left, Right | Anterior, Posterior | Quadriceps, hamstring | Skin temperature, IRT | O, P | Anterior and posterior thigh should be distinguished |
|  | 20 | Lower leg: Calf/Shin | Left, Right | Anterior, Posterior | Shin: Tibial region; Calf: Gastrocnemius | Skin temperature, IRT | Q, R | Shin and calf should be distinguished whenever possible |
|  | 21 | Ankle | Left, Right | Medial, Lateral, Posterior | Malleolar area, Achilles region | Skin temperature | — | Exact aspect matters substantially |
|  | 22 | Foot/Sole | Left, Right | Dorsal, Plantar | Foot: Foot dorsum, instep; Sole: Plantar foot | Skin temperature, IRT, pressure, sweat | S, T, U | Plantar and dorsal surfaces are physiologically distinct |
:::

### Cavity-based measurement sites

:::{table} Anatomical reference taxonomy for cavity-based physiological measurements.
:name: tab-anatomical-taxonomy-cavity

| **Body domain** | **Region code** | **Site / region** | **Laterality** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Head** | 23 | Ear canal/Tympanic site | Left, Right | — | Aural canal, tympanic canal | Core body temperature proxy | — | Distinguish ear-canal measurement from true tympanic measurement |
|  | 24 | Oral cavity | — | Sublingual/Oral | Sublingual, oral temperature | Core body temperature proxy | — | Oral and sublingual measurements should be distinguished |
| **Trunk** | 25 | Rectum | — | — | Rectal site | Core body temperature | — | Depth of insertion strongly affects comparability |
:::

### Internal measurement sites

:::{table} Anatomical reference taxonomy for invasive internal physiological measurements.
:name: tab-anatomical-taxonomy-internal

| **Body domain** | **Region code** | **Site / region** | **Laterality** | **Aspect / surface** | **Common aliases / variants** | **Typical modalities / signals** | **MST code(s)** | **Notes** |
|---|---|---|---|---|---|---|---|---|
| **Trunk** | 26 | Gastrointestinal tract | — | — | GI lumen, intestinal site | CBT pill / ingestible telemetry | — | Used in ambulatory and exercise physiology studies |
|  | 27 | Oesophagus | — | — | Esophageal site | Core body temperature | — | Insertion depth should always be reported |
|  | 28 | Bladder | — | — | Vesical site | Core body temperature | — | Mostly clinical / catheter-based |
|  | 29 | Pulmonary artery | — | — | PA catheter site | Core body temperature | — | Clinical gold standard; highly invasive |
:::