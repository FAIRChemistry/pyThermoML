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


class TemperatureBase(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit,
        compoundID=None,
    ):

        super().__init__(
            varType="eTemperature",
            varName=varName,
            ID=ID,
            unit=unit,
            compoundID = compoundID
        )

# Initializers

def Temperature(
    ID: "Unique identifier",
    compoundID = None
):
    
    # not component specific!
    if compoundID is not None:
        compoundID=None

    temperatureVar = TemperatureBase(
        varName="Temperature",
        ID=ID,
        unit="K",
        compoundID = compoundID
    )

    return temperatureVar


def UpperTemperature(
    ID: "Unique identifier",
    compoundID = None
):
    if compoundID is not None:
        compoundID = None
    upperTemperatureVar = TemperatureBase(
        varName="Upper temperature",
        ID=ID,
        unit="K",
        compoundID=compoundID
    )

    return upperTemperatureVar

def LowerTemperature(
    ID: "Unique identifier",
    compoundID = None
):
    if compoundID is not None:
        compoundID = None
    lowerTemperatureVar = TemperatureBase(
        varName="Lower temperature",
        ID=ID,
        unit="K",
        compoundID=None
    )

    return lowerTemperatureVar