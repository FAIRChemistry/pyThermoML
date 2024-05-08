from enum import Enum


class eBioVariables(Enum):
    PH = "pH"
    IONIC_STRENGTH_MOLALITY_BASIS_MOLKG = "Ionic strength (molality basis), mol/kg"
    IONIC_STRENGTH_AMOUNT_CONCENTRATION_BASIS_MOLDM3 = (
        "Ionic strength (amount concentration basis), mol/dm3"
    )
    PC_AMOUNT_CONCENTRATION_BASIS = "pC (amount concentration basis)"
    SOLVENT_PC_AMOUNT_CONCENTRATION_BASIS = "Solvent: pC (amount concentration basis)"
