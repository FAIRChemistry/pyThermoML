from pythermo.thermoml.tools.analyseTools import getData
from pythermo.thermoml.tools.visualizationTools import plotArrhenius
import os
import numpy as np




path = "DataGudrunGygli/cml2ThermoML/ChCL_glycerol"
R = 8.31446261815324/1000

def transformViscosity(eta):
    return np.log(eta*1000)


def tranformTemperature(temperature):
    return 1 / (R*temperature)

def visualizeWater():
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

        viscData, tempData, doi = getData(
            path=filename,
            pureOrMixtureDataID="1",
            propertyID="1",
            variableID="1"
        )

        # Add to dicitonaries
        viscDict[doi] = list(map(
            transformViscosity,
            viscData
        ))
        tempDict[doi] = list(map(
            tranformTemperature,
            tempData
        ))

    # Visualize data
    plotArrhenius(tempDict, viscDict, "Arrhenius water")
    
if __name__ == "__main__":
    visualizeWater()
