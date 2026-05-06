# Standardization challenges in derived metrics

Derived and composite physiological metrics often exhibit substantial variability in weighting schemes, anatomical site selection, preprocessing steps, and reporting conventions. In many cases, studies appear to report the same variable while relying on non-equivalent underlying definitions. This reduces comparability across experiments, complicates meta-analysis, and obscures whether observed differences arise from physiology, instrumentation, or calculation method.

(mean-skin-temperature-formulas)=
## Mean Skin Temperature Formulas

The below table aligns mean skin temperature calculations based on meta-reviews of {cite:p}`choi_evaluation_1997,noauthor_iso_2004,kuwabara_fundamental_2006,liu_evaluation_2011,song_exploring_2025,winslow_new_1936`.

:::{table} Measurement sites and weighting factors for mean skin temperature formulas. 
:name: tab-mst-formulas
:class: mst-table wide-table

| **Pts** | **Var** | **A** | **B** | **C** | **D** | **E** | **F** | **G** | **H** | **I** | **J** | **K** | **L** | **M** | **N** | **O** | **P** | **Q** | **R** | **S** | **T** | **U** | **By** | **Year** | **Reference** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---|
|  |  | Forehead | Cheek(l) | Neck(l) | Upper arm(r) | Elbow(l) | Forearm(l) | Palm(l) | Hand(r) | Hand(l) | Back(l) | Chest(l) | Lumbar(l) | Abdomen | Buttocks(l) | Thigh(a) | Thigh(l)(p) | Calf(a)(r) | Calf(p)(l) | Foot(l) | Foot(r) | Sole(l) |  |  |  |
| **3** | a |  |  |  |  |  | 0.14 |  |  |  |  | 0.50 |  |  |  |  |  | 0.36 |  |  |  |  | Burton | 1935 | {cite:p}`mitchell_comparison_1969` |
|  | b |  |  |  |  |  | 0.14 |  |  |  |  | 0.50 |  |  |  |  |  |  | 0.36 |  |  |  | Olesen | 1984 | {cite:p}`olesen_how_1984` |
|  | c | 0.25 |  |  |  |  | 0.50 |  |  |  |  |  |  |  |  |  |  |  |  | 0.25 |  |  | Cho et al. | 1996 | {cite:p}`cho_development_1996` |
|  | d |  |  |  |  |  | 0.30 |  |  |  |  | 0.35 |  |  |  |  |  | 0.35 |  |  |  |  | Wu et al. | 2020 | {cite:p}`wu_evaluation_2020` |
|  | e |  |  |  | 0.25 |  |  |  |  |  |  | 0.43 |  |  |  | 0.32 |  |  |  |  |  |  | Roberts et al. | 1977 | {cite:p}`kuwabara_fundamental_2006` |
| **4** | a |  |  |  |  |  | 0.15 |  |  |  |  | 0.34 |  |  |  | 0.33 |  | 0.18 |  |  |  |  | Newburgh & Spealman | 1943 | {cite:p}`teichner_assessment_1958` |
|  | b |  |  |  | 0.30 |  |  |  |  |  |  | 0.30 |  |  |  | 0.20 |  | 0.20 |  |  |  |  | Ramanathan | 1964 | {cite:p}`ramanathan_new_1964` |
|  | c |  |  | 0.28 |  |  |  |  | 0.16 |  | 0.28 |  |  |  |  |  |  | 0.28 |  |  |  |  | ISO 9886 + | 1992 | {cite:p}`noauthor_iso_2004` |
|  | d |  |  |  |  |  | 0.14 |  |  |  |  | 0.35 |  |  |  | 0.26 |  | 0.25 |  |  |  |  | Wu et al. | 2020 | {cite:p}`wu_evaluation_2020` |
|  | e |  |  |  | 0.14 |  |  |  |  |  |  | 0.35 |  |  |  | 0.26 |  | 0.25 |  |  |  |  | Wu et al. | 2020 | {cite:p}`wu_evaluation_2020` |
| **5** | a | 0.07 |  |  |  |  |  |  | 0.05 |  |  | 0.50 |  |  |  | 0.18 |  | 0.20 |  |  |  |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | b |  | 0.07 |  | 0.19(a) |  |  |  |  |  |  |  | 0.175 | 0.175 |  |  | 0.39 |  |  |  |  |  | Houdas | 1982 | {cite:p}`houdas_temperature_1982` |
|  | c | 0.07 |  |  |  |  |  |  | 0.05 |  |  | 0.42 |  |  |  | 0.26 |  | 0.20 |  |  |  |  | Wu et al. | 2020 | {cite:p}`wu_evaluation_2020` |
|  | d | 0.20 |  |  | 0.18 |  |  |  | 0.05 |  | 0.50 |  |  |  |  | 0.07 |  |  |  |  |  |  | Wang et al. | 2013 | {cite:p}`wang_human_2013` |
| **6** | a |  | 0.14 |  |  |  | 0.11 | 0.05 |  |  | 0.19 | 0.19 |  |  |  | 0.32 |  |  |  |  |  |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | b |  | 0.149 |  | 0.107 |  |  |  |  |  |  | 0.186 | 0.186 |  |  | 0.186 | 0.186 |  |  |  |  |  | Teichner | 1958 | {cite:p}`teichner_assessment_1958` |
|  | c | 0.10 |  |  |  |  | 0.05 |  | 0.05 |  |  | 0.40 |  |  |  | 0.20 |  | 0.20 |  |  |  |  | Miura et al. | 1960 | {cite:p}`mochida_tohru_mean_1983` |
|  | d | 0.11 |  |  | 0.1 |  | 0.13 |  |  |  |  | 0.28 |  |  |  | 0.21 |  | 0.20 |  |  |  |  | Mochida | 1983 | {cite:p}`mochida_tohru_mean_1983` |
|  | e |  | 0.14 |  |  |  | 0.11 |  | 0.05 |  |  | 0.19 | 0.19 |  |  | 0.32 |  |  |  |  |  |  | Palmes & Park | 1947 | {cite:p}`palmes_thermocouples_1947` |
| **7** | a | 0.07 |  |  |  |  | 0.14 | 0.05 |  |  |  | 0.35 |  |  |  | 0.19 |  | 0.13 |  |  |  | 0.07 | Hardy & DuBois | 1938 | {cite:p}`hardy_technic_1938` |
|  | b |  |  |  |  |  | 1/7 |  | 1/7 |  | 1/7 | 1/7 |  |  |  | 1/7 |  |  | 1/7 | 1/7 |  |  | Park | 1988 | {cite:p}`park_effect_1988` |
|  | c | 0.21 |  |  | 0.12 |  | 0.06 |  |  |  |  | 0.21 |  | 0.17 |  | 0.15 |  | 0.08 |  |  |  |  | Nadel | ? | {cite:p}`mochida_tohru_mean_1983` |
|  | d |  |  | 0.098 | 0.082 |  | 0.114 |  |  |  | 0.162 | 0.166 |  |  |  | 0.182 |  | 0.206 |  |  |  |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | e | 0.066 |  |  | 0.149 |  | 0.151 |  |  |  |  | 0.153 |  | 0.153 |  | 0.163 |  | 0.183 |  |  |  |  | Mochida | 1983 | {cite:p}`mochida_tohru_mean_1983` |
|  | f | 0.198 |  |  | 0.138 |  | 0.076 |  |  |  |  | 0.179 |  | 0.145 |  | 0.153 |  | 0.092 |  |  |  |  | Mochida | 1983 | {cite:p}`mochida_tohru_mean_1983` |
| **8** | a |  |  |  | 0.085 |  | 0.09 |  |  |  | 0.11 | 0.11 | 0.11 | 0.11 |  | 0.23 |  | 0.16 |  |  |  |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | b | 0.07 |  |  | 0.07 |  | 0.07 |  | 0.05 |  | 0.175 | 0.175 |  |  |  | 0.19 |  | 0.20 |  |  |  |  | Gagge & Nishi + | 1977 | {cite:p}`prakash_heat_1977` |
|  | c | 0.21 |  |  | 0.12 |  | 0.06(a) |  |  |  | 0.11 | 0.10 |  | 0.17 |  | 0.15 |  | 0.08 |  |  |  |  | Nadel | 1973 | {cite:p}`nadel_differential_1973` |
|  | d | 0.07 |  |  | 0.13 |  | 0.12 |  |  |  | 0.09 | 0.09 |  | 0.18 |  | 0.16 |  | 0.16 |  |  |  |  | Nadel | 1973 | {cite:p}`nadel_differential_1973` |
|  | e | 0.19 |  |  | 0.13 |  | 0.12(a) |  |  |  | 0.09 | 0.08 |  | 0.12 |  | 0.12 |  | 0.15 |  |  |  |  | Crawshaw | 1975 | {cite:p}`crawshaw_effect_1975` |
| **9** | a | 0.07 |  |  | 0.07 |  | 0.07 |  | 0.05 |  | 0.18 | 0.18 |  |  |  | 0.19 |  | 0.13 |  |  | 0.06 |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
| **10** | a |  | 0.10 |  | 0.07 |  | 0.07 |  | 0.06 |  | 0.125 | 0.13 |  |  |  | 0.25* |  | 0.15 |  |  | 0.05 |  | Teichner ++ | 1943 | {cite:p}`teichner_assessment_1958` |
|  | b | 0.06 |  |  | 0.09 |  | 0.06 |  | 0.045 |  | 0.19 | 0.095 |  | 0.095 |  | 0.19 |  | 0.115 |  |  |  | 0.06 | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | c | 0.06 |  |  | 0.08 |  | 0.06 |  | 0.05 |  | 0.12 | 0.12 |  | 0.12 |  | 0.19 |  | 0.13 |  |  | 0.07 |  | Colin & Houdas | 1982 | {cite:p}`colin_computation_1971` |
|  | d |  | 0.20 |  | 0.1** |  | 0.05 |  |  |  | 0.20 | 0.05 |  | 0.125(r) |  | 0.125*** |  | 0.075 | 0.075 |  |  |  | Houdas & Ring | 1982 | {cite:p}`colin_computation_1971` |
|  | f | 0.10 |  |  | 0.10 |  |  |  | 0.10 |  | 0.10 | 0.10 |  | 0.10 |  | 0.10 | 0.10 |  | 0.10 |  | 0.10 |  | Stolwijk & Hardy | 1966 | {cite:p}`gagge_comfort_1967` |
| **11** | a | 0.031 |  | 0.043 | 0.082 |  | 0.061 |  | 0.053 |  | 0.166 |  |  | 0.081 | 0.081 | 0.172 |  |  | 0.134 |  | 0.072 |  | Kurata & Funazu | ? | {cite:p}`mochida_tohru_mean_1983` |
|  | b | 0.06 |  |  | 0.07 |  | 0.07 |  | 0.05 |  | 0.09 | 0.09 | 0.09 | 0.09 |  | 0.19 |  | 0.13 |  |  | 0.07 |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
| **12** |  | 0.07 |  |  |  |  | 0.14 |  | 0.05 |  | 0.0875 | 0.0875 | 0.0875 | 0.0875 |  | 0.095 | 0.095 | 0.065 | 0.065 |  | 0.07 |  | Hardy & DuBois | 1938 | {cite:p}`hardy_technic_1938` |
| **14** |  | 0.071 |  | 0.071 | 0.071 | 0.071 |  |  | 0.071 |  | 0.071 | 0.071 | 0.071 | 0.071(r) |  | 0.071(r) | 0.071 | 0.071 | 0.071 |  | 0.071 |  | Olesen + | 1992 | {cite:p}`noauthor_iso_2004,olesen_how_1984` |
| **15** | a | 0.06 |  |  | 0.07 |  | 0.05 |  | 0.0225 | 0.0225 | 0.18 | 0.20 |  |  |  | 0.1025 | 0.1025 | 0.0625 | 0.0625 | 0.0325 | 0.0325 |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |
|  | b | 0.07 |  | 0.07 | 0.07 |  | 0.07 |  | 0.07 |  | 0.07 | 0.07 | 0.07 | 0.07 |  | 0.07* | 0.07 | 0.07 | 0.07 |  | 0.07 |  | Mitchell & Wyndham | 1969 | {cite:p}`mitchell_comparison_1969` |
| **17** |  | 0.037 | 0.037 |  | 0.075 |  | 0.075 |  | 0.025 | 0.025 | 0.0625 | 0.0625 | 0.0625 | 0.0625 | 0.0625 | 0.0875 | 0.0875 | 0.0875 | 0.0875 | 0.0305 | 0.0305 |  | Ouyang | 1985 | {cite:p}`ouyang_clothes_1985` |

