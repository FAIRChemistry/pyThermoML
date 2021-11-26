from pythermo.thermoml.core import DataReport, Compound
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader




writer = ThermoMLWriter(dataRep="github.json", filename="a.xml")
writer.writeThermo()

reader = ThermoMLReader(path="a.xml")
dr = reader.readFromThermoMLFile()


x = dr.getPureOrMixtureData("pom1").getMeasurement("meas1")._getProperty("pdens")
print(x)