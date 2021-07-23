from core.pureOrMixtureData import PureOrMixtureData
import lxml.etree as etree
import xml.etree.ElementTree as ET

import json

# dataRep json
# DataReport ThermoML
def toThermoML(dataRep, filename):
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    DataReport = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)
    
    DataReport = __createVersion(DataReport, dataRep)
    DataReport = __createCitation(DataReport, dataRep)
    DataReport = __createCompound(DataReport, dataRep)
    DataReport = __createPureOrMixtureData(DataReport, dataRep)
    ET.dump(DataReport)
    __writeFile(DataReport, filename)

def __createVersion(DataReport, dataRep):
    
    Version = etree.SubElement(DataReport, 'Version')
    nVersionMajor = etree.SubElement(Version, 'nVersionMajor')
    nVersionMajor.text = '4'
    nVersionMinor = etree.SubElement(Version, 'nVersionMinor')
    nVersionMinor.text = '0'

    return DataReport

def __createCitation(DataReport, dataRep):
    Citation = etree.SubElement(DataReport, 'Citation')
    for i in range(len(dataRep['authors'])):
        sAuthor = etree.SubElement(Citation, 'sAuthor')
        sAuthor.text = dataRep['authors'][i]
    sDOI = etree.SubElement(Citation, 'sDOI')
    sDOI.text = dataRep['_DOI']
    sTitle = etree.SubElement(Citation, 'sTitle')
    sTitle.text = dataRep['_title']
    return DataReport

def __createCompound(DataReport, dataRep):
    for elem in dataRep['compounds']:
        Compound = etree.SubElement(DataReport, 'Compound')
        RegNum = etree.SubElement(Compound, 'RegNum')
        nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
        nOrgNum.text = str(elem)
        sStandardInChI = etree.SubElement(Compound, 'sStandardInChi')
        
        subdict = dataRep['compounds'][str(elem)]
        subjson = json.loads(str(subdict))
        sStandardInChI.text = subjson['_standardInchi']
        sStandardInChIKey = etree.SubElement(Compound, 'sStandardInChiKey')
        sStandardInChIKey.text = subjson['_standardInchiKey']
        sCommonName = etree.SubElement(Compound, 'sCommonName')
        sCommonName.text = subjson['_commonName']
        sSmiles = etree.SubElement(Compound, 'sSmiles')
        sSmiles.text = subjson['_smiles']

    return DataReport

def __createPureOrMixtureData(DataReport, dataRep):
    for elem in dataRep['pureOrMixtureData']:
        PureOrMixtureData = etree.SubElement(DataReport, 'PureOrMixtureData')
        # ID of respective PureOrMixtureData
        nPureOrMixtureDataNumber = etree.SubElement(PureOrMixtureData, 'nPureOrMixtureDataNumber')
        nPureOrMixtureDataNumber.text = str(elem)

        pureOrMixtureDict = json.loads(str(dataRep['pureOrMixtureData'][str(elem)]))
    
        # Declaration of components
        for comp in pureOrMixtureDict['comps']:
            Component = etree.SubElement(PureOrMixtureData, 'Component')
            RegNum = etree.SubElement(Component, 'RegNum')
            nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
            nOrgNum.text = comp
        
        # Information about compiler -> necessary
        #sCompiler = etree.SubElement(PureOrMixtureData, 'sCompiler')
        #sCompiler.text = 'ThermoWriter by Matthias Gueltig'

        print(pureOrMixtureDict)
        # Property
        for prop in pureOrMixtureDict['_properties']:
            Property = etree.SubElement(PureOrMixtureData, 'Property')
            nPropNumber = etree.SubElement(Property, 'nPropNumber')
            nPropNumber.text = prop
            PropertyMethodID = etree.SubElement(Property, 'PropertyMethod-ID')
            
            jsonData = pureOrMixtureDict["_properties"][str(prop)]
            
            # why need this?!!!!
            jsonData = json.dumps(jsonData)
            propertyDict = json.loads(str(jsonData))
            PropertyGroup = etree.SubElement(PropertyMethodID, 'PropertyGroup')

            # Get property Group Name of json
            propertyGroupName = etree.SubElement(PropertyGroup, propertyDict['_propGroup'])
            ePropName = etree.SubElement(propertyGroupName, 'ePropName')
            ePropName.text = propertyDict['_propName'] + ', ' + propertyDict['_unit']
            eMethodName = etree.SubElement(propertyGroupName, 'eMethodName')

            # WARNING! NOT controlled vocabulary of ThermoML
            eMethodName.text = propertyDict['_method']
        
        # Variables
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

            varName = etree.SubElement(VariableType, varDict['_varType'])

            if len(varDict['_unit']) >= 1:
                varName.text = varDict['_varName'] + ', ' + varDict['_unit']
            # e.g component Composition
            else: 
                varName.text = varDict['_varName']
            
            if '_compoundID' in varDict:
                RegNum = etree.SubElement(VariableID, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = varDict['_compoundID']
        
        # Datapoints
        for points in pureOrMixtureDict['_measurements']:
            NumValues = etree.SubElement(PureOrMixtureData, 'NumValues')
            pointsDict = json.loads(str(json.dumps(pureOrMixtureDict['_measurements'][str(points)])))
            varValuesDict = json.loads(str(json.dumps(pointsDict['variables'])))
            propValuesDict = json.loads(str(json.dumps(pointsDict['properties'])))

            for vars in pointsDict['variables']:                
                VariableValue = etree.SubElement(NumValues, 'VariableValue')
                nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
                nVarNumber.text = str(vars)
                nVarValue = etree.SubElement(VariableValue, 'nVarValue')
                nVarValue.text = str(varValuesDict[str(vars)])


            for props in pointsDict['properties']:
                PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
                nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
                nPropNumber.text = str(props)
                nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
                nPropValue.text = str(propValuesDict[str(props)])
    
    return DataReport

def __writeFile(DataReport, filename):
    convertedString = etree.tostring(DataReport, pretty_print=True, xml_declaration=True, encoding="utf-8")
    file = open(filename + '.xml', 'wb')
    file.write(convertedString)
    file.close()
