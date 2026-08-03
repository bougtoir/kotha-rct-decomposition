.PHONY: all validate build clean

all: validate build

validate:
	python validation/run_validation.py

build:
	python build_paper.py

clean:
	rm -f 04_paper_rsm.md KOTHA_Framework_RSM.docx
	rm -rf validation/figures/*.png validation/results_summary.txt
