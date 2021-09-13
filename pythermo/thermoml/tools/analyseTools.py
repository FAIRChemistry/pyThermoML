from pythermo.thermoml.props.bioproperties import PeakTemperature
from pythermo.thermoml.props.volumetricproperties import MassDensity
from pythermo.thermoml.props.refractionSurfaceTensionSoundSpeedproperties import SurfaceTension, SpeedOfSound
from pythermo.thermoml.props.heatcapacityproperties import MolarHCconstPressure, MolarHCconstVolume
from pythermo.thermoml.props.transportproperties import Diffusioncoefficient, KinematicViscosity, Microviscosity, Viscosity

from pythermo.thermoml.vars.temperature import LowerTemperature, Temperature, UpperTemperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.vars.componentcomposition import MoleFraction

from pythermo.thermoml.core import Compound, DataPoint, DataReport, PureOrMixtureData

from lxml import etree
import pandas as pd

propMapping = {
    'Viscosity, Pa*s': Viscosity,
    'Kinematic Viscosity, m2/s': KinematicViscosity,
    'Self diffusion coefficient, m2/s': Diffusioncoefficient,
    'Mass density, kg/m3': MassDensity,
    'Surface tension liquid-gas, N/m': SurfaceTension,
    'Speed of sound, m/s': SpeedOfSound,
    'Molar heat capacity at constant pressure, J/K/mol': MolarHCconstPressure,
    'Molar heat capacity at constant volume, J/K/mol': MolarHCconstVolume,
    'Peak temperature, K': PeakTemperature,

    # not in ThermoML
    'Microviscosity, Pa*s': Microviscosity
}

varMapping = {
    'Temperature, K': Temperature,
    'Lower temperature, K': LowerTemperature,
    'Upper temperature, K': UpperTemperature,
    'Mole fraction': MoleFraction,
    'Pressure, kPa': Pressure
}

def getProps(path):
    tree = etree.parse(path)
    root = tree.getroot()

