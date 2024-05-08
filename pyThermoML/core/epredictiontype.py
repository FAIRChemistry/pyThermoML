from enum import Enum


class ePredictionType(Enum):
    AB_INITIO = "Ab initio"
    MOLECULAR_DYNAMICS = "Molecular dynamics"
    SEMIEMPIRICAL_QUANTUM_METHODS = "Semiempirical quantum methods"
    MOLECULAR_MECHANICS = "Molecular mechanics"
    STATISTICAL_MECHANICS = "Statistical mechanics"
    CORRESPONDING_STATES = "Corresponding states"
    CORRELATION = "Correlation"
    GROUP_CONTRIBUTION = "Group contribution"
