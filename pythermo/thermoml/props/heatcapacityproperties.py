'''
File: heatcapacityproperties.py
Project: props
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from pythermo.thermoml.props.propertyBase import PropertyBase


class HeatCapacityProperty(PropertyBase):
    """
    Class representing heat capacity properties. The following properties are taken over from ThermoML - schema definition:
    Molar heat capacity at constant pressure (molarHCconstPressure)
    Malar heat capacity at constant volume (molarHCconstVolume)
    Inherited from PropertyBase.

        Args:
            propGroup (str): Heat capacity and derived properies

    """
    propGroup: str = "HeatCapacityAndDerivedProp"

    @classmethod
    def molarHCconstPressure(cls, ID: str, method: str, compoundID: str = None):
        """creates molarHCconstPressure object. For more information vist documentation of PropertyBase.

        Note:
            Unit: J/K/mol

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because heat capacity is not component specific.

        Returns:
            HeatCapacityProperty: object of type HeatCapacityProperty.
        """
        return cls(
            propName="Molar heat capacity at constant pressure",
            ID=ID,
            unit="J/K/mol",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def molarHCconstVolume(cls, ID: str, method: str, compoundID: str = None):
        """creates molarHCconstVolume object. For more information vist documentation of PropertyBase.

        Note:
            Unit: J/K/mol

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because heat capacity is not component specific.

        Returns:
            HeatCapacityProperty: object of type HeatCapacityProperty.
        """
        return cls(
            propName="Molar heat capacity at constant volume",
            ID=ID,
            unit="J/K/mol",
            method=method,
            compoundID=compoundID
        )
