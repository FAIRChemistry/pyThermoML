from pythermo.thermoml.tools.readTools import readThermo
import json


dataRep = readThermo("testThermo.xml")
datajson = dataRep.toJSON()
print(datajson)
print(type(datajson).__name__)
