'''
File: variableBase.py
Project: vars
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 11:51:44 am
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

class VariableBase(object):
    
    def __init__(
        self,
        varType: 'Variable Type',
        varName: 'Variable Name',
        ID: 'Variable identifier',
        unit: 'Measured unit'
    ) -> None:

        self.varType = varType
        self.varName = varName
        self.ID = ID
        self.unit = unit

    @property
    def varType(self):
        return self._varType

    @varType.setter
    def varType(self, varType):
        self._varType = varType

    @property
    def varName(self):
        return self._varName

    @varName.setter
    def varName(self, varName):
        self._varName = varName

    @property
    def ID(self):
        return self.ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        self._unit = unit
