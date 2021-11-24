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

from pythermo.thermoml.vars.variableBase import VariableBase


class TemperatureBase(VariableBase):

    varType: str = "eTemperature"

    @classmethod
    def temperature(cls, ID: str, compoundID: str = None):
        return cls (
            varName = "Temperature",
            ID=ID,
            unit="K",
            compoundID=compoundID
        )

    @classmethod
    def upperTemperature(cls, ID: str, compoundID: str = None):
        return cls(
            varName = "Upper temperature",
            ID = ID,
            unit = "K",
            compoundID = compoundID
        )

    @classmethod
    def lowerTemperature(cls, ID: str, compoundID: str = None):
        return cls(
            varName = "Lower temperature",
            ID = ID,
            unit = "K",
            compoundID = compoundID
        )