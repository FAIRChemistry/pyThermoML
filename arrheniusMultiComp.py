from pythermo.thermoml.tools.analyseTools import getMoleFractionRatios
from pythermo.thermoml.tools.visualizationTools import plotArrhenius
from pythermo.thermoml.tools.readTools import readThermo
import os
import numpy as np




path = ""
R = 8.31446261815324/1000

def transformViscosity(eta):
    return np.log(eta*1000)


def tranformTemperature(temperature):
    return 1 / (R*temperature)

def getArrheniusData():
    # temps, viscs = doArrhenius(path)

    dirpath = os.path.join(
        "./DataGudrunGygli/cml2ThermoML/ChCL_glycerol/"
    )

    # Change working directory and get files
    os.chdir(dirpath)
    fileList = os.listdir(os.getcwd())

    # Initialize data dictionary
    viscDict, tempDict = {}, {}

    for filename in fileList:
        
        # Load ThermoML
        dataReport = readThermo(path)
        doi = dataReport.DOI


        # Get pureOrMixtureData from the dataReport
        pureOrMixtureData = dataReport.getPureOrMixtureData("1")
        
        # Find measurements with same moleFractions
        sameMoleFracDict = getMoleFractionRatios(pureOrMixtureData=pureOrMixtureData)
        
        for dataMapKey in sameMoleFracDict:
            # erhaöte aus sameMoleFracDict Ids mit gleichen mole Fractions
            measurements = pureOrMixtureData.getSameMoleFracMeasurementsListByID(IDs=sameMoleFracDict):
        
        propList = extractPropertyValues(measurements, propertyID)
    
if __name__ == "__main__":
    getArrheniusData()
