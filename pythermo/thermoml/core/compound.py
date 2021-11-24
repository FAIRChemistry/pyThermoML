from typing import Optional
from pydantic import BaseModel, validator, PrivateAttr


class Compound(BaseModel):
    """class representing a compound used in ThermoML"""
    ID: str
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    commonName: Optional[str] = None
    _type: str = PrivateAttr(default="comp")

    @validator("ID")
    def validate_ID_string(cls, ID):
        """[summary]

        Args:
            ID ([type]): [description]

        Raises:
            TypeError: [description]

        Returns:
            [type]: [description]
        """
        if ID.startswith("c"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'c[digit/s]'"
            )
