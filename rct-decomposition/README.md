# KOTHA Framework — Reproducible Manuscript Pipeline

This repository contains the empirical validation, figures, and manuscript-generation pipeline for the KOTHA (Knowledge-driven Observational-Trial Harmonization Approach) Framework manuscript.

## One-command build

```bash
make all
```

This runs the analysis (`validation/run_validation.py`) and then generates the manuscript (`04_paper_rsm.md`) and formatted Word document (`KOTHA_Framework_RSM.docx`) from code and data.

## Pipeline steps

1. **Data** — `data/magnesium_ami.csv`, `data/statins_hf_obs.csv`, and `data/statins_hf_rct.csv` contain the study-level inputs and are documented in `data/SOURCES.md`.
2. **Analysis** — `validation/run_validation.py` reads the CSVs and produces:
   - `validation/figures/*.png` (eight figures)
   - `validation/results_summary.txt` (numerical summary)
3. **Manuscript** — `build_paper.py` reads `paper_template.md`, injects the computed results, tables, and figures, and writes `04_paper_rsm.md`.
4. **DOCX** — `generate_rsm_docx_final.py` converts `04_paper_rsm.md` into `KOTHA_Framework_RSM.docx` with inline figures.

## Reproducibility principle

No study-level counts, effect estimates, or summary statistics are hard-coded in the manuscript source. All numbers in `04_paper_rsm.md` and the generated Word document are produced by `build_paper.py` from the CSVs and the analysis code. Edit `paper_template.md` for prose; rerun `make build` to refresh all numbers, tables, and figures.
