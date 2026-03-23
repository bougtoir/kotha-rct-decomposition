# The KOTHA Framework: a counterfactual simulation and Bayesian integration approach to diagnosing structural information loss in randomized controlled trial meta-analyses

**Authors**: [To be determined]

**Corresponding Author**: [To be determined]

---

## Abstract

**Background**: Discrepancies between meta-analyses of observational studies and randomized controlled trials (RCTs) are conventionally attributed to confounding in observational data. However, an alternative structural explanation --- that RCTs systematically exclude high-risk patients, leading to event dilution and insufficient statistical power --- remains underexplored and poorly operationalized. We developed the KOTHA (Knowledge-driven Observational-Trial Harmonization Approach) Framework to diagnose and address this structural information loss.

**Methods**: The KOTHA Framework comprises three modules. Module K uses counterfactual Monte Carlo power simulation, sampling patients from real-world risk distributions and comparing statistical power under actual RCT enrollment versus target-population scenarios. The simulation study design follows the ADEMP (Aims, Data-generating mechanisms, Estimands, Methods, Performance measures) structure. Module T integrates RCT and observational evidence through hierarchical Bayesian meta-analysis with design-specific bias terms and power-prior discounting. Module H provides a structured checklist for guideline committees based on optimal information size, trial sequential analysis boundaries, and the GRADE framework. We illustrate the framework using a hypothetical clinical scenario of early treatment initiation in acute heart failure patients with comorbid chronic kidney disease.

**Results**: In the illustrative scenario, applying RCT eligibility criteria to a real-world cohort reduced the mean baseline 1-year event rate from 22% to 12%, and the proportion of patients with CKD stage $\geq$ 3 from 45% to 18%. Counterfactual power simulation (Module K) estimated that under the RCT-enrolled risk distribution, the cumulative evidence (N = 3,800, 380 events) had only 48% power to detect a hazard ratio (HR) of 0.80, compared with 82% power under the real-world risk distribution. Bayesian integration (Module T) with observational evidence discounted at $\alpha$ = 0.3 yielded a posterior HR of 0.82 (95% CrI: 0.74--0.91) with P(HR < 1) > 99%. Module H assessment identified that only 60% of the optimal information size had been reached, classifying the RCT evidence as informationally insufficient.

**Conclusions**: The KOTHA Framework provides a reproducible, quantitative approach to distinguishing "evidence of no effect" from "no evidence of effect" in underpowered RCT meta-analyses. By integrating counterfactual simulation, Bayesian evidence synthesis, and structured interpretation guidelines, the framework may help prevent undervaluation of treatments that appear effective in real-world practice but fail to achieve statistical significance in structurally underpowered trials.

**Keywords**: randomized controlled trials, meta-analysis, observational studies, evidence-based medicine, counterfactual simulation, Bayesian evidence synthesis, GRADE, optimal information size, trial sequential analysis, power analysis

---

## Background

Evidence-based medicine (EBM) places randomized controlled trials (RCTs) and their meta-analyses at the apex of the evidence hierarchy [1]. This paradigm rests on the principle that randomization minimizes confounding, providing the most internally valid estimates of treatment effects. However, a recurring challenge in clinical research is the discordance between meta-analyses of observational studies and RCTs: for certain clinical questions, observational evidence demonstrates statistically significant treatment benefit, whereas RCT meta-analyses fail to reach significance [2, 3].

The conventional interpretation attributes this discrepancy to residual confounding, selection bias, or publication bias in observational data. While these explanations are valid in many contexts, an alternative structural explanation deserves systematic attention: RCTs may suffer from **structural information loss** --- a cascade of enrollment processes that systematically exclude high-risk patients, reduce event rates, and produce meta-analyses with insufficient statistical information to detect clinically meaningful effects.

### The structural information loss hypothesis

We hypothesize that the following five-step causal chain explains a substantial proportion of observational-RCT discordance:

1. **Representativeness loss**: RCTs lose population representativeness through eligibility criteria, consent requirements, and site selection [4, 5].
2. **Event concentration in excluded populations**: Clinical events occur disproportionately in high-risk subgroups (patients with comorbidities, advanced disease, organ dysfunction) who are preferentially excluded during screening.
3. **Inadequate design compensation**: RCT protocols rarely quantify the expected impact of risk-profile shifts on event rates and do not adjust sample sizes, follow-up duration, or stratification accordingly.
4. **Systematic underpowering**: The cumulative result is a body of RCTs with insufficient statistical power, producing meta-analyses that lack the information size necessary for definitive conclusions.
5. **Distorted recommendations**: "No significant difference" in underpowered meta-analyses is misinterpreted as "no effect," leading to failure to recommend treatments that may be effective in the target population.

### Optimal information size and trial sequential analysis

The concept of optimal information size (OIS) [6, 7] recognizes that meta-analyses, like individual trials, require a minimum amount of information to produce reliable conclusions. When cumulative information falls below the OIS, the meta-analysis result is inconclusive rather than definitive. Trial sequential analysis (TSA) [8, 9] formalizes this concept by applying sequential monitoring boundaries, distinguishing between evidence of no effect (the cumulative Z-curve crosses the futility boundary) and no evidence of effect (the monitoring boundary has not been crossed and the required information size has not been reached). This distinction is critical but frequently overlooked in guideline development.

