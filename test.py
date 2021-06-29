'''
File: test.py
Project: pyThermoML
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 11:23:31 am
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from props.bioproperties import peakTemperature

nuClass = peakTemperature('S0')

print(nuClass.__dict__)