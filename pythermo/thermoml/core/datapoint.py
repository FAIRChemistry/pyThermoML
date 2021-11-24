
from typing import Union, Optional
from pydantic import BaseModel, validator


class DataPoint(BaseModel):

    measurementID: str
    value: Union[float, int]
    propID: Optional[str] = None
    varID: Optional[str] = None
    uncertainty: Optional[float]
    numberOfDigits: Optional[int]
    elementID: Optional[str] = None
    data_point_type: Optional[str] = None

    @validator("elementID", always=True)
    def specify_element_id(cls, v, values):
        propID = values.get("propID")
        varID = values.get("varID")

        if propID:
            values["data_point_type"] = "Property"
            return propID
        elif varID:
            values["data_point_type"] = "Variable"
            return varID
        else:
            raise TypeError(
                "Neither propertyID or variableID has been specified."
            )


if __name__ == "__main__":
    dp = DataPoint(measurementID="1", value="1", varID="11")
    print(dp.dict(exclude_none=True))
