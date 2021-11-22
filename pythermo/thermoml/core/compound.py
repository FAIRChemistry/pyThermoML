from typing import Optional
from pydantic import BaseModel, validator, PrivateAttr


class Compound(BaseModel):

    ID: str
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    commonName: Optional[str] = None
    _type: str = PrivateAttr(default="comp")

    @validator("ID")
    def validate_ID_string(cls, ID):
        if ID.startswith("c"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'c[digit/s]'"
            )
