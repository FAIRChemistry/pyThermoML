'''
File: test.py
Project: pyThermoML
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:37:04 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from core import PureOrMixtureData, Measurement
from props import Bioproperty


from props.bioproperties import peakTemperature
from vars.temperature import upperTemperature


experiment = PureOrMixtureData("ID", "name")

# Property definitions
peakTemp = peakTemperature('S0')

# Variable definitions
upperTemp = upperTemperature('S1')

peakTempID = experiment.addProperty(peakTemp)
upperTempID = experiment.addVariable(upperTemp)

values = {
    upperTempID: 100.0,
    peakTempID: 1000.0
}

meas = Measurement(
    values,
    pureOrMixtureData=experiment
)

