from pythermo.thermoml.props.propertyBase import PropertyBase


class TransportProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method, compoundID):

        super().__init__(
            propName=propName,
            propGroup="TransportProp",
            ID=ID,
            unit=unit,
            method=method,
            compoundID= compoundID
        )


# functions
# dynamic viscosity
def Viscosity(ID, method, compoundID = None):
    if compoundID is not None:
        compoundID = None

    viscosityProp = TransportProperty(
        propName="Viscosity",
        ID=ID,
        unit="Pa*s",
        method=method,
        compoundID=compoundID
    )

    return viscosityProp

def KinematicViscosity(ID, method, compoundID = None):
    if compoundID is not None:
        compoundID=None
    viscosityProp = TransportProperty(
        propName="Kinematic Viscosity",
        ID=ID,
        unit="m2/s",
        method=method,
        compoundID = compoundID
    )

    return viscosityProp

# Note: not inncluded in ThermoMl.xsd
def Microviscosity(ID, method, compoundID = None):
    if compoundID is not None:
        compoundID = None
    microviscosityProp = TransportProperty(
        propName="Microviscosity",
        ID=ID,
        unit="Pa*s",
        method=method,
        compoundID = compoundID
    )

    return microviscosityProp


def Selfdiffusioncoefficient(ID, method, compoundID):

    diffProp = TransportProperty(
        propName="Self diffusion coefficient",
        ID=ID,
        unit="m2/s",
        method=method,
        compoundID = compoundID
    )

    return diffProp
