from pythermo.thermoml.tools.readTools import readThermo

from io import StringIO
import os

path = os.getcwd()
file = open(path + "\DataGudrunGygli\cml2ThermoML\water_DOI1.xml")
dataRep = readThermo(file)

print(dataRep)