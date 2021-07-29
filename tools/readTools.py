from props.propertyBase import PropertyBase
from props.bioproperties import peakTemperature
from props.volumetricproperties import massDensity
from props.refractionSurfaceTensionSoundSpeedproperties import surfaceTension, speedOfSound
from props.heatcapacityproperties import molarHCconstPressure, molarHCconstVolume
from props.transportproperties import TransportProperty, diffusioncoefficient, kinematicViscosity, microviscosity, viscosity

from vars.temperature import lowerTemperature, temperature, upperTemperature
from vars.pressure import pressure
from vars.componentcomposition import moleFraction

from core.pureOrMixtureData import PureOrMixtureData
from core.datareport import DataReport
from core.compound import Compound
from core.measurement import Measurement

from lxml import etree
import xmltodict
import json

namespace = {'ThermoML': 'http://www.iupac.org/namespaces/ThermoML'}
namespaceString = '{http://www.iupac.org/namespaces/ThermoML}'


def get(parent, tag) -> str:
    '''
    Returns value of tag in ThermoML. Only first element of THermoML!
    controlled vocabulary!!

    Args:
        parent
        String tag: Name of element
    '''
    return parent.find('{http://www.iupac.org/namespaces/ThermoML}' + tag).text


def getChild(parent, childName):
    '''
    Returns subelement of parent
    '''
    return parent.find('.//{http://www.iupac.org/namespaces/ThermoML}' + childName)

# specific functions... not smart!


def __getAuthors__(Citation) -> list:
    '''
    Returns all authors of ThermoML in array representation
    '''
    authors = []
    for author in Citation.iter('{http://www.iupac.org/namespaces/ThermoML}sAuthor'):
        authors.append(author.text)
    return authors


def __addComponents__(dataReport, root) -> list:
    '''
    adds components in ThermoML to object layer
    returns compID array
    '''
    compIDs = []
    for compound in root.iter('{http://www.iupac.org/namespaces/ThermoML}Compound'):
        #compound = getChild(root, 'Compound')
        regNum = getChild(compound, 'RegNum')
        comp = Compound(get(regNum, 'nOrgNum'), get(compound, 'sStandardInChi'), get(
            compound, 'sStandardInChiKey'), get(compound, 'sCommonName'), get(compound, 'sSmiles'))
        compID = dataReport.addCompound(comp)
        compIDs.append(compID)
    return compIDs


def __addProperties__(pureOrMixtureData, exp) -> list:
    '''
    adds propeties used in thermoML - file to objectlayer
    returns array of property IDs
    '''
    propIDs = []
    for prop in list(pureOrMixtureData):
        elem = prop.findall(
            ".//{http://www.iupac.org/namespaces/ThermoML}ePropName")
        for ePropName in elem:
            propIDs.append(exp.addProperty(
                __propertyTypeChecker__(ePropName.text, prop)))
    return propIDs


def __propertyTypeChecker__(ePropName, prop) -> PropertyBase:
    '''
    str ePropName
    Element prop
    '''
    if 'Viscosity, Pa*s' == ePropName:
        return viscosity(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'TransportProp'), 'eMethodName'))

    if 'Kinematic Viscosity, m2/s' == ePropName:
        return kinematicViscosity(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'TransportProp'), 'eMethodName'))

    if 'Microviscosity, Pa*s' == ePropName:
        return microviscosity(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'TransportProp'), 'eMethodName'))

    if 'Self diffusion coefficient, m2/s' == ePropName:
        return diffusioncoefficient(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'TransportProp'), 'eMethodName'))

    if 'Mass density, kg/m3' == ePropName:
        return massDensity(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'VolumetricProp'), 'eMethodName'))

    if 'Surface tension liquid-gas, N/m' == ePropName:
        return surfaceTension(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'RefractionSurfaceTensionSoundSpeed'), 'eMethodName'))

    if 'Speed of sound, m/s' == ePropName:
        return speedOfSound(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'RefractionSurfaceTensionSoundSpeed'), 'eMethodName'))

    if 'Molar heat capacity at constant pressure, J/K/mol' == ePropName:
        return molarHCconstPressure(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'HeatCapacityAndDerivedProp'), 'eMethodName'))

    if 'Molar heat capacity at constant volume, J/K/mol' == ePropName:
        return molarHCconstVolume(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'HeatCapacityAndDerivedProp'), 'eMethodName'))

    if 'Peak temperature, K' == ePropName:
        return peakTemperature(get(prop, 'nPropNumber'), get(getChild(getChild(getChild(prop, 'PropertyMethod-ID'), 'PropertyGroup'), 'BioProperties'), 'eMethodName'))


