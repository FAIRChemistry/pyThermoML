'''
File: test.py
Project: pyThermoML
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 2:16:28 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from props.bioproperties import peakTemperature
from vars.temperature import upperTemperature

peakTemp = peakTemperature('S0')
upperTemp = upperTemperature('S1')
print(upperTemp)