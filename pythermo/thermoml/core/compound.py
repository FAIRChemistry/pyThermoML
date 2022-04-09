# @File          :   compound.py
# @Last modified :   2022/04/09 19:26:58
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pydantic import BaseModel, validator, PrivateAttr


class Compound(BaseModel):
    """
    Class representing a compound used in ThermoML.

    Args:
        ID (str): user specified ID
        standardInchI (Optional[str]): standardInchI of used compound (Optional)
        standardInchIKey (Optional[str]): standardInchIKey of used compound (Optional)
        smiles (Optional[str]): smiles code of used compound (Optional)
        commonName (Optional[str]): common name of used compound (Optional)
    """
    ID: str
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    commonName: Optional[str] = None
    _type: str = PrivateAttr(default="comp")

    @validator("ID", always=True)
    def validate_ID_string(cls, ID: str):
        """User specified ID of compund has to be in the following pattern: 'c[digit/s]'.

        Args:
            ID (str): User specified ID

        Raises:
            TypeError: If ID does not match expected pattern.

        Returns:
            str: ID
        """
        if ID.startswith("c"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'c[digit/s]'"
            )
