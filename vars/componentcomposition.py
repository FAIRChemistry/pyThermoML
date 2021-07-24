from vars.variableBase import VariableBase

class ComponentComposition(VariableBase):

    def __init__(
        self,
        varName,
        ID,
        unit,
        compoundID,
    ) -> None:

        super().__init__(
            varType="eComponentComposition",
            varName=varName,
            ID=ID,
            unit=unit
        )

        self.compoundID = compoundID

    @property
    def compoundID(self):
        return self._compoundID

    @compoundID.setter
    def compoundID(self, compoundID):
        self._compoundID = compoundID

# Initializers
# TODO: reference to compound ID -> Done?
def moleFraction(
    ID: "Unique identifier",
    compoundID: "ID of compound"
):
    moleFractionVar = ComponentComposition(
        varName="Mole fraction",
        ID=ID,
        unit="",
        compoundID=compoundID
    )

    return moleFractionVar



