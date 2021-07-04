from vars.variableBase import VariableBase

class ComponentComposition(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit
    ):

        super().__init__(
            varType="eComponentComposition",
            varName=varName,
            ID=ID,
            unit=unit
        )

# Initializers
# TODO: reference to compound ID
def moleFraction(
    ID: "Unique identifier"
):
    moleFractionVar = ComponentComposition(
        varName="Mole fraction",
        ID=ID,
        unit=""
    )

    return moleFractionVar