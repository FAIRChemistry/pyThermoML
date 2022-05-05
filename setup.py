# @File          :   setup.py
# @Last modified :   2022/04/09 19:29:41
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

import setuptools
from setuptools import setup

setup(
    name='PyThermoML',
    version='1.1.1',
    description='Handling of ThermoML files',
    url = 'https://github.com/ThermoPyML/pyThermoML',
    author='Gueltig, Matthias',
    packages=setuptools.find_packages(),
    install_requires=['lxml', 'json', 'pydantic',],
    extras_requires={
        'dataverse': ['pyDaRUS']
    }
)