### Existing approaches to mitigate event dilution

Several trial design strategies can mitigate event dilution (Table 1), but their adoption remains limited and no established framework exists to retrospectively diagnose information loss in completed RCTs or to prospectively integrate discordant evidence sources in a principled manner.

### Aim

We developed the KOTHA (Knowledge-driven Observational-Trial Harmonization Approach) Framework, a three-module methodological system designed to (1) diagnose structural information loss through counterfactual power simulation (Module K), (2) integrate discordant evidence using hierarchical Bayesian meta-analysis (Module T), and (3) guide interpretation and recommendation under information insufficiency (Module H). This paper describes the framework's methodological foundations and demonstrates its application through an illustrative clinical scenario.

---

## Methods

### Overview of the KOTHA Framework

The KOTHA Framework comprises three interconnected modules (Fig. 1):

- **Module K** (Kontrafaktische Power Simulation): Counterfactual power analysis using retrospective data
- **Module T** (Trial-Observational Bayesian Integration): Hierarchical Bayesian evidence synthesis with design-specific bias modeling
- **Module H** (Hermeneutic Guideline Interpreter): Structured interpretation guidelines for low-information meta-analyses mapped to the GRADE framework

Each module can be applied independently, but the framework achieves maximum utility when all three modules are applied in sequence. Module K outputs feed into Module T (baseline risk distributions for absolute effect estimation) and Module H (quantification of risk-profile shift for indirectness assessment).

### Module K: Counterfactual power simulation

Module K addresses the question: *"If the RCTs in this meta-analysis had enrolled patients with the risk profile of the real-world target population, would their combined evidence have been sufficient to detect the treatment effect observed in observational studies?"*

The simulation study component of Module K is described below following the ADEMP structure [10].

#### Aims

The aim of the Module K simulation is to estimate statistical power under counterfactual enrollment scenarios. Specifically, we compare the expected power of a meta-analysis when patients are drawn from (a) the actual RCT-enrolled risk distribution versus (b) the real-world target population risk distribution, for a given treatment effect size. This quantifies the degree to which enrollment-driven risk-profile shifts reduce the information content of the trial evidence.

#### Data-generating mechanisms

The data-generating process proceeds as follows:

1. **Baseline risk model construction**: Using a retrospective cohort (registry, administrative database, or electronic health records), fit a prognostic model to characterize the event-generating distribution. For time-to-event outcomes, a Cox proportional hazards model is used: $h(t \mid X) = h_0(t) \cdot \exp(X\beta)$, where $X$ represents baseline covariates (age, comorbidities, severity scores, laboratory values). For binary outcomes, logistic regression is used: $P(\text{event} \mid X) = \text{logit}^{-1}(X\beta)$. The purpose is to characterize baseline risk, not to estimate treatment effects.

2. **Scenario definition**: Three enrollment scenarios are defined:
   - *Scenario S1 (real-world target)*: The full retrospective cohort, representing the population for whom the clinical question is relevant.
   - *Scenario S2 (RCT-enrolled equivalent)*: The retrospective cohort filtered by the published eligibility criteria of existing RCTs, approximating the enrolled population.
   - *Scenario S3 (design-optimized)*: A modified enrollment strategy incorporating prognostic enrichment (e.g., mandating a minimum proportion of high-risk patients).

3. **Treatment effect specification**: The true treatment effect (e.g., hazard ratio, HR) is set at multiple values:
   - The point estimate from the observational meta-analysis (if available)
   - Attenuated values accounting for possible residual confounding (e.g., HR multiplied by 1.2 or 1.3)
   - The minimal clinically important difference

4. **Event generation**: For each simulated patient, baseline risk is sampled from the scenario-specific covariate distribution. Events are generated for the control arm according to the fitted risk model and for the treatment arm with hazards modified by the specified HR, assuming proportional hazards.

#### Estimands

The primary estimand is statistical power: the probability of rejecting the null hypothesis $H_0$: HR $\geq$ 1 at significance level $\alpha$ = 0.05 (two-sided) under the specified alternative HR, for each enrollment scenario.

Secondary estimands include:
- Expected number of events under each scenario for fixed total N and follow-up duration
- Sample size required to achieve 80% power under each scenario
- Event rate ratio between scenarios (quantifying the magnitude of event dilution)

#### Methods

For each combination of enrollment scenario and treatment effect size, 10,000 Monte Carlo replications are performed:

1. Sample N patients (matching the cumulative sample size of the actual RCTs) from the scenario-specific risk distribution by resampling with replacement from the filtered retrospective cohort.
2. Randomly assign patients 1:1 to treatment and control arms.
3. Generate event times for each patient based on the fitted risk model, applying the specified HR for treatment-arm patients. Administrative censoring is applied at the trial-specific follow-up duration.
4. Conduct the primary statistical test (log-rank test or Cox regression) at the two-sided $\alpha$ = 0.05 level.
5. Record whether the null hypothesis was rejected.

