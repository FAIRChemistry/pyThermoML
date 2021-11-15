from pythermo.thermoml.props.propertyBase import PropertyBase


class RefractionSurfaceTensionSoundSpeedproperty(PropertyBase):

    def __init__(self, propName, ID, unit, method, compoundID = None):

        super().__init__(
            propName=propName,
            propGroup="RefractionSurfaceTensionSoundSpeed",
            ID=ID,
            unit=unit,
            method=method,
            compoundID=compoundID
        )


# Initializer functions
# TODO: convert unnits?
def SurfaceTension(ID, method, compoundID):

    if compoundID is not None:
        compoundID = None

    rprop = RefractionSurfaceTensionSoundSpeedproperty(
        propName="Surface tension liquid-gas",
        ID=ID,
        unit="N/m",
        method=method,
        compoundID=compoundID
    )

    return rprop

def SpeedOfSound(ID, method, compoundID):

    if compoundID is not None:
        compoundID = None
    speedProp = RefractionSurfaceTensionSoundSpeedproperty(
        propName="Speed of sound",
        ID = ID,
        unit="m/s",
        method = method,
        compoundID = compoundID
    )

    return speedProp