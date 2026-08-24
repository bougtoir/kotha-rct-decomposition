# KOTHA Framework — Reproducible Manuscript Pipeline

This repository contains the empirical validation, figures, and manuscript-generation pipeline for the KOTHA (Knowledge-driven Observational-Trial Harmonization Approach) Framework manuscript.

## One-command builds

```bash
make all              # run validation and generate the RSM-target manuscript
make clinical_trials  # generate the Clinical Trials submission package
```

`make clinical_trials` reuses the pre-computed CCTC outputs and produces:
`05_paper_clinical_trials.md`, `KOTHA_Framework_ClinicalTrials.docx`, `KOTHA_Framework_ClinicalTrials_tables.docx`, `KOTHA_Framework_ClinicalTrials_figures.pptx`, `KOTHA_Framework_ClinicalTrials_supplementary_tables.docx`, `cover_letter_ClinicalTrials.docx`, and `submission_package_ClinicalTrials.zip`.

## Pipeline steps

1. **Data** — `data/magnesium_ami.csv`, `data/statins_hf_obs.csv`, and `data/statins_hf_rct.csv` contain the study-level inputs and are documented in `data/SOURCES.md`.
2. **Analysis** — `validation/run_validation.py` reads the CSVs and produces:
   - `validation/figures/*.png` (eight figures)
   - `validation/results_summary.txt` (numerical summary)
3. **Manuscript** — `build_paper.py` reads `paper_template.md`, injects the computed results, tables, and figures, and writes `04_paper_rsm.md`. `build_paper_cct.py` writes `05_paper_cctc.md`, and `build_paper_clinical_trials.py` restructures it for *Clinical Trials*.
4. **DOCX / PPTX** — `generate_cct_docx.py` converts the markdown into `KOTHA_Framework_ClinicalTrials.docx` with inline figures, tables, and Sage Vancouver superscript citations.

## Reproducibility principle

No study-level counts, effect estimates, or summary statistics are hard-coded in the manuscript source. All numbers in `04_paper_rsm.md` and the generated Word document are produced by `build_paper.py` from the CSVs and the analysis code. Edit `paper_template.md` for prose; rerun `make build` to refresh all numbers, tables, and figures.
