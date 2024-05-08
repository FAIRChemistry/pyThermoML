from enum import Enum


class ePropPhase(Enum):
    CRYSTAL_5 = "Crystal 5"
    CRYSTAL_4 = "Crystal 4"
    CRYSTAL_3 = "Crystal 3"
    CRYSTAL_2 = "Crystal 2"
    CRYSTAL_1 = "Crystal 1"
    CRYSTAL = "Crystal"
    CRYSTAL_OF_UNKNOWN_TYPE = "Crystal of unknown type"
    CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = "Crystal of intercomponent compound 1"
    CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = "Crystal of intercomponent compound 2"
    CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = "Crystal of intercomponent compound 3"
    METASTABLE_CRYSTAL = "Metastable crystal"
    GLASS = "Glass"
    SMECTIC_LIQUID_CRYSTAL = "Smectic liquid crystal"
    SMECTIC_LIQUID_CRYSTAL_1 = "Smectic liquid crystal 1"
    SMECTIC_LIQUID_CRYSTAL_2 = "Smectic liquid crystal 2"
    NEMATIC_LIQUID_CRYSTAL = "Nematic liquid crystal"
    NEMATIC_LIQUID_CRYSTAL_1 = "Nematic liquid crystal 1"
    NEMATIC_LIQUID_CRYSTAL_2 = "Nematic liquid crystal 2"
    CHOLESTERIC_LIQUID_CRYSTAL = "Cholesteric liquid crystal"
    LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = "Liquid crystal of unknown type"
    LIQUID = "Liquid"
    LIQUID_MIXTURE_1 = "Liquid mixture 1"
    LIQUID_MIXTURE_2 = "Liquid mixture 2"
    LIQUID_MIXTURE_3 = "Liquid mixture 3"
    SOLUTION = "Solution"
    SOLUTION_1 = "Solution 1"
    SOLUTION_2 = "Solution 2"
    SOLUTION_3 = "Solution 3"
    SOLUTION_4 = "Solution 4"
    FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = (
        "Fluid (supercritical or subcritical phases)"
    )
    IDEAL_GAS = "Ideal gas"
    GAS = "Gas"
    AIR_AT_1_ATMOSPHERE = "Air at 1 atmosphere"
