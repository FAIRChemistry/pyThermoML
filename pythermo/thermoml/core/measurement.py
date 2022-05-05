# @File          :   measurement.py
# @Last modified :   2022/04/09 19:27:25
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from pydantic import BaseModel

from pythermo.thermoml.core.datapoint import DataPoint


class Measurement(BaseModel):
    """
    Class representing a measurement in a DataReport. 
    Each measurement is a list of property/variable datapoints that have the same measurement ID.

    Args:
        ID (str): user specified measurement ID.
        properties (dict[str, DataPoint]): dict with keys: propID, values: DataPoint of type Property.
        variables (dict[str, DataPoint]): dict with keys: varID, values: DataPoint of type Variable.

    """

    ID: str
    properties: dict[str, DataPoint] = {}
    variables: dict[str, DataPoint] = {}

    def addDataPoint(self, dataPoint: DataPoint, pureMixtureData) -> None:
        """Adds a datapoint to measurement.

        Args:
            dataPoint (DataPoint]): Datapoint that should be added to the measurement.
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
        """Returns datapoint representation of property in measurement.

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
        """Returns datapoint representation of variable in measurement.

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

    def getDataPointList(self) -> list[DataPoint]:
        """Returns list representation of datapoints used in measurement

        Returns:
            list[DataPoint]: list with data points.
        """
        dplist = []

        for propDp in self.properties.values():
            dplist.append(propDp)
        for varDp in self.variables.values():
            dplist.append(varDp)
        
        return dplist

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

    def to_string(self) -> str:
        """returns nice printed string representation of measurement object.

        Returns:
            str: string representation
        """

        return self.json(indent=4, exclude_none=True)