:::

**Legend (sites):**  
A: Forehead, B: Left cheek, C: Left neck;  
D: Right upper arm, E: Left elbow, F: Left forearm, G: Left palm, H: Right hand, I: Left hand;  
J: Left back, K: Left chest, L: Left lumbar, M: Abdomen, N: Left buttocks;  
O: Anterior thigh, P: Left {ref}`posterior <label-spatial-orientation>` thigh, Q: Right anterior calf, R: Left posterior calf, S: Left foot, T: Right foot, U: Left sole.

**Notes:**  
(a) measured on the anterior  
(p) measured on the posterior 
(r) measured on the right
(l) measured on the left  
\* measured on anterior thigh and antero-medial thigh (same weighting factor)  
** measured on two locations (anterior and posterior; same weighting factor)  
*** measured on antero-medial thigh  
\+ adopted by ISO 9886:2004  
++ adopted by QREC  

(mean-skin-temperature-calculator)=
## Mean Skin Temperature Calculator
The interactive calculator shows Mean Skin Temperature results using different formulas. The default values are computer generated and do not rely on any real data. The values for each body site can be manually changed, if the selected formula includes those sites.  

```{raw} html
<link rel="stylesheet" href="../../mst-widget/mst-widget.css?v=final">

<div class="mst-widget">
  <div class="mst-top">
    <div class="mst-control">
      <label>Number of sites</label>
      <select data-mst-n></select>
    </div>
    <div class="mst-control">
      <label>Formula</label>
      <select data-mst-formula></select>
    </div>
    <div class="mst-result-wrap">
      <label class="mst-result-label">MST</label>
      <div class="mst-result"><b data-mst-result>—</b></div>
    </div>
  </div>

  <div class="mst-main">
    <div class="mst-figure">
      <img src="../../mst-widget/man_silhouette.svg" alt="body silhouette for skin temperature measurement sites">
      <div data-mst-badges></div>
    </div>

    <aside class="mst-sites-panel">
      <h4>Body-site values</h4>
      <p class="mst-site-note">All A–U sites are listed. Sites not used by the selected formula are locked.</p>
      <div class="mst-sliders" data-mst-sliders></div>
    </aside>
  </div>

  <div class="mst-equation"><code data-mst-text></code></div>
</div>

<script src="../../mst-widget/mst-widget.js?v=final"></script>
```

