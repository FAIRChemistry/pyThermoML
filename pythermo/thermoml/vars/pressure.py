'''
File: pressure.py
Project: vars
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''
from pythermo.thermoml.vars.variableBase import VariableBase


class PressureBase(VariableBase):
    """
    Class representing pressure variables. The following variables are taken over from ThermoML - schema definition:
    pressure.
    Inherited from VariableBase.
    
        Args:
            varType (str): extracted from schema definition: ePressure
    
    """
    varType: str ="ePressure"

    @classmethod
    def pressure(cls, ID: str, compoundID: str = None):
        """creates pressure object. For more information visit documentation of VariableBase.

        Note:
            Unit: "kPa"

        Args:
            ID (str): ID
            compoundID (str, optional): Default is None, because pressure is not component specific

        Returns:
            PressureBase: object of type PressureBase.
        """
        return cls(
            varName = "Pressure",
            ID = ID,
            unit = "kPa",
            compoundID = compoundID
        )