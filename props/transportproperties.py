from props.propertyBase import PropertyBase


class TransportProperty(PropertyBase):

    def __init__(self, propName, ID, unit):

        super().__init__(
            propName=propName,
            propGroup="TransportProperties",
            ID=ID,
            unit=unit
        )


# functions
def viscosity(ID):

    viscosityProp = TransportProperty(
        propName="Viscosity",
        ID=ID,
        unit="Pa*s"
    )

    return viscosityProp

# Note: not inncluded in ThermoMl.xsd
# component specific?
def microviscosity(ID):

    microviscosityProp = TransportProperty(
        propName="Microviscosity",
        ID=ID,
        unit="Pa*s"
    )

    return microviscosityProp

