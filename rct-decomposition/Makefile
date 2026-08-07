.PHONY: all validate build generic cctc clean

all: validate build

validate:
	python validation/run_validation.py

build:
	python build_paper.py

generic: build
	cp 04_paper_rsm.md 04_paper_generic.md
	cp KOTHA_Framework_RSM.docx KOTHA_Framework_generic.docx

cctc:
	python build_paper_cct.py
	python build_figures_pptx.py --md 05_paper_cctc.md --out KOTHA_Framework_CCTC_figures.pptx
	python build_tables_docx.py --src KOTHA_Framework_CCTC.docx --out KOTHA_Framework_CCTC_tables.docx

clean:
	rm -f 04_paper_rsm.md KOTHA_Framework_RSM.docx
	rm -f 04_paper_generic.md KOTHA_Framework_generic.docx
	rm -f 05_paper_cctc.md KOTHA_Framework_CCTC.docx KOTHA_Framework_CCTC_tables.docx KOTHA_Framework_CCTC_figures.pptx
	rm -rf validation/figures/*.png validation/results_summary.txt
