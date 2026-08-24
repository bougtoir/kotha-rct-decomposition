#!/usr/bin/env python3
"""Build the KOTHA manuscript for Clinical Trials: Journal of the Society for Clinical Trials.

This script reuses the Contemporary Clinical Trials Communications (CCTC) manuscript
(05_paper_cctc.md / KOTHA_Framework_CCTC.docx) and restructures it for *Clinical Trials*:
- <= 6 main-text tables/figures
- Sage Vancouver superscript citations without brackets
- Background/Aims abstract heading
- First-three-authors + et al. reference list
- Separate supplementary tables and high-resolution figure files
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile

BASE = os.path.dirname(os.path.abspath(__file__))

CCTC_MD = os.path.join(BASE, '05_paper_cctc.md')
CCTC_DOCX = os.path.join(BASE, 'KOTHA_Framework_CCTC.docx')
CCTC_SUPP_DOCX = os.path.join(BASE, 'KOTHA_Framework_CCTC_supplementary_tables.docx')

OUT_MD = os.path.join(BASE, '05_paper_clinical_trials.md')
OUT_DOCX = os.path.join(BASE, 'KOTHA_Framework_ClinicalTrials.docx')
OUT_FIGURES_PPTX = os.path.join(BASE, 'KOTHA_Framework_ClinicalTrials_figures.pptx')
OUT_TABLES_DOCX = os.path.join(BASE, 'KOTHA_Framework_ClinicalTrials_tables.docx')
OUT_SUPP_DOCX = os.path.join(BASE, 'KOTHA_Framework_ClinicalTrials_supplementary_tables.docx')
SUBMISSION_FIGURES_DIR = os.path.join(BASE, 'ClinicalTrials_figures')

HIGHLIGHTS_BLOCK = r"""## Highlights

* KOTHA separates structural information loss from residual confounding.
* Counterfactual power simulation quantifies enrollment-driven event dilution.
* Power-prior Bayesian synthesis transparently discounts observational evidence.
* GRADE-compatible output labels evidence as sufficient or insufficient.

"""

OLD_BG = (
    "**Background**: Evidence-based medicine ranks RCTs and meta-analyses highest, "
    "yet observational-RCT discordance is usually attributed to confounding. We highlight "
    "a structural explanation: trial enrollment progressively excludes higher-risk patients, "
    "diluting event rates and statistical information. The Knowledge-driven "
    "Observational-Trial Harmonization Approach (KOTHA) Framework diagnoses this structural "
    "information loss."
)
NEW_BG = (
    "**Background/Aims**: Evidence-based medicine ranks RCTs and meta-analyses highest, "
    "yet observational-RCT discordance is usually attributed to confounding. We highlight "
    "a structural explanation: trial enrollment progressively excludes higher-risk patients, "
    "diluting event rates and statistical information. The Knowledge-driven "
    "Observational-Trial Harmonization Approach (KOTHA) Framework diagnoses this structural "
    "information loss. We aimed to develop and illustrate KOTHA so that trialists can "
    "distinguish structural information loss from residual confounding and improve "
    "prospective trial design."
)

TABLE1_BLOCK = r"""**Table 1: Existing approaches to mitigate event dilution in RCTs**

| Approach | Mechanism | Adoption level |
|---|---|---|
| Stratified randomization | Risk-based stratification of randomization and analysis | Common for basic strata; rare for event-rate-driven strata |
| Prognostic enrichment | Intentional enrollment of high-risk patients to increase event rates | Endorsed by FDA and EMA guidance; limited in non-drug trials |
| Event-driven design | Continue enrollment/follow-up until target event count is reached | Common in cardiology and oncology; rare in other specialties |
| Adaptive sample size re-estimation | Mid-trial re-estimation of required sample size based on observed event rates | Statistically powerful; regulatory complexity limits adoption |
| External data-informed design | Use retrospective data to quantify expected event loss and adjust design | Ideal but very rare in practice |
| Pragmatic / registry-based trials | Broad eligibility, minimal exclusions, real-world enrollment | Growing (e.g., REMAP-CAP, RECOVERY) but not yet standard |

