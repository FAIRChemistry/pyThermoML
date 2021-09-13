import lxml.etree as etree
from pythermo.thermoml.core import DataReport
import json

#fillename of JSON
#targetfilename of thermoML which should be createde
def writeThermoFromJSON(filename, targetfilename):
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    dataRepXml = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)
    
    with open(filename, 'r') as file:
        dataRep = file.read()
    
    dataRep = json.loads(dataRep)
    
    print(dataRep)
    dataRepXml = __createVersion(dataRepXml, dataRep)
    dataRepXml = __createCitation(dataRepXml, dataRep)
    dataRepXml = __createCompoundFromJSON(dataRepXml, dataRep)
    dataRepXml = __createPureOrMixtureDataFromJSON(dataRepXml, dataRep)

    __writeFile(dataRepXml, targetfilename)

def writeThermo(dataRep, filename):
    '''
    Converts a given object layer to ThermoML
    
    Args:
        DataReport dataRep: Object layer element
        String filename: Filename of ThermoML file which should be created
    
    '''
    dataRep = dataRep.toJSON()

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
    #print(dataRep)
    Citation = etree.SubElement(dataRepXml, 'Citation')
    if __keyInDict(dataRep, '_authors'):
        print(dataRep['_title'])
        for i in range(len(dataRep['_authors'])):
            sAuthor = etree.SubElement(Citation, 'sAuthor')
            sAuthor.text = dataRep['_authors']['_author' + str(i)]
    if __keyInDict(dataRep, '_DOI'):
        sDOI = etree.SubElement(Citation, 'sDOI')
        sDOI.text = dataRep['_DOI']
    if __keyInDict(dataRep, '_title'):
        sTitle = etree.SubElement(Citation, 'sTitle')
        sTitle.text = dataRep['_title']
    return dataRepXml

def __createCompound(dataRepXml, dataRep):
    if __keyInDict(dataRep, 'compounds'):
        for elem in dataRep['compounds']:
            
            Compound = etree.SubElement(dataRepXml, 'Compound')
            RegNum = etree.SubElement(Compound, 'RegNum')
            nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
            nOrgNum.text = str(elem)
        
            subdict = dataRep['compounds'][str(elem)]
            subjson = json.loads(str(subdict))
            if __keyInDict(subjson, '_standardInchI'):
                sstandardInchI = etree.SubElement(Compound, 'sstandardInchI')
                sstandardInchI.text = subjson['_standardInchI']
            
            if __keyInDict(subjson, '_standardInchIKey'):
                sstandardInchIKey = etree.SubElement(Compound, 'sstandardInchIKey')
                sstandardInchIKey.text = subjson['_standardInchIKey']
            
            if __keyInDict(subjson, '_commonName'):
                sCommonName = etree.SubElement(Compound, 'sCommonName')
                sCommonName.text = subjson['_commonName']
            
            if __keyInDict(subjson, '_smiles'):
                sSmiles = etree.SubElement(Compound, 'sSmiles')
                sSmiles.text = subjson['_smiles']

        return dataRepXml

def __createCompoundFromJSON(dataRepXml, dataRep):
    
    if __keyInDict(dataRep, 'compounds'):   
        for key, value in dataRep['compounds'].items():
        
            Compound = etree.SubElement(dataRepXml, 'Compound')
            RegNum = etree.SubElement(Compound, 'RegNum')
            nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
            nOrgNum.text = str(key)
        
            #subjson = dataRep['compounds']
            if __keyInDict(value, '_standardInchI'):
                sstandardInchI = etree.SubElement(Compound, 'sstandardInchI')
                sstandardInchI.text = value['_standardInchI']
            
            if __keyInDict(value, '_standardInchIKey'):
                sstandardInchIKey = etree.SubElement(Compound, 'sstandardInchIKey')
                sstandardInchIKey.text = value['_standardInchIKey']
            
            if __keyInDict(value, '_commonName'):
                sCommonName = etree.SubElement(Compound, 'sCommonName')
                sCommonName.text = value['_commonName']
            
            if __keyInDict(value, '_smiles'):
                sSmiles = etree.SubElement(Compound, 'sSmiles')
                sSmiles.text = value['_smiles']
    
    return dataRepXml

def __createPureOrMixtureData(dataRepXml, dataRep):
    if __keyInDict(dataRep, 'pureOrMixtureData'):
        for elem in dataRep['pureOrMixtureData']:
            PureOrMixtureData = etree.SubElement(dataRepXml, 'PureOrMixtureData')
            # ID of respective PureOrMixtureData
            nPureOrMixtureDataNumber = etree.SubElement(PureOrMixtureData, 'nPureOrMixtureDataNumber')
            nPureOrMixtureDataNumber.text = str(elem)

            pureOrMixtureDict = json.loads(str(dataRep['pureOrMixtureData'][str(elem)]))

            PureOrMixtureData = __createComponents(pureOrMixtureDict, PureOrMixtureData)
            PureOrMixtureData = __createProperties(pureOrMixtureDict, PureOrMixtureData)
            PureOrMixtureData = __createVariables(pureOrMixtureDict, PureOrMixtureData)
            PureOrMixtureData = __createDatapoints(pureOrMixtureDict, PureOrMixtureData)

    return dataRepXml

