from pythermo.thermoml.tools.readTools import readThermo

path = "DataGudrunGygli/cml2ThermoML/ChCl_glycerol/ChCl_glycerol_DOI3.xml"

def getData(path, pureOrMixtureDataID, propertyID, variableID):
    '''
    returns propList, variableList, DOI
    '''
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

if __name__ == "__main__":
    dataReport = readThermo(path)

    pureOrMixtureData = dataReport.getPureOrMixtureData("1")
    moleFractionID = pureOrMixtureData.getMoleFractionID("2")