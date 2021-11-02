from pythermo.thermoml.tools.analyseTools import extractPropertyValues, extractVariableValues, getMeasurementsWithSameMoleFractions, getMoleFractionRatios
from pythermo.thermoml.tools.visualizationTools import plotArrhenius
from pythermo.thermoml.tools.readTools import readThermo
import os
import numpy as np
import pprint
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.cm as cm

path = ""
R = 8.31446261815324/1000

def transformViscosity(eta):
    return np.log(eta*1000)


def tranformTemperature(temperature):
    return 1 / (R*temperature)

def getArrheniusData(pathLastName) -> tuple[dict, dict]:
    """returns dictionary with viscosities and temperatures"""
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
    
        #pprint.pprint(superTempDict)
    return superViscDict, superTempDict

def plotArrheniusSameDOIsOverMoleFractions(superViscDict, superTempDict):
    
    # counter for name of stored plots
    counter = 0
    eta0 = dict()
    
    # for each DOI
    for (viscMoleFraction, viscDictionary), (tempMoleFraction, tempDictionary) in zip(superViscDict.items(), superTempDict.items()):
        
        # for each different mole fraction
        for moleFraction in tempDictionary:
            #print(moleFraction)
            x = np.array(tempDictionary[moleFraction])
            x = x.reshape(-1, 1)
            y = np.array(viscDictionary[moleFraction])

            model = LinearRegression()
            model.fit(x, y)
            
            # Information about R^2
            #print("R2: ", round(model.score(x, y), 2))

            t = (min(x), max(x))

            plt.scatter(x, y, alpha=0.5)
        
            plt.plot(t, model.predict(t), label=moleFraction)

        
        plt.grid()
        plt.title(str(viscMoleFraction))
        plt.xlabel("1/RT in [mol/KJ]")
        plt.ylabel("ln(eta) in [cP]")
        plt.legend(bbox_to_anchor=(0.5, -0.1), title="Mole Fractions", mode="expand", ncol=2)
        plt.savefig("./plots/DOI"+ str(counter) + ".jpg", bbox_inches="tight")
        
        counter += 1


def getEEta(superViscDict, superTempDict):
    # need Dictionary with top level molefraction -> DOI -> values, current Dicts have DOI -> molefraction -> values
    superViscDict = _transpose(superViscDict)
    superTempDict = _transpose(superTempDict)

    dois = []
    for doiDict in superViscDict.values():
        for doi in doiDict.keys():
            if doi not in dois:
                dois.append(doi)

    
    #keys: mole fractions, values: dict with key: doi, array of eta0
    eEtaDict = dict()
    for (viscMoleFraction, viscDictionary), (tempMoleFraction, tempDictionary) in zip(superViscDict.items(), superTempDict.items()):
        xw = viscMoleFraction.split(",")[0]
        xw = float(xw)
        eEtaDict[xw] = dict()
        for doi in tempDictionary:
            x = np.array(tempDictionary[doi])
            x = x.reshape(-1, 1)
            y = np.array(viscDictionary[doi])

            model = LinearRegression()
            model.fit(x, y)
            eEta = model.coef_[0]
            eEtaDict[xw][doi] = eEta
    
    
    return eEtaDict

def getEta0(superViscDict, superTempDict):
    
    # need Dictionary with top level molefraction -> DOI -> values, current Dicts have DOI -> molefraction -> values
    superViscDict = _transpose(superViscDict)
    superTempDict = _transpose(superTempDict)

    dois = []
    #pprint.pprint(superViscDict)
    for doiDict in superViscDict.values():
        for doi in doiDict.keys():
            if doi not in dois:
                dois.append(doi)

    
    #keys: mole fractions, values: dict with key: doi, array of eta0
    eta0dict = dict()
    
    for (viscMoleFraction, viscDictionary), (tempMoleFraction, tempDictionary) in zip(superViscDict.items(), superTempDict.items()):
        xw = viscMoleFraction.split(",")[0]
        xw = float(xw)
        eta0dict[xw] = dict()
        for doi in tempDictionary:
            x = np.array(tempDictionary[doi])
            x = x.reshape(-1, 1)
            y = np.array(viscDictionary[doi])

            model = LinearRegression()
            model.fit(x, y)
            eta0 = model.intercept_

            eta0dict[xw][doi] = eta0

    return eta0dict


def plotEEta(eEtaDict, folderName):
    dois = []
    for doiDictionary in eEtaDict.values():
        for doi in doiDictionary:
            if doi not in dois:
                dois.append(doi)
                
    pprint.pprint(eEtaDict)
    

    
    for DOI in dois:
        xs1 = []
        ys1 = []
        for xw, doiDict in eEtaDict.items():
            for doi, eEta in doiDict.items():
                if doi == DOI:
                    xs1.append(xw)
                    ys1.append(eEta)
                
        plt.plot(xs1, ys1, "o", label=DOI, alpha = 0.5)
        plt.legend()
        
    plt.xlabel("chi w")
    plt.ylabel("Eeta in KJ/mol")
    plt.title(folderName)
    plt.savefig("./plots/Xw_EEta.jpg", bbox_inches="tight")

    
def plotEta0(eta0dict, folderName):
    dois = []
    for doiDictionary in eta0dict.values():
        for doi in doiDictionary:
            if doi not in dois:
                dois.append(doi)
                

        
    for DOI in dois:
        xs1 = []
        ys1 = []
        for xw, doiDict in eta0dict.items():
            for doi, eta0 in doiDict.items():
                if doi == DOI:
                    xs1.append(xw)
                    ys1.append(eta0)
    
        plt.plot(xs1, ys1, "o", label=DOI, alpha = 0.5)
        plt.legend()
        
    plt.xlabel("chi w")
    plt.ylabel("ln(eta0)")
    plt.title(folderName)
    plt.savefig("./plots/Xw_Eta0.jpg", bbox_inches="tight")
    
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
    """folderName = "water"
    superViscDict, superTempDict = getArrheniusData(folderName)
    #plotArrheniusMoleFractionConstant(superViscDict=superViscDict, superTempDict=superTempDict)
    eta0dict = getEta0(superViscDict=superViscDict, superTempDict=superTempDict)
    plotEta0(eta0dict=eta0dict, folderName=folderName)
    
    eEtadict = getEEta(superViscDict=superViscDict, superTempDict=superTempDict)
    plotEEta(eEtadict, folderName=folderName)"""
    