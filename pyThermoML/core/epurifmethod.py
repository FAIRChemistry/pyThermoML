from enum import Enum


class ePurifMethod(Enum):
    IMPURITY_ADSORPTION = "Impurity adsorption"
    VACUUM_DEGASIFICATION = "Vacuum degasification"
    CHEMICAL_REAGENT_TREATMENT = "Chemical reagent treatment"
    CRYSTALLIZATION_FROM_MELT = "Crystallization from melt"
    CRYSTALLIZATION_FROM_SOLUTION = "Crystallization from solution"
    LIQUID_CHROMATOGRAPHY = "Liquid chromatography"
    DRIED_WITH_CHEMICAL_REAGENT = "Dried with chemical reagent"
    DRIED_IN_A_DESICCATOR = "Dried in a desiccator"
    DRIED_BY_OVEN_HEATING = "Dried by oven heating"
    DRIED_BY_VACUUM_HEATING = "Dried by vacuum heating"
    DEGASSED_BY_BOILING_OR_ULTRASONICALLY = "De-gassed by boiling or ultrasonically"
    DEGASSED_BY_EVACUATION = "De-gassed by evacuation"
    DEGASSED_BY_FREEZING_AND_MELTING_IN_VACUUM = (
        "De-gassed by freezing and melting in vacuum"
    )
    FRACTIONAL_CRYSTALLIZATION = "Fractional crystallization"
    FRACTIONAL_DISTILLATION = "Fractional distillation"
    MOLECULAR_SIEVE_TREATMENT = "Molecular sieve treatment"
    UNSPECIFIED = "Unspecified"
    PREPARATIVE_GAS_CHROMATOGRAPHY = "Preparative gas chromatography"
    SUBLIMATION = "Sublimation"
    STEAM_DISTILLATION = "Steam distillation"
    SOLVENT_EXTRACTION = "Solvent extraction"
    SALTING_OUT_OF_SOLUTION = "Salting out of solution"
    ZONE_REFINING = "Zone refining"
    OTHER = "Other"
    NONE_USED = "None used"
