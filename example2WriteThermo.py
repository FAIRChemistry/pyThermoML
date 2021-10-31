import os
from pythermo.thermoml.tools.writeTools import writeThermo
from pythermo.thermoml.tools.readTools import readThermo

directory = os.getcwd() 
#path = "C:/Users/Matthias Gültig/Documents/pyThermoML/DataGudrunGygli/cml2ThermoML/glycerol"

#writeThermo('testThermo.json', 'testThermo2')

dataRep = readThermo(path="DataGudrunGygli/cml2ThermoML/glycerol/glycerol_DOI1.xml")

for comp in dataRep.getCompoundList():
   print(comp.toJSON())