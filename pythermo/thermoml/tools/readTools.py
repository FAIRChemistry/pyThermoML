from pythermo.thermoml.props.bioproperties import PeakTemperature
from pythermo.thermoml.props.volumetricproperties import MassDensity
from pythermo.thermoml.props.refractionSurfaceTensionSoundSpeedproperties import SurfaceTension, SpeedOfSound
from pythermo.thermoml.props.heatcapacityproperties import MolarHCconstPressure, MolarHCconstVolume
from pythermo.thermoml.props.transportproperties import Selfdiffusioncoefficient, KinematicViscosity, Microviscosity, Viscosity

from pythermo.thermoml.vars.temperature import LowerTemperature, Temperature, UpperTemperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.vars.componentcomposition import MoleFraction

from pythermo.thermoml.core import Compound, DataPoint, DataReport, PureOrMixtureData

from lxml import etree

namespace = './/{http://www.iupac.org/namespaces/ThermoML}'

propMapping = {
    'Viscosity, Pa*s': Viscosity,
    'Kinematic Viscosity, m2/s': KinematicViscosity,
    'Self diffusion coefficient, m2/s': Selfdiffusioncoefficient,
    'Mass density, kg/m3': MassDensity,
    'Surface tension liquid-gas, N/m': SurfaceTension,
    'Speed of sound, m/s': SpeedOfSound,
    'Molar heat capacity at constant pressure, J/K/mol': MolarHCconstPressure,
    'Molar heat capacity at constant volume, J/K/mol': MolarHCconstVolume,
    'Peak temperature, K': PeakTemperature,

    # not in ThermoML
    'Microviscosity, Pa*s': Microviscosity
}

varMapping = {
    'Temperature, K': Temperature,
    'Lower temperature, K': LowerTemperature,
    'Upper temperature, K': UpperTemperature,
    'Mole fraction': MoleFraction,
    'Pressure, kPa': Pressure
}

def readThermo(path) -> DataReport:
    '''
    Reads ThermoML document to an object layer ThermoML

    Args:
        String path: Path to ThermoML file
    '''
    
    tree = etree.parse(path)
    root = tree.getroot()

    
    datareport = DataReport(*__getCitation__(root))
    comps = __getCompounds__(root)
    
    for comp in comps.values():
        datareport.addCompound(comp)
    
    pOMData = __getPOMData__(root, comps)
    
    # experiment[0] Object
    # experiment[1] ElementTree
    
    for key, experiment in pOMData.items():
        props = __getProperties__(experiment[1])
        vars = __getVariables__(experiment[1])
        for id, value in props.items():
            experiment[0].addProperty(value[0](id, value[1], value[2]))
        
        for id, value in vars.items():
            experiment[0].addVariable(value[0](id, value[1]))
        
        datareport.addPureOrMixtureData(__getMeasurements__(experiment[0], experiment[1]))

    return datareport



def __get__(root, tag, namespace=namespace):
    '''
    just refactored method to get text of one  Element
    '''
    try:
        textelem = root.findall(namespace + tag)[0].text
    except IndexError:
        textelem = ""
    return textelem

    

def __getCitation__(root, namespace=namespace):
    if len(root.findall(namespace + "sTitle")) > 0:
        title = root.findall(namespace + "sTitle")[0].text
    else:
        title = ""
    if len(root.findall(namespace + "sTitle")) > 0:
        doi = root.findall(namespace + 'sDOI')[0].text
    else:
        doi = ""

    authorList = root.findall(namespace + 'sAuthor')
    authors = dict()

    for index, author in enumerate(authorList):
        authors[str(index)] = author.text

    return title, doi, authors

def __getCompounds__(root) -> dict:
    '''
    adds components in ThermoML to object layer
    returns dictionary with compounds
    '''
    comps = dict()
    for compound in root.findall(namespace + 'Compound'):
        comps[__get__(compound, 'nOrgNum')] = Compound(__get__(compound, 'nOrgNum'), 
        __get__(compound, 'sStandardInChI'), __get__(compound, 'sStandardInChIKey'), 
        __get__(compound, 'sSmiles'), __get__(compound, 'sCommonName'))
    return comps