Power is estimated as the proportion of replications achieving rejection, with Monte Carlo standard errors computed as $\sqrt{\hat{p}(1 - \hat{p})/B}$, where $B$ is the number of replications.

#### Performance measures

The primary performance measure is estimated power with its Monte Carlo 95% confidence interval. Comparisons across scenarios are reported as power differences (absolute) and power ratios. Secondary performance measures include the mean and variance of the estimated log-HR across replications (to assess bias in estimation), and the coverage probability of 95% confidence intervals.

### Module T: Hierarchical Bayesian evidence integration

#### Rationale

When Module K establishes that RCT evidence is informationally insufficient, Module T provides a principled framework for integrating observational and RCT evidence, avoiding the dichotomy of either ignoring observational evidence entirely or treating it as equivalent to RCT evidence.

#### Model specification

Let $y_i$ denote the reported log hazard ratio from study $i$, with standard error $s_i$. The hierarchical model is:

**Observation level:**

$$y_i \sim \text{Normal}(\theta_i, s_i^2)$$

**Study-level effects:**

$$\theta_i = \mu + u_i + b_i$$

where:
- $\mu$ is the overall mean treatment effect (the target of inference)
- $u_i \sim \text{Normal}(0, \tau^2)$ captures between-study heterogeneity
- $b_i$ captures design-related bias, with design-specific priors:
  - For RCTs: $b_i \sim \text{Normal}(0, \sigma^2_{\text{RCT}})$, where $\sigma^2_{\text{RCT}}$ is constrained to be small (e.g., half-normal prior with scale 0.05)
  - For observational studies: $b_i \sim \text{Normal}(\delta, \sigma^2_{\text{OBS}})$, where $\delta$ represents the expected direction and magnitude of confounding bias, and $\sigma^2_{\text{OBS}}$ represents uncertainty in bias magnitude

#### Prior specifications

Priors are specified as follows:
- $\mu \sim \text{Normal}(0, 10^2)$ (weakly informative)
- $\tau \sim \text{Half-Cauchy}(0, 0.5)$
- $\delta \sim \text{Normal}(0, \sigma_\delta^2)$, where $\sigma_\delta$ is informed by empirical estimates of observational-RCT discrepancies in the relevant clinical domain [11, 12]
- $\sigma_{\text{OBS}} \sim \text{Half-Cauchy}(0, 0.5)$

#### Sensitivity analyses via alternative discounting approaches

Three complementary approaches are implemented:

**Approach 1: Design-class bias distributions** (primary analysis). The model above with empirically calibrated bias priors.

**Approach 2: Power priors** [13]. The likelihood contribution of observational studies is weighted by a discounting parameter $\alpha \in [0, 1]$:

$$L_{\text{discounted}}(\mu \mid y_{\text{obs}}) = L(\mu \mid y_{\text{obs}})^{\alpha}$$

Results are presented across a grid of $\alpha$ values (0, 0.1, 0.2, ..., 1.0).

**Approach 3: Robust mixture priors** [14]. A mixture prior incorporates observational evidence with automatic conflict detection:

$$p(\mu) = w \cdot p_{\text{informative}}(\mu \mid \text{obs data}) + (1 - w) \cdot p_{\text{vague}}(\mu)$$

where $w$ is estimated from the data, allowing the model to downweight observational evidence when it conflicts with RCT findings.

#### Model outputs

- Posterior distribution of $\mu$: median, 95% credible interval (CrI)
- P(HR < 1): posterior probability of any treatment benefit
- P(HR < $c$): posterior probability that the HR is below a clinically meaningful threshold $c$
- Posterior predictive distribution for a hypothetical future study
- Subgroup-specific absolute risk reductions (ARR) and numbers needed to treat (NNT), computed using baseline risk estimates from Module K

#### Computational details

Models are implemented in Stan [15] via the R interface (rstan or cmdstanr). Four chains of 4,000 iterations (2,000 warmup) are run. Convergence is assessed using $\hat{R}$ < 1.01, effective sample size > 400 per parameter, and visual inspection of trace plots.

### Module H: Hermeneutic guideline interpreter

Module H translates the quantitative outputs of Modules K and T into a structured assessment for guideline committees. It comprises a five-point checklist that maps onto the GRADE framework [1] (Table 2).

#### Assessment 1: Information sufficiency (GRADE imprecision domain)

Calculate the optimal information size (OIS) for the target effect size using the formula for the required number of events in a two-arm trial [6]. Compare with the total number of events in the meta-analysis. If total events < OIS, classify the evidence as informationally insufficient.

#### Assessment 2: Confidence interval assessment (GRADE imprecision domain)

Evaluate whether the confidence interval of the pooled RCT effect estimate spans both clinically meaningful benefit (e.g., RR < 0.80) and no effect (RR = 1.0). If so, the conclusion should be "inconclusive" rather than "no effect."

#### Assessment 3: Representativeness assessment (GRADE indirectness domain)

