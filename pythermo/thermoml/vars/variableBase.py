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
    Base class for variables. All variables that were taken over by the ThermoML-schema definition inherit from this class.

    Args:
        varName (str): Name of the variable. Determined in child classes.
        varType (str): Name of belonging variable type. Determined in child classes.
        ID (str): User specified variable ID. Will be stored in nVarNumber tag in ThermoML .xml
        unit (str): Unit of Variable. Determined in child classes.
        compoundID (str, optional): ID of reffered compound

    """

    varType: str
    varName: str
    ID: int
    unit: str
    compoundID: Optional[int] = None
    _type: str = PrivateAttr(default="Variable")

    def to_string(self) -> str:
        """returns nice printed string representation of variableBase object.

        Returns:
            str: string representation
        """

        return self.json(indent=4, exclude_none=True)