def __createPureOrMixtureDataFromJSON(dataRepXml, dataRep):
    
    if __keyInDict(dataRep, 'pureOrMixtureData'):
        for key, value in dataRep['pureOrMixtureData'].items():
            PureOrMixtureData = etree.SubElement(dataRepXml, 'PureOrMixtureData')
            
            # ID of respective PureOrMixtureData
            nPureOrMixtureDataNumber = etree.SubElement(PureOrMixtureData, 'nPureOrMixtureDataNumber')
            nPureOrMixtureDataNumber.text = str(key)

            PureOrMixtureData = __createComponents(value, PureOrMixtureData)
            PureOrMixtureData = __createPropertiesFromJSON(value, PureOrMixtureData)
            PureOrMixtureData = __createVariablesFromJSON(value, PureOrMixtureData)
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
    if __keyInDict(pureOrMixtureDict, '_properties'):
        for prop in pureOrMixtureDict['_properties']:
            Property = etree.SubElement(PureOrMixtureData, 'Property')
            nPropNumber = etree.SubElement(Property, 'nPropNumber')
            nPropNumber.text = prop
            PropertyMethodID = etree.SubElement(Property, 'PropertyMethod-ID')
            
            jsonData = pureOrMixtureDict["_properties"][str(prop)]
            
            # why need this?!!!!
            jsonData = json.dumps(jsonData)
            propertyDict = json.loads(str(jsonData))
            


            # Get property Group Name of json
            if __keyInDict(propertyDict, '_propName'):
                PropertyGroup = etree.SubElement(PropertyMethodID, 'PropertyGroup')
                propertyGroupName = etree.SubElement(PropertyGroup, propertyDict['_propGroup'])
                ePropName = etree.SubElement(propertyGroupName, 'ePropName')
                ePropName.text = propertyDict['_propName'] + ', ' + propertyDict['_unit']
                

            # WARNING! NOT controlled vocabulary of ThermoML
            if __keyInDict(propertyDict, '_method'):
                eMethodName = etree.SubElement(propertyGroupName, 'eMethodName')
                eMethodName.text = propertyDict['_method']

            CombinedUncertainty = etree.SubElement(Property, 'CombinedUncertainty')
            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssessNum')
            
            #one uncertainty for each property
            nCombUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createPropertiesFromJSON(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, '_properties'):
        for key, value in pureOrMixtureDict['_properties'].items():
            Property = etree.SubElement(PureOrMixtureData, 'Property')
            nPropNumber = etree.SubElement(Property, 'nPropNumber')
            nPropNumber.text = key
            PropertyMethodID = etree.SubElement(Property, 'PropertyMethod-ID')
            
            if __keyInDict(value, '_propName'):
                PropertyGroup = etree.SubElement(PropertyMethodID, 'PropertyGroup')
                propertyGroupName = etree.SubElement(PropertyGroup, value['_propGroup'])
                ePropName = etree.SubElement(propertyGroupName, 'ePropName')
                ePropName.text = value['_propName'] + ', ' + value['_unit']
                

            # WARNING! NOT controlled vocabulary of ThermoML
            if __keyInDict(value, '_method'):
                eMethodName = etree.SubElement(propertyGroupName, 'eMethodName')
                eMethodName.text = value['_method']

            CombinedUncertainty = etree.SubElement(Property, 'CombinedUncertainty')
            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssessNum')
            
            #one uncertainty for each property
            nCombUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createVariables(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, '_variables'):
        for vars in pureOrMixtureDict['_variables']:
            Variable = etree.SubElement(PureOrMixtureData, 'Variable')
            nVarNumber = etree.SubElement (Variable, 'nVarNumber')
            nVarNumber.text = vars
            VariableID = etree.SubElement(Variable, 'VariableID')
            VariableType = etree.SubElement(VariableID, 'VariableType')

            x = pureOrMixtureDict["_variables"][str(vars)]
            # why need this?!!!!
            x = json.dumps(x)
            varDict = json.loads(str(x))
            if __keyInDict(varDict, '_varType'):
                varName = etree.SubElement(VariableType, varDict['_varType'])
                if __keyInDict(varDict, '_unit'):
                    if len(varDict['_unit']) >= 1:
                        if __keyInDict(varDict, '_varName'):
                            varName.text = varDict['_varName'] + ', ' + varDict['_unit']
                    # e.g component Composition
                    else:
                        if __keyInDict(varDict, '_varName'):
                            varName.text = varDict['_varName']
            
            if '_compoundID' in varDict:
                RegNum = etree.SubElement(VariableID, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = varDict['_compoundID']
            
            VarUncertainty = etree.SubElement(Variable, 'VarUncertainty')
            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssessNum')
            # one uncertainty for each variable
            nUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createVariablesFromJSON(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, '_variables'):
        for key, value in pureOrMixtureDict['_variables'].items():
            Variable = etree.SubElement(PureOrMixtureData, 'Variable')
            nVarNumber = etree.SubElement (Variable, 'nVarNumber')
            nVarNumber.text = key
            VariableID = etree.SubElement(Variable, 'VariableID')
            VariableType = etree.SubElement(VariableID, 'VariableType')


            if __keyInDict(value, '_varType'):
                varName = etree.SubElement(VariableType, value['_varType'])
                if __keyInDict(value, '_unit'):
                    if len(value['_unit']) >= 1:
                        if __keyInDict(value, '_varName'):
                            varName.text = value['_varName'] + ', ' + value['_unit']
                    # e.g component Composition
                    else:
                        if __keyInDict(value, '_varName'):
                            varName.text = value['_varName']
            
            if '_compoundID' in value:
                RegNum = etree.SubElement(VariableID, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = value['_compoundID']
            
            VarUncertainty = etree.SubElement(Variable, 'VarUncertainty')
            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssessNum')
            # one uncertainty for each variable
            nUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createDatapoints(pureOrMixtureDict, PureOrMixtureData):
    if __keyInDict(pureOrMixtureDict, '_measurements'):
        for measKey, measurements in pureOrMixtureDict['_measurements'].items():
            NumValues = etree.SubElement(PureOrMixtureData, 'NumValues', ID=str(measKey))

            if __keyInDict(measurements, '_variables'):
                for key, vars in measurements['_variables'].items():
                    if __keyInDict(vars[0], '_elementID'):
                        VariableValue = etree.SubElement(NumValues, 'VariableValue')
                        nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
                        nVarNumber.text = str(vars[0]['_elementID'])
                    if __keyInDict(vars[0], '_value'):
                        nVarValue = etree.SubElement(VariableValue, 'nVarValue')
                        nVarValue.text = str(vars[0]['_value'])
                    
                    if __keyInDict(vars[0], '_numberOfDigits'):
                        nVarDigits = etree.SubElement(VariableValue, 'nVarDigits')
                        nVarDigits.text = str(vars[0]['_numberOfDigits'])
                    
                    if __keyInDict(vars[0], '_uncertainty'):
                        # ExpandUncertValue is the quantity defining an interval about the result of a measurement that may
                        # be expected to encompass a large fraction of the distribution of values that
                        # could reasonably be attributed to the measurand. ExpandUncertValue
                        VarUncertainty = etree.SubElement(VariableValue, 'VarUncertainty')
                        nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssesNum')
                        nUncertAssessNum.text = str(1)
                        nExpandUncertValue = etree.SubElement(VarUncertainty, 'nExpandUncertValue')
                        nExpandUncertValue.text = str(vars[0]['_uncertainty'])
                    


            if __keyInDict(measurements, '_properties'):        
                for key, props in measurements['_properties'].items():
                    if __keyInDict(props[0], '_elementID'):
                        PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
                        nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
                        nPropNumber.text = str(props[0]['_elementID'])
                    if __keyInDict(props[0], '_value'):
                        nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
                        nPropValue.text = str(props[0]['_value'])
                    
                    if __keyInDict(props[0], '_numberOfDigits'):
                        nPropDigits = etree.SubElement(PropertyValue, 'nPropDigits')
                        nPropDigits.text = str(props[0]['_numberOfDigits'])
                    
                    if __keyInDict(props[0], '_uncertainty'):
                        # The combined standard uncertainty ucomb is included only for the quantity designated as the property. 
                        # The combined coverage factor kcomb and the combined expanded uncertainty Ucomb, which also apply only 
                        # to the designated property, are defined through the equation Ucomb = ucomb * kcomb
                        CombinedUncertainty = etree.SubElement(PropertyValue, 'CombinedUncertainty')
                        nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssesNum')
                        nCombUncertAssessNum.text = str(1)
                        nCombExpandUncertValue = etree.SubElement(CombinedUncertainty, 'nCombExpandUncertValue')
                        nCombExpandUncertValue.text = str(props[0]['_uncertainty'])

    return PureOrMixtureData

def __keyInDict(dictionary, keyOfDict) -> bool:
    if keyOfDict in dictionary:
        return True
    else:
        return False
    
def __writeFile(dataRepXml, filename):
    convertedString = etree.tostring(dataRepXml, pretty_print=True, xml_declaration=True, encoding="utf-8")
    file = open(filename + '.xml', 'wb')
    file.write(convertedString)
    file.close()