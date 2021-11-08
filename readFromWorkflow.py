from pythermo.thermoml.core import PureOrMixtureData, DataReport, Compound, DataPoint

from pythermo.thermoml.vars.componentcomposition import MoleFraction
from pythermo.thermoml.vars.temperature import Temperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.props.transportproperties import Viscosity
from pythermo.thermoml.props.volumetricproperties import MassDensity
from pythermo.thermoml.props.transportproperties import Diffusioncoefficient
# TODO: import writer not intuitiv
from pythermo.thermoml.tools.writeTools import writeThermo
import json

def readJson(loc):
    return json.load(open(loc))

def createDataReport(jsonData, dataPointKey=None) -> DataReport:
    """
    creates dataReport object based on json output of workflow from Benjamin Schmitz
    
    Args:
        jsonData: This is json input of workflow
        dataPointKey: the key, where actual data is stored in jsonData
    
    Returns:
        DataReport object which can be converted with writeThermo-function to .xml (ThermoML)

    Raises:
        KeyError: if keys are not found in compound
    """
    if dataPointKey is None:
        dataPointKey = __getDatapointsKey__(jsonData)
    
    authors = {
        "author1": "Benjamin Schmitz"
    }

    dataReport = DataReport(authors=authors)
    compDict = dict()
    
    for index, molec in enumerate(jsonData['molecules']):
        try:
            comp = Compound(ID=str(index), standardInchIKey=molec['InChI key'], smiles=molec['SMILES code'], commonName=molec['Name'])
            compDict[molec['Name']] = dataReport.addCompound(comp)
        except KeyError:
            print("key in 'molecules' not found")
    
    experiment = PureOrMixtureData("data 1", *compDict.values())

    variables = dict()
    properties = dict()
    
    # variable definitions
    for index, point in enumerate(jsonData['units']):
        for name in point.keys():
            if name == "temperature":
                variables[name] = experiment.addVariable(Temperature(str(index)))
            elif name == "pressure":
                variables[name] = experiment.addVariable(Pressure(str(index)))


    maxIndex = __getMaximumIndex__(variables)

    for compID in compDict.values():
        maxIndex = int(maxIndex)+1
        variables[f'mole fraction comp{compID}'] = experiment.addVariable(MoleFraction(str(maxIndex), compID))


            
    # property defnitions
    index = 0
    for point in jsonData['units']:
        for name, unit in point.items():
            if name == "density":
                dens = MassDensity(str(index), "simulation")
                properties[name] = experiment.addProperty(dens)
                index += 1
            elif name == "self_diffusion_coefficient":
                sdiff = Diffusioncoefficient(str(index), "simulation")
                properties[name] = experiment.addProperty(sdiff)
                index += 1
            elif name == "viscosity":
                visc = Viscosity(str(index), "simulation")
                properties[name] = experiment.addProperty(visc)
                index += 1
    
    # Datapoint definition
    for measindex, point in enumerate(jsonData[dataPointKey]):
        measurementID = f'meas{measindex}'
        dataPoints = list()
        for name, varindex in variables.items():
            if name in point.keys():
                # conversion from bar to kPa
                if name == "pressure":
                    x = point[name]*100
                else:
                    x = point[name]
                dataPoints.append(DataPoint(measurementID=measurementID, value=x, varID=str(varindex)))

            # not ideal bot enough for  2 component mixutres of benni
            # TODO: Number of digits
            if name == 'mole fraction comp0':
                dataPoints.append(DataPoint(measurementID=measurementID, value=point["chi_water"], varID=str(varindex)))
            if name == 'mole fraction comp1':
                dataPoints.append(DataPoint(measurementID=measurementID, value=1 - float(point["chi_water"]), varID=str(varindex)))    
        
        for propName, propindex in properties.items():
            if f'average_{propName}' in point.keys():
                if f'average_{propName}' == 'average_density':
                    x = point[f'average_{propName}']*1000
                else:
                    x = point[f'average_{propName}']
                dataPoints.append(DataPoint(measurementID=measurementID, value=point[f'average_{propName}'], propID=str(propindex), uncertainty=point[f'stdev_{propName}']))
        
        experiment.addMeasurement(dataPoints)            

    dataReport.addPureOrMixtureData(experiment)
    
    return dataReport

def __getMaximumIndex__(dictionary) -> int:
    """
    just indexing stuf. Used for index variables properly
    """
    for index in dictionary.values():
        maxIndex = -1
        if int(index) > maxIndex:
            maxIndex = index

    return maxIndex

def __getDatapointsKey__(jsonData) -> str:
    """
    Returns:
        key where actual data might be stored
    """
    for key in jsonData.keys():
        if "average" in key:
            return key

if __name__ == "__main__":
    LOCATION = "outputWorkflow/Example JSON/viscosities.json"
    jsonData = readJson(LOCATION)
    DATA_POINT_KEY = "viscosities"

    dataReport = createDataReport(jsonData, DATA_POINT_KEY)
    writeThermo(dataReport.toJSON(), 'testThermoWFJSON.xml')
