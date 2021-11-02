from typing import Type
import lxml.etree as etree
from pythermo.thermoml.core import DataReport, datareport
import json

def writeThermo(dataRep, filename):
    '''
    Converts a given jsonformats to ThermoML
    
    Args:
        dataRep: JSON dictionary
        String filename: Filename of ThermoML file which should be created
    
    '''
    #read json from file
    if "{" not in dataRep:
        with open (dataRep) as f:
            dataRep = json.load(f)
    
    #read json from object layer
    else:
        dataRep = json.loads(dataRep)



    
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    dataRepXml = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)
    
    dataRepXml = __createVersion(dataRepXml, dataRep)
    
    dataRepXml = __createCitation(dataRepXml, dataRep)
    dataRepXml = __createCompound(dataRepXml, dataRep)
    dataRepXml = __createPureOrMixtureData(dataRepXml, dataRep)

    __writeFile(dataRepXml, filename)

def __createVersion(dataRepXml, dataRep):
    
    Version = etree.SubElement(dataRepXml, 'Version')
    nVersionMajor = etree.SubElement(Version, 'nVersionMajor')
    nVersionMajor.text = '4'
    nVersionMinor = etree.SubElement(Version, 'nVersionMinor')
    nVersionMinor.text = '0'

    return dataRepXml

def __createCitation(dataRepXml, dataRep):
    Citation = etree.SubElement(dataRepXml, 'Citation')
    if __keyInDict(dataRep, 'authors'):
        for key in dataRep['authors'].keys():
            sAuthor = etree.SubElement(Citation, 'sAuthor')
            sAuthor.text = dataRep['authors'][key]
    if __keyInDict(dataRep, 'DOI'):
        sDOI = etree.SubElement(Citation, 'sDOI')
        sDOI.text = dataRep['DOI']
    if __keyInDict(dataRep, 'title'):
        sTitle = etree.SubElement(Citation, 'sTitle')
        sTitle.text = dataRep['title']
    return dataRepXml

def __createCompound(dataRepXml, dataRep):
    
    if __keyInDict(dataRep, 'compounds'):   
        for key, value in dataRep['compounds'].items():
        
            Compound = etree.SubElement(dataRepXml, 'Compound')
            RegNum = etree.SubElement(Compound, 'RegNum')
            nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
            nOrgNum.text = str(key)
        
            #subjson = dataRep['compounds']
            if __keyInDict(value, 'standardInchI'):
                sstandardInchI = etree.SubElement(Compound, 'sStandardInChI')
                sstandardInchI.text = value['standardInchI']
            
            if __keyInDict(value, 'standardInchIKey'):
                sstandardInchIKey = etree.SubElement(Compound, 'sStandardInChIKey')
                sstandardInchIKey.text = value['standardInchIKey']
            
            if __keyInDict(value, 'commonName'):
                sCommonName = etree.SubElement(Compound, 'sCommonName')
                sCommonName.text = value['commonName']
            
            if __keyInDict(value, 'smiles'):
                sSmiles = etree.SubElement(Compound, 'sSmiles')
                sSmiles.text = value['smiles']
    
    return dataRepXml

def __createPureOrMixtureData(dataRepXml, dataRep):
    
    if __keyInDict(dataRep, 'pureOrMixtureData'):
        for key, value in dataRep['pureOrMixtureData'].items():
            PureOrMixtureData = etree.SubElement(dataRepXml, 'PureOrMixtureData')
            
            # ID of respective PureOrMixtureData
            nPureOrMixtureDataNumber = etree.SubElement(PureOrMixtureData, 'nPureOrMixtureDataNumber')
            nPureOrMixtureDataNumber.text = str(key)

            PureOrMixtureData = __createComponents(value, PureOrMixtureData)
            PureOrMixtureData = __createProperties(value, PureOrMixtureData)
            PureOrMixtureData = __createVariables(value, PureOrMixtureData)
            PureOrMixtureData = __createDatapoints(value, PureOrMixtureData)

    return dataRepXml

def __createComponents(pureOrMixtureDict, PureOrMixtureData):
    # Declaration of components
    if __keyInDict(pureOrMixtureDict, 'comps'):
        for comp in pureOrMixtureDict['comps']:
            Component = etree.SubElement(PureOrMixtureData, 'Component')
            RegNum = etree.SubElement(Component, 'RegNum')
            nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
            nOrgNum.text = comp
    return PureOrMixtureData

