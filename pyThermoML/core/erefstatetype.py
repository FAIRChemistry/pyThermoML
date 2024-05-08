from enum import Enum


class eRefStateType(Enum):
    REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_AT_FIXED_TEMPERATURE_AND_PRESSURE = (
        "Reference phase with the same composition at fixed temperature and pressure"
    )
    REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_TEMPERATURE_AND_PRESSURE = (
        "Reference phase with the same composition, temperature and pressure"
    )
    REFERENCE_PHASE_AT_FIXED_TEMPERATURE_AND_THE_SAME_PRESSURE = (
        "Reference phase at fixed temperature and the same pressure"
    )
    REFERENCE_PHASE_AT_THE_SAME_TEMPERATURE_AND_FIXED_PRESSURE = (
        "Reference phase at the same temperature and fixed pressure"
    )
    IDEAL_GAS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION = (
        "Ideal gas at the same amount density, temperature, and composition"
    )
    IDEAL_MIXTURE_OF_PURE_FLUID_COMPONENTS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION = (
        "Ideal mixture of pure fluid components at the same amount density,"
        " temperature, and composition"
    )
    PHASE_IN_EQUILIBRIUM_WITH_PRIMARY_PHASE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = (
        "Phase in equilibrium with primary phase at the same temperature and pressure"
    )
    PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_FIXED_TEMPERATURE_AND_PRESSURE = (
        "Pure components in the same proportion at fixed temperature and pressure"
    )
    PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = (
        "Pure components in the same proportion at the same temperature and pressure"
    )
    PURE_SOLVENT_AT_THE_TEMPERATURE_OF_THE_SAME_PHASE_EQUILIBRIUM = (
        "Pure solvent at the temperature of the same phase equilibrium"
    )
    PURE_SOLVENT_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = (
        "Pure solvent at the same temperature and pressure"
    )
    PURE_SOLUTE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = (
        "Pure solute at the same temperature and pressure"
    )
