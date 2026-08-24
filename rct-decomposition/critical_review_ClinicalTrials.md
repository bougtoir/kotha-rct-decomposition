# Reviewer-perspective critical review — Clinical Trials submission

Review date: 2026-08-21
Target journal: *Clinical Trials: Journal of the Society for Clinical Trials*
Manuscript: "The KOTHA Framework: diagnosing structural information loss in randomized controlled trial meta-analyses to inform trial design"

## 1. Manuscript content and narrative

| Item | Severity | Finding | Proposed fix |
|---|---|---|---|
| Novelty and framing | Low | The framing that KOTHA is the first integrated framework is plausible but broad; the manuscript avoids overclaiming by positioning modules as complementary. | Keep current wording; consider toning "no existing framework integrates" to "no widely adopted framework explicitly links..." if reviewers object. |
| TSA boundary wording | **High** (fixed) | The original sentence reported "crossing the O'Brien-Fleming boundary of 0.27" for a negative Z-statistic (-2.90). Because the boundary for benefit is negative (-0.27), the sign and interpretation were incorrect and would confuse readers. | Corrected to: fixed-effect Z "did not cross the conventional two-sided boundary for benefit or harm (\|Z\| = 1.96)"; random-effects Z "crossing the lower O'Brien-Fleming boundary of -0.27". |
| Results-conclusions alignment | Low | Conclusions about magnesium (serious inconsistency) and statins (serious indirectness) follow directly from Module H outputs. | No change needed. |
| Abstract keywords | Low | Six keywords are within the 3–10 range; all are relevant. | No change. |

## 2. Statistical design and methods

| Item | Severity | Finding | Proposed fix |
|---|---|---|---|
| Unit of analysis / ecological bias | Low | Aggregate study-level data are used; ecological bias is acknowledged. | Keep limitation wording. |
| Confounding and discounting | Low | Module T uses power-prior discounting but cannot remove unmeasured confounding; this is stated. | No change. |
| Multiple comparisons | Low | α grid is sensitivity/exploratory; no formal multiplicity adjustment is claimed. | No change. |
| Effect measures and uncertainty | Low | OR/HR with 95% CrI/CI reported; RMST alternatives mentioned. | No change. |
| TSA model heterogeneity | Low | Fixed-effect and random-effects TSA give different conclusions; the manuscript now explicitly frames this as era-dependent heterogeneity rather than a contradiction. | No change. |

## 3. Figures and tables

| Item | Severity | Finding | Proposed fix |
|---|---|---|---|
| Main-text count | Low | 4 figures + 2 numbered tables = 6 items, satisfying the journal limit. The abbreviations section is rendered as a definition list, not a table, so it does not count toward the 6-table/figure limit. | No change. |
| Supplementary reorganization | Low | Original CCTC Tables 1/3 and Figs. 5/6/7 correctly moved to Supplementary Tables S1/S4 and Supplementary Figs. S2–S4. Trace plots remain S1a/b. | No change. |
| Figure 4 caption | Low | Lists selected α levels for Bayesian pooled estimates; matches text. | No change. |
| Table 2 color coding | Low | Uses color for concern level; ensure gray-scale readability or add text labels. | Verify in the editable PPTX that colors are also encoded by wording (e.g., "serious"). |

## 4. Reproducibility

| Item | Severity | Finding | Proposed fix |
|---|---|---|---|
| Public data and code | Low | All study-level data are in `data/` with documented sources; analysis and manuscript scripts are in the public repository. | No change. |
| Build pipeline | Low | `make clinical_trials` reuses committed CCTC outputs and regenerates all Clinical Trials deliverables without re-running MCMC. | Documented in README; no change. |
| Dependency on pandoc | Medium | `generate_cct_docx.py` requires pandoc; the script searches a user-local path and PATH, but a fresh clone may not have pandoc. | Add a README note that pandoc is required and point to the download location. The environment blueprint can also install it. |
| No hard-coded results | Low | Manuscript numbers are injected by `build_paper_cct.py` from the analysis pipeline, not hand-entered in the generator scripts. Cover letter summary numbers were removed to avoid hard-coding. | No change. |

## 5. Strength of claims

| Item | Severity | Finding | Proposed fix |
|---|---|---|---|
| Causal interpretation | Low | The manuscript consistently uses "diagnoses" and "quantifies information loss" rather than claiming to prove that event dilution caused a negative trial. | No change. |
| Generalizability | Low | Illustrative cases are retrospective and well-known; prospective validation is acknowledged as future work. | No change. |
| GRADE compatibility | Low | Module H maps to GRADE domains without altering GRADE structure; this is clear. | No change. |

## Summary

- One **high-severity** wording issue (TSA boundary sign/interpretation) was identified and corrected before final file generation.
- No fatal scientific or reproducibility issue was found.
- Outstanding minor items: (1) confirm whether the abbreviations table counts toward the 6-figure/table limit; (2) add a brief README note about pandoc for clean-clone users.
