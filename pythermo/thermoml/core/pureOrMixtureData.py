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

from pythermo.thermoml.core import measurement
from pythermo.thermoml.core.measurement import Measurement
import json


class PureOrMixtureData(object):

    def __init__(
        self,
        ID,
        *components,

    ):
        # Initialize metadata
        self.ID = ID

        # Initialize dictionaries
        self.comps = []
        self.properties = dict()
        self.variables = dict()
        self.measurements = dict()

        for comp in components:
            self.comps.append(comp)

    def __str__(self):

        def transformAttributes(self):

            jsonDict = dict()
            for key, value in self.__dict__.items():

                try:
                    jsonDict[key.replace('_', '')] = value
                except TypeError:
                    jsonDict[key.replace('_', '')] = str(value)

            return jsonDict

        return json.dumps(
            self,
            default=transformAttributes,
            indent=4
        )

    def addProperty(self, prop):
        if prop.dataType == "prop":

            # Add property to dicitonary
            self.properties[prop.ID] = prop

            return prop.ID

    def addVariable(self, variable):
        if variable.dataType == "var":

            # Add variable to dicitonary
            self.variables[variable.ID] = variable

            return variable.ID

    def addMeasurement(self, dataPoints):
        # print(dataPoints)
        for dataPoint in dataPoints:

            measurementID = dataPoint.measurementID
            # print(measurementID)
            # print(dataPoint)
            if measurementID not in self.measurements.keys():
                self.measurements[measurementID] = Measurement(measurementID)

            self.measurements[measurementID].addDataPoints(dataPoint, self)
            # print(self.measurements[measurementID])

    def getMeasurementsList(self):
        return [
            measurement
            for measurement in self._measurements.values()
        ]

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._properties = properties

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables):
        self._variables = variables

    @property
    def measurements(self):
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        self._measurements = measurements

    # TODO: getter/setter comps
