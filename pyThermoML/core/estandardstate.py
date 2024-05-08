from enum import Enum


class eStandardState(Enum):
    PURE_COMPOUND = "Pure compound"
    PURE_LIQUID_SOLUTE = "Pure liquid solute"
    STANDARD_MOLALITY_1_MOLKG_SOLUTE = "Standard molality (1 mol/kg) solute"
    STANDARD_AMOUNT_CONCENTRATION_1_MOLDM3_SOLUTE = (
        "Standard amount concentration (1 mol/dm3) solute"
    )
    INFINITE_DILUTION_SOLUTE = "Infinite dilution solute"
