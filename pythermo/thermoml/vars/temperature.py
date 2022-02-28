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
    """
    Class representing temperature variables. The following variables are taken over from ThermoML - schema definition:
    Temperature, upper temperature and lower temperature.
    Inherited from VariableBase.
    
    Args:
        varType (str): extracted from schema definition: eTemperature
    
    """
    varType: str = "eTemperature"

    @classmethod
    def temperature(cls, ID: str, compoundID: str = None):
        """creates temperature object. For more information visit documentation of VariableBase.
    
        Note:
            Unit: "K"

        Args:
            ID (str): ID
            compoundID (str, optional): Default is None, because temperature is not component specific

        Returns:
            TemperatureBase: object of type TemperatureBase.
        """
        return cls (
            varName = "Temperature",
            ID=ID,
            unit="K",
            compoundID=compoundID
        )

    @classmethod
    def upperTemperature(cls, ID: str, compoundID: str = None):
        """creates upper temperature object. For more information visit documentation of VariableBase.
        
        Note:
            Unit: "K"

        Args:
            ID (str): ID
            compoundID (str, optional): Default is None, because temperature is not component specific

        Returns:
            TemperatureBase: object of type TemperatureBase.
        """
        return cls(
            varName = "Upper temperature",
            ID = ID,
            unit = "K",
            compoundID = compoundID
        )

    @classmethod
    def lowerTemperature(cls, ID: str, compoundID: str = None):
        """creates lower temperature object. For more information visit documentation of VariableBase.

        Note:
            Unit: "K"

        Args:
            ID (str): ID
            compoundID (str, optional): Default is None, because temperature is not component specific

        Returns:
            TemperatureBase: object of type TemperatureBase.
        """
        return cls(
            varName = "Lower temperature",
            ID = ID,
            unit = "K",
            compoundID = compoundID
        )