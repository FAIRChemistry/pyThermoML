'''
File: measurement.py
Project: core
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from pydantic import BaseModel, validator

from pythermo.thermoml.core.datapoint import DataPoint


class Measurement(BaseModel):
    """
    Class representing a measurement in DataReport. 
    Each measurement contains property/variable data point of one measurement (same measurement ID).

        Args:
            ID (str): user specified measurement ID.
            properties (dict[str, DataPoint]): dict with keys: propID, values: DataPoint of type Property.
            variables (dict[str, DataPoint]): dict with keys: varID, values: DataPoint of type Variable.

    """

    ID: str
    properties: dict[str, DataPoint] = {}
    variables: dict[str, DataPoint] = {}

    @validator("ID", always=True)
    @classmethod
    def validate_ID_string(cls, ID: str):
        """user specified ID of a measurement data has to be determined in the following pattern: 'meas[digit/s]'.

        Args:
            ID (str): user specified ID

        Raises:
            TypeError: ID does not match expected pattern.

        Returns:
            str: ID
        """
        if ID.startswith("meas"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'meas[digit/s]'"
            )

    def addDataPoint(self, dataPoint: DataPoint, pureMixtureData) -> None:
        """Adds list of DataPoints to measurement.

        Args:
            dataPoints (list[DataPoint]): list with data points, that should be added to measurement.
            pureMixtureData (PureOrMixtureData): pure or mixture data base class which contains measurement.

        Raises:
            AttributeError: property/variable with respective ID is not defined.
        """
        elementID = dataPoint.elementID
        data_point_type = dataPoint.data_point_type

        if elementID in pureMixtureData.properties.keys() and data_point_type == "Property":
            self._addDataPointToMeasurement(elementID, self.properties, dataPoint)
        elif elementID in pureMixtureData.variables.keys() and data_point_type == "Variable":
            self._addDataPointToMeasurement(elementID, self.variables, dataPoint)
        else:
            raise AttributeError(
                f"The property/variable with ID {elementID} is not defined yet.")

    def getProperty(self, propertyID:str) -> DataPoint:
        """Returns DataPoint representation of property in measurement.

        Args:
            propertyID (str): ID of property

        Returns:
            DataPoint: Datapoint representation of respective property.
        """
        return self._getElement(
            propertyID,
            self.properties,
            "Property"
        )

    def getVariable(self, variableID:str) -> DataPoint:
        """Returns DataPoint representation of variable in measurement.

        Args:
            variableID (str): ID of variable

        Returns:
            DataPoint: Datapoint representation of respective variable
        """
        return self._getElement(
            variableID,
            self.variables,
            "Variable"
        )

    @staticmethod
    def _addDataPointToMeasurement(elementID:str, dictionary:dict[str, DataPoint], dataPoint:DataPoint):
        """Refactored method for adding dataPoint to variable/property dictionary.
        
        Args:
            elementID (str): ID of prop/var
            dictionary (dict[str, DataPoint]): variable/property dictionary
            datapoint (DataPoint): DataPoint object
        """
        dictionary[elementID] = dataPoint

    @staticmethod
    def _getElement(elementID:str, dictionary:dict[str, DataPoint], data_point_type:str) -> DataPoint:
        """Refactored method to get prop/var.

        Args:
            elementID (str): ID of var/prop
            dictionary (dict[str, DataPoint]): variable/property dict
            data_point_type (str): type of DataPoint ("Property" or "Variable")

        Raises:
            KeyError: variable/property is not defined.

        Returns:
            DataPoint: DataPoint representation of variable/property.
        """
        try:
            return dictionary[elementID]
        except KeyError:
            raise KeyError(
                f"{data_point_type} {elementID} is not defined yet."
            )
