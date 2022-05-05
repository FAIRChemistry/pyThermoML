# @File          :   refractionSurfaceTensionSoundSpeedproperties.py
# @Last modified :   2022/04/09 19:28:27
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from pythermo.thermoml.props.propertyBase import PropertyBase


class RefractionSurfaceTensionSoundSpeedproperty(PropertyBase):
    """
    Class representing refraction surface tension and speed of sound properties. The following properties are taken over from ThermoML - schema definition:
    Surface tension, speed of sound.
    Inherited from PropertyBase.
    
    Args:
        propGroup (str): surface tension and speed of sound property group
    
    """

    propGroup: str = "RefractionSurfaceTensionSoundSpeed"

    @classmethod
    def surfaceTension(cls, ID: str, method: str, compoundID: str = None) -> 'RefractionSurfaceTensionSoundSpeedproperty':
        """creates surfaceTension object. For more information vist documentation of PropertyBase.
        Unit: N/m

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because surface Tension of a mixture is not component specific.

        Returns:
            RefractionSurfaceTensionSoundSpeedproperty: object of type RefractionSurfaceTensionSoundSpeedproperty
        """
        return cls(
            propName="Surface tension liquid-gas",
            ID=ID,
            unit="N/m",
            method=method,
            compoundID = compoundID
        )

    @classmethod
    def speedOfSound(cls, ID: str, method: str, compoundID: str = None) -> 'RefractionSurfaceTensionSoundSpeedproperty':
        """creates speed of sound object. For more information vist documentation of PropertyBase.
        Unit: m/s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str, optional): Defaults to None, because speed of sound in a mixture is not component specific.

        Returns:
            RefractionSurfaceTensionSoundSpeedproperty: object of type RefractionSurfaceTensionSoundSpeedproperty
        """
        return cls(
            propName="Speed of sound",
            ID=ID,
            unit="m/s",
            method=method,
            compoundID = compoundID
        )
