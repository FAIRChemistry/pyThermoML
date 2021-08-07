import lxml.etree as etree

import json

# dataRep json
# DataReport ThermoML
def writeThermo(dataRep, filename):
    '''
    Converts a given object layer to ThermoML
    
    Args:
        JSON dataRep: Object layer element
        String filename: Filename of ThermoML file which should be created
    
    '''
    dataRep = dataRep.toJSON()

    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    DataReport = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)
    
    DataReport = __createVersion(DataReport, dataRep)
    DataReport = __createCitation(DataReport, dataRep)
    DataReport = __createCompound(DataReport, dataRep)
    DataReport = __createPureOrMixtureData(DataReport, dataRep)

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
    for i in range(len(dataRep['_authors'])):
        sAuthor = etree.SubElement(Citation, 'sAuthor')
        sAuthor.text = dataRep['_authors']['_author' + str(i)]
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
    
        PureOrMixtureData = __createComponents(pureOrMixtureDict, PureOrMixtureData)
        PureOrMixtureData = __createProperties(pureOrMixtureDict, PureOrMixtureData)
        PureOrMixtureData = __createVariables(pureOrMixtureDict, PureOrMixtureData)
        PureOrMixtureData = __createDatapoints(pureOrMixtureDict, PureOrMixtureData)

    return DataReport
    
def __createComponents(pureOrMixtureDict, PureOrMixtureData):
    # Declaration of components
    for comp in pureOrMixtureDict['comps']:
        Component = etree.SubElement(PureOrMixtureData, 'Component')
        RegNum = etree.SubElement(Component, 'RegNum')
        nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
        nOrgNum.text = comp
    return PureOrMixtureData

def __createProperties(pureOrMixtureDict, PureOrMixtureData):
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

        CombinedUncertainty = etree.SubElement(Property, 'CombinedUncertainty')
        nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssessNum')
        
        #one uncertainty for each property
        nCombUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createVariables(pureOrMixtureDict, PureOrMixtureData):
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
        
        VarUncertainty = etree.SubElement(Variable, 'VarUncertainty')
        nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssessNum')
        # one uncertainty for each variable
        nUncertAssessNum.text = str(1)
    return PureOrMixtureData

def __createDatapoints(pureOrMixtureDict, PureOrMixtureData):

    for measKey, measurements in pureOrMixtureDict['_measurements'].items():
        NumValues = etree.SubElement(PureOrMixtureData, 'NumValues')
        
        for key, vars in measurements['_variables'].items():
            VariableValue = etree.SubElement(NumValues, 'VariableValue')
            nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
            nVarNumber.text = str(vars[0]['_elementID'])
            nVarValue = etree.SubElement(VariableValue, 'nVarValue')
            nVarValue.text = str(vars[0]['_value'])

            # ExpandUncertValue is the quantity defining an interval about the result of a measurement that may
            # be expected to encompass a large fraction of the distribution of values that
            # could reasonably be attributed to the measurand. ExpandUncertValue
            VarUncertainty = etree.SubElement(VariableValue, 'VarUncertainty')
            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssesNum')
            nUncertAssessNum.text = str(1)
            nExpandUncertValue = etree.SubElement(VarUncertainty, 'nExpandUncertValue')
            nExpandUncertValue.text = str(vars[0]['_uncertainty'])
            
        for key, props in measurements['_properties'].items():
            PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
            nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
            nPropNumber.text = str(props[0]['_elementID'])
            nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
            nPropValue.text = str(props[0]['_value'])

            # The combined standard uncertainty ucomb is included only for the quantity designated as the property. 
            # The combined coverage factor kcomb and the combined expanded uncertainty Ucomb, which also apply only 
            # to the designated property, are defined through the equation Ucomb = ucomb * kcomb
            CombinedUncertainty = etree.SubElement(PropertyValue, 'CombinedUncertainty')
            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssesNum')
            nCombUncertAssessNum.text = str(1)
            nCombExpandUncertValue = etree.SubElement(CombinedUncertainty, 'nCombExpandUncertValue')
            nCombExpandUncertValue.text = str(props[0]['_uncertainty'])

    return PureOrMixtureData

def __writeFile(DataReport, filename):
    convertedString = etree.tostring(DataReport, pretty_print=True, xml_declaration=True, encoding="utf-8")
    file = open(filename + '.xml', 'wb')
    file.write(convertedString)
    file.close()
