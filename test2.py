from core import PureOrMixtureData, Measurement, DataReport, Compound

from vars.componentcomposition import moleFraction
from vars.temperature import temperature
from props.transportproperties import viscosity

# TODO: uncertainty, significant digits
dataReport = DataReport(
    "Examination of blablabla",
    "DOI734",
    "author1", "author2", "author3"
)

comp1 = Compound("1", "inhi1", "inchikey1", "smiles1", "water")
comp2 = Compound("2", "inchi2", "inchikey2", "smiles2", "ethanol")

dataReport.addCompound(comp1)
dataReport.addCompound(comp2)

comp1_ID = dataReport.addCompound(comp1)
comp2_ID = dataReport.addCompound(comp2)

experiment = PureOrMixtureData("ID", "experiment1")

# Property definitions
visc = viscosity('V')

# Variable definitions
temp = temperature('T')

# TODO: Reference to Compounds
frac1 = moleFraction('MF1')
frac2 = moleFraction('MF2')

viscID = experiment.addProperty(visc)

tempID = experiment.addVariable(temp)
frac1ID = experiment.addVariable(frac1)
frac2ID = experiment.addVariable(frac2)



values = {
    tempID: 273.15,
    frac1ID: 0.5,
    frac2ID: 0.5,
    
    viscID: 1.0
}



meas = Measurement(
    values,
    pureOrMixtureData=experiment
)

print(meas)