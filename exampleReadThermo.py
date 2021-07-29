from core.pureOrMixtureData import PureOrMixtureData
from tools.readTools import readThermo
from tools.writeTools import writeThermo

dataRep = readThermo("testThermo.xml")


dataRep._DOI = "DOI244"


dataRep.addPureOrMixtureData()


writeThermo(dataRep, "testThermo")


#dataRep.
'''values2 = dict()

values2[viscID] = 1.0

values2[tempID] = 277
values2[frac1ID] = 0.5
values2[frac2ID] = 0.4
meas2 = Measurement(
    "meas2",
    values2,
    pureOrMixtureData=experiment
)
experiment.addMeasurements(meas2)'''