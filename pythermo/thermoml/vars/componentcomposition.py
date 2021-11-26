'''
File: componentcomposition.py
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
    def moleFraction(cls, ID: str, compoundID: str):
        """creates mole fraction object. For more information visit documentation of VariableBase.
        
        Note:
            Unit: ""

        Args:
            ID (str): ID
            compoundID (str): ID of referred compound

        Returns:
            ComponentCompositionBase: object of type ComponentComposition.
        """
        return cls(varName="Mole fraction",
        ID=ID,
        unit="",
        compoundID=compoundID
    )
