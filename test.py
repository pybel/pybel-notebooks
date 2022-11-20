import itertools as itt
import os
import unittest

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor

DIRECTORY = os.path.dirname(os.path.realpath(__file__))


# CHECK THIS http://stackoverflow.com/questions/1676269/writing-a-re-usable-parametrized-unittest-testcase-method


def get_all_ipynb(directory):
    for root, directory, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb") and "checkpoints" not in root:
                yield os.path.join(root, file)


@pytest.mark.parametrize("path", get_all_ipynb(DIRECTORY))
def test_notebook(path):
    with open(os.path.join(DIRECTORY, path)) as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": DIRECTORY}})
