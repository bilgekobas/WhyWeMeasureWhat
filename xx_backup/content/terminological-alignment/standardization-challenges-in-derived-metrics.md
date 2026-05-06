# Standardization challenges in derived metrics

Derived physiological metrics often exhibit substantial variability in weighting schemes, anatomical site selection, and reporting conventions. 



(mean-skin-temperature-formulas)=
## Mean Skin Temperature Formulas

Mean skin temperature (MST) provides a paradigmatic example of such fragmentation, with multiple competing formulae and inconsistent site definitions across disciplines.

<div style="overflow-x:auto; -webkit-overflow-scrolling: touch; border: 1px solid #ddd; border-radius: 6px; padding: 0.75rem; margin: 1rem 0;">
  <figure style="margin:0;">
    <figcaption id="tab-mst-formulas-caption" style="font-weight:600; margin-bottom:0.5rem;">
      Table 7. Measurement sites and weighting factors for mean skin temperature formulas.
    </figcaption>
    <pre aria-describedby="tab-mst-formulas-caption" style="margin:0; white-space:pre; font-size:0.85em; line-height:1.25;">

Pts       A       B       C       D          E       F       G      H        I        J        K        L        M           N        O             P        Q        R        S        T        U      by                    Year   Ref
----- --- ------- ------- ------- ---------- ------- ------- ------ -------- -------- -------- -------- -------- ----------- -------- ------------- -------- -------- -------- -------- -------- ------ --------------------- ------ ------------------------------------
3     a                                              0.14                                      0.50                                                          0.36                                       Burton                1935   {cite:p}`mitchell_comparison_1969`
3     b                                              0.14                                      0.50                                                                   0.36                              Olesen                1984   {cite:p}`olesen_how_1984`
3     c   0.25                                       0.50                                                                                                                      0.25                     Cho et al.            1996   {cite:p}`cho_development_1996`
3     d                                              0.30                                      0.35                                                          0.35                                       Wu et al.             2020   {cite:p}`wu_evaluation_2020`

4     a                                              0.15                                      0.34                                   0.33                   0.18                                       Newburgh & Spealman   1943   {cite:p}`teichner_assessment_1958`
4     b                           0.30                                                         0.30                                   0.20                   0.20                                       Ramanathan            1964   {cite:p}`ramanathan_new_1964`
4     c                   0.28                                      0.16              0.28                                                                   0.28                                       ? +                   1992   {cite:p}`noauthor_iso_2004`
4     d                                              0.14                                      0.35                                   0.26                   0.25                                       Wu et al.             2020   {cite:p}`wu_evaluation_2020`

5     a   0.07                                                      0.05                       0.50                                   0.18                   0.20                                       Ouyang                1985   {cite:p}`ouyang_clothes_1985`
5     b           0.07            0.19 (a)                                                              0.175    0.175                              0.39                                                Houdas                1982   {cite:p}`houdas_temperature_1982`
5     c   0.07                                                      0.05                       0.42                                   0.26                   0.20                                       Wu et al.             2020   {cite:p}`wu_evaluation_2020`
5     d   0.20                    0.18                              0.05              0.50                                            0.07                                                              Wang et al.           2013   {cite:p}`wang_human_2013`

6     a           0.14                               0.11    0.05                     0.19     0.19                                   0.32                                                              Ouyang                1985   {cite:p}`ouyang_clothes_1985`
6     b           0.149           0.107                                                        0.186    0.186                         0.186         0.186                                               Teichner              1958   {cite:p}`teichner_assessment_1958`
6     c   0.10                                       0.05           0.05                       0.40                                   0.20                   0.20                                       Miura et al           ?      {cite:p}`mochida_tohru_mean_1983`
6     d   0.11                    0.1                0.13                                      0.28                                   0.21                   0.20                                       Mochida               1983   {cite:p}`mochida_tohru_mean_1983`
6     e           0.14                               0.11           0.05                       0.19     0.19                          0.32                                                              Palmes & Park         1947   {cite:p}`palmes_thermocouples_1947`

7     a   0.07                                       0.14    0.05                              0.35                                   0.19                   0.13                                0.07   Hardy & DuBois        1938   {cite:p}`hardy_technic_1938`
7     b                                              0.14           0.14              0.07     0.07                                   0.14                            0.14     0.14                     Park                  1988   {cite:p}`park_effect_1988`
7     c   0.21                    0.12               0.06                                      0.21              0.17                 0.15                   0.08                                       Nadel                 ?      {cite:p}`mochida_tohru_mean_1983`
7     d                   0.098   0.082              0.114                            0.162    0.166                                  0.182                  0.206                                      Ouyang                1985   {cite:p}`ouyang_clothes_1985`
7     e   0.066                   0.149              0.151                                     0.153             0.153                0.163                  0.183                                      Mochida               1983   {cite:p}`mochida_tohru_mean_1983`
7     f   0.198                   0.138              0.076                                     0.179             0.145                0.153                  0.092                                      Mochida               1983   {cite:p}`mochida_tohru_mean_1983`

