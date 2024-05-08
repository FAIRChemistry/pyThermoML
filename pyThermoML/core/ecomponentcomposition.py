from enum import Enum


class eComponentComposition(Enum):
    MOLE_FRACTION = "Mole fraction"
    MASS_FRACTION = "Mass fraction"
    MOLALITY_MOLKG = "Molality, mol/kg"
    AMOUNT_CONCENTRATION_MOLARITY_MOLDM3 = "Amount concentration (molarity), mol/dm3"
    VOLUME_FRACTION = "Volume fraction"
    RATIO_OF_AMOUNT_OF_SOLUTE_TO_MASS_OF_SOLUTION_MOLKG = (
        "Ratio of amount of solute to mass of solution, mol/kg"
    )
    RATIO_OF_MASS_OF_SOLUTE_TO_VOLUME_OF_SOLUTION_KGM3 = (
        "Ratio of mass of solute to volume of solution, kg/m3"
    )
    AMOUNT_RATIO_OF_SOLUTE_TO_SOLVENT = "Amount ratio of solute to solvent"
    MASS_RATIO_OF_SOLUTE_TO_SOLVENT = "Mass ratio of solute to solvent"
    VOLUME_RATIO_OF_SOLUTE_TO_SOLVENT = "Volume ratio of solute to solvent"
    INITIAL_MOLE_FRACTION_OF_SOLUTE = "Initial mole fraction of solute"
    FINAL_MOLE_FRACTION_OF_SOLUTE = "Final mole fraction of solute"
    INITIAL_MASS_FRACTION_OF_SOLUTE = "Initial mass fraction of solute"
    FINAL_MASS_FRACTION_OF_SOLUTE = "Final mass fraction of solute"
    INITIAL_MOLALITY_OF_SOLUTE_MOLKG = "Initial molality of solute, mol/kg"
    FINAL_MOLALITY_OF_SOLUTE_MOLKG = "Final molality of solute, mol/kg"
