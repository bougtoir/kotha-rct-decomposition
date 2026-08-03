.PHONY: all validate build generic clean

all: validate build

validate:
	python validation/run_validation.py

build:
	python build_paper.py

generic: build
	cp 04_paper_rsm.md 04_paper_generic.md
	cp KOTHA_Framework_RSM.docx KOTHA_Framework_generic.docx

clean:
	rm -f 04_paper_rsm.md KOTHA_Framework_RSM.docx
	rm -f 04_paper_generic.md KOTHA_Framework_generic.docx
	rm -rf validation/figures/*.png validation/results_summary.txt
