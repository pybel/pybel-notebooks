import os

import click
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

DIRECTORY = os.path.dirname(os.path.realpath(__file__))


# CHECK THIS http://stackoverflow.com/questions/1676269/writing-a-re-usable-parametrized-unittest-testcase-method

def get_all_ipynb(directory):
    for path in os.listdir(directory):
        if path.endswith('.ipynb'):
            yield path


def execute_notebook(file):
    nb = nbformat.read(file, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})


@click.group()
def main():
    """"""


@main.command()
@click.option('--path', type=click.File())
def run(path):
    execute_notebook(path)


@main.command()
@click.option('--path')
def ls(path):
    for path in get_all_ipynb(path):
        click.echo(path)


@main.command()
@click.argument('directory')
def rund(directory):
    for path in get_all_ipynb(directory):
        with open(path) as f:
            execute_notebook(f)


if __name__ == '__main__':
    main()
