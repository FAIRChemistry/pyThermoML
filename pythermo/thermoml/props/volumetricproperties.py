f
from pythermo.thermoml.props.propertyBase import PropertyBase


class VolumetricProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method):

        super().__init__(
            propName=propName,
            propGroup="VolumetricProp",
            ID=ID,
            unit=unit,
            method=method
        )

# functions
def MassDensity(ID, method):

    volumetricProp = VolumetricProperty(
        propName="Mass density",
        ID=ID,
        unit="kg/m3",
        method=method
    )

    return volumetricProp
