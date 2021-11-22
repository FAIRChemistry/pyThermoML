from pythermo.thermoml.props.propertyBase import PropertyBase


class TransportProperty(PropertyBase):

    propGroup: str = "TransportProp"

    @classmethod
    def viscosity(cls, ID: str, method: str, compoundID: str):
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def kinematicViscosity(cls, ID: str, method: str, compoundID: str):
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def microViscosity(cls, ID: str, method: str, compoundID: str):
        return cls(
            propName="Microviscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def selfDiffusionCoefficient(cls, ID: str, method: str, compoundID: str):
        return cls(
            propName="Self diffusion coefficient",
            ID=ID,
            unit="m2/s",
            method=method,
            compoundID=compoundID
        )