def __createProperties(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, 'properties'):
        for key, value in pureOrMixtureDict['properties'].items():
            Property = etree.SubElement(PureOrMixtureData, 'Property')
            nPropNumber = etree.SubElement(Property, 'nPropNumber')
            nPropNumber.text = key
            PropertyMethodID = etree.SubElement(Property, 'PropertyMethod-ID')
            
            if __keyInDict(value, 'propName'):
                PropertyGroup = etree.SubElement(PropertyMethodID, 'PropertyGroup')
                propertyGroupName = etree.SubElement(PropertyGroup, value['propGroup'])
                ePropName = etree.SubElement(propertyGroupName, 'ePropName')
                ePropName.text = value['propName'] + ', ' + value['unit']
                

            # WARNING! NOT controlled vocabulary of ThermoML
            if __keyInDict(value, 'method'):
                eMethodName = etree.SubElement(propertyGroupName, 'eMethodName')
                eMethodName.text = value['method']

            CombinedUncertainty = etree.SubElement(Property, 'CombinedUncertainty')
            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssessNum')
            
            #one uncertainty for each property
            nCombUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createVariables(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, 'variables'):
        for key, value in pureOrMixtureDict['variables'].items():
            Variable = etree.SubElement(PureOrMixtureData, 'Variable')
            nVarNumber = etree.SubElement (Variable, 'nVarNumber')
            nVarNumber.text = key
            VariableID = etree.SubElement(Variable, 'VariableID')
            VariableType = etree.SubElement(VariableID, 'VariableType')


            if __keyInDict(value, 'varType'):
                varName = etree.SubElement(VariableType, value['varType'])
                if __keyInDict(value, 'unit'):
                    if len(value['unit']) >= 1:
                        if __keyInDict(value, 'varName'):
                            varName.text = value['varName'] + ', ' + value['unit']
                    # e.g component Composition
                    else:
                        if __keyInDict(value, 'varName'):
                            varName.text = value['varName']
            
            if 'compoundID' in value:
                RegNum = etree.SubElement(VariableID, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = value['compoundID']
            
            VarUncertainty = etree.SubElement(Variable, 'VarUncertainty')
            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssessNum')
            # one uncertainty for each variable
            nUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createDatapoints(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, 'measurements'):
        for measKey, measurements in pureOrMixtureDict['measurements'].items():
            NumValues = etree.SubElement(PureOrMixtureData, 'NumValues', ID=str(measKey))

            if __keyInDict(measurements, 'variables'):
                for key, vars in measurements['variables'].items():
                    if __keyInDict(vars[0], 'elementID'):
                        VariableValue = etree.SubElement(NumValues, 'VariableValue')
                        nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
                        nVarNumber.text = str(vars[0]['elementID'])
                    if __keyInDict(vars[0], 'value'):
                        nVarValue = etree.SubElement(VariableValue, 'nVarValue')
                        nVarValue.text = str(vars[0]['value'])
                    
                    if __keyInDict(vars[0], 'numberOfDigits'):
                        nVarDigits = etree.SubElement(VariableValue, 'nVarDigits')
                        nVarDigits.text = str(vars[0]['numberOfDigits'])
                    
                    if __keyInDict(vars[0], 'uncertainty'):
                        # ExpandUncertValue is the quantity defining an interval about the result of a measurement that may
                        # be expected to encompass a large fraction of the distribution of values that
                        # could reasonably be attributed to the measurand. ExpandUncertValue
                        VarUncertainty = etree.SubElement(VariableValue, 'VarUncertainty')
                        nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssesNum')
                        nUncertAssessNum.text = str(1)
                        nExpandUncertValue = etree.SubElement(VarUncertainty, 'nExpandUncertValue')
                        nExpandUncertValue.text = str(vars[0]['uncertainty'])
                    


            if __keyInDict(measurements, 'properties'):        
                for key, props in measurements['properties'].items():
                    if __keyInDict(props[0], 'elementID'):
                        PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
                        nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
                        nPropNumber.text = str(props[0]['elementID'])
                    if __keyInDict(props[0], 'value'):
                        nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
                        nPropValue.text = str(props[0]['value'])
                    
                    if __keyInDict(props[0], 'numberOfDigits'):
                        nPropDigits = etree.SubElement(PropertyValue, 'nPropDigits')
                        nPropDigits.text = str(props[0]['numberOfDigits'])
                    
                    if __keyInDict(props[0], 'uncertainty'):
                        # The combined standard uncertainty ucomb is included only for the quantity designated as the property. 
                        # The combined coverage factor kcomb and the combined expanded uncertainty Ucomb, which also apply only 
                        # to the designated property, are defined through the equation Ucomb = ucomb * kcomb
                        CombinedUncertainty = etree.SubElement(PropertyValue, 'CombinedUncertainty')
                        nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssesNum')
                        nCombUncertAssessNum.text = str(1)
                        nCombExpandUncertValue = etree.SubElement(CombinedUncertainty, 'nCombExpandUncertValue')
                        nCombExpandUncertValue.text = str(props[0]['uncertainty'])

    return PureOrMixtureData

def __keyInDict(dictionary, keyOfDict) -> bool:
    if keyOfDict in dictionary:
        return True
    else:
        return False
    
def __writeFile(dataRepXml, filename):
    convertedString = etree.tostring(dataRepXml, pretty_print=True, xml_declaration=True, encoding="utf-8")
    file = open(filename, 'wb')
    file.write(convertedString)
    file.close()