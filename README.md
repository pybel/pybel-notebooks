# Table of Contents

## [Summary](https://github.com/pybel/pybel-notebooks/tree/master/summary)

This directory contains notebooks that analyze the contents of a BEL graph.

1. Graph Summary
2. Citation Summary
3. Error Analysis

## [Algorithms](https://github.com/pybel/pybel-notebooks/tree/master/algorithms)

This directory contains notebooks demonstrating algorithms implemented with PyBEL and NetworkX.

1. Unbiased Candidate Mechanism Generation
2. Subgraph Expansion
3. Subgraph Comparison
4. Network Perturbation Algorithm

## [Resources](https://github.com/pybel/pybel-notebooks/tree/master/resources)

This directory contains notebooks related to the generation of BEL resources (namespaces and 
annotations)

1. Rebuilding the HGNC Gene Symbol Namespace
2. Building the HGNC Gene Family Namespace
3. Building the dbSNP Namespace
4. Parsing the JSON Graph Interchange Format from CBN


## Root Directory

### Template Notebook ([source](https://github.com/pybel/pybel-notebooks/blob/master/Template.ipynb))

This notebook serves as a style guide for other notebooks in this repository.

### BEL Compiler Comparison Notebook ([source](https://github.com/pybel/pybel-notebooks/blob/master/BEL%20Compiler%20Comparison.ipynb)\) ([nbviewer](http://nbviewer.jupyter.org/github/pybel/pybel-notebooks/blob/master/BEL%20Compiler%20Comparison.ipynb)\)
	
The speed and usability of the PyBEL compiler is compared to the two legacy options: bel.rb and the OpenBEL Framework.

### test.py ([source](https://github.com/pybel/pybel-notebooks/blob/master/test.py))

This file can be run with `python3 -m nose` to check that notebooks run to completion.
