from core import PureOrMixtureData, Measurement, DataReport, Compound, datareport

from vars.componentcomposition import moleFraction
from vars.temperature import temperature
from props.transportproperties import viscosity

# TODO: import writer not intuitiv
import tools.writeTools as wrt
import json as j

# TODO: reading input data from excel spreadsheet
# TODO: uncertainty, significant digits

# title, DOI, authors
dataReport = DataReport(
    "Examination of blablabla",
    "DOI734",
    "author1", "author2", "author3"
)

# declaration of compound used in measurements
# TODO: Compound ID is fix? 1,2,3,... in ThermoML integers necesarry
comp1 = Compound("id1", "inhi1", "inchikey1", "smiles1", "water")
comp2 = Compound("id2", "inchi2", "inchikey2", "smiles2", "ethanol")

comp1_ID = dataReport.addCompound(comp1)
comp2_ID = dataReport.addCompound(comp2)

# components which are used in respective experiment
experiment = PureOrMixtureData("ID", "experiment1", comp1_ID, comp2_ID)

# Property definitions
visc = viscosity('V', "simulation")

# Variable definitions
temp = temperature('T')

# mole fractions, depends on compound
frac1 = moleFraction('MF1', comp1_ID)
frac2 = moleFraction('MF2', comp2_ID)

viscID = experiment.addProperty(visc)

tempID = experiment.addVariable(temp)
frac1ID = experiment.addVariable(frac1)
frac2ID = experiment.addVariable(frac2)

dataReport.addPureOrMixtureData(experiment)

values = {
    tempID: 273.15,
    frac1ID: 0.5,
    frac2ID: 0.5,

    viscID: 1.0
}


meas = Measurement(
    "meas1",
    values,
    pureOrMixtureData=experiment
)

experiment.addMeasurements(meas)


print(dataReport)
wrt.toThermoML(dataReport.toJSON(), 'testThermo')


obj = {

    "Viscosity": viscosity
}

for tagName in tags:

    fun = obj[tagName] - -> viscosity

    fun()
