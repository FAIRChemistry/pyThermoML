from pythermo.thermoml.vars.variableBase import VariableBase


class PressureBase(VariableBase):

    varType: str ="ePressure"

    @classmethod
    def pressure(cls, ID: str, compoundID: str = None):
        return cls(
            varName = "Pressure",
            ID = ID,
            unit = "kPa",
            compoundID = compoundID
        )