from vars.variableBase import VariableBase

class ComponentCompositionBase(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit,
        compoundID
    ) -> None:

        super().__init__(
            varType="eComponentComposition",
            varName=varName,
            ID=ID,
            unit=unit,
            compoundID = compoundID
        )

# Initializers
# TODO: reference to compound ID -> Done?
def MoleFraction(
    ID: "Unique identifier",
    compoundID: "ID of compound"
):
    moleFractionVar = ComponentCompositionBase(
        varName="Mole fraction",
        ID=ID,
        unit="",
        compoundID=compoundID
    )

    return moleFractionVar



