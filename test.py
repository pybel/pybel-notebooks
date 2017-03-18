import os
import unittest

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# CHECK THIS http://stackoverflow.com/questions/1676269/writing-a-re-usable-parametrized-unittest-testcase-method

def get_all_ipynb(directory):
    for path in os.listdir(directory):
        if path.endswith('.ipynb'):
            yield path

class TestNotebooks(unittest.TestCase):
    """This test class checks that Jupyter notebooks run to completion"""
    def help(self, path):
        with open(os.path.join(DIRECTORY, path)) as f:
            nb = nbformat.read(file, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': DIRECTORY}})
    
    def test_citation_demo(self):
        self.help('Citation Analysis.ipynb')
        
    def test_npa_demo(self):
        self.help('NPA Demo.ipynb')
        
if __name__ == '__main__':
    unittest.main()