Compare the risk profile of enrolled RCT populations with the target population. When Module K results are available, report the event rate ratio between scenarios S1 and S2. If the ratio exceeds a prespecified threshold (e.g., > 1.5), apply indirectness downgrading with explicit quantification.

#### Assessment 4: Trial sequential analysis (GRADE imprecision domain)

Apply TSA monitoring boundaries to the cumulative meta-analysis. Report whether the required information size has been reached and whether the cumulative Z-curve has crossed an efficacy or futility boundary. If neither boundary has been crossed and the information fraction is < 100%, explicitly state that the meta-analysis is analogous to an interim analysis.

#### Assessment 5: Recommendation language

Provide standardized templates for recommendation language that distinguish between:
- "Evidence of no effect": TSA futility boundary crossed (strong language permissible)
- "No evidence of effect (informationally insufficient)": OIS not met, TSA boundaries not crossed (conditional language required)
- "Integrated evidence suggests benefit": Module T posterior probability exceeds threshold (conditional recommendation with explicit uncertainty quantification)

### Illustrative scenario specification

To demonstrate the framework, we constructed a hypothetical clinical scenario based on plausible parameter values derived from the published literature on heart failure interventions:

**Clinical question**: In patients with acute heart failure and comorbid chronic kidney disease (CKD), does early initiation of Treatment A (vs. standard care) reduce 1-year all-cause mortality?

**Available evidence**:
- *Observational evidence*: Three large retrospective cohort studies (total N = 45,000; 8,200 events) with pooled HR = 0.78 (95% CI: 0.73--0.83) favoring Treatment A [hypothetical]
- *RCT evidence*: Four RCTs (total N = 3,800; 380 events) with pooled HR = 0.88 (95% CI: 0.72--1.08), not statistically significant [hypothetical]

**Real-world reference population**: A hypothetical registry of 50,000 heart failure patients with documented CKD status, comorbidities, and 1-year mortality follow-up.

All numerical values in the illustrative scenario are hypothetical and intended solely to demonstrate the framework's application.

---

## Results

### Module K: Counterfactual power simulation

#### Risk-profile shift quantification

Applying published RCT eligibility criteria to the hypothetical real-world registry produced the following comparison (Table 3):

**Table 3: Risk-profile comparison between enrollment scenarios**

| Metric | S1 (Real-world) | S2 (RCT-equivalent) | S3 (Enriched) |
|---|---|---|---|
| Mean predicted 1-year event rate | 22% | 12% | 18% |
| Median predicted 1-year event rate | 19% | 10% | 16% |
| Proportion CKD stage $\geq$ 3 | 45% | 18% | 35% |
| Mean age (years) | 72 | 64 | 68 |
| Proportion with diabetes | 42% | 28% | 38% |
| Event rate ratio vs. S1 | 1.00 | 0.55 | 0.82 |

The eligibility criteria reduced the mean baseline event rate by 45% (from 22% to 12%), primarily by excluding patients with CKD stage $\geq$ 3 (reduced from 45% to 18% of the enrolled population), advanced age, and multiple comorbidities.

#### Power simulation results

Table 4 presents the estimated power for the cumulative RCT evidence (N = 3,800) under each scenario and a range of true treatment effects.

**Table 4: Estimated power (%) by enrollment scenario and true hazard ratio (N = 3,800; 10,000 replications)**

| True HR | S1 (Real-world) | S2 (RCT-equivalent) | S3 (Enriched) |
|---|---|---|---|
| 0.70 | 97 (97--98) | 78 (77--79) | 92 (91--93) |
| 0.75 | 91 (90--92) | 63 (62--64) | 82 (81--83) |
| 0.80 | 82 (81--83) | 48 (47--49) | 71 (70--72) |
| 0.85 | 66 (65--67) | 33 (32--34) | 54 (53--55) |
| 0.90 | 45 (44--46) | 21 (20--22) | 35 (34--36) |

Values in parentheses represent Monte Carlo 95% confidence intervals.

At the observational point estimate (HR = 0.78), the RCT-equivalent scenario (S2) yielded only 55% power, compared with 87% under the real-world scenario (S1). Even assuming a more conservative effect (HR = 0.85, accounting for approximately 30% confounding attenuation), power under S2 was only 33%.

#### Required sample size analysis

To achieve 80% power at HR = 0.80, the required cumulative sample sizes were:

- S1 (Real-world risk distribution): N = 3,400 (approximately the actual cumulative N)
- S2 (RCT-equivalent risk distribution): N = 7,800 (approximately 2.3 times the actual N)
- S3 (Enriched risk distribution): N = 4,600

### Module T: Bayesian evidence integration

Table 5 presents the integrated treatment effect estimates under varying degrees of observational evidence discounting.

**Table 5: Posterior treatment effect estimates by discounting approach**

