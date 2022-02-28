'''
File: datapoint.py
Project: core
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from typing import Union, Optional
from pydantic import BaseModel, validator


class DataPoint(BaseModel):
    """
    Class that represents a data point. Datapoint is used to describe one value of a specific measurement.
    
    Args:
        measurementID (str): ID of the whole measurement.
        value (Union[float, int]): measured/determined value.
        propID (Optional[str]): reference to ID of measured property. propID = None when type of dataPoint is "Variable".
        varID (Optional[str]): reference to ID of determined variable. varID = None when type of dataPoint is "Property".
        uncertainty (Optional[float]): Depending whether type of dataPoint is "Variable" or "Property".
            If data point is a variable: 
                Quantity defining an interval about the result of a measurement that may be expected to 
                encompass a large fraction of the distribution of values that could reasonably be attributed to the measurand. 
                (In ThermoML the expanded uncertainty value) 

            If data point is property:
                The combined standard uncertainty ucomb. The combined coverage factor kcomb and the combined expanded uncertainty Ucomb, 
                which also apply only to the designated property, are defined through the equation Ucomb = ucomb * kcomb. 
                For further information visit the link below.

            (From: ThermoML An XML-Based Approach for Storage and Exchange of Experimental and Critically Evaluated Thermophysical and Thermochemical 
            Property Data. 1. Experimental Data, Michael Frenkel et. al., DOI: https://doi.org/10.1021/je025645o)
        numberOfDigits (Optional[int]): number of digits of determined value.
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
