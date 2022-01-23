import sys

sys.path.insert(1, 'C://Users//Matthias Gültig//Documents//pyThermoML')

from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader



# creating ThermoML - writer object to convert json file to ThermoML file.
writer = ThermoMLWriter(dataRep="testThermo.json", filename="testThermo.xml")
writer.writeThermo()

reader = ThermoMLReader(path="testThermo.xml")
dataReport = reader.readFromThermoMLFile()

print(dataReport.compounds)
print(dataReport.getPureOrMixtureData("pom1").getPOMProperty("p1"))
#method = dataReport.getPureOrMixtureData("pom1").getMeasurement("meas1").getProperty("pdens").value

#print(method)
