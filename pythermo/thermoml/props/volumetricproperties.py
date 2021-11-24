from pythermo.thermoml.props.propertyBase import PropertyBase


class VolumetricProperty(PropertyBase):

    propGroup: str = "VolumetricProp"

    @classmethod
    def massDensity(cls, ID: str, method: str, compoundID: str = None):
        return cls(
            propName="Mass density",
            ID=ID,
            unit="kg/m3",
            method=method,
            compoundID=compoundID
        )
