from pythermo.thermoml.core import PureOrMixtureData, Measurement, DataReport, Compound, DataPoint

from pythermo.thermoml.vars.componentcomposition import MoleFraction
from pythermo.thermoml.vars.temperature import Temperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.props.transportproperties import Viscosity
from pythermo.thermoml.props.volumetricproperties import MassDensity
from pythermo.thermoml.props.transportproperties import Diffusioncoefficient
# TODO: import writer not intuitiv
from pythermo.thermoml.tools.writeTools import writeThermo
from pythermo.thermoml.tools.readTools import readThermo
import json
from lxml import etree

def readJson(loc):
    return json.load(open(loc))

def createDataReport(jsonData):
    authors = {
        "author1": "Benjamin Schmitz"
    }

    dataReport = DataReport(authors=authors)
    compDict = dict()
    
    for index, molec in enumerate(jsonData['molecules']):
        print(molec)
        try:
            comp = Compound(ID=str(index), standardInchIKey=molec['InChI key'], smiles=molec['SMILES code'], commonName=molec['Name'])
            compDict[molec['Name']] = dataReport.addCompound(comp)
        except KeyError:
            print("key in 'molecules' not found")
    
    experiment = PureOrMixtureData("data 1", *compDict.values())

    variables = dict()
    properties = dict()
    
    # variable definitions
    # TODO: unit conversions
    for index, point in enumerate(jsonData['units']):    
        for name, unit in point.items():
            if name == "temperature":
                variables[name] = experiment.addVariable(Temperature(str(index)))
            elif name == "pressure":
                variables[name] = experiment.addVariable(Pressure(str(index)))


    maxIndex = __getMaximumIndex__(variables)

    for compID in compDict.values():
        maxIndex = int(maxIndex)+1
        variables[maxIndex] = experiment.addVariable(MoleFraction(maxIndex, compID))


            
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
    
    print(properties)
    for measindex, (propName, propindex) in enumerate(properties.items()):
        if f'averaged_{propName}' in jsonData.keys():
            measurementID = f'meas{measindex}'
            
            for point in jsonData[f'averaged_{propName}']:
                dataPoints = list()
                for name, varindex in variables.items():
                    if len(str(name)) > 1:
                        dataPoints.append(DataPoint(measurementID=measurementID, value=point[name], varID=str(varindex), numberOfDigits=len(str(point[name]))-1))
                    # Really bad... -> optimize output JSON
                    if name == 2:
                        
                        dataPoints.append(DataPoint(measurementID=measurementID, value=point["chi_water"], varID=str(varindex), numberOfDigits=len(str(point['chi_water']))-1))
                    if name == 3: 
                        dataPoints.append(DataPoint(measurementID=measurementID, value=1 - float(point["chi_water"]), varID=str(varindex), numberOfDigits=len(str(point["chi_water"]))-1))
                
                print(str(point[f'stdev_{propName}']))
                dataPoints.append(DataPoint(measurementID=measurementID, value=point[f'average_{propName}'], propID=str(propindex), uncertainty=str(point[f'stdev_{propName}']), numberOfDigits=len(str(point[f'average_{propName}']))))

                for dp in dataPoints:
                    print(dp)
    
                experiment.addMeasurement(dataPoints)
    
    dataReport.addPureOrMixtureData(experiment)
    print(dataReport)

def __getMaximumIndex__(dictionary):
        
    for index in dictionary.values():
        maxIndex = -1
        if int(index) > maxIndex:
            maxIndex = index

    return maxIndex

if __name__ == "__main__":
    loc = "outputWorkflow/Example JSON/densities.json"
    jsonData = readJson(loc)

    createDataReport(jsonData)


"""


datapoints = [viscDataPoint, tempDataPoint, frac1DataPoint, frac2DataPoint]
datapoints2 = [viscDataPoint2, tempDataPoint2,
               frac1DataPoint2, frac2DataPoint2]
# add Measurement to experiment
experiment.addMeasurement(dataPoints=datapoints)
experiment.addMeasurement(dataPoints=datapoints2)
# add experiment to dataReport
dataReport.addPureOrMixtureData(experiment)

writeThermo(dataReport.toJSON(), 'testThermo.xml')

#file = etree.parse("testThermo.xml")
#print(etree.tostring(file, pretty_print=True, encoding=str))

#data = readThermo("testThermo.xml")
#print(data)
"""