# The KOTHA Framework: Quantifying Structural Information Loss in Randomized Controlled Trials and Its Impact on Evidence-Based Recommendations

## A Methodological Framework for Harmonizing Observational and Trial Evidence

---

**Authors**: [To be determined]

**Corresponding Author**: [To be determined]

**Keywords**: randomized controlled trials, meta-analysis, observational studies, evidence-based medicine, counterfactual simulation, Bayesian evidence synthesis, GRADE, information size, trial design

---

## Abstract

### Background

Discrepancies between observational study meta-analyses and randomized controlled trial (RCT) meta-analyses are common in clinical research. While such discrepancies are conventionally attributed to confounding in observational studies, an alternative structural explanation exists: RCTs systematically exclude high-risk patients through eligibility criteria and enrollment processes, leading to reduced event rates, insufficient statistical power, and ultimately inadequate information size in meta-analyses.

### Objectives

We propose the KOTHA Framework (Knowledge-driven Observational-Trial Harmonization Approach), a three-module methodological framework that (1) quantifies structural information loss in RCTs through counterfactual power simulation, (2) integrates RCT and observational evidence using hierarchical Bayesian models with explicit bias modeling, and (3) provides interpretation guidelines for low-event RCT meta-analyses to prevent misclassification of inconclusive evidence as evidence of no effect.

### Methods

Module K (Kontrafaktische Power Simulation) uses retrospective cohort data to construct counterfactual trial scenarios, comparing expected power under real-world versus RCT-enrolled risk distributions. Module T (Trial-Observational Bayesian Integration) employs hierarchical Bayesian models with design-specific bias terms to synthesize evidence across study types. Module H (Hermeneutic Guideline Interpreter) operationalizes optimal information size assessment, trial sequential analysis, and standardized recommendation language for guideline committees.

### Expected Results

The framework is expected to demonstrate that for clinical questions where observational and RCT evidence diverge, the divergence can be quantitatively explained by event dilution due to risk-profile shifts during RCT enrollment, and that appropriately discounted integration of observational data can provide more informative estimates for clinical decision-making.

### Conclusions

The KOTHA Framework offers a systematic, reproducible approach to diagnosing and addressing structural underpowering in RCT meta-analyses, with the potential to improve the accuracy of evidence-based treatment recommendations.

---

## 1. Introduction

### 1.1 The Paradox of Discordant Evidence

Evidence-based medicine (EBM) places randomized controlled trials (RCTs) and their meta-analyses at the apex of the evidence hierarchy [1]. This paradigm assumes that RCTs provide the most reliable estimates of treatment effects due to their capacity to minimize confounding through randomization. However, a recurring observation challenges this assumption: for certain clinical questions, meta-analyses of observational (retrospective) studies demonstrate statistically significant treatment benefits, while meta-analyses of RCTs fail to achieve significance [2,3].

The conventional interpretation attributes this discrepancy to residual confounding, selection bias, or publication bias in observational studies. While these explanations are valid in many contexts, they are not universally sufficient. An alternative, complementary explanation focuses on structural limitations within the RCT evidence base itself.

### 1.2 The Structural Information Loss Hypothesis

We propose that the following causal chain explains a substantial proportion of discordant findings:

1. **Representativeness loss**: RCTs lose population representativeness through patient selection processes (eligibility criteria, consent requirements, site capabilities).
2. **Event concentration in excluded populations**: Clinical events (the primary outcomes of interest) occur disproportionately in high-risk subgroups (patients with comorbidities, advanced disease, organ dysfunction) who are preferentially excluded during screening.
3. **Inadequate design compensation**: RCT protocols rarely quantify the expected impact of risk-profile shifts on event rates and adjust sample sizes, follow-up duration, or stratification accordingly.
4. **Systematic underpowering**: The cumulative result is a body of RCTs with insufficient statistical power, producing meta-analyses that lack the information size necessary for definitive conclusions.
5. **Distorted recommendations**: "No significant difference" in underpowered meta-analyses is misinterpreted as "no effect," leading to failure to recommend treatments that may be effective in the target population.

