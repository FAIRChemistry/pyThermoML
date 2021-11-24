from pythermo.thermoml.vars.variableBase import VariableBase

class ComponentCompositionBase(VariableBase):

    varType: str = "eComponentComposition"

    @classmethod
    def moleFraction(cls, ID: str, compoundID: str):
        return cls(varName="Mole fraction",
        ID=ID,
        unit="",
        compoundID=compoundID
    )
