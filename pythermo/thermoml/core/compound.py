from typing import Optional
from pydantic import BaseModel, PrivateAttr


class Compound(BaseModel):
    """class representing a compound used in ThermoML"""
    ID: str
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    commonName: Optional[str] = None
    _type: str = PrivateAttr(default="comp")