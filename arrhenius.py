from pythermo.thermoml.tools.readTools import readThermo
import json
import os
import numpy as np

from sklearn.linear_model import LinearRegression
import math as mth
import matplotlib.pyplot as plt


path = "DataGudrunGygli/cml2ThermoML/water"
R = 8.31446261815324/1000


def getData(path, pureOrMixtureDataID, propertyID, variableID):

    # Load ThermoML
    dataReport = readThermo(path)
    doi = dataReport.DOI

    # Get pureOrMixtureData from the dataReport
    pureOrMixtureData = dataReport.getPureOrMixtureData(
        pureOrMixtureDataID
    )

    measurements = pureOrMixtureData.getMeasurementsList()
    propList = extractPropertyValues(measurements, propertyID)
    variableList = extractVariableValues(measurements, variableID)

    return propList, variableList, doi


def extractPropertyValues(measurements, propertyID):
    return _extractElementValues(
        measurements,
        propertyID,
        "property"
    )


def extractVariableValues(measurements, variableID):
    return _extractElementValues(
        measurements,
        variableID,
        "variable"
    )


def _extractElementValues(measurements, ID, type_):
    elementList = list()
    for measurement in measurements:
        if type_ == "property":
            dataPoints = measurement.getProperty(ID)
        elif type_ == "variable":
            dataPoints = measurement.getVariable(ID)

        elementList += list(map(
            lambda dataPoint: dataPoint.value,
            dataPoints
        ))

    return elementList


def visualizeDatapoints(tempdict, viscdict):

    for key in tempdict.keys():

        x = np.array(tempdict[key])
        x = x.reshape(-1, 1)
        y = np.array(viscdict[key])

        model = LinearRegression()
        model.fit(x, y)

        # print("infinit temperature:", model.intercept_)
        # print("slope: ", model.coef_)
        print("R2: ", round(model.score(x, y), 2))

        t = (min(x), max(x))
        # plt.text(0.4, -0.8, "R2 of " + str(key) + ": " + str(round(model.score(x,y), 2)) + "\n \n", horizontalalignment='center', verticalalignment='center')

        plt.scatter(x, y, alpha=0.5)
        plt.plot(t, model.predict(t), label=key)

    plt.grid()
    plt.title("arrhenius pure water")
    plt.xlabel("1/RT")
    plt.ylabel("ln(eta)")
    plt.legend()
    plt.show()


def transformViscosity(eta):
    return np.log(eta*1000)


def tranformTemperature(temperature):
    return 1 / (R*temperature)


if __name__ == "__main__":
    # temps, viscs = doArrhenius(path)

    dirpath = os.path.join(
        "./DataGudrunGygli/cml2ThermoML/water/"
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
    visualizeDatapoints(tempDict, viscDict)
