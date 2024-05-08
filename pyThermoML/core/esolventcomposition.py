from enum import Enum


class eSolventComposition(Enum):
    SOLVENT_MOLE_FRACTION = "Solvent: Mole fraction"
    SOLVENT_MASS_FRACTION = "Solvent: Mass fraction"
    SOLVENT_VOLUME_FRACTION = "Solvent: Volume fraction"
    SOLVENT_MOLALITY_MOLKG = "Solvent: Molality, mol/kg"
    SOLVENT_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3 = (
        "Solvent: Amount concentration (molarity), mol/dm3"
    )
    SOLVENT_AMOUNT_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = (
        "Solvent: Amount ratio of component to other component of binary solvent"
    )
    SOLVENT_MASS_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = (
        "Solvent: Mass ratio of component to other component of binary solvent"
    )
    SOLVENT_VOLUME_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = (
        "Solvent: Volume ratio of component to other component of binary solvent"
    )
    SOLVENT_RATIO_OF_AMOUNT_OF_COMPONENT_TO_MASS_OF_SOLVENT_MOLKG = (
        "Solvent: Ratio of amount of component to mass of solvent, mol/kg"
    )
    SOLVENT_RATIO_OF_COMPONENT_MASS_TO_VOLUME_OF_SOLVENT_KGM3 = (
        "Solvent: Ratio of component mass to volume of solvent, kg/m3"
    )
