from enum import Enum


class ePresentation(Enum):
    DIRECT_VALUE_X = "Direct value, X"
    DIFFERENCE_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT1 = (
        "Difference between upper and lower temperature, X(T2)-X(T1)"
    )
    DIFFERENCE_BETWEEN_UPPER_AND_LOWER_PRESSURE_XP2XP1 = (
        "Difference between upper and lower pressure, X(P2)-X(P1)"
    )
    MEAN_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT12 = (
        "Mean between upper and lower temperature, [X(T2)+X(T1)]/2"
    )
    DIFFERENCE_WITH_THE_REFERENCE_STATE_XXREF = (
        "Difference with the reference state, X-X(REF)"
    )
    RATIO_WITH_THE_REFERENCE_STATE_XXREF = "Ratio with the reference state, X/X(REF)"
    RATIO_OF_DIFFERENCE_WITH_THE_REFERENCE_STATE_TO_THE_REFERENCE_STATE_XXREFXREF = (
        "Ratio of difference with the reference state to the reference state,"
        " [X-X(REF)]/X(REF)"
    )
