from pythermo.thermoml.core import DataReport, Compound
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.tools.writeTools import writeThermo
from pythermo.thermoml.tools.readTools import readThermo


"""dataRep1 = readThermo(path="DataGudrunGygli\cml2ThermoML\glycerol\glycerol_DOI1.xml")

pom = dataRep1.getPureOrMixtureData("1")


print(pom.getPOMPropertyList())
print(pom.getPOMVariableList())

measurements = pom.getMeasurementsList()
for meas in measurements:
   prop = meas.getProperty(list(pom.getPOMPropertyList())[0])
   var1 = meas.getVariable(list(pom.getPOMVariableList)[0])
   var2 = meas.getVariable(list(pom.getPOMVariableList)[1])
   var3 = meas.getVariable(list(pom.getPOMVariableList)[2])
"""
writeThermo("testThermo2.json", "testastas.xml")