This hypothesis does not claim that all discrepancies are explained by information loss; rather, it argues that structural underpowering is an underrecognized and quantifiable contributor that current evidence evaluation frameworks inadequately address.

### 1.3 Purpose and Scope

This paper introduces the KOTHA Framework (Knowledge-driven Observational-Trial Harmonization Approach), a three-module methodological system designed to:

- **Diagnose** structural information loss in existing RCT evidence (Module K)
- **Integrate** discordant evidence sources with explicit bias modeling (Module T)
- **Guide** interpretation and recommendation under information insufficiency (Module H)

We describe the theoretical foundations, operational specifications, and anticipated applications of each module, illustrated with a hypothetical clinical scenario.

---

## 2. Background

### 2.1 Evidence Discordance: Scope of the Problem

The phenomenon of observational-RCT discordance has been documented across multiple clinical domains:

- **Cardiovascular medicine**: Observational studies suggesting benefits of specific antiarrhythmic strategies not confirmed in RCTs [4]
- **Critical care**: Registry-based evidence supporting interventions that RCTs fail to validate [5]
- **Surgery**: Large database studies showing superiority of surgical approaches not replicated in small, underpowered RCTs [6]

Systematic analyses comparing RCT and observational findings have shown that while agreement is common, discordance occurs in approximately 10-20% of clinical questions, with inadequate power in RCTs cited as a frequent contributing factor [7,8].

### 2.2 The Mechanics of Risk-Profile Shift in RCTs

The transformation from target population to enrolled population occurs through multiple filters:

**Eligibility criteria**: Safety-driven exclusions (organ dysfunction, concurrent medications, comorbidities) systematically remove patients at highest event risk. While necessary for internal validity, these criteria can substantially alter the risk composition of the study population.

**Site selection**: Participating centers tend to be academic or tertiary hospitals with specific referral patterns that may not reflect the broader patient population.

**Consent and protocol compliance**: Complex informed consent procedures and protocol requirements create barriers for elderly, cognitively impaired, or seriously ill patients.

**Investigator discretion**: Even when formally eligible, investigators may exercise judgment to exclude patients perceived as "difficult" or likely to have protocol deviations.

The net effect is a phenomenon we term **event dilution**: the enrolled RCT population has a lower baseline event rate than the target population, directly reducing the expected number of events and, consequently, statistical power.

### 2.3 Information Size and the Limits of Meta-Analysis

The concept of **Optimal Information Size (OIS)** [9,10] recognizes that meta-analyses, like individual trials, require a minimum amount of information (measured in events for time-to-event outcomes, or total sample size for binary outcomes) to produce reliable conclusions. When the cumulative information falls below the OIS, the meta-analysis is analogous to an interim analysis of an underpowered trial --- the result is inconclusive rather than definitive.

**Trial Sequential Analysis (TSA)** [11,12] formalizes this concept by applying monitoring boundaries to cumulative meta-analyses, distinguishing between:

- **Evidence of no effect**: The cumulative Z-curve crosses the futility boundary
- **No evidence of effect**: The cumulative Z-curve has not crossed either boundary and the required information size has not been reached

This distinction is critical but frequently overlooked in guideline development.

### 2.4 Existing Approaches and Their Limitations

Several trial design strategies can mitigate event dilution (Table 1), but their adoption remains limited:

**Table 1: Existing approaches to address event dilution in RCTs**

| Approach | Mechanism | Adoption |
|---|---|---|
| Stratified design | Risk-based stratified randomization and analysis | Common for basic strata; rare for event-driven strata |
| Prognostic enrichment | Intentional enrollment of high-risk patients | Endorsed by FDA/EMA; limited in non-drug trials |
| Event-driven design | Trial endpoints tied to event accrual | Common in cardiology/oncology; rare elsewhere |
| Adaptive design (SSR) | Mid-trial sample size re-estimation | Theoretically powerful; complex and uncommon |
| External data-informed design | Retrospective data to quantify expected event loss | Ideal but very rare in practice |
| Pragmatic/registry-based trials | Minimal exclusions, real-world enrollment | Growing but not yet standard |

