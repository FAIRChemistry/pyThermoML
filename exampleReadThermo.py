from core.pureOrMixtureData import PureOrMixtureData
from tools.readTools import readThermo
from tools.writeTools import writeThermo

dataRep = readThermo("testThermo.xml")


dataRep._DOI = "DOI244"


writeThermo(dataRep, "testThermo")