8     a                           0.085              0.09                             0.11     0.11     0.11     0.11                 0.23                   0.16                                       Ouyang                1985   {cite:p}`ouyang_clothes_1985`
8     b   0.07                    0.07               0.07           0.05              0.175    0.175                                  0.19                   0.20                                       Gagge & Nishi +       1977   {cite:p}`noauthor_iso_2004,prakash_heat_1977`
8     c   0.21                    0.12               0.06                             0.11     0.10              0.17                 0.15                   0.08                                       Nadel                 1973   {cite:p}`nadel_differential_1973`
8     d   0.07                    0.13               0.12                             0.09     0.09              0.18                 0.16                   0.16                                       Nadel                 1973   {cite:p}`nadel_differential_1973`
8     e   0.19                    0.13               0.12                             0.09     0.08              0.12                 0.12                   0.15                                       Crawshaw              1975   {cite:p}`crawshaw_effect_1975`

9     a   0.07                    0.07               0.07           0.05              0.18     0.18                                   0.19                   0.13                       0.06            Ouyang                1985   {cite:p}`ouyang_clothes_1985`
9     b   0.12                    0.18               0.05           0.04                       0.18              0.16                 0.18                   0.11                       0.08            Neuroth               ?      {cite:p}`houdas_temperature_1982`

10    a           0.10            0.07               0.07           0.06              0.125    0.13                                   0.125*                0.15                       0.05            Teichner ++           1943   {cite:p}`teichner_assessment_1958`
10    b   0.06                    0.09               0.06           0.05              0.19     0.10              0.095                0.19                   0.12                                0.06   Ouyang                1985   {cite:p}`ouyang_clothes_1985`
10    c   0.06                    0.08               0.06           0.05              0.12     0.12              0.12                 0.19                   0.13                       0.07            Colin & Houdas        1982   {cite:p}`colin_computation_1971`
10    d           0.20            0.05**           0.05                             0.20     0.05              0.125 (r)            0.125***            0.075    0.075                             Houdas & Ring         1982   {cite:p}`colin_computation_1971`
10    e           0.10            0.07               0.07           0.06              0.13     0.13                                   0.125**              0.15                       0.05            Omrec                 ?     {cite:p}`houdas_temperature_1982` 
10    f   0.031           0.043   0.082              0.06           0.05              0.17                       0.081       0.081    0.17                            0.134             0.07            Kurata & Funazu       ?      {cite:p}`mochida_tohru_mean_1983`
10    g   0.10                    0.10                              0.10              0.10     0.10              0.10                 0.10          0.10              0.10              0.10            Stolwijk & Hardy      1966   {cite:p}`gagge_comfort_1967`

11        0.06                    0.07               0.07           0.05              0.09     0.09     0.09     0.09                 0.19                   0.13                       0.07            Ouyang                1985   {cite:p}`ouyang_clothes_1985`
12        0.07                                       0.14           0.05              0.0875   0.0875   0.0875   0.0875               0.095         0.095    0.065    0.065             0.07            Hardy & DuBois        1938   {cite:p}`hardy_technic_1938`
13        0.077           0.077   0.077              0.077          0.077             0.077    0.077    0.077    0.077                0.077                  0.077                      0.077           Nielsen               1984   {cite:p}`nielsen_measurement_1984`
14        0.071           0.071   0.071      0.071                  0.071             0.071    0.071    0.071    0.071 (r)            0.071 (r)     0.071    0.071    0.071             0.071           Olesen +              1992   {cite:p}`noauthor_iso_2004,olesen_how_1984`

15    a   0.06                    0.035              0.025          0.0225   0.0225   0.18     0.20                                   0.1025        0.1025   0.0625   0.0625   0.325    0.325           Ouyang                1985   {cite:p}`ouyang_clothes_1985`
15    b   0.07            0.07    0.07               0.07           0.07              0.07     0.07     0.07     0.07                 0.07*        0.07     0.07     0.07              0.07            Mitchell & Wyndham    1969   {cite:p}`mitchell_comparison_1969`

17        0.037   0.037           0.075              0.075          0.025    0.025    0.0625   0.0625   0.0625   0.0625      0.0625   0.0875        0.0875   0.0875   0.0875   0.0305   0.0305          Ouyang                1985   {cite:p}`ouyang_clothes_1985`

  </pre>
  </figure>
</div>

**Legend (sites):**  
A: Forehead, B: Left cheek, C: Left neck;  
D: Right upper arm, E: Left elbow, F: Left forearm, G: Left palm, H: Right hand, I: Left hand;  
J: Left back, K: Left chest, L: Left lumbar, M: Abdomen, N: Left buttocks;  
O: Anterior thigh, P: Left posterior thigh, Q: Right anterior calf, R: Left posterior calf, S: Left foot, T: Right foot, U: Left sole.

**Notes:**  
- (a) measured anteriorly  
- (r) measured on the right  
- '*' measured on anterior thigh and antero-medial thigh (same weighting factor)  
- ** measured on two locations (anterior and posterior; same weighting factor)  
- *** measured on antero-medial thigh  
- '+' adopted by ISO 9886:2004  
- ++ adopted by QREC
