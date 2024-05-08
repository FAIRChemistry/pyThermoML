from enum import Enum


class eRepeatMethod(Enum):
    STANDARD_DEVIATION_OF_A_SINGLE_VALUE_BIASED = (
        "Standard deviation of a single value (biased)"
    )
    STANDARD_DEVIATION_OF_A_SINGLE_VALUE_UNBIASED = (
        "Standard deviation of a single value (unbiased)"
    )
    STANDARD_DEVIATION_OF_THE_MEAN = "Standard deviation of the mean"
    OTHER = "Other"
