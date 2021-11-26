from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader



# creating ThermoML - writer object to convert json file to ThermoML file.
writer = ThermoMLWriter(dataRep="githubExample.json", filename=".githubExample.xml")
writer.writeThermo()

reader = ThermoMLReader(path="github.json")
dataReport = reader.readFromJSON()


method = dataReport.getPureOrMixtureData("pom1").getMeasurement("meas1").getProperty("pdens").value

print(method)