The gap is clear: **methodologies exist to prevent information loss, but they are not systematically applied**. Furthermore, no established framework exists to **retrospectively diagnose** information loss in completed RCTs or to **prospectively integrate** discordant evidence sources in a principled manner.

---

## 3. The KOTHA Framework

### 3.1 Overview

The KOTHA Framework comprises three interconnected modules:

- **Module K** (Kontrafaktische Power Simulation): Counterfactual power analysis using retrospective data
- **Module T** (Trial-Observational Bayesian Integration): Hierarchical Bayesian evidence synthesis
- **Module H** (Hermeneutic Guideline Interpreter): Structured interpretation guidelines for low-information meta-analyses

Each module can be applied independently, but the framework achieves maximum impact when all three are used in concert (Figure 1).

### 3.2 Module K: Counterfactual Power Simulation

#### 3.2.1 Rationale

Module K addresses the question: *"If the RCTs in this meta-analysis had enrolled patients with the risk profile of the real-world target population, would their combined evidence have been sufficient to detect the treatment effect observed in observational studies?"*

This is a counterfactual question --- it asks about a scenario that did not occur --- and it is answered through simulation using retrospective (real-world) data as the reference distribution.

#### 3.2.2 Methodological Steps

**Step 1: Define the clinical endpoint and time horizon.**

The analysis should match the endpoint used in the RCTs under evaluation. For time-to-event endpoints (the most common scenario in underpowered settings), the framework uses event counts as the primary measure of information.

**Step 2: Construct a baseline risk model from retrospective data.**

Using a retrospective cohort (registry, administrative database, or electronic health records), fit a prognostic model:

- For binary outcomes: logistic regression yielding P(event | X)
- For time-to-event outcomes: Cox proportional hazards model yielding h(t | X)

where X represents baseline covariates (age, comorbidities, severity scores, laboratory values). The purpose is not to estimate treatment effects but to characterize the **event-generating distribution** of the population.

**Step 3: Define comparison scenarios.**

Three scenarios form the core comparison:

- **Scenario 1 (Real-world target)**: The full retrospective cohort, representing the population for whom the clinical question is relevant
- **Scenario 2 (RCT-enrolled equivalent)**: The retrospective cohort filtered by the eligibility criteria of existing RCTs, approximating the enrolled population
- **Scenario 3 (Design-optimized)**: A modified enrollment strategy (e.g., mandating a minimum proportion of high-risk patients, or using enrichment criteria)

For each scenario, compute the **expected baseline event rate** and the **risk score distribution**.

**Step 4: Specify the treatment effect for simulation.**

Set the treatment effect (e.g., hazard ratio) at multiple values for sensitivity analysis:

- The point estimate from observational meta-analysis (if available)
- Conservative values accounting for possible residual confounding (e.g., attenuated by 20-30%)
- The minimal clinically important difference

**Step 5: Monte Carlo power simulation.**

For each scenario and effect size combination, repeat the following 1,000--10,000 times:

1. Sample N patients from the scenario-specific risk distribution
2. Randomize 1:1 to treatment and control
3. Generate events according to the baseline risk model, with treatment-arm hazards modified by the specified HR
4. Perform the statistical test (log-rank, Cox regression, or proportion test)
5. Record whether p < α

The proportion of simulations achieving significance is the estimated power.

**Step 6: Report results.**

Present results as:
- A table of estimated power by scenario and effect size
- Risk distribution comparisons (density plots or histograms)
- Expected event counts under each scenario (for fixed N and follow-up)
- The sample size required to achieve 80% power under each scenario

#### 3.2.3 Interpretation

Module K does **not** prove that a treatment is effective. It demonstrates whether observed "null" results in RCTs can be structurally explained by information insufficiency due to risk-profile shifts. This reframes the question from "Is treatment A effective?" to "Did the RCTs have sufficient information to answer this question?"

### 3.3 Module T: Hierarchical Bayesian Evidence Integration

#### 3.3.1 Rationale

When Module K establishes that RCT evidence is informationally insufficient, a natural next step is to ask whether incorporating observational evidence --- with appropriate bias adjustments --- can yield more informative treatment effect estimates.