def __addVariables__(pureOrMixtureData, exp) -> list:
    '''
    adds variables used in thermoML - file to objectlayer
    returns array of variable IDs
    '''
    varIDs = []
    for var in list(pureOrMixtureData):
        varType = var.findall(
            ".//{http://www.iupac.org/namespaces/ThermoML}VariableType")
        for varEnum in list(varType):
            for varName in list(varEnum):
                varIDs.append(exp.addVariable(
                    __variableTypeChecker__(varName.text, var)))

    return varIDs


def __variableTypeChecker__(varName, var):
    if varName == 'Temperature, K':
        return temperature(get(var, 'nVarNumber'))

    if varName == 'Upper temperature, K':
        return upperTemperature(get(var, 'nVarNumber'))

    if varName == 'Lower temperature, K':
        return lowerTemperature(get(var, 'nVarNumber'))

    if varName == 'Mole fraction':
        return moleFraction(get(var, 'nVarNumber'), get(getChild(getChild(var, 'VariableID'), 'RegNum'), 'nOrgNum'))

    if varName == 'Pressure, kPa':
        return pressure(get(var, 'nVarNumber'))


def __addMeasurements__(pureOrMixtureData, exp, propIDs, varIDs):
    # TODO: meas name?
    # in this case just number (measnumb)
    measnumb = 1
    for point in pureOrMixtureData.findall(".//{http://www.iupac.org/namespaces/ThermoML}NumValues"):

        values = dict()
        varIndex = 0
        propIndex = 0

        for var in point.findall(".//{http://www.iupac.org/namespaces/ThermoML}VariableValue"):
            values[varIDs[varIndex]] = get(var, 'nVarValue')
            varIndex += 1

        for prop in point.findall(".//{http://www.iupac.org/namespaces/ThermoML}PropertyValue"):
            values[propIDs[propIndex]] = get(prop, 'nPropValue')
            propIndex += 1

        exp.addMeasurements(Measurement(
            str(measnumb), values, pureOrMixtureData=exp))
        measnumb += 1


def __addPureOrMixtureData__(dataReport, root, compIDs):
    for pureOrMixtureData in root.iter('{http://www.iupac.org/namespaces/ThermoML}PureOrMixtureData'):
        # TODO: POMD name
        # Warning!!! all compounds declared in comp are used in PureOrMixtureData
        exp = PureOrMixtureData(
            get(pureOrMixtureData, 'nPureOrMixtureDataNumber'), "", *compIDs)

        propIDs = __addProperties__(pureOrMixtureData, exp)
        varIDs = __addVariables__(pureOrMixtureData, exp)
        __addMeasurements__(pureOrMixtureData, exp, propIDs, varIDs)
        dataReport.addPureOrMixtureData(exp)


def readThermo(path) -> DataReport:
    '''
    Reads ThermoML document to an object layer ThermoML

    Args:
        String path: Path to ThermoML file
    '''

    tree = etree.parse(path)
    root = tree.getroot()

    dataReport = DataReport(get(getChild(root, 'Citation'), 'sTitle'), get(
        getChild(root, 'Citation'), 'sDOI'), *__getAuthors__(getChild(root, 'Citation')))
    compIDs = __addComponents__(dataReport, root)

    __addPureOrMixtureData__(dataReport, root, compIDs)

    return dataReport