| Analysis | Pooled HR (95% CrI) | P(HR < 1) | P(HR < 0.90) | P(HR < 0.80) |
|---|---|---|---|---|
| RCT-only (frequentist) | 0.88 (0.72--1.08) | --- | --- | --- |
| RCT-only (Bayesian) | 0.88 (0.70--1.10) | 89% | 52% | 27% |
| Observational-only | 0.78 (0.73--0.83) | > 99% | > 99% | 56% |
| Integrated ($\alpha$ = 0.1) | 0.86 (0.72--1.03) | 95% | 65% | 32% |
| Integrated ($\alpha$ = 0.3) | 0.82 (0.74--0.91) | > 99% | 92% | 53% |
| Integrated ($\alpha$ = 0.5) | 0.80 (0.74--0.87) | > 99% | 96% | 55% |
| Integrated (bias-adjusted) | 0.83 (0.73--0.94) | 99% | 87% | 42% |
| Integrated (robust mixture) | 0.84 (0.74--0.95) | 99% | 84% | 39% |

CrI, credible interval.

All three integration approaches (power prior, bias-adjusted, robust mixture) yielded posterior estimates suggesting > 99% probability of any benefit and 84--92% probability that the HR is below 0.90. The credible intervals excluded 1.0 for all integration approaches with $\alpha \geq$ 0.3.

#### Absolute effect estimates by risk subgroup

Using Module K baseline risk estimates, we computed subgroup-specific absolute risk reductions (Table 6).

**Table 6: Estimated absolute risk reduction and NNT by risk subgroup (Module T integrated estimate, $\alpha$ = 0.3; HR = 0.82)**

| Risk subgroup | Baseline 1-year mortality | ARR (95% CrI) | NNT (95% CrI) |
|---|---|---|---|
| Low risk (event rate 8%) | 8% | 1.5% (0.7--2.2%) | 67 (45--143) |
| Moderate risk (event rate 15%) | 15% | 2.8% (1.4--4.0%) | 36 (25--71) |
| High risk (event rate 25%) | 25% | 4.8% (2.4--6.8%) | 21 (15--42) |
| Very high risk (event rate 35%) | 35% | 6.8% (3.4--9.5%) | 15 (11--29) |

ARR, absolute risk reduction; NNT, number needed to treat.

### Module H: Structured guideline assessment

Applying the Module H checklist to the illustrative scenario:

**Assessment 1 (Information sufficiency)**: The OIS for detecting HR = 0.80 at $\alpha$ = 0.05 (two-sided) with 80% power was estimated at 630 events. The total RCT events were 380 (information fraction = 60%). **Classification: informationally insufficient.**

**Assessment 2 (CI assessment)**: The RCT 95% CI (0.72--1.08) spans from substantial benefit (HR = 0.72) through no effect (HR = 1.08). The confidence interval is consistent with both clinically important benefit and null effect. **Classification: inconclusive.**

**Assessment 3 (Representativeness)**: Module K identified that the RCT-enrolled population had substantially lower baseline risk than the target population (event rate ratio S2/S1 = 0.55). CKD stage $\geq$ 3 prevalence was reduced from 45% to 18%. **Classification: serious indirectness for the high-risk subgroup.**

**Assessment 4 (TSA)**: At an information fraction of 60%, the cumulative Z-curve had not crossed either the efficacy boundary or the futility boundary. **Classification: meta-analysis analogous to an interim analysis; neither benefit nor futility can be concluded from RCT data alone.**

**Assessment 5 (Recommendation language)**:

> "Current RCT evidence is informationally insufficient to determine the effect of Treatment A on 1-year all-cause mortality in heart failure patients with CKD (380 of 630 required events; information fraction 60%). Substantial exclusion of high-risk patients during RCT enrollment (CKD prevalence 18% vs. 45% in the target population) contributed to event dilution. Trial sequential analysis indicates that neither benefit nor futility boundaries have been crossed. Bayesian integration of all available evidence, with observational data discounted to 30% weight, yields HR = 0.82 (95% CrI: 0.74--0.91), P(HR < 0.90) = 92%. A conditional recommendation favoring Treatment A in high-risk patients (CKD stage $\geq$ 3) is supported, with recognition of moderate uncertainty. Adequately powered trials enrolling sufficient high-risk patients are strongly recommended."

**Table 7: Module H assessment mapped to GRADE domains**

| GRADE domain | Standard assessment | KOTHA-enhanced assessment |
|---|---|---|
| Risk of bias | Low (RCTs) | Low (RCTs) |
| Inconsistency | Low ($I^2$ = 15%) | Low ($I^2$ = 15%) |
| Indirectness | Not typically assessed quantitatively for internal enrollment bias | Serious: event rate ratio 0.55; CKD prevalence 18% vs. 45% |
| Imprecision | Serious (CI crosses null) | Very serious: OIS not met (60% information fraction); TSA boundaries not crossed |
| Publication bias | Not suspected | Not suspected |
| Overall certainty | Low (downgraded 1 level for imprecision) | Very low (downgraded 2 levels for imprecision + 1 level for indirectness) |
| Recommendation | "Treatment A is not recommended" | "Conditional recommendation for Treatment A in high-risk patients; evidence informationally insufficient for definitive conclusion" |

---

## Discussion

### Principal findings

