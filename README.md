# PyBEL Notebooks

This repository contains Jupyter notebooks demonstrating the [PyBEL](https://github.com/pybel/pybel) and 
[PyBEL Tools](https://github.com/pybel/pybel-tools) packages.

## [Summary](https://github.com/pybel/pybel-notebooks/tree/master/summary)

This directory contains notebooks that analyze the contents of a BEL graph.

1. Graph Summary
2. Citation Summary
3. Error Analysis

## [Integration](https://github.com/pybel/pybel-notebooks/tree/master/integration)

This directory contains notebooks dealing with input/output and data integration.

1. Parsing JGIF
2. Resolving Protein Complexes

## [Algorithms](https://github.com/pybel/pybel-notebooks/tree/master/algorithms)

This directory contains notebooks demonstrating algorithms implemented with PyBEL and NetworkX.

1. Generation of Unbiased Candidate Mechanisms
2. Subgraph Expansion
3. Subgraph Comparison
4. Candidate Mechanism Pertubation Amplitude
5. Time Series Analysis with CMPA
6. Concordance Analysis

## Root Directory

### Template Notebook ([source](https://github.com/pybel/pybel-notebooks/blob/master/Template.ipynb))

This notebook serves as a style guide for other notebooks in this repository.

### BEL Compiler Comparison Notebook ([source](https://github.com/pybel/pybel-notebooks/blob/master/BEL%20Compiler%20Comparison.ipynb)\) ([nbviewer](http://nbviewer.jupyter.org/github/pybel/pybel-notebooks/blob/master/BEL%20Compiler%20Comparison.ipynb)\)
	
The speed and usability of the PyBEL compiler is compared to the two legacy options: bel.rb and the OpenBEL Framework.

### test.py ([source](https://github.com/pybel/pybel-notebooks/blob/master/test.py))

This file can be run with `python3 -m nose` to check that notebooks run to completion.