Module T provides a principled framework for this integration, avoiding the false dichotomy of either ignoring observational evidence entirely (the traditional approach) or treating it as equivalent to RCT evidence (which ignores bias concerns).

#### 3.3.2 Model Specification

Let y_i denote the reported effect estimate (e.g., log hazard ratio) from study i, with standard error s_i. The model is:

**Observation level:**
$$y_i \sim \text{Normal}(\theta_i, s_i^2)$$

**Study-level effects:**
$$\theta_i = \mu + u_i + b_i$$

where:
- μ is the overall mean treatment effect (the target of inference)
- u_i captures between-study heterogeneity: u_i ~ Normal(0, τ²)
- b_i captures design-related bias:
  - For RCTs: b_i ~ Normal(0, σ²_RCT) with σ²_RCT small (close to 0)
  - For observational studies: b_i ~ Normal(δ, σ²_OBS) with δ and σ²_OBS reflecting potential bias magnitude and uncertainty

#### 3.3.3 Approaches to Observational Evidence Discounting

Three complementary approaches are implemented for sensitivity analysis:

**Approach 1: Evidence-class bias distributions.** Assign separate prior distributions to b_i based on study design. The key parameters (δ, σ²_OBS) encode the prior belief about the magnitude and variability of bias in observational studies. These can be informed by empirical estimates from the literature on historical discrepancies between RCTs and observational studies in the relevant domain.

**Approach 2: Power priors.** Weight the likelihood contribution of observational studies by a discounting parameter α ∈ [0, 1]:

$$L_{\text{discounted}}(\mu | y_{\text{obs}}) = L(\mu | y_{\text{obs}})^{\alpha}$$

α = 0 ignores observational evidence entirely; α = 1 treats it as equivalent to RCT evidence. Results are presented across a range of α values.

**Approach 3: Robust mixture priors.** Use a mixture prior that automatically downweights observational evidence when it conflicts with RCT evidence:

$$p(\mu) = w \cdot p_{\text{informative}}(\mu | \text{obs data}) + (1-w) \cdot p_{\text{vague}}(\mu)$$

This provides a form of automatic conflict detection and resolution.

#### 3.3.4 Outputs

- Posterior distribution of μ (median, 95% credible interval)
- P(HR < 1): probability that treatment is beneficial
- P(HR < clinically meaningful threshold): probability of clinically meaningful benefit
- Predictive distribution for a future study
- Subgroup-specific absolute effects (ARR, NNT) using baseline risk from Module K

### 3.4 Module H: Hermeneutic Guideline Interpreter

#### 3.4.1 Rationale

Even when Modules K and T provide quantitative evidence of information insufficiency and integrated estimates, the practical impact depends on how this evidence is interpreted and communicated in clinical guidelines. Module H provides a structured decision framework for guideline panels evaluating low-event RCT meta-analyses.

#### 3.4.2 Structured Assessment Checklist

**Assessment 1: Information sufficiency.**
- Report the total number of events across included RCTs
- Calculate the Optimal Information Size (OIS) using the formula for the target effect size
- If total events < OIS, classify as **informationally insufficient** and apply imprecision downgrading

**Assessment 2: Clinical significance of the confidence interval.**
- Evaluate whether the CI spans both clinically meaningful benefit and no effect
- If CI includes substantial benefit (e.g., RR < 0.80) alongside null (RR = 1.0), the conclusion should be **inconclusive** rather than **no effect**

**Assessment 3: Representativeness (indirectness).**
- Compare the risk profile of enrolled RCT populations with the target population
- Use Module K results (if available) to quantify the magnitude of risk-profile shift
- If substantial, apply indirectness downgrading with explicit quantification

**Assessment 4: Trial Sequential Analysis.**
- Apply TSA monitoring boundaries to the cumulative meta-analysis
- Report whether the information fraction has been reached
- If not, explicitly state that the meta-analysis is analogous to an interim analysis

