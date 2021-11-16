'''
File: pureOrMixtureData.py
Project: core
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:31:16 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from typing import Union, Any
from pydantic import BaseModel, validate_arguments
from pythermo.thermoml.props.propertyBase import PropertyBase
from pythermo.thermoml.vars.variableBase import VariableBase
from pythermo.thermoml.core.measurement import Measurement
from pythermo.thermoml.core.datapoint import DataPoint
from pythermo.thermoml.core.exceptions import ThermoMLTypeError


class PureOrMixtureData(BaseModel):

    ID: str
    comps: list[str] = []
    properties: dict[str, Any] = {}
    variables: dict[str, Any] = {}
    measurements: dict[str, Any] = {}

    def addProperty(self, prop: PropertyBase) -> str:
        if prop.dataType != "prop":
            raise ThermoMLTypeError(
                given_type=prop.dataType, expected_type="Property"
            )

        # Add property to dicitonary
        self.properties[prop.ID] = prop

        return prop.ID

    def addVariable(self, variable: VariableBase) -> str:
        if variable.dataType != "var":
            raise ThermoMLTypeError(
                given_type=variable.dataType, expected_type="Variable"
            )

        # Add variable to dicitonary
        self.variables[variable.ID] = variable

        return variable.ID

    def addMeasurement(self, dataPoints: list[DataPoint]) -> None:
        for dataPoint in dataPoints:

            measurementID = dataPoint.measurementID
            if measurementID not in self.measurements.keys():
                self.measurements[measurementID] = Measurement(measurementID)

            self.measurements[measurementID].addDataPoints(dataPoint, self)

    def getMeasurementsList(self) -> list[Measurement]:
        return list(self.measurements.values())

    @validate_arguments
    def getPOMProperty(self, propertyID: str) -> PropertyBase:
        return self._getElement(
            propertyID,
            self.properties,
        )

    @validate_arguments
    def getPOMVariable(self, variableID: str) -> VariableBase:
        return self._getElement(
            variableID,
            self.variables,
        )

    def _getElement(
        self,
        elementID: str,
        dictionary: Union[dict[str, VariableBase],
                          dict[str, PropertyBase]]
    ) -> Union[VariableBase, PropertyBase]:

        try:
            return dictionary[elementID]
        except KeyError:
            raise KeyError(
                f"{elementID} is not defined yet."
            )

    @validate_arguments
    def getPOMPropertyList(self) -> dict:
        """returns dictionary with ID (key) of property (value) used in pure or mixture data"""
        propertyDict = dict()
        for value in self.properties.values():
            propertyDict[value.ID] = value
        return propertyDict

    @validate_arguments
    def getPOMVariableList(self) -> dict:
        """returns dictionary with ID (key) of variable (value) used in pure or mixture data"""
        variableDict = dict()
        for value in self.variables.values():
            variableDict[value.ID] = value
        return variableDict

    @validate_arguments
    def getMoleFractionIDs(self):
        '''
        returns dictionary of compound <-> molefraction assignement
        keys: compoundIDs
        values: moleFractionVariableIDs
        '''

        moleFracCompound = dict()

        for key in self.comps:

            for value in self.variables:
                try:
                    if self.getPOMVariable(value).compoundID == key:
                        moleFracCompound[key] = value

                except AttributeError:
                    continue
        return moleFracCompound


if __name__ == "__main__":
    pom = PureOrMixtureData(
        ID="Lol"
    )

    print(pom)
