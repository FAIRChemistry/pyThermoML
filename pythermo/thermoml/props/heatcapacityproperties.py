from pythermo.thermoml.props.propertyBase import PropertyBase


class HeatCapacityProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method, compoundID=None):

        super().__init__(
            propName=propName,
            propGroup="HeatCapacityAndDerivedProp",
            ID=ID,
            unit=unit,
            method=method,
            compoundID = compoundID
        )


# Initializer functions
def MolarHCconstPressure(ID, method, compoundID):

    hcprop = HeatCapacityProperty(
        propName="Molar heat capacity at constant pressure",
        ID=ID,
        unit="J/K/mol",
        method=method,
        compoundID=None
    )
    if compoundID is not None:
        compoundID=None
    return hcprop

def MolarHCconstVolume(ID, method, compoundID):

    if compoundID is not None:
        compoundID = None
    hcprop = HeatCapacityProperty(
        propName="Molar heat capacity at constant volume",
        ID = ID,
        unit="J/K/mol",
        method = method,
        compoundID = compoundID
    )

    return hcprop