"""

FIG5_BLOCK = r"""**Fig. 5** Trial sequential analysis for magnesium in AMI. The cumulative Z-curve is plotted against cumulative events. Vertical dashed line indicates the optimal information size (OIS). Curved lines show O'Brien-Fleming monitoring boundaries.

![Fig. 5](validation/figures/fig5_tsa_magnesium.png)

"""

TABLE3_FIG6_BLOCK = r"""**Table 3: Bayesian integration results by case and discounting factor (power prior)**

| Case | $\alpha$ | OR/HR (95% CrI) | P(effect < 1) | P(effect < 0.90) | P(effect < 0.80) |
|---|---|---|---|---|---|
| Magnesium (OR) | 0.0 (ISIS-4 / RCTs only) | OR 1.05 (0.03--27.97) | 42.8% | 33.4% | 27.0% |
| Statins (HR) | 0.0 (ISIS-4 / RCTs only) | HR 0.97 (0.58--1.65) | 62.9% | 21.2% | 8.9% |
| Magnesium (OR) | 0.1 | OR 0.93 (0.15--2.92) | 58.3% | 46.3% | 36.2% |
| Statins (HR) | 0.1 | HR 0.92 (0.53--1.64) | 71.9% | 42.7% | 19.2% |
| Magnesium (OR) | 0.2 | OR 0.83 (0.22--1.75) | 71.4% | 58.9% | 46.9% |
| Statins (HR) | 0.2 | HR 0.89 (0.53--1.41) | 79.8% | 54.7% | 24.4% |
| Magnesium (OR) | 0.3 | OR 0.74 (0.25--1.43) | 80.7% | 69.6% | 57.4% |
| Statins (HR) | 0.3 | HR 0.85 (0.55--1.24) | 86.5% | 66.0% | 31.1% |
| Magnesium (OR) | 0.5 | OR 0.63 (0.28--1.10) | 94.0% | 87.2% | 76.3% |
| Statins (HR) | 0.5 | HR 0.82 (0.59--1.10) | 93.9% | 79.6% | 41.9% |
| Magnesium (OR) | 0.7 | OR 0.59 (0.29--0.98) | 98.1% | 94.8% | 87.1% |
| Statins (HR) | 0.7 | HR 0.80 (0.62--1.00) | 97.3% | 88.3% | 49.7% |
| Magnesium (OR) | 1.0 (full weight) | OR 0.55 (0.32--0.87) | 99.6% | 98.4% | 94.4% |
| Statins (HR) | 1.0 (full weight) | HR 0.78 (0.64--0.93) | 99.3% | 95.7% | 63.3% |

**Fig. 6** Sensitivity analysis of Bayesian integration to the discounting parameter $\alpha$. (A) Magnesium in AMI. (B) Statins in HF. Three posterior probability thresholds are shown: P(effect < 1.0), P(effect < 0.90), and P(effect < 0.80). Horizontal dashed line indicates 95% probability.

![Fig. 6](validation/figures/fig7_sensitivity_analysis.png)

"""

FIG7_BLOCK = r"""**Fig. 7** Module H assessment comparison: standard GRADE vs. KOTHA-enhanced evaluation for both illustrative cases. Color coding indicates severity of concern (green = no concern, yellow = moderate, red = serious).

![Fig. 7](validation/figures/fig8_module_h_comparison.png)

