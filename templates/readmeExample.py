import sys

sys.path.insert(1, 'C://Users//matth//Documents//GitHub//pyThermoML')

from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader

jsonData = {
    "title": "Examination of something",
    "authors": {
        "author1": "Matthias Gueltig"
    },
    "DOI": "1234356"
}

def bla():
    # creating ThermoML - writer object to convert json file to ThermoML file.
    writer = ThermoMLWriter(dataRep="githubExample.json", filename="githubExample.xml")
    writer.writeThermo()

    reader = ThermoMLReader(path="githubExample.xml")
    dataReport = reader.readFromThermoMLFile()
    print(dataReport.json(exclude_none=True, indent=4))
    #print(list(dataReport.getPureOrMixtureData("pom1").properties.values()))
    #method = dataReport.getPureOrMixtureData("pom1").getMeasurement("meas1").getProperty("pdens").value

    #print(method)

reader = ThermoMLReader(path=jsonData)
print(reader.readFromJSON())