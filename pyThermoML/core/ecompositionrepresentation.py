from enum import Enum


class eCompositionRepresentation(Enum):
    AMOUNT_RATIO_OF_SOLVENT_TO_PARTICIPANT = "Amount ratio of solvent to participant"
    MOLALITY_AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLVENT_MOLKG = (
        "Molality - amount of participant per mass of solvent, mol/kg"
    )
    AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLUTION_MOLKG = (
        "Amount of participant per mass of solution, mol/kg"
    )
    AMOUNT_CONCENTRATION_AMOUNT_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_MOLDM3 = (
        "Amount concentration - amount of participant per volume of solution, mol/dm3"
    )
    AMOUNT_RATIO_OF_PARTICIPANT_TO_SOLVENT = "Amount ratio of participant to solvent"
    MASS_RATIO_OF_PARTICIPANT_TO_SOLVENT = "Mass ratio of participant to solvent"
    VOLUME_RATIO_OF_PARTICIPANT_TO_SOLVENT = "Volume ratio of participant to solvent"
    MASS_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_KGM3 = (
        "Mass of participant per volume of solution, kg/m3"
    )