(mean-body-temperature)=
## Mean Body Temperature

Several formulations of mean body temperature have been proposed, most commonly as weighted combinations of core and mean skin temperature. In addition to differences in weighting coefficients, these formulations also vary in whether "core temperature" refers to a measured anatomical site or a model-defined internal node.

:::{table} Mean body temperature formulations and weighting coefficients
:name: tab-mean-body-temperature-formulas

| Author / formulation | Year | Formula | Core weighting | Skin weighting | Assumed / typical core-temperature input | Rationale / notes | Typical use | Ref |
|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---:|
| Burton | 1935 | {math}`T_b = 0.64\,T_{core} + 0.36\,T_{sk}` | 0.64 | 0.36 | Core site not explicitly fixed; later applications typically use rectal temperature | Derived empirically using whole-body {ref}`calorimetry <label-calorimetry>`; assumes relatively homogeneous core tissues and a peripheral temperature gradient from core to skin | Classical {ref}`thermoregulation <label-thermoregulation>` studies; early heat-balance models | {cite:p}`burton_human_1935` |
| Hardy & DuBois | 1938 | {math}`T_b = 0.70\,T_{core} + 0.30\,T_{sk}` | 0.70 | 0.30 | Typically rectal or equivalent deep-body measurements | Coefficient estimated for neutral environmental conditions | Physiological heat-balance studies | {cite:p}`hardy_basal_1938` |
| Stolwijk & Hardy | 1966 | {math}`T_b = 0.70\,T_{core} + 0.30\,T_{sk}` | 0.70 | 0.30 | Deep-body node in model framework; commonly approximated by rectal or esophageal temperature | Derived from partitional calorimetric studies and two-node thermoregulation modelling under hot conditions | Thermophysiological modelling | {cite:p}`stolwijk_partitional_1966` |
| Snellen | 1966 | {math}`T_b \approx 0.80\,T_{core} + 0.20\,T_{sk}` | ~0.80 | ~0.20 | Deep-body temperature during exercise (often rectal) | Higher core weighting observed during muscular work in hot environments | Exercise physiology; heat-strain research | {cite:p}`snellen_mean_1966` |
| Colin et al. | 1971 | {math}`T_b = a\,T_{core} + (1-a)\,T_{sk}` | 0.64–0.79 | 0.36–0.21 | Rectal temperature typically used | Confirmed Burton coefficient for neutral conditions but showed coefficient increases under extreme heat stress | Thermoregulation experiments | {cite:p}`colin_computation_1971` |

:::
