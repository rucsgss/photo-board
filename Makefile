OUTPUT=photoboard.pdf

all: $(OUTPUT)

clean:
	rm -rf *.aux *.log *.tex *-eps-converted-to.pdf a0header.ps $(OUTPUT)

photoboard.tex: make-photoboard-tex.py
	./$< > $@

%.pdf: %.tex
	pdflatex $<
