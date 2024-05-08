
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'This repository enables users to read and write ThermoML files using sdRDM and python.'

# Setting up
setup(
    name="pyThermoML",
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/SimTech-Research-Data-Management/ThermoML-Specifications',
    author="Jan Range, Samir Darouich",
    author_email="jan.range@simtech.uni-stuttgart.de",
    license_files = ('LICENSE'),
    packages=find_packages(),
    install_requires=['numpy',
                      'pandas',
                      'sdrdm',
                      'pubchempy',
                      'pyYaml',
                      'seaborn'
                      ],
)