from pythermo.thermoml.props.propertyBase import PropertyBase


class RefractionSurfaceTensionSoundSpeedproperty(PropertyBase):

    propGroup: str = "RefractionSurfaceTensionSoundSpeed"

    @classmethod
    def surfaceTension(cls, ID: str, method: str, compoundID: str = None):
        return cls(
            propName="Surface tension liquid-gas",
            ID=ID,
            unit="N/m",
            method=method,
            compoundID = compoundID
        )

    @classmethod
    def speedOfSound(cls, ID: str, method: str, compoundID: str = None):
        return cls(
            propName="Speed of sound",
            ID=ID,
            unit="m/s",
            method=method,
            compoundID = compoundID
        )