The KOTHA Framework provides a systematic, quantitative approach to a problem that is well recognized but poorly operationalized in evidence-based medicine: the interpretation of discordant evidence from observational studies and RCTs. Applied to our illustrative scenario, the framework revealed that (1) RCT enrollment criteria reduced the baseline event rate by 45%, (2) the resulting meta-analysis had only 48% power to detect the observational effect estimate, (3) Bayesian integration with conservatively discounted observational evidence yielded high posterior probability of benefit, and (4) the standard GRADE assessment was substantially modified when KOTHA-enhanced assessments were applied.

### Comparison with existing methods

Several existing methodologies address components of the problem that KOTHA integrates.

**Counterfactual simulation**: Target trial emulation methods [16, 17] use observational data to emulate specific trial designs, primarily to estimate treatment effects. Module K differs in its focus: rather than estimating effects, it quantifies the **information loss** attributable to trial design decisions. This diagnostic orientation is complementary to target trial emulation.

**Bayesian evidence synthesis**: Methods for combining RCT and observational evidence have been proposed [14, 18, 19], including hierarchical models with design-specific bias terms, power priors, and meta-analytic-predictive priors. Module T builds on these methods but integrates them within a broader framework that explicitly links the need for integration (diagnosed by Module K) with the interpretation of integrated estimates (operationalized by Module H).

**Information size and TSA**: The concepts of optimal information size [6, 7] and trial sequential analysis [8, 9] are established but underutilized in guideline development. Module H embeds these assessments within a structured checklist and provides standardized recommendation language, lowering the barrier to adoption.

**GRADE**: The GRADE framework [1] provides domains for assessing evidence certainty but does not currently include tools for quantifying the contribution of enrollment-driven event dilution to imprecision or indirectness. KOTHA provides quantitative inputs to these domains without modifying the GRADE structure itself.

### Implications for clinical practice

The practical significance of KOTHA lies in its capacity to change the interpretation of "negative" RCT meta-analyses. In our illustrative example, the standard interpretation --- "no significant benefit, therefore not recommended" --- is replaced by a nuanced assessment that recognizes information insufficiency, quantifies the structural reasons for it, and provides an integrated estimate that accounts for all available evidence. This may be particularly important in clinical domains where:

- The target population is inherently high-risk but RCTs preferentially enroll lower-risk patients
- Events are rare or require long follow-up, making adequately powered RCTs expensive and time-consuming
- Observational evidence from large databases is abundant and of high methodological quality
- Guideline recommendations have direct consequences for treatment access (e.g., formulary decisions, insurance coverage)

### Implications for trial design

Module K has prospective utility beyond retrospective analysis. By quantifying expected information loss under different enrollment strategies before a trial is conducted, it can inform:

- Sample size planning adjusted for anticipated event dilution
- Eligibility criteria optimization, balancing safety exclusions against information loss
- Enrichment threshold specification (minimum high-risk enrollment proportions)
- Endpoint selection favoring outcomes with sufficient event rates across risk strata

### Strengths and limitations

**Strengths**: The KOTHA Framework integrates three complementary analytical approaches into a coherent workflow. The simulation component (Module K) follows the ADEMP reporting structure for transparency and reproducibility [10]. The Bayesian integration (Module T) provides multiple discounting approaches with mandatory sensitivity analysis, avoiding reliance on any single assumption about observational evidence quality. The guideline interpretation module (Module H) maps directly onto the established GRADE framework, facilitating adoption.

**Limitations**: Several important limitations should be acknowledged.

First, Module K depends on the availability and quality of retrospective data. If the retrospective cohort is not representative of the target population, the counterfactual scenarios will be biased. External validation of the risk model is essential.

Second, Module T results are sensitive to the specification of bias priors and discounting parameters. While sensitivity analysis across multiple approaches is mandatory, the interpretation of integrated estimates remains conditional on modeling assumptions. Users must be transparent about these assumptions and their impact on conclusions.

Third, Module H requires adoption by guideline committees and systematic review groups, which involves institutional and cultural change beyond methodological innovation.

Fourth, the framework as presented here has been demonstrated using a single hypothetical scenario with constructed data. Empirical validation across multiple real clinical questions is necessary to establish its practical utility.

Fifth, the framework addresses information loss due to enrollment-driven event dilution but cannot resolve all sources of observational-RCT discordance. Residual confounding in observational studies remains a genuine concern, and Module T's bias adjustments may not fully capture all confounding mechanisms.

### Future research

Several directions for future work are identified:

1. **Empirical validation**: Apply the KOTHA Framework to clinical questions with well-documented observational-RCT discordance to assess performance against known ground truth (where available) or against expert consensus.
2. **Software development**: Develop open-source tools (R package and Python library) implementing all three modules with standardized reporting templates.
3. **Guideline pilot**: Collaborate with guideline development groups to pilot Module H in real recommendation processes and evaluate its impact on recommendation language and certainty ratings.
4. **Extension to network meta-analysis**: Adapt the framework for indirect comparisons and network evidence synthesis.
5. **Calibration of bias priors**: Conduct systematic empirical studies to estimate the distribution of observational-RCT discrepancies by clinical domain, providing calibrated priors for Module T.
6. **Flexible risk models**: Evaluate machine learning-based risk models for Module K (e.g., gradient boosting, neural networks) with appropriate calibration assessment, comparing performance against conventional regression models.

