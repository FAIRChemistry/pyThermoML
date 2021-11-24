import setuptools
from setuptools import setup

setup(
    name='PyThermoML',
    version='1.1.1',
    description='Handling of ThermoML files',
    url = 'https://github.com/matzegltg/pyThermoML',
    author='Gültig, Matthias',
    packages=setuptools.find_packages(),
    _install_requires=['lxml', 'json'],
)