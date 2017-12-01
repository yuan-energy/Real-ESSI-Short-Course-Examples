
TARGET=short_courses_examples


all:
	pdflatex $(TARGET).tex
	# bibtex   $(TARGET).aux
	pdflatex $(TARGET).tex
	pdflatex $(TARGET).tex
	# pdflatex $(TARGET).tex

	$(MAKE) -s clean

clean:
	find . -name "*.aux" -delete
	find . -name "*.log" -delete
	find . -name "*.toc" -delete
	find . -name "*.out" -delete
	find . -name "*.synctex.gz" -delete
	find . -name "*.fdb_latexmk" -delete
	find . -name "*.bbl" -delete
	find . -name "*.blg" -delete
	find . -name "*.fls" -delete
	find . -name "*.spl" -delete

# .SILENT:clean


extract:
	pdftk short_courses_examples.pdf cat 63-86 output nonlinear_steps.pdf
