# @File          :   volumetricproperties.py
# @Last modified :   2022/04/09 19:28:38
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart
from pythermo.thermoml.props.propertyBase import PropertyBase

class VolumetricProperty(PropertyBase):
    """
    Class representing heat volumetric properties. The following properties are taken over from ThermoML - schema definition:
    Mass density.
    Inherited from PropertyBase.
    
    Args:
        propGroup (str): Volumetric property group
    
    """
    propGroup: str = "VolumetricProp"

    @classmethod
    def massDensity(cls, ID: str, method: str, compoundID: str = None) -> 'VolumetricProperty':
        """creates massDensity object. For more information visit documentation of PropertyBase.

        Note:
            Unit: kg/m3

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because massDensity is not component specific.

        Returns:
            VolumetricProperty: object of type VolumetricProperty
        """
        return cls(
            propName="Mass density",
            ID=ID,
            unit="kg/m3",
            method=method,
            compoundID=compoundID
        )