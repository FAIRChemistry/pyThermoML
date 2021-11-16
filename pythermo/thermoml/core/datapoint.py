
from typing import Union, Any, Optional
from pydantic import BaseModel, validator

class DataPoint(BaseModel):

    measurementID: str
    value: Union[float, int]
    propID: Optional[str] = None
    varID: Optional[str] = None
    uncertainty: Optional[float]
    numberOfDigits: Optional[int]
    elementID: Optional[str] = None
    _type: Optional[str] = None
    

if __name__ == "__main__":
    dp = DataPoint(measurementID="1", value="1", varID="11")
    print(dp.__dict__)
