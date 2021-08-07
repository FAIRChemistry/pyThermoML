from props.propertyBase import PropertyBase


class HeatCapacityProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method):

        super().__init__(
            propName=propName,
            propGroup="HeatCapacityAndDerivedProp",
            ID=ID,
            unit=unit,
            method=method
        )


# Initializer functions
def MolarHCconstPressure(ID, method):

    hcprop = HeatCapacityProperty(
        propName="Molar heat capacity at constant pressure",
        ID=ID,
        unit="J/K/mol",
        method=method,
    )

    return hcprop

def MolarHCconstVolume(ID, method):

    hcprop = HeatCapacityProperty(
        propName="Molar heat capacity at constant volume",
        ID = ID,
        unit="J/K/mol",
        method = method
    )

    return hcprop