def __getPOMData__(root, comps) -> dict:
    '''
    Return dictionary of pureOrMixtureData in dataReport
    
    Key: nPureOrMixtureDataNumber
    Value: [PureOrMixtureData, pureOrMixtureData]
    First argument is Object of PureOrMixtureData, second argument returns ET Element. 
    -> only get following properties/variables of pureOrMixtureData, not whole root
    '''
    pOMData = dict()
    
    for pureOrMixtureData in root.findall(namespace + 'PureOrMixtureData'):
        # All declared compounds should be used in pure or mixture Data
        pOMData[__get__(pureOrMixtureData, 'nPureOrMixtureDataNumber')] = (
            PureOrMixtureData(__get__(pureOrMixtureData, 'nPureOrMixtureDataNumber'), *comps.keys()),
            pureOrMixtureData)
    
    return pOMData

def __getProperties__(pureOrMixtureData) -> dict:
    '''
    Return dictionary of properties used in pureOrMixtureData
    
    Key: nPropNumber
    Value: [Func, eMethodName]
    '''
    properties = dict()
    for property in pureOrMixtureData.findall(namespace + 'Property'):
        try:
            compID = __get__(property, 'nOrgNum')
        except IndexError:
            compID = ""
        properties[__get__(property, 'nPropNumber')] = (__getPropMapping__(__get__(property, 'ePropName')),
         __get__(property, 'eMethodName'), compID)
    return properties


def __getPropMapping__(ePropName):
    '''
    Returns function that matches to ePropName
    '''
    try:
        func = propMapping[ePropName]
    except KeyError:
        print('Property not found')
    return func

def __getVariables__(pureOrMixtureData) -> dict:
    '''
    Returns dict of variables used in pureOrMixtureData
    
    Key: nVarNumber
    Value: [Func, compID]
    compID is gonna be ignored if variable is not component specific
    '''

    variables = dict()
    for variable in pureOrMixtureData.findall(namespace + 'Variable'):
        variableType = variable.findall(namespace + 'VariableType')
        varName = variableType[0].getchildren()[0].text
        try:
            compID = __get__(variable, 'nOrgNum')
        except IndexError:
            compID = ""
        
        variables[__get__(variable, 'nVarNumber')] = (__getVarMapping__(varName), compID)
    return variables

def __getVarMapping__(varName):
    '''
    Return function that matches to variable
    '''
    try:
        func = varMapping[varName]
    except KeyError:
        print('Variable not found')
    return func

def __getMeasurements__(experiment, pureOrMixtureData):

    measID = 0
    for numValues in pureOrMixtureData.findall(namespace + 'NumValues'):        
        if 'ID' in numValues.attrib:
            measID = numValues.attrib['ID']
        else:
            # default measurmentIDs
            measID = int(measID)
            measID+= 1
            measID = str(measID)

        datapoints = []
        for variableValue in numValues.findall(namespace + 'VariableValue'):
            try:
                uncert = float(__get__(variableValue, 'nExpandUncertValue'))
            except ValueError:
                uncert = "NG"
            
            try:
                numbOfDig = int(__get__(variableValue, 'nVarDigits'))
            except ValueError:
                numbOfDig = ""
            #varDict[__get__(variableValue, 'nVarNumber')]
            #
            datapoints.append(DataPoint(measID, float(__get__(variableValue, 'nVarValue')), varID = __get__(variableValue, 'nVarNumber'), uncertainty=uncert, numberOfDigits=numbOfDig))

        for propertyValue in numValues.findall(namespace + 'PropertyValue'):
            try:
                uncert = float(__get__(propertyValue, 'nCombExpandUncertValue'))
            except ValueError:
                uncert = "NG"
            
            try:
                numbOfDig = int(__get__(propertyValue, 'nPropDigits'))
            except ValueError:
                numbOfDig = ""
            # datapoint[__get__(propertyValue, 'nPropNumber')]    
            datapoints.append(DataPoint(measID, float(__get__(propertyValue, 'nPropValue')), propID =__get__(propertyValue, 'nPropNumber'), uncertainty= uncert, numberOfDigits=numbOfDig))

        
        
        #for elem in datapoints:
        #    print(elem)
        #print(datapoints)
        experiment.addMeasurement(dataPoints=datapoints)

    return experiment