F=2_Bayesian_PredictorCorrector
${F}.png: ${F}.tikz
	tikz2pdf.py -o ${F}.pdf ${F}.tikz
	convert -quality 00  -density 600x600  ${F}.pdf ${F}.png
	rm ${F}.pdf


FH.svg : FilterHierarchy.dot
	dot -Tsvg $< > $@