**Assessment 5: Recommendation language.**
- Avoid: "Treatment A is not recommended" (implies evidence of no effect)
- Prefer: "Current RCT evidence is informationally insufficient to determine the effect of Treatment A. Observational evidence suggests potential benefit, particularly in high-risk subgroups. Additional adequately powered trials are needed."
- When Module T results are available, include: "Bayesian integration of all available evidence yields P(benefit) = X%"
- Preserve space for conditional recommendations, particularly for subgroups identified as high-risk

#### 3.4.3 Integration with GRADE

The KOTHA Module H assessments map directly onto existing GRADE domains:

| GRADE Domain | Module H Enhancement |
|---|---|
| Imprecision | OIS-based quantification + TSA boundary assessment |
| Indirectness | Module K-based quantification of risk-profile shift |
| Certainty of evidence | Module T posterior probability as supplementary metric |
| Recommendation formulation | Standardized language distinguishing absence of evidence from evidence of absence |

---

## 4. Illustrative Application: Hypothetical Scenario

### 4.1 Clinical Question

*In patients with acute heart failure and comorbid chronic kidney disease (CKD), does early initiation of Treatment A (vs. standard care B) reduce 1-year all-cause mortality?*

### 4.2 Available Evidence

- **Observational evidence**: Three large retrospective cohort studies (total N = 45,000, events = 8,200) show pooled HR = 0.78 (95% CI: 0.73--0.83) favoring Treatment A
- **RCT evidence**: Four RCTs (total N = 3,800, events = 380) show pooled HR = 0.88 (95% CI: 0.72--1.08), not statistically significant

### 4.3 Module K Application

Using a retrospective registry of 50,000 heart failure patients:

**Risk model**: Cox model with predictors: age, eGFR, NYHA class, NT-proBNP, diabetes, prior MI

**Scenario comparison**:

| Metric | Scenario 1 (Real-world) | Scenario 2 (RCT-equivalent) | Scenario 3 (Enriched) |
|---|---|---|---|
| Mean predicted 1-year event rate | 22% | 12% | 18% |
| Proportion CKD stage ≥3 | 45% | 18% | 35% |
| Expected events (N=1000, 1yr) | 220 | 120 | 180 |

**Power simulation results** (HR = 0.80, N = 3,800 total across 4 trials):

| Scenario | Expected total events | Estimated power |
|---|---|---|
| Scenario 1 (Real-world) | 836 | 82% |
| Scenario 2 (RCT-equivalent) | 456 | 48% |
| Scenario 3 (Enriched) | 684 | 71% |

**Interpretation**: Under the RCT-equivalent risk distribution, the combined trials had only ~48% power to detect HR = 0.80 --- well below the conventional 80% threshold. The "non-significant" result is structurally predictable.

### 4.4 Module T Application

Hierarchical Bayesian model integrating all 7 studies:

| Parameter | RCT-only | Observational-only | KOTHA integrated (α=0.3) | KOTHA integrated (α=0.5) |
|---|---|---|---|---|
| Pooled HR (95% CrI) | 0.88 (0.71--1.09) | 0.78 (0.73--0.83) | 0.82 (0.74--0.91) | 0.80 (0.74--0.87) |
| P(HR < 1) | 89% | >99% | 99% | >99% |
| P(HR < 0.90) | 52% | >99% | 92% | 96% |

**Interpretation**: Even with substantial discounting of observational evidence (α = 0.3), the integrated estimate suggests >99% probability of benefit and 92% probability of clinically meaningful benefit.

### 4.5 Module H Application

1. **Information sufficiency**: OIS for HR = 0.80 ≈ 630 events. Total RCT events = 380. **OIS not met** (information fraction = 60%).
2. **CI assessment**: RCT CI (0.72--1.08) spans clinically meaningful benefit through no effect. **Inconclusive**.
3. **Representativeness**: Module K shows RCT populations had 18% CKD stage ≥3 vs. 45% in real-world. **Substantial indirectness**.
4. **TSA**: Information fraction 60%, monitoring boundary not crossed. **Premature conclusion**.
5. **Recommended language**: "Current RCT evidence is informationally insufficient (380 of 630 required events). Substantial exclusion of high-risk patients (CKD prevalence 18% vs 45% in target population) contributed to event dilution. Bayesian integration with appropriately discounted observational evidence suggests P(HR < 0.90) = 92%. A conditional recommendation favoring Treatment A in high-risk patients (CKD stage ≥3) is supported, with strong need for adequately powered confirmatory trials."

