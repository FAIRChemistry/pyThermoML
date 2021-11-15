from pythermo.thermoml.props.propertyBase import PropertyBase


class VolumetricProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method, compoundID=None):

        super().__init__(
            propName=propName,
            propGroup="VolumetricProp",
            ID=ID,
            unit=unit,
            method=method,
            compoundID=compoundID
        )

# functions
def MassDensity(ID, method, compoundID=None):
    print(compoundID)
    if compoundID is not None:
        compoundID = None

    volumetricProp = VolumetricProperty(
        propName="Mass density",
        ID=ID,
        unit="kg/m3",
        method=method,
        compoundID = compoundID
    )
    return volumetricProp
