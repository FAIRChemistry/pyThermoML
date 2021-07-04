'''
File: temperature.py
Project: vars
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 12:08:59 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from vars.variableBase import VariableBase


class Temperature(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit
    ):

        super().__init__(
            varType="eTemperature",
            varName=varName,
            ID=ID,
            unit=unit
        )

# Initializers

def temperature(
    ID: "Unique identifier"
):
    temperatureVar = Temperature(
        varName="Temperature",
        ID=ID,
        unit="K"
    )

    return temperatureVar


def upperTemperature(
    ID: "Unique identifier"
):
    upperTemperatureVar = Temperature(
        varName="Upper temperature",
        ID=ID,
        unit="K"
    )

    return upperTemperatureVar

def lowerTemperature(
    ID: "Unique identifier"
):
    lowerTemperatureVar = Temperature(
        varName="Lower temperature",
        ID=ID,
        unit="K"
    )

    return lowerTemperatureVar