---

## 5. Discussion

### 5.1 Contribution to Evidence-Based Medicine

The KOTHA Framework addresses a recognized but inadequately operationalized gap in evidence evaluation. The concept that RCTs can be underpowered due to enrollment biases is not novel [13,14]; what is novel is the **systematic, quantitative operationalization** of this concept into a reproducible framework that can be applied across clinical domains.

The framework moves beyond the qualitative observation that "RCTs may not be representative" to a quantitative demonstration of *how much* representativeness was lost, *what impact* this had on information content, and *what conclusions* are supported when all evidence is appropriately integrated.

### 5.2 Relationship to Existing Frameworks

**GRADE**: KOTHA is not a replacement for GRADE but an enhancement. Module H maps directly onto GRADE domains (imprecision, indirectness) while providing more precise quantification. The Bayesian integration (Module T) offers a complementary perspective to the frequentist framework underlying standard GRADE assessments.

**Trial Sequential Analysis**: TSA is incorporated within Module H as one component of information sufficiency assessment. KOTHA extends TSA by providing a causal explanation (via Module K) for why information is insufficient.

**Bayesian meta-analysis**: Module T builds on established Bayesian meta-analytic methods [15,16] but adds the specific innovation of design-specific bias modeling calibrated to the observational-RCT discordance context.

### 5.3 Limitations

**Module K** depends on the availability and quality of retrospective data. If the retrospective cohort itself is not representative of the target population, the counterfactual scenarios will be biased. Risk model calibration and external validation are essential.

**Module T** results are sensitive to the specification of bias priors and discounting parameters. This is addressed through mandatory sensitivity analysis, but users must understand that the integrated estimate is conditional on modeling assumptions.

**Module H** requires adoption by guideline committees and systematic review groups, which involves institutional and cultural change beyond methodological innovation.

**General**: The framework addresses information loss but cannot resolve all sources of observational-RCT discordance. Residual confounding in observational studies remains a concern, and Module T's bias adjustments may not fully capture all confounding mechanisms.

### 5.4 Implications for Trial Design

Beyond retrospective analysis, Module K has prospective utility. By quantifying the expected information loss under different enrollment strategies, it can inform:

- **Sample size planning**: Adjusting required N for anticipated event dilution
- **Eligibility criteria optimization**: Balancing safety exclusions against information loss
- **Enrichment thresholds**: Setting minimum high-risk enrollment proportions
- **Endpoint selection**: Choosing endpoints with sufficient event rates across risk strata

### 5.5 Future Directions

1. **Empirical validation**: Apply the KOTHA Framework to clinical questions with well-documented observational-RCT discordance to assess its performance
2. **Software implementation**: Develop open-source tools (R package, Python library) implementing all three modules
3. **Guideline pilot**: Collaborate with guideline development groups to pilot Module H in real recommendation processes
4. **Extension to network meta-analysis**: Adapt the framework for indirect comparisons and network evidence
5. **Machine learning integration**: Explore the use of more flexible risk models in Module K, with appropriate calibration safeguards

---

## 6. Conclusion

The KOTHA Framework (Knowledge-driven Observational-Trial Harmonization Approach) provides a systematic methodology for diagnosing structural information loss in RCT meta-analyses, integrating discordant evidence with explicit bias modeling, and guiding clinical recommendations under information insufficiency.

By reframing the question from "Does the treatment work?" to "Did the evidence base have sufficient information to answer this question?", KOTHA offers a pathway to more nuanced, accurate, and clinically useful evidence evaluation. The framework has the potential to prevent the systematic undervaluation of treatments that appear effective in real-world practice but fail to achieve significance in structurally underpowered trials.

The distinction between "evidence of no effect" and "no evidence of effect" is not merely semantic --- it has direct consequences for patient care. The KOTHA Framework operationalizes this distinction with quantitative rigor.

