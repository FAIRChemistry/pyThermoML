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

from pythermo.thermoml.props.propertyBase import PropertyBase


class Bioproperty(PropertyBase):
    """
    Class representing bioproperties. The following properties are taken over from ThermoML - schema definition:
    Peak temperature.
    Inherited from PropertyBase.
    
        Args:
            propGroup (str): Bioproperty
    
    """
    propGroup: str = "Bioproperty"

    @classmethod
    def peakTemperature(cls, ID: str, method: str, compoundID: str = None):
        """creates bioproperty object. For more information vist documentation of PropertyBase.

        Note:
            Unit: K

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because peak temperature is not component specific.

        Returns:
            Bioproperty: object of type Bioproperty.
        """
        return cls(
            propName="Peak temperature",
            ID=ID,
            unit="K",
            method=method,
            compoundID = compoundID
        )
