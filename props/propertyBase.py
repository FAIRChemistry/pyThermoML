'''
File: property.py
Project: props
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 11:22:57 am
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

class PropertyBase(object):

    def __init__(
        self,
        propName:'Property name',
        propGroup: 'Property group name',
        ID: 'Property identifier',
        unit: 'Measured unit'
    ) -> None:
        
        self.propName = propName
        self.ID = ID
        self.propGroup = propGroup
        self.unit = unit

    @property
    def propName(self):
        return self._propName

    @propName.setter
    def propName(self, propName):
        self._propName = propName

    @property
    def ID(self):
        return self._ID

    @propName.setter
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

if __name__ == '__main__':

    newClass = Property("name", "propertygroup", "ID")
    print(newClass.propGroup)