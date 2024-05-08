from enum import Enum


class eCombUncertEvalMethod(Enum):
    PROPAGATION_OF_EVALUATED_STANDARD_UNCERTAINTIES = (
        "Propagation of evaluated standard uncertainties"
    )
    COMPARISON_WITH_REFERENCE_PROPERTY_VALUES = (
        "Comparison with reference property values"
    )
