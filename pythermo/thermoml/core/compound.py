from typing import Optional
from pydantic import BaseModel, validator


class Compound(BaseModel):

    ID: str
    standardInchI: Optional[str] = None
    standardInchIKey: Optional[str] = None
    smiles: Optional[str] = None
    commonName: Optional[str] = None
    _type: str = "comp"

    @validator("ID")
    def validate_ID_string(cls, ID):
        if ID.startswith("c"):
            return ID
        else:
            raise TypeError("ID blabla")


if __name__ == "__main__":
    comp = Compound(
        ID="c100"
    )

    print(comp.dict(exclude_none=True))
