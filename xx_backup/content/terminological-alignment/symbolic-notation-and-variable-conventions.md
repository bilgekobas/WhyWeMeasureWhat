# Symbolic notation and variable conventions

<div style="overflow-x:auto; -webkit-overflow-scrolling: touch; border: 1px solid #ddd; border-radius: 6px; padding: 0.75rem; margin: 1rem 0;">
  <figure style="margin:0;">
    <figcaption id="tab-symbolic-caption" style="font-weight:600; margin-bottom:0.5rem;">
      Table 6. Physiological variable naming conventions in thermal physiology studies.
    </figcaption>
    <pre aria-describedby="tab-symbolic-caption" style="margin:0; white-space:pre; font-size:0.85em; line-height:1.25;">

Metric family                                  Specific variable / measure          Unit          Common aliases / symbols                                              Notes
--------------------------------------------   ----------------------------------   ----------   ----------------------------------------------------------------   -----------------------------------------
Core body temperature (CBT; Tcore, TCORE,      Rectal temperature                   °C           trect, trec, tr, tre, Trect, Trec, Tr, tre                             tre in ISO 9886
tcore, tcr)                                    Oesophageal temperature              °C           teso, tes, tes, Teso, Tes, Tes                                          tes in ISO 9886
                                               Gastrointestinal telemetry           °C           tab, tgi, tpill, TGI, TPILL                                             tab in ISO 9886
                                               Tympanic temperature                 °C           tty, Tty, Tear                                                         tty in ISO 9886
                                               Aural canal temperature              °C           tac, TAUR                                                               tac in ISO 9886
                                               Oral temperature                     °C           tor, Tor                                                                tor in ISO 9886

Skin temperature                               Local skin temperature               °C           tsk, Tsk, Tskin, Tsk_i                                                  Index i denotes site (e.g., tsk,chest)
                                               Mean skin temperature                °C           tsk, T̄sk, MST, Tmean_skin, Tsk_mean                                     Also tsk in ISO 9886; MST common in building studies
                                               Gradients                            °C, K        ΔTcore–skin, ΔTneck–ankle, ΔTprox–dist, DPG                           Order varies; must define sign convention

Sweat / skin moisture                          Local sweat rate                     mg·cm⁻²·min⁻¹ SW, ṁsw, SRlocal, SR                                            SW in ISO 9886
                                               Whole-body sweat loss                mL, % mass    Δmsw, WBSL, Δm                                                       Δmsw in ISO 9886; WBSL common in sports; Δm in ergonomics
                                               Skin wettedness                      —            w                                                                     —
                                               Electrodermal activity (family)      mS           EDA, SC, GSR                                                          EDA preferred; GSR deprecated; SC may be confused with sweat chloride
                                               Tonic component (level)              mS           SCL, EDA tonic, SC                                                     SCL standard
                                               Phasic component (response)          µS           SCR, SL, EDA phasic                                                    SCR standard; SL used in psychophysiology

Cardiovascular                                 Heart rate                           beats·min⁻¹   HR, bpm                                                               —
                                               Inter-beat interval                  ms           IBI, RR, RRi                                                          RR from ECG; IBI preferred for PPG
                                               Systolic pressure                    mmHg         SBP, Ps                                                              Ps legacy
                                               Diastolic pressure                   mmHg         DBP, Pd                                                              Pd legacy
                                               Mean arterial pressure               mmHg         MAP, Pm                                                              Pm legacy
                                               Stroke volume                        mL           SV                                                                    —
                                               Cardiac output                       L·min⁻¹      Q̇, CO                                                               Dot indicates flow; CO older clinical style

Autonomic modulation (HRV)                     Time-domain indices                  ms           RMSSD, SDNN, pNN50, NNmean                                             Task Force (1996) naming
                                               Frequency-domain indices             ms² or n.u.   LF, HF, LF/HF, TP                                                     LF/HF not dimensioned; n.u. = normalised units
                                               Nonlinear indices                    —            SD1, SD2, SampEn, ApEn                                               Case-sensitive

Vascular control                               Skin blood flow                      PU, % max     SkBF, SBF, Flux                                                       Flux from LDF; PU = perfusion units
                                               Cutaneous vascular conductance       PU·mmHg⁻¹     CVC, CVCnorm                                                          CVC = SkBF / MAP; “norm” if normalised
                                               Forearm blood flow                   mL·min⁻¹·100mL⁻¹ FBF                                                                 —

Metabolic / systemic                           Oxygen consumption                   mL·kg⁻¹·min⁻¹ VO₂, V̇O₂, VO2abs                                                Dot indicates rate
                                               Carbon dioxide production            mL·kg⁻¹·min⁻¹ VCO₂, V̇CO₂                                                       —
                                               Metabolic rate                       W·m⁻², Met    M, Met, qmet                                                         Met capitalised as unit
                                               Respiratory exchange ratio           —            RER, RQ                                                              RER short-term; RQ steady-state
                                               Heat storage rate                    °C·h⁻¹, kJ·kg⁻¹ S, ΔH                                                            ΔH = enthalpy change
                                               Body surface area                    m²           BSA                                                                   Du Bois vs Mosteller constants differ

    </pre>
  </figure>
</div>