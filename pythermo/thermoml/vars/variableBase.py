# @File          :   variableBase.py
# @Last modified :   2022/04/09 19:26:43
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

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
        
    def to_string(self) -> str:
        """returns nice printed string representation of variableBase object.

        Returns:
            str: string representation
        """

        return self.json(indent=4, exclude_none=True)