---

## Conclusions

The KOTHA Framework (Knowledge-driven Observational-Trial Harmonization Approach) addresses the underrecognized problem of structural information loss in RCT meta-analyses through three complementary modules: counterfactual power simulation (Module K), hierarchical Bayesian evidence integration (Module T), and structured guideline interpretation (Module H). The framework provides a reproducible, quantitative approach to distinguishing "evidence of no effect" from "no evidence of effect" --- a distinction with direct consequences for clinical recommendations and patient care.

By reframing the question from "Does the treatment work?" to "Did the evidence base have sufficient information to answer this question?", KOTHA offers a pathway to more nuanced and clinically useful evidence evaluation, with the potential to prevent systematic undervaluation of treatments that may benefit the patients who need them most.

---

## List of abbreviations

| Abbreviation | Definition |
|---|---|
| ADEMP | Aims, Data-generating mechanisms, Estimands, Methods, Performance measures |
| ARR | Absolute risk reduction |
| CKD | Chronic kidney disease |
| CrI | Credible interval |
| CI | Confidence interval |
| EBM | Evidence-based medicine |
| GRADE | Grading of Recommendations Assessment, Development and Evaluation |
| HR | Hazard ratio |
| KOTHA | Knowledge-driven Observational-Trial Harmonization Approach |
| NNT | Number needed to treat |
| OIS | Optimal information size |
| RCT | Randomized controlled trial |
| TSA | Trial sequential analysis |

---

## Declarations

### Ethics approval and consent to participate

Not applicable. This study proposes a methodological framework and uses only hypothetical data for illustration.

### Consent for publication

Not applicable.

### Availability of data and materials

No empirical data were used in this study. The illustrative scenario is based on hypothetical parameter values. Software implementing the KOTHA Framework will be made available upon publication [repository URL to be determined].

### Competing interests

The authors declare that they have no competing interests.

### Funding

[To be determined]

### Authors' contributions

[To be determined]

### Acknowledgements

[To be determined]

---

## References

1. Guyatt GH, Oxman AD, Vist GE, Kunz R, Falck-Ytter Y, Alonso-Coello P, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924--6.
2. Concato J, Shah N, Horwitz RI. Randomized, controlled trials, observational studies, and the hierarchy of research designs. N Engl J Med. 2000;342(25):1887--92.
3. Anglemyer A, Horvath HT, Bero L. Healthcare outcomes assessed with observational study designs compared with those assessed in randomized trials. Cochrane Database Syst Rev. 2014;(4):MR000034.
4. Kennedy-Martin T, Curtis S, Faries D, Robinson S, Johnston J. A literature review on the representativeness of randomized controlled trial samples and implications for the external validity of trial results. Trials. 2015;16:495.
5. Rothwell PM. External validity of randomised controlled trials: "to whom do the results of this trial apply?" Lancet. 2005;365(9453):82--93.
6. Pogue JM, Yusuf S. Cumulating evidence from randomized trials: utilizing sequential monitoring boundaries for cumulative meta-analysis. Control Clin Trials. 1997;18(6):580--93.
7. Wetterslev J, Thorlund K, Brok J, Gluud C. Estimating required information size by quantifying diversity in random-effects model meta-analyses. BMC Med Res Methodol. 2009;9:86.
8. Brok J, Thorlund K, Gluud C, Wetterslev J. Trial sequential analysis reveals insufficient information size and potentially false positive results in many meta-analyses. J Clin Epidemiol. 2008;61(8):763--9.
9. Thorlund K, Engstrom J, Wetterslev J, Brok J, Imberger G, Gluud C. User manual for trial sequential analysis (TSA). Copenhagen Trial Unit, Centre for Clinical Intervention Research; 2011.
10. Morris TP, White IR, Crowther MJ. Using simulation studies to evaluate statistical methods. Stat Med. 2019;38(11):2074--102.
11. Benson K, Hartz AJ. A comparison of observational studies and randomized, controlled trials. N Engl J Med. 2000;342(25):1878--86.
12. Ioannidis JP, Haidich AB, Pappa M, Pantazis N, Kokori SI, Tektonidou MG, et al. Comparison of evidence of treatment effects in randomized and nonrandomized studies. JAMA. 2001;286(7):821--30.
13. Ibrahim JG, Chen MH. Power prior distributions for regression models. Stat Sci. 2000;15(1):46--60.
14. Schmidli H, Gsteiger S, Roychoudhury S, O'Hagan A, Spiegelhalter D, Neuenschwander B. Robust meta-analytic-predictive priors in clinical trials with historical control information. Biometrics. 2014;70(4):1023--32.
15. Carpenter B, Gelman A, Hoffman MD, Lee D, Goodrich B, Betancourt M, et al. Stan: a probabilistic programming language. J Stat Softw. 2017;76(1):1--32.
16. Hernan MA, Robins JM. Using big data to emulate a target trial when a randomized trial is not available. Am J Epidemiol. 2016;183(8):758--64.
17. Hernan MA, Wang W, Leaf DE. Target trial emulation: a framework for causal inference from observational data. JAMA. 2022;328(24):2446--7.
18. Verde PE, Ohmann C. Combining randomized and non-randomized evidence in clinical research: a review of methods and applications. Res Synth Methods. 2015;6(1):45--62.
19. Efthimiou O, Mavridis D, Debray TPA, Samara M, Belger M, Salanti G, et al. Combining randomized and non-randomized evidence in network meta-analysis. Stat Med. 2017;36(8):1210--26.

