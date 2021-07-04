from props.propertyBase import PropertyBase


class VolumetricProperty(PropertyBase):

    def __init__(self, propName, ID, unit):

        super().__init__(
            propName=propName,
            propGroup="VoumeltricProperties",
            ID=ID,
            unit=unit
        )

# functions
def massDensity(ID):

    volumetricProp = VolumetricProperty(
        propName="Mass density",
        ID=ID,
        unit="kg/m3"
    )

    return volumetricProp
