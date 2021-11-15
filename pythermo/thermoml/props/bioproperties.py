'''
File: bioproperties.py
Project: props
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 2:12:04 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from pythermo.thermoml.core import compound
from pythermo.thermoml.props.propertyBase import PropertyBase


class Bioproperty(PropertyBase):

    def __init__(self, propName, ID, unit, method, compoundID=None):

        super().__init__(
            propName=propName,
            propGroup="BioProperties",
            ID=ID,
            unit=unit,
            method=method,
            compoundID=compoundID
        )


# Initializer functions
def PeakTemperature(ID, method, compoundID):

    # not component specific property
    if compoundID is not None:
        compoundID=None
    
    bioProp = Bioproperty(
        propName="Peak temperature",
        ID=ID,
        unit="K",
        method=method,
        compoundID = compoundID
    )

    return bioProp