---

## Tables

**Table 1: Existing approaches to mitigate event dilution in RCTs**

| Approach | Mechanism | Adoption level |
|---|---|---|
| Stratified randomization | Risk-based stratification of randomization and analysis | Common for basic strata (e.g., site, sex); rare for event-rate-driven strata |
| Prognostic enrichment | Intentional enrollment of high-risk patients to increase event rates | Endorsed by FDA and EMA guidance; limited in non-drug trials |
| Event-driven design | Continue enrollment/follow-up until target event count is reached | Common in cardiology and oncology; rare in other specialties |
| Adaptive sample size re-estimation | Mid-trial re-estimation of required sample size based on observed event rates | Statistically powerful; regulatory complexity limits adoption |
| External data-informed design | Use retrospective data prospectively to quantify expected event loss and adjust design | Ideal but very rare in practice |
| Pragmatic / registry-based trials | Broad eligibility, minimal exclusions, real-world enrollment | Growing (e.g., REMAP-CAP, RECOVERY) but not yet standard |

**Table 2: Module H assessment checklist mapped to GRADE domains**

| Module H assessment | GRADE domain | Analytical tool | Decision criterion |
|---|---|---|---|
| Information sufficiency | Imprecision | OIS calculation | Total events < OIS $\rightarrow$ informationally insufficient |
| CI assessment | Imprecision | CI inspection | CI spans benefit through null $\rightarrow$ inconclusive |
| Representativeness | Indirectness | Module K event rate ratio | Event rate ratio > 1.5 $\rightarrow$ serious indirectness |
| TSA | Imprecision | Sequential monitoring boundaries | Boundaries not crossed $\rightarrow$ interim analysis equivalent |
| Recommendation language | Overall assessment | Standardized templates | Tailored to information sufficiency classification |

---

## Figures

**Fig. 1** Overview of the KOTHA Framework. Module K (Counterfactual Power Simulation) uses retrospective cohort data to quantify risk-profile shift and estimate power under counterfactual enrollment scenarios. Module T (Bayesian Evidence Integration) combines RCT and observational evidence using hierarchical models with design-specific bias terms. Module H (Guideline Interpreter) synthesizes outputs from Modules K and T into a structured GRADE-compatible assessment for guideline committees. Arrows indicate data flow between modules.

**Fig. 2** Conceptual illustration of risk-profile shift from target population (S1) to RCT-enrolled population (S2). The shaded area represents the high-risk subgroup preferentially excluded by RCT eligibility criteria, where events are concentrated. S3 represents a design-optimized enrollment strategy with prognostic enrichment.

**Fig. 3** Estimated power by enrollment scenario and true hazard ratio for the illustrative scenario (N = 3,800; 10,000 Monte Carlo replications). Horizontal dashed line indicates conventional 80% power threshold. Vertical dashed line indicates the observational point estimate (HR = 0.78).

**Fig. 4** Forest plot comparing RCT-only (frequentist), RCT-only (Bayesian), observational-only, and KOTHA-integrated (power prior $\alpha$ = 0.1, 0.3, 0.5; bias-adjusted; robust mixture) effect estimates for the illustrative scenario. Diamond widths represent 95% confidence or credible intervals.

**Fig. 5** Trial sequential analysis plot for the illustrative scenario. The cumulative Z-curve (solid line) is plotted against the required information size (vertical dashed line), the conventional significance boundary (horizontal dashed line), and the O'Brien-Fleming-adjusted monitoring boundaries (curved dashed lines). The information fraction (60%) is indicated.

---

## Additional files

**Additional file 1**: Mathematical derivations. Detailed derivations for the optimal information size formula, its relationship to event dilution, and the power prior likelihood formulation.

**Additional file 2**: Stan code. Complete Stan model code for the Module T hierarchical Bayesian meta-analysis with design-specific bias terms (model_T_bias.stan) and power prior implementation (model_T_power_prior.stan).

**Additional file 3**: R code. R scripts for Module K counterfactual power simulation (module_K_simulation.R) and Module T model fitting and postprocessing (module_T_analysis.R).

**Additional file 4**: Sensitivity analysis results. Complete sensitivity analysis tables for the illustrative scenario across all Module T discounting approaches and Module K treatment effect assumptions.

**Additional file 5**: Module H checklist template. Fillable checklist template for guideline committees implementing Module H assessment, with worked examples and decision flowchart.

**Additional file 6**: ADEMP reporting checklist for Module K. Completed ADEMP checklist for the simulation study component, following Morris et al. [10].