"""

FIGURE_MAP = {
    'validation/figures/fig1_framework_overview.png': 'Figure_1_framework_overview.png',
    'validation/figures/fig2_risk_profile_shift.png': 'Figure_2_risk_profile_shift.png',
    'validation/figures/fig3_power_curves.png': 'Figure_3_power_curves.png',
    'validation/figures/fig4_forest_combined.png': 'Figure_4_forest_combined.png',
    'validation/figures/fig5_tsa_magnesium.png': 'Figure_S2_tsa_magnesium.png',
    'validation/figures/fig7_sensitivity_analysis.png': 'Figure_S3_sensitivity_analysis.png',
    'validation/figures/fig8_module_h_comparison.png': 'Figure_S4_module_h_comparison.png',
    'validation/figures/figS1a_trace_mcmc_magnesium.png': 'Figure_S1a_trace_mcmc_magnesium.png',
    'validation/figures/figS1b_trace_mcmc_statins.png': 'Figure_S1b_trace_mcmc_statins.png',
}


def _run(script, *args):
    """Run a Python script in the repository root."""
    subprocess.run([sys.executable, script, *args], cwd=BASE, check=True)


def _ensure_cctc_outputs():
    """Generate CCTC outputs if they are not already present."""
    if not os.path.exists(CCTC_MD) or not os.path.exists(CCTC_DOCX):
        print('CCTC outputs missing; running build_paper_cct.py ...')
        _run('build_paper_cct.py')
    if not os.path.exists(CCTC_SUPP_DOCX):
        print('CCTC supplementary tables missing; running build_supplementary_tables_docx.py ...')
        _run('build_supplementary_tables_docx.py')


def _word_count(md):
    """Count main-text words excluding abstract, declarations, tables, figures, references."""
    wc_match = re.search(r'## 1\. Introduction(.*?)## Declarations', md, re.S)
    wc_text = wc_match.group(1) if wc_match else md
    wc_text = re.sub(r'!\[.*?\]\(.*?\)', '', wc_text)
    wc_text = re.sub(r'\*\*Fig\.\s*\d+\*\*.*', '', wc_text)
    wc_text = re.sub(r'\*\*Table[^*]+\*\*', '', wc_text)
    wc_text = re.sub(r'(?:\|.*\n)+', '', wc_text)
    wc_text = re.sub(r'[#*_`$\\]', ' ', wc_text)
    wc_text = re.sub(r'\[.*?\]', '', wc_text)
    return len(wc_text.split())


def _abbreviate_reference_line(line):
    """Reduce a Vancouver reference to first three authors + et al."""
    m = re.match(r'^(\d+\.\s+)(.+?)\.\s+(.*)$', line)
    if not m:
        return line
    prefix, authors, rest = m.groups()
    parts = [p.strip() for p in authors.split(',') if p.strip()]
    parts = [p for p in parts if p.lower() != 'et al.']
    if len(parts) > 3:
        parts = parts[:3] + ['et al']
    return f'{prefix}{", ".join(parts)}. {rest}'


def _abbreviate_references(md):
    """Abbreviate author lists in the References section to Sage Vancouver style."""
    ref_start = md.find('## References')
    if ref_start == -1:
        return md
    before = md[:ref_start]
    ref_section = md[ref_start:]
    lines = ref_section.splitlines()
    new_lines = [lines[0]]
    for line in lines[1:]:
        if re.match(r'^\d+\.', line):
            new_lines.append(_abbreviate_reference_line(line))
        else:
            new_lines.append(line)
    return before + '\n'.join(new_lines)


def _restructure(md):
    """Restructure CCTC markdown for Clinical Trials."""
    md = md.replace(HIGHLIGHTS_BLOCK, '')
    md = md.replace(OLD_BG, NEW_BG)

    # Update in-text references to supplementary items
    md = md.replace('(Table 1)', '(Supplementary Table S1)')
    md = md.replace('(Fig. 5)', '(Supplementary Fig. S2)')
    md = md.replace('(Table 3)', '(Supplementary Table S4)')
    md = md.replace('(Fig. 6A)', '(Supplementary Fig. S3A)')
    md = md.replace('(Fig. 6B)', '(Supplementary Fig. S3B)')
    md = md.replace('Table 4 and Fig. 7', 'Table 4 and Supplementary Fig. S4')

    # Renumber remaining main-text tables sequentially (Table 2 -> 1, Table 4 -> 2)
    md = re.sub(r'\bTable 2\b', 'Table 1', md)
    md = re.sub(r'\bTable 4\b', 'Table 2', md)

    # Remove moved main-text figure/table blocks
    md = md.replace(TABLE1_BLOCK, '')
    md = md.replace(FIG5_BLOCK, '')
    md = md.replace(TABLE3_FIG6_BLOCK, '')
    md = md.replace(FIG7_BLOCK, '')

    md = _abbreviate_references(md)

    # Update main-text word count
    wc = _word_count(md)
    md = re.sub(r'^word_count:\s*\d+', f'word_count: {wc}', md, flags=re.MULTILINE)
    return md, wc


def _copy_submission_figures():
    """Copy high-resolution figure files into a submission-ready folder."""
    if os.path.exists(SUBMISSION_FIGURES_DIR):
        shutil.rmtree(SUBMISSION_FIGURES_DIR)
    os.makedirs(SUBMISSION_FIGURES_DIR)
    for src, dst in FIGURE_MAP.items():
        src_path = os.path.join(BASE, src)
        if os.path.exists(src_path):
            shutil.copy2(src_path, os.path.join(SUBMISSION_FIGURES_DIR, dst))
        else:
            print(f'  WARNING: figure not found: {src_path}')


def _build_submission_package():
    """Zip all Clinical Trials deliverables."""
    zip_path = os.path.join(BASE, 'submission_package_ClinicalTrials.zip')
    files_to_zip = [
        OUT_MD,
        OUT_DOCX,
        OUT_TABLES_DOCX,
        OUT_FIGURES_PPTX,
        OUT_SUPP_DOCX,
        os.path.join(BASE, 'cover_letter_ClinicalTrials.docx'),
    ]
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in files_to_zip:
            if os.path.exists(f):
                zf.write(f, os.path.basename(f))
        for root, _, files in os.walk(SUBMISSION_FIGURES_DIR):
            for file in files:
                full = os.path.join(root, file)
                arc = os.path.relpath(full, BASE)
                zf.write(full, arc)
    print(f'Created {zip_path}')


def main():
    parser = argparse.ArgumentParser(description='Build Clinical Trials manuscript package')
    parser.add_argument('--no-cctc', action='store_true', help='Skip CCTC build even if outputs are missing')
    args = parser.parse_args()

    if not args.no_cctc:
        _ensure_cctc_outputs()

    print(f'Reading {CCTC_MD} ...')
    with open(CCTC_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    md, wc = _restructure(md)
    print(f'Restructured main-text word count: {wc}')

    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'Wrote {OUT_MD}')

    # Generate main manuscript docx with Sage-style unbracketed superscript citations
    _run(
        'generate_cct_docx.py',
        OUT_MD,
        OUT_DOCX,
        '--journal', 'Clinical Trials: Journal of the Society for Clinical Trials',
        '--strip-citation-brackets',
    )

    # Editable figures PPTX
    _run('build_figures_pptx.py', '--md', OUT_MD, '--out', OUT_FIGURES_PPTX)

    # Editable tables docx extracted from the main manuscript
    _run('build_tables_docx.py', '--src', OUT_DOCX, '--out', OUT_TABLES_DOCX)

    # Supplementary tables docx (S1-S4) extracted from CCTC outputs
    _run('build_supplementary_tables_clinical_trials_docx.py')

    # Copy high-resolution figure files for upload
    _copy_submission_figures()

    # Build zip package
    _build_submission_package()

    print('\nClinical Trials deliverables ready:')
    for p in [OUT_MD, OUT_DOCX, OUT_TABLES_DOCX, OUT_FIGURES_PPTX, OUT_SUPP_DOCX,
              os.path.join(BASE, 'submission_package_ClinicalTrials.zip')]:
        print(' -', os.path.basename(p))


if __name__ == '__main__':
    main()
