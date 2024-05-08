from enum import Enum


class eMethodName(Enum):
    STATIC_EQUILIBRATION = "Static equilibration"
    DYNAMIC_EQUILIBRATION = "Dynamic equilibration"
    CHROMATOGRAPHY = "Chromatography"
    IR_SPECTROMETRY = "IR spectrometry"
    UV_SPECTROSCOPY = "UV spectroscopy"
    NMR_SPECTROMETRY = "NMR spectrometry"
    TITRATION = "Titration"
    POTENTIAL_DIFFERENCE_OF_AN_ELECTROCHEMICAL_CELL = (
        "Potential difference of an electrochemical cell"
    )
    ANION_EXCHANGE = "Anion exchange"
    CATION_EXCHANGE = "Cation exchange"
    CELL_POTENTIAL_WITH_GLASS_ELECTRODE = "Cell potential with glass electrode"
    CELL_POTENTIAL_WITH_PLATINUM_ELECTRODE = "Cell potential with platinum electrode"
    CELL_POTENTIAL_WITH_QUINHYDRONE_ELECTRODE = (
        "Cell potential with quinhydrone electrode"
    )
    CELL_POTENTIAL_WITH_REDOX_ELECTRODE = "Cell potential with redox electrode"
    COLORIMETRY = "Colorimetry"
    CONDUCTIVITY_MEASUREMENT = "Conductivity measurement"
    COULOMETRY = "Coulometry"
    CRYOSCOPY = "Cryoscopy"
    DISTRIBUTION_BETWEEN_TWO_PHASES = "Distribution between two phases"
    ION_SELECTIVE_ELECTRODE = "Ion selective electrode"
    MOLAR_VOLUME_DETERMINATION = "Molar volume determination"
    POLAROGRAPHY = "Polarography"
    POTENTIOMETRY = "Potentiometry"
    PROTON_RELAXATION = "Proton relaxation"
    RATE_OF_REACTION = "Rate of reaction"
    SOLUBILITY_MEASUREMENT = "Solubility measurement"
    SPECTROPHOTOMETRY = "Spectrophotometry"
    THERMAL_LENSING_SPECTROPHOTOMETRY = "Thermal lensing spectrophotometry"
    TRANSIENT_CONDUCTIVITY_MEASUREMENT = "Transient conductivity measurement"
    SOLVENT_EXTRACTION = "Solvent extraction"
    VOLTAMMETRY = "Voltammetry"
    OTHER = "Other"
