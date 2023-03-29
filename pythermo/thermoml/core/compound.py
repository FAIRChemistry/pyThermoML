# @File          :   compound.py
# @Last modified :   2022/04/09 19:26:58
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pydantic import BaseModel, PrivateAttr


class Sample(BaseModel):
    """Class representing a Sample used in ThermoML.

    Args:
        BaseModel (_type_): _description_
    """

    sample_number: int


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

    ID: int
    commonName: Optional[str] = None
    cas_name: Optional[str] = None
    molecular_formula: Optional[str] = None
    iupac_name: Optional[str] = None
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    sample: Optional[Sample] = None

    _type: str = PrivateAttr(default="comp")
