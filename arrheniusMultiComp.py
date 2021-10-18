from pythermo.thermoml.tools.analyseTools import extractPropertyValues, extractVariableValues, getMeasurementsWithSameMoleFractions, getMoleFractionRatios
from pythermo.thermoml.tools.visualizationTools import plotArrhenius
from pythermo.thermoml.tools.readTools import readThermo
import os
import numpy as np
import pprint
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


path = ""
R = 8.31446261815324/1000

def transformViscosity(eta):
    return np.log(eta*1000)


def tranformTemperature(temperature):
    return 1 / (R*temperature)

def getArrheniusData(pathLastName):
    # temps, viscs = doArrhenius(path)

    dirpath = os.path.join(
        "./DataGudrunGygli/cml2ThermoML/" + pathLastName
    )
    
    # Change working directory and get files
    os.chdir(dirpath)
    fileList = os.listdir(os.getcwd())

    # Initialize data dictionary
    # superDicts have as key dois, values dictionary with key MoleRatios and values arrays of viscositys
    superViscDict, superTempDict, viscDict, tempDict = {}, {}, {}, {}
    
    
    for filename in fileList:

        if ".xml" in filename:
            # Load ThermoML
            dataReport = readThermo(filename)
            doi = dataReport.DOI

            # Get pureOrMixtureData from the dataReport
            pureOrMixtureData = dataReport.getPureOrMixtureData("1")
            
            # Find measurements with same moleFractions
            moleFracRatios = getMoleFractionRatios(pureOrMixtureData=pureOrMixtureData)
            dataDict = getMeasurementsWithSameMoleFractions(moleFractionRatios=moleFracRatios)
            
            # basic dict with key: MoleFraction, value: Array viscositys of one paper
            viscDict = dict()
            tempDict = dict()

            for dataMapKey in dataDict:
                
                # array of measurement objects with same mole fractions and same DOI (two for loops)
                measurements = pureOrMixtureData.getSameMoleFracMeasurementsListByID(IDs=dataDict[dataMapKey]["same measurements"])
                #TODO: abstract propertyID/variableID getter  1 = viscosity, 1 = temperature
                viscList = extractPropertyValues(measurements, propertyID="1")
                tempList = extractVariableValues(measurements, variableID="1")
                # recalculate temperature and viscosity
                tempList = list(map(tranformTemperature, tempList))
                viscList = list(map(transformViscosity, viscList))
                #add Lists to basic dictionary
                viscDict[dataMapKey] = viscList
                tempDict[dataMapKey] = tempList
                
            
            superViscDict[doi] = viscDict
            superTempDict[doi] = tempDict
        
        
        
        # need Dictionary with top level molefraction -> DOI -> values, current Dicts have DOI -> molefraction -> values
        #superViscDict = _transpose(superViscDict)
        #superTempDict = _transpose(superTempDict)
        
        numberOfMoleFractions = len(superTempDict)

        #pprint.pprint(superTempDict)
    return superViscDict, superTempDict

def plotArrheniusSameDOIsOverMoleFractions(superViscDict, superTempDict):
    
    # counter to store plots
    counter = 0

    for (viscMoleFraction, viscDictionary), (tempMoleFraction, tempDictionary) in zip(superViscDict.items(), superTempDict.items()):
    

        for key in tempDictionary:
            x = np.array(tempDictionary[key])
            x = x.reshape(-1, 1)
            y = np.array(viscDictionary[key])

            model = LinearRegression()
            model.fit(x, y)
            
            # Information about R^2
            #print("R2: ", round(model.score(x, y), 2))

            t = (min(x), max(x))

            plt.scatter(x, y, alpha=0.5)
        
            plt.plot(t, model.predict(t), label=key)

        
        plt.grid()
        plt.title(str(viscMoleFraction))
        plt.xlabel("1/RT in [mol/KJ]")
        plt.ylabel("ln(eta) in [cP]")
        plt.legend(bbox_to_anchor=(0.5, -0.1), title="Mole Fractions", mode="expand", ncol=2)

        #print(os.path)
        plt.savefig("./plots/plot" + str(counter) + ".jpg", bbox_inches="tight")
        
        counter += 1


def _transpose(dictionary):
    '''
    method changes key, value order of dictionaries key1 -> key2 -> value to key2 -> key1 -> value
    '''
    transposedDict = dict()
    for doi, value in dictionary.items():
        for moleFracRatio, viscValues in value.items():
            if moleFracRatio not in transposedDict:
                transposedDict[moleFracRatio] = dict()
                if doi not in transposedDict[moleFracRatio]:
                    transposedDict[moleFracRatio][doi] = viscValues
                else:
                    transposedDict[moleFracRatio][doi].append(viscValues)
            else:
                if doi in transposedDict[moleFracRatio]:
                    transposedDict[moleFracRatio][doi].append(viscValues)
                else:
                    transposedDict[moleFracRatio][doi] = viscValues
    
    return transposedDict

if __name__ == "__main__":
    superViscDict, superTempDict = getArrheniusData("glycerol")
    plotArrheniusSameDOIsOverMoleFractions(superTempDict=superTempDict, superViscDict=superViscDict)
    