# @File          :   pressure.py
# @Last modified :   2022/04/09 19:29:22
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pythermo.thermoml.vars.variableBase import VariableBase


class PressureBase(VariableBase):
    """
    Class representing pressure variables. The following variables are taken over from ThermoML - schema definition:
    pressure.
    Inherited from VariableBase.

    Args:
        varType (str): extracted from schema definition: ePressure

    """

    varType: str = "ePressure"

    @classmethod
    def pressure(cls, ID: int, compoundID: Optional[int] = None) -> "PressureBase":
        """creates pressure object. For more information visit documentation of VariableBase.

        Note:
            Unit: "kPa"

        Args:
            ID (str): ID
            compoundID (str, optional): Default is None, because pressure is not component specific

        Returns:
            PressureBase: object of type PressureBase.
        """
        return cls(varName="Pressure", ID=ID, unit="kPa", compoundID=compoundID)
