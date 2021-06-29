'''
File: bioproperties.py
Project: props
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 11:22:51 am
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from props.propertyBase import PropertyBase

class Bioproperty(PropertyBase):

    def __init__(self, propName, ID, unit):

        super().__init__(
            propName=propName,
            propGroup="BioProperties",
            ID=ID,
            unit=unit
        )

# Initializer functions

def peakTemperature(
    ID: 'Unique Identifier'
):

    bioProp = Bioproperty(
        propName="Peak temperature",
        ID=ID,
        unit="K"
    )

    return bioProp
