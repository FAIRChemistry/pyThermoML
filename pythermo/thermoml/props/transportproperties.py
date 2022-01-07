'''
File: transportproperties.py
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


class TransportProperty(PropertyBase):
    """
    Class representing transport properties. The following properties are taken over from ThermoML - schema definition:
    Viscosity, kinematic viscosity, micro viscosity (not included in ThermoML schema), self diffusion coefficient.
    Inherited from PropertyBase.
    
        Args:
            propGroup (str): Transport property group
    
    """
    propGroup: str = "TransportProp"

    @classmethod
    def viscosity(cls, ID: str, method: str, compoundID: str = None):
        """creates viscosity object. For more information vist documentation of PropertyBase.
        
        Note:
            Unit: Pa*s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): ID of referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def kinematicViscosity(cls, ID: str, method: str, compoundID: str = None):
        """creates kinematic viscosity object. For more information vist documentation of PropertyBase.
        
        Note:
            Unit: Pa*s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): ID of referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def microViscosity(cls, ID: str, method: str, compoundID: str):
        """creates microviscosity object. For more information vist documentation of PropertyBase.
        
        Note:
            Unit: Pa*s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): ID of referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Microviscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def selfDiffusionCoefficient(cls, ID: str, method: str, compoundID: str):
        """creates self diffusion coefficient object. For more information vist documentation of PropertyBase.
        
        Note:
            Unit: m2/s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): determines referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Self diffusion coefficient",
            ID=ID,
            unit="m2/s",
            method=method,
            compoundID=compoundID
        )
