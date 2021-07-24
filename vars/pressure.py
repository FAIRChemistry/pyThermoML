from vars.variableBase import VariableBase


class Pressure(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit
    ):

        super().__init__(
            varType="ePressure",
            varName=varName,
            ID=ID,
            unit=unit
        )

# Initializers

def pressure(
    ID: "Unique identifier"
):
    pressureVar = Pressure(
        varName="Pressure",
        ID=ID,
        unit="kPa"
    )

    return pressureVar
