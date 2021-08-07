from core import PureOrMixtureData, Measurement, DataReport, Compound, DataPoint

from vars.componentcomposition import MoleFraction
from vars.temperature import LowerTemperature, Temperature
from vars.pressure import Pressure
from props.transportproperties import Viscosity

# TODO: import writer not intuitiv
from tools.writeTools import writeThermo
import json as j

# TODO: reading input data from excel spreadsheet
# TODO: significant digits

# title, DOI, authors
dataReport = DataReport("Title of referred paper", "DOI of referred paper", "author 1", "author 2")

# declaration of compound used in measurements
# TODO: Compound ID is fix? 1,2,3,... in ThermoML integers necesarry
comp1 = Compound("id1", "inhi1", "inchikey1", "smiles1", "water")
comp2 = Compound("id2", "inchi2", "inchikey2", "smiles2", "ethanol")


comp1_ID = dataReport.addCompound(comp1)
comp2_ID = dataReport.addCompound(comp2)

# components which are used in respective experiment
experiment = PureOrMixtureData("ID", comp1_ID, comp2_ID)

#property definitions
visc = Viscosity('visc1', "simulation")
# Variable definitions
temp = Temperature('temp1')

frac1 = MoleFraction('moleFrac1', comp1_ID)
frac2 = MoleFraction('moleFrac2', comp2_ID)

viscID = experiment.addProperty(visc)
tempID = experiment.addVariable(temp)
frac1ID = experiment.addVariable(frac1)
frac2ID = experiment.addVariable(frac2)

# not used in ThermoML
measurementID = "meas1"

viscDataPoint = DataPoint(
    measurementID=measurementID,
    value=10.0,
    propID=viscID,
    uncertainty=0.1
)

tempDataPoint = DataPoint(
    measurementID=measurementID,
    value=300.0,
    varID=tempID,
    uncertainty=10.0
)

frac1DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.2,
    varID=frac1ID,
    uncertainty=0.01
)

frac2DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.8,
    varID=frac2ID,
    uncertainty=0.02
)

print(viscDataPoint)
datapoints = [viscDataPoint, tempDataPoint, frac1DataPoint, frac2DataPoint]

# add Measurement to experiment
experiment.addMeasurement(dataPoints=datapoints)

# add experiment to dataReport
dataReport.addPureOrMixtureData(experiment)
print(dataReport)

writeThermo(dataReport, 'testThermo')


