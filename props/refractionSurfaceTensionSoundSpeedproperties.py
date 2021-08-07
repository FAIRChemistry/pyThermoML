from props.propertyBase import PropertyBase


class RefractionSurfaceTensionSoundSpeedproperty(PropertyBase):

    def __init__(self, propName, ID, unit, method):

        super().__init__(
            propName=propName,
            propGroup="RefractionSurfaceTensionSoundSpeed",
            ID=ID,
            unit=unit,
            method=method
        )


# Initializer functions
# TODO: convert unnits?
def SurfaceTension(ID, method):

    rprop = RefractionSurfaceTensionSoundSpeedproperty(
        propName="Surface tension liquid-gas",
        ID=ID,
        unit="N/m",
        method=method
    )

    return rprop

def SpeedOfSound(ID, method):

    speedProp = RefractionSurfaceTensionSoundSpeedproperty(
        propName="Speed of sound",
        ID = ID,
        unit="m/s",
        method = method
    )

    return speedProp