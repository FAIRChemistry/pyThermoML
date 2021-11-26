'''
File: variableBase.py
Project: vars
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:12:14 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''
from typing import Optional
from pydantic import BaseModel, validator
from pydantic.fields import PrivateAttr


class VariableBase(BaseModel):
    """
    Base class for variables. For more information visit ThermoMLSchema definition.

        Args:
            varName (str): Name of the variable. Determined in child classes.
            varType (str): Name of belonging variable type. Determined in child classes.
            ID (str): User specified variable ID. Will be stored in nVarNumber tag in ThermoML .xml
            unit (str): Unit of Variable. Determined in child classes.
            compoundID (str, optional): ID of reffered compound
            _type (str): type of varable. Default is "Variable"

    """
    varType: str
    varName: str
    ID: str
    unit: str
    compoundID: Optional[str] = None
    _type: str = PrivateAttr(default="Variable")

    @validator("ID", always=True)
    @classmethod
    def validate_ID_string(cls, ID:str) -> str:
        """user specified ID of variable has to be in the following pattern: 'v[digit/s]'.

        Args:
            ID (str): user specified ID

        Raises:
            TypeError: ID does not match expected pattern.

        Returns:
            str: ID
        """
        if ID.startswith("v"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'v[digit/s]'"
            )