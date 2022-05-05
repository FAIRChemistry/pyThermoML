# @File          :   datapoint.py
# @Last modified :   2022/04/09 19:27:06
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Union, Optional
from pydantic import BaseModel, PrivateAttr, validator


class DataPoint(BaseModel):
    """
    Class that represents the value of one single variable/property.
    
    Args:
        measurementID (str): The ID of the measurement to which the value of the variable/property belongs.
        value (Union[float, int]): determined, averaged value
        propID (Optional[str]): reference to ID of measured property. propID = None when type of dataPoint is "Variable".
        varID (Optional[str]): reference to ID of determined variable. varID = None when type of dataPoint is "Property".
        uncertainty (Optional[float]): standard uncertainty around the value
        numberOfDigits (Optional[int]): number of digits of the value: Describes the accuracy of the measured value
        data_point_type (Optional[str]): deciedes whether data point is "Variable" or "Property"
        elementID (Optional[str]): Contains in both cases (Variable and Property) the respective ID.
    """

    measurementID: str
    value: Union[float, int]
    propID: Optional[str] = None
    varID: Optional[str] = None
    uncertainty: Optional[float]
    numberOfDigits: Optional[int]
    data_point_type: Optional[str] = None
    _elementID: PrivateAttr(Optional[str]) = None

    @validator("_elementID", always=True)
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
