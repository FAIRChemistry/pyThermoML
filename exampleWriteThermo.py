from pythermo.thermoml.core import PureOrMixtureData, DataReport, Compound, DataPoint

from pythermo.thermoml.vars.componentcomposition import MoleFraction
from pythermo.thermoml.vars.temperature import LowerTemperature, Temperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.props.transportproperties import Viscosity
from pythermo.thermoml.tools.writeTools import writeThermo
from pythermo.thermoml.tools.readTools import readThermo
from pythermo.thermoml.props.volumetricproperties import MassDensity
import json as j
from lxml import etree
# TODO: reading input data from excel spreadsheet

# title, DOI, authors
authors = {
    "author 1": "Koichi Takamura",
    "author 2": "Herbert Fischer",
    "author 3": "Norman R. Morrow"
}

dataReport = DataReport("Physical properties of aqueous glycerol solutions",
                        "10.1016/j.petrol.2012.09.003", authors=authors)

# declaration of compound used in measurements
# TODO: Compound ID is fix? 1,2,3,... in ThermoML integers necesarry
comp1 = Compound("1", "InChI=1S/H2O/h1H2", "XLYOFNOQVPJJNP-UHFFFAOYSA-N", "O", "water")
comp2 = Compound("2", "InChI=1S/C3H8O3/c4-1-3(6)2-5/h3-6H,1-2H2", "PEDCQBHIVMGVHV-UHFFFAOYSA-N", "C(C(CO)O)O", "glycerol")


comp1_ID = dataReport.addCompound(comp1)
comp2_ID = dataReport.addCompound(comp2)

# components which are used in respective experiment
experiment = PureOrMixtureData("1", comp1_ID, comp2_ID)

# property definitions
dens = MassDensity('1', "simulation")
# Variable definitions
temp = Temperature('temp1')

frac1 = MoleFraction('moleFrac1', comp1_ID)
frac2 = MoleFraction('moleFrac2', comp2_ID)

densID = experiment.addProperty(dens)
tempID = experiment.addVariable(temp)
frac1ID = experiment.addVariable(frac1)
frac2ID = experiment.addVariable(frac2)

# not used in ThermoML
measurementID = "meas1"

viscDataPoint = DataPoint(
    measurementID=measurementID,
    value=10.0,
    propID=densID,
)

tempDataPoint = DataPoint(
    measurementID=measurementID,
    value=300.0,
    varID=tempID,
)

frac1DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.2,
    varID=frac1ID,
)

frac2DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.8,
    varID=frac2ID,
)

measurementID = "meas2"

viscDataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    propID=viscID,
    uncertainty=0.1
)

tempDataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    varID=tempID,
    uncertainty=10.0
)

frac1DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    varID=frac1ID,
    uncertainty=0.01
)

frac2DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000,
    varID=frac2ID,
    uncertainty=0.02
)

datapoints = [viscDataPoint, tempDataPoint, frac1DataPoint, frac2DataPoint]
datapoints2 = [viscDataPoint2, tempDataPoint2,
               frac1DataPoint2, frac2DataPoint2]
# add Measurement to experiment
experiment.addMeasurement(dataPoints=datapoints)
experiment.addMeasurement(dataPoints=datapoints2)
# add experiment to dataReport
dataReport.addPureOrMixtureData(experiment)

writeThermo(dataReport.toJSON(), 'testThermo.xml')

#file = etree.parse("testThermo.xml")
#print(etree.tostring(file, pretty_print=True, encoding=str))

#data = readThermo("testThermo.xml")
#print(data)
