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

# not used
def getMoleFractionsOfComp(pureOrMixtureData, compID):
    """
    method returns all values of molefractions stored in ThermoML file
    
    :param measurements: measurementID
    :param compID: compID
    :return: list of mole fractions
    """
    moleFractions = []
    measurements = pureOrMixtureData.getMeasurementsList()
    varID = pureOrMixtureData.getMoleFractionID(compID)
    
    for elem in measurements:
        # TODO: Why getVariable returns dictionary with one variable?
        
        if elem.getVariable(varID)[0].value not in moleFractions:
            moleFractions.append(elem.getVariable(varID)[0].value)
        
    return moleFractions

def getMoleFractionRatios(pureOrMixtureData):
    """
    method returns dictionary
    key: meas ID
    value: dictionary with compID as key and respective mole fraction as value"""
    moleFracAssignment = pureOrMixtureData.getMoleFractionIDs()
    measurements = pureOrMixtureData.getMeasurementsList()
    
    moleFractionRatios = dict()
    
    for meas in measurements:
        moleFractionRatios[meas.ID] = dict()
        for compID, moleFractionID in moleFracAssignment.items():
            moleFractionRatios[meas.ID][compID] = meas.getVariable(variableID=moleFractionID)[0].value

    return moleFractionRatios

def getMeasurementsWithSameMoleFractions(moleFractionRatios):
    """
    returns dictionary. key is concatenated mole fraction
    "'ratio': dictionary with compIds as key and moleFractions as values
    "'same measurements': list with same measuremnts
    """
    dataMap = dict()

    for measID, value in moleFractionRatios.items():
        dataMapKey = ""
        for moleFractions in value.values():
            
            dataMapKey = dataMapKey + str(moleFractions) + ", "
        
        dataMapKey = dataMapKey.rstrip(", ")
        for moleFractions in value.values():
            if dataMapKey not in dataMap:
                
                dataMap[dataMapKey] = dict()
                dataMap[dataMapKey]["ratio"] = value
                dataMap[dataMapKey]["same measurements"] = []
                
                    
            if measID not in dataMap[dataMapKey]["same measurements"]:
                 dataMap[dataMapKey]["same measurements"].append(measID)

    return dataMap