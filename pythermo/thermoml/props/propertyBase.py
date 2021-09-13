'''
File: property.py
Project: props
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:10:28 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

import json
from pythermo.thermoml.core.functionalities import TypeChecker


class PropertyBase(object):

    def __init__(
        self,
        propName,
        propGroup,
        ID,
        unit,
        method,
    ) -> None:

        self.propName = propName
        self.ID = ID
        self.propGroup = propGroup
        self.unit = unit
        self.method = method
        self.__type = "prop"
    def __str__(self):
        return json.dumps(
            self.__dict__,
            indent=4
        )

    @property
    def dataType(self):
        return self.__type

    @property
    def propName(self):
        return self._propName

    @propName.setter
    def propName(self, propName):
        self._propName = propName

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def propGroup(self):
        return self._propGroup

    @propGroup.setter
    def propGroup(self, propGroup):
        self._propGroup = propGroup

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        self._unit = unit

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method
