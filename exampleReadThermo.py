from pythermo.thermoml.tools.readTools import readThermo
import json


dataRep = readThermo("DataGudrunGygli/cml2ThermoML/water/water_DOI1.xml")

dataRep = dataRep.toJSON()

with open("testThermo2.json", "w") as outfile:
    outfile.write(dataRep)



