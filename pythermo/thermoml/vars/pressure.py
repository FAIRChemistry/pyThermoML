from pythermo.thermoml.vars.variableBase import VariableBase


class PressureBase(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit,
        compoundID=None
    ):

        super().__init__(
            varType="ePressure",
            varName=varName,
            ID=ID,
            unit=unit,
            compoundID=compoundID
        )

# Initializers

def Pressure(
    ID: "Unique identifier",
    compoundID=None
):
    # not component specific!
    
    if compoundID is not None:
        compoundID=None
    
    pressureVar = PressureBase(
        varName="Pressure",
        ID=ID,
        unit="kPa",
        compoundID=compoundID
    )

    return pressureVar
