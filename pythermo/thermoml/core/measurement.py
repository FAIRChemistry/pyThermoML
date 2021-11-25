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

    def addDataPoints(self, dataPoints: list[DataPoint], pureMixtureData) -> None:
        """adds list of data points to measurement

        Args:
            dataPoints (list[DataPoint]): list with data points, that should be added to measurement.
            pureMixtureData (PureOrMixtureData): pure or mixture data base class which contains measurement.

        Raises:
            AttributeError: property/variable with respective ID is not defined.
        """
        if isinstance(dataPoints, DataPoint):
            dataPoints = [dataPoints]

        for dataPoint in dataPoints:

            elementID = dataPoint.elementID
            data_point_type = dataPoint.data_point_type

            if elementID in pureMixtureData.properties.keys() and data_point_type == "Property":
                self._addToElementList(elementID, self.properties, dataPoint)
            elif elementID in pureMixtureData.variables.keys() and data_point_type == "Variable":
                self._addToElementList(elementID, self.variables, dataPoint)
            else:
                raise AttributeError(
                    f"The property/variable with ID {elementID} is not defined yet.")

    def _getProperty(self, propertyID):
        return self._getElement(
            propertyID,
            self.properties,
            "Property"
        )

    def _getVariable(self, variableID):
        return self._getElement(
            variableID,
            self.variables,
            "Variable"
        )

    @staticmethod
    def _addToElementList(elementID, dictionary, dataPoint):
        if elementID not in dictionary:
            dictionary[elementID] = list()

        dictionary[elementID].append(dataPoint)

    @staticmethod
    def _getElement(elementID, dictionary, type_):
        try:
            return dictionary[elementID]
        except KeyError:
            raise KeyError(
                f"{type_} {elementID} is not defined yet."
            )
