from enum import Enum


class eAnalMeth(Enum):
    CHEMICAL_ANALYSIS = "Chemical analysis"
    DIFFERENCE_BETWEEN_BUBBLE_AND_DEW_TEMPERATURES = (
        "Difference between bubble and dew temperatures"
    )
    DENSITY = "Density"
    DSC = "DSC"
    ESTIMATION = "Estimation"
    GAS_CHROMATOGRAPHY = "Gas chromatography"
    FRACTION_MELTING_IN_AN_ADIABATIC_CALORIMETER = (
        "Fraction melting in an adiabatic calorimeter"
    )
    MASS_SPECTROMETRY = "Mass spectrometry"
    NMR_PROTON = "NMR (proton)"
    NMR_OTHER = "NMR (other)"
    NOT_KNOWN = "Not known"
    SPECTROSCOPY = "Spectroscopy"
    THERMAL_ANALYSIS_USING_TEMPERATURETIME_MEASUREMENT = (
        "Thermal analysis using temperature-time measurement"
    )
    ACIDBASE_TITRATION = "Acid-base titration"
    OTHER_TYPES_OF_TITRATION = "Other types of titration"
    MASS_LOSS_ON_DRYING = "Mass loss on drying"
    KARL_FISCHER_TITRATION = "Karl Fischer titration"
    HPLC = "HPLC"
    ION_CHROMATOGRAPHY = "Ion chromatography"
    IONSELECTIVE_ELECTRODE = "Ion-selective electrode"
    CO2_YIELD_IN_COMBUSTION_PRODUCTS = "CO2 yield in combustion products"
    OTHER = "Other"
    ESTIMATED_BY_THE_COMPILER = "Estimated by the compiler"
    STATED_BY_SUPPLIER = "Stated by supplier"
