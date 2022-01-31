import sys

sys.path.insert(1, 'C://Users//matth//Documents//GitHub//pyThermoML')

from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader



# creating ThermoML - writer object to convert json file to ThermoML file.
writer = ThermoMLWriter(dataRep="testThermo.json", filename="testThermo.xml")
writer.writeThermo()

reader = ThermoMLReader(path="testThermo.xml")
dataReport = reader.readFromThermoMLFile()

print(list(dataReport.getPureOrMixtureData("pom1").properties.values()))
#method = dataReport.getPureOrMixtureData("pom1").getMeasurement("meas1").getProperty("pdens").value

#print(method)
