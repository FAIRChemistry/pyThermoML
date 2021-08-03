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

from core.functionalities import TypeChecker
from core.datapoint import DataPoint
import json


class Measurement(object):

    def __init__(
        self,
        ID
    ):
        self.ID = ID
        self.properties = dict()
        self.variables = dict()

    def __str__(self):
        return json.dumps(
            self.__dict__,
            indent=4
        )

    def addDataPoints(self, dataPoints, pureMixtureData):

        if isinstance(dataPoints, DataPoint):
            dataPoints = [dataPoints]

        for dataPoint in dataPoints:

            elementID = dataPoint.elementID

            if elementID in pureMixtureData.properties.keys():
                self.addToElementList(elementID, self.properties, dataPoint)
            elif elementID in pureMixtureData.variables.keys():
                self.addToElementList(elementID, self.variables, dataPoint)
            else:
                raise AttributeError(
                    f"The property/variable with ID {elementID} is not defined yet.")

    @staticmethod
    def addToElementList(elementID, dictionary, dataPoint):
        if elementID not in dictionary:
            dictionary[elementID] = list()

        dictionary[elementID].append(dataPoint)

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
        self._properties = TypeChecker(properties, dict)

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables):
        self._variables = TypeChecker(variables, dict)
