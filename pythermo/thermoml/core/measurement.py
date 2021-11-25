'''
File: measurement.py
Project: core
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:35:56 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from pydantic import BaseModel

from pythermo.thermoml.core.datapoint import DataPoint
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData

class Measurement(BaseModel):
    """class representing a measurement in data report. Each measurement has a user specified ID. 
    Each measurement contains all property/variable data point of one measurement."""

    ID: str
    properties: dict[str, DataPoint] = {}
    variables: dict[str, DataPoint] = {}

    def addDataPoints(self, dataPoints: list[DataPoint], pureMixtureData: PureOrMixtureData) -> None:
        """adds list of data points of measurement

        Args:
            dataPoints (list[DataPoint]): list with data points.
            pureMixtureData (PureOrMixtureData): pure or mixture data base class which contains measurement

        Raises:
            AttributeError: [description]
        """
        if isinstance(dataPoints, DataPoint):
            dataPoints = [dataPoints]

        for dataPoint in dataPoints:

            elementID = dataPoint.elementID
            data_point_type = dataPoint.data_point_type

            if elementID in pureMixtureData.properties.keys() and data_point_type == "Property":
                self.addToElementList(elementID, self.properties, dataPoint)
            elif elementID in pureMixtureData.variables.keys() and data_point_type == "Variable":
                self.addToElementList(elementID, self.variables, dataPoint)
            else:
                raise AttributeError(
                    f"The property/variable with ID {elementID} is not defined yet.")

    @staticmethod
    def addToElementList(elementID, dictionary, dataPoint):
        if elementID not in dictionary:
            dictionary[elementID] = list()

        dictionary[elementID].append(dataPoint)

    def getProperty(self, propertyID):
        return self._getElement(
            propertyID,
            self.properties,
            "Property"
        )

    def getVariable(self, variableID):
        return self._getElement(
            variableID,
            self.variables,
            "Variable"
        )

    def _getElement(self, elementID, dictionary, type_):
        try:
            return dictionary[elementID]
        except KeyError:
            raise KeyError(
                f"{type_} {elementID} is not defined yet."
            )
