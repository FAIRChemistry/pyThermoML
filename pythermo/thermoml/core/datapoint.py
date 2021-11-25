from typing import Union, Optional
from pydantic import BaseModel, validator


class DataPoint(BaseModel):
    """class that represents a data point"""

    measurementID: str
    value: Union[float, int]
    propID: Optional[str] = None
    varID: Optional[str] = None
    uncertainty: Optional[float]
    numberOfDigits: Optional[int]
    data_point_type: Optional[str] = None
    elementID: Optional[str] = None

    @validator("elementID", always=True)
    @classmethod
    def specify_element_id(cls, v, values) -> str:
        """specifies whether elementID of new data point is property or variable. 
        Sets propID/varID as elementID and sets dat_point_type as "Variable" or "Property".

        Args:
            values (dict): dict representation of input

        Raises:
            TypeError: when neither propertyID or variableID has been specified.

        Returns:
            str: the varID or propID stored as elementID
        """
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
