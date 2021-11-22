from pythermo.thermoml.props.propertyBase import PropertyBase


class HeatCapacityProperty(PropertyBase):

    propGroup: str = "HeatCapacityAndDerivedProp"

    @classmethod
    def molarHCconstPressure(cls, ID: str, method: str, compoundID: str):
        return cls(
            propName="Molar heat capacity at constant pressure",
            ID=ID,
            unit="J/K/mol",
            method=method,
            compoundID=compoundID
        )

    @classmethod
    def MolarHCconstVolume(cls, ID: str, method: str, compoundID: str):
        return HeatCapacityProperty(
            propName="Molar heat capacity at constant volume",
            ID=ID,
            unit="J/K/mol",
            method=method,
            compoundID=compoundID
        )
