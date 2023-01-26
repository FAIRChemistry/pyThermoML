# @File          :   componentcomposition.py
# @Last modified :   2022/04/09 19:29:17
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from pythermo.thermoml.vars.variableBase import VariableBase


class ComponentCompositionBase(VariableBase):
    """
    Class representing component composition variables. The following variables are taken over from ThermoML - schema definition:
    Mole fraction.
    Inherited from VariableBase.

    Args:
        varType (str): extracted from schema definition: eComponentComposition

    """

    varType: str = "eComponentComposition"

    @classmethod
    def moleFraction(cls, ID: int, compoundID: int) -> "ComponentCompositionBase":
        """creates mole fraction object. For more information visit documentation of VariableBase.

        Note:
            Unit: ""

        Args:
            ID (str): ID
            compoundID (str): ID of referred compound

        Returns:
            ComponentCompositionBase: object of type ComponentComposition.
        """
        return cls(varName="Mole fraction", ID=ID, unit="", compoundID=compoundID)