---

## References

[1] Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924-926.

[2] Concato J, Shah N, Horwitz RI. Randomized, controlled trials, observational studies, and the hierarchy of research designs. N Engl J Med. 2000;342(25):1887-1892.

[3] Anglemyer A, Horvath HT, Bero L. Healthcare outcomes assessed with observational study designs compared with those assessed in randomized trials. Cochrane Database Syst Rev. 2014;(4):MR000034.

[4] Echt DS, Liebson PR, Mitchell LB, et al. Mortality and morbidity in patients receiving encainide, flecainide, or placebo. The Cardiac Arrhythmia Suppression Trial. N Engl J Med. 1991;324(12):781-788.

[5] Ospina-Tascón GA, Büchele GL, Vincent JL. Multicenter, randomized, controlled trials evaluating mortality in intensive care: doomed to fail? Crit Care Med. 2008;36(4):1311-1322.

[6] Stable A, Macaskill P, Irwig L, et al. Could the failure to find a survival advantage of laparoscopic surgery be due to systematic reviews being underpowered? A simulation study. Surg Endosc. 2007;21(12):2263-2267.

[7] Benson K, Hartz AJ. A comparison of observational studies and randomized, controlled trials. N Engl J Med. 2000;342(25):1878-1886.

[8] Ioannidis JP, Haidich AB, Pappa M, et al. Comparison of evidence of treatment effects in randomized and nonrandomized studies. JAMA. 2001;286(7):821-830.

[9] Pogue JM, Yusuf S. Cumulating evidence from randomized trials: utilizing sequential monitoring boundaries for cumulative meta-analysis. Control Clin Trials. 1997;18(6):580-593.

[10] Wetterslev J, Thorlund K, Brok J, Gluud C. Estimating required information size by quantifying diversity in random-effects model meta-analyses. BMC Med Res Methodol. 2009;9:86.

[11] Brok J, Thorlund K, Gluud C, Wetterslev J. Trial sequential analysis reveals insufficient information size and potentially false positive results in many meta-analyses. J Clin Epidemiol. 2008;61(8):763-769.

[12] Thorlund K, Engstrøm J, Wetterslev J, Brok J, Imberger G, Gluud C. User manual for trial sequential analysis (TSA). Copenhagen Trial Unit, Centre for Clinical Intervention Research. 2011.

[13] Kennedy-Martin T, Curtis S, Faries D, Robinson S, Johnston J. A literature review on the representativeness of randomized controlled trial samples and implications for the external validity of trial results. Trials. 2015;16:495.

[14] Rothwell PM. External validity of randomised controlled trials: "to whom do the results of this trial apply?" Lancet. 2005;365(9453):82-93.

[15] Schmidli H, Gsteiger S, Roychoudhury S, O'Hagan A, Spiegelhalter D, Neuenschwander B. Robust meta-analytic-predictive priors in clinical trials with historical control information. Biometrics. 2014;70(4):1023-1032.

[16] Verde PE, Ohmann C. Combining randomized and non-randomized evidence in clinical research: a review of methods and applications. Res Synth Methods. 2015;6(1):45-62.

---

## Figures

**Figure 1**: Overview of the KOTHA Framework showing the three modules and their interconnections.

**Figure 2**: Conceptual illustration of risk-profile shift from target population to RCT-enrolled population, showing event dilution.

**Figure 3**: Hypothetical results from Module K showing power curves under different risk distribution scenarios.

**Figure 4**: Forest plot comparing RCT-only, observational-only, and KOTHA-integrated effect estimates.

**Figure 5**: Trial Sequential Analysis plot showing information fraction and monitoring boundaries.

---

## Supplementary Materials

**Supplement 1**: Mathematical derivations for the optimal information size formula and its relationship to event dilution.

**Supplement 2**: Stan/PyMC code for Module T hierarchical Bayesian model.

**Supplement 3**: R/Python code for Module K counterfactual power simulation.

**Supplement 4**: Complete sensitivity analysis results for the illustrative example.

**Supplement 5**: KOTHA Module H checklist template for guideline committees.
