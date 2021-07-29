from props.propertyBase import PropertyBase


class TransportProperty(PropertyBase):

    def __init__(self, propName, ID, unit, method):

        super().__init__(
            propName=propName,
            propGroup="TransportProp",
            ID=ID,
            unit=unit,
            method=method
        )


# functions
# dynamic viscosity
# TODO: convert mPa*s -> Pa*s
def viscosity(ID, method):

    viscosityProp = TransportProperty(
        propName="Viscosity",
        ID=ID,
        unit="Pa*s",
        method=method,
    )

    return viscosityProp

# kinematic visosity
def kinematicViscosity(ID, method):

    viscosityProp = TransportProperty(
        propName="Kinematic Viscosity",
        ID = ID,
        unit="m2/s",
        method=method,
    )

    return viscosityProp

# Note: not inncluded in ThermoMl.xsd
# component specific?
def microviscosity(ID, method):

    microviscosityProp = TransportProperty(
        propName="Microviscosity",
        ID=ID,
        unit="Pa*s",
        method=method
    )

    return microviscosityProp

# TODO: self, tracer, binary?
def diffusioncoefficient(ID, method):
    
    diffProp = TransportProperty(
        propName="Self diffusion coefficient",
        ID = ID,
        unit="m2/s",
        method=method
    )

    return diffProp