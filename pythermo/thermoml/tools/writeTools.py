import lxml.etree as etree
from pythermo.thermoml.core import DataReport
import json
from pydantic import BaseModel, validator
from typing import  Union
from pythermo.thermoml.core.exceptions import ThermoMLFileFormatError, ThermoMLWriterDataReportTypeError
from pydantic.json import pydantic_encoder

class ThermoMLWriter(BaseModel):
    """class that contains methods used for thermoML 

    Args:
        BaseModel ([type]): [description]

    Raises:
        TypeError: [description]
        ThermoMLFileFormatError: [description]

    Returns:
        [type]: [description]
    """
        

    dataRep: Union[DataReport, dict, str]
    filename: str
    _attr_qname: etree.QName = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    _nsmap: dict[str, str] = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    
    @validator('dataRep')
    @classmethod
    def check_dataReport(cls, v):
        if type(v) is DataReport:
            return json.loads(json.dumps(v, indent=4, default=pydantic_encoder))
        elif type(v) is str:
            with open (v) as f:
                return json.load(f)
        else:
            raise ThermoMLWriterDataReportTypeError(type=v)

    
    @validator('filename')
    @classmethod
    def check_filename(cls, v):
        if type(v) is not str:
            raise TypeError('filename must be a string')
        elif ".xml" not in v:
            raise ThermoMLFileFormatError()
        else:
            return v
    
    
    
    def writeThermo(self):
        dataRepXml = etree.Element("DataReport", {self._attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=self._nsmap)
        
        dataRepXml = self.__createVersion(dataRepXml)
        dataRepXml = self.__createCitation(dataRepXml)
        dataRepXml = self.__createCompound(dataRepXml)
        dataRepXml = self.__createPureOrMixtureData(dataRepXml)

        self.__writeFile(dataRepXml)

    def __createVersion(self, dataRepXml):
        
        Version = etree.SubElement(dataRepXml, 'Version')
        nVersionMajor = etree.SubElement(Version, 'nVersionMajor')
        nVersionMajor.text = '4'
        nVersionMinor = etree.SubElement(Version, 'nVersionMinor')
        nVersionMinor.text = '0'

        return dataRepXml

    def __createCitation(self, dataRepXml):
        Citation = etree.SubElement(dataRepXml, 'Citation')
        if 'title' in self.dataRep:
            sTitle = etree.SubElement(Citation, 'sTitle')
            sTitle.text = self.dataRep['title']
        if 'authors' in self.dataRep:
            for key in self.dataRep['authors'].keys():
                sAuthor = etree.SubElement(Citation, 'sAuthor')
                sAuthor.text = self.dataRep['authors'][key]
        if 'DOI' in self.dataRep:
            sDOI = etree.SubElement(Citation, 'sDOI')
            sDOI.text = self.dataRep['DOI']

        return dataRepXml

    def __createCompound(self, dataRepXml):
        
        if 'compounds' in self.dataRep:   
            for key, value in self.dataRep['compounds'].items():
            
                Compound = etree.SubElement(dataRepXml, 'Compound')
                RegNum = etree.SubElement(Compound, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = str(key)
            
                #subjson = dataRep['compounds']
                if 'standardInchI' in value:
                    sstandardInchI = etree.SubElement(Compound, 'sStandardInChI')
                    sstandardInchI.text = value['standardInchI']
                
                if 'standardInchIKey' in value:
                    sstandardInchIKey = etree.SubElement(Compound, 'sStandardInChIKey')
                    sstandardInchIKey.text = value['standardInchIKey']
                
                if 'commonName' in value:
                    sCommonName = etree.SubElement(Compound, 'sCommonName')
                    sCommonName.text = value['commonName']
                
                if 'smiles' in value:
                    sSmiles = etree.SubElement(Compound, 'sSmiles')
                    sSmiles.text = value['smiles']
        
        return dataRepXml

    def __createPureOrMixtureData(self, dataRepXml):
        
        if 'pureOrMixtureData' in self.dataRep:
            for key, value in self.dataRep['pureOrMixtureData'].items():
                PureOrMixtureData = etree.SubElement(dataRepXml, 'PureOrMixtureData')
                
                # ID of respective PureOrMixtureData
                nPureOrMixtureDataNumber = etree.SubElement(PureOrMixtureData, 'nPureOrMixtureDataNumber')
                nPureOrMixtureDataNumber.text = str(key)

                PureOrMixtureData = self.__createComponents(value, PureOrMixtureData)
                PureOrMixtureData = self.__createProperties(value, PureOrMixtureData)
                PureOrMixtureData = self.__createVariables(value, PureOrMixtureData)
                PureOrMixtureData = self.__createDatapoints(value, PureOrMixtureData)

        return dataRepXml

    def __createComponents(self, pureOrMixtureDict, PureOrMixtureData):
        # Declaration of components
        if 'comps' in pureOrMixtureDict:
            for comp in pureOrMixtureDict['comps']:
                Component = etree.SubElement(PureOrMixtureData, 'Component')
                RegNum = etree.SubElement(Component, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = comp
        return PureOrMixtureData

    def __createProperties(self, pureOrMixtureDict, PureOrMixtureData):
        if 'properties' in pureOrMixtureDict:
            for key, value in pureOrMixtureDict['properties'].items():
                Property = etree.SubElement(PureOrMixtureData, 'Property')
                nPropNumber = etree.SubElement(Property, 'nPropNumber')
                nPropNumber.text = key
                PropertyMethodID = etree.SubElement(Property, 'PropertyMethod-ID')
                
                if 'propName' in value:
                    PropertyGroup = etree.SubElement(PropertyMethodID, 'PropertyGroup')
                    propertyGroupName = etree.SubElement(PropertyGroup, value['propGroup'])
                    ePropName = etree.SubElement(propertyGroupName, 'ePropName')
                    ePropName.text = value['propName'] + ', ' + value['unit']
                    

                # not used in ThermoML schema definition
                if 'method' in value:
                   eMethodName = etree.SubElement(propertyGroupName, 'eMethodName')
                   eMethodName.text = value['method']

                if 'compoundID' in value:
                    RegNum = etree.SubElement(PropertyMethodID, 'RegNum')
                    nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                    nOrgNum.text = value['compoundID']
                CombinedUncertainty = etree.SubElement(Property, 'CombinedUncertainty')
                nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssessNum')
                
                #one uncertainty for each property
                nCombUncertAssessNum.text = str(1)
        return PureOrMixtureData

    def __createVariables(self, pureOrMixtureDict, PureOrMixtureData):
        if 'variables' in pureOrMixtureDict:
            for key, value in pureOrMixtureDict['variables'].items():
                Variable = etree.SubElement(PureOrMixtureData, 'Variable')
                nVarNumber = etree.SubElement (Variable, 'nVarNumber')
                nVarNumber.text = key
                VariableID = etree.SubElement(Variable, 'VariableID')
                VariableType = etree.SubElement(VariableID, 'VariableType')


                if 'varType' in value:
                    varName = etree.SubElement(VariableType, value['varType'])
                    if 'unit' in value:
                        if len(value['unit']) >= 1:
                            if 'varName' in value:
                                varName.text = value['varName'] + ', ' + value['unit']
                        # e.g component Composition
                        else:
                            if 'varName' in value:
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

    def __createDatapoints(self, pureOrMixtureDict, PureOrMixtureData):
        if 'measurements' in pureOrMixtureDict:
            for measKey, measurements in pureOrMixtureDict['measurements'].items():
                NumValues = etree.SubElement(PureOrMixtureData, 'NumValues', ID=str(measKey))

                if 'variables' in measurements:
                    for vars in measurements['variables'].values():
                        if 'elementID' in vars[0]:
                            VariableValue = etree.SubElement(NumValues, 'VariableValue')
                            nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
                            nVarNumber.text = str(vars[0]['elementID'])
                        if 'value' in vars[0]:
                            nVarValue = etree.SubElement(VariableValue, 'nVarValue')
                            nVarValue.text = str(vars[0]['value'])
                        
                        if 'numberOfDigits' in vars[0]:
                            nVarDigits = etree.SubElement(VariableValue, 'nVarDigits')
                            nVarDigits.text = str(vars[0]['numberOfDigits'])
                        
                        if  'uncertainty' in vars[0]:
                            # ExpandUncertValue is the quantity defining an interval about the result of a measurement that may
                            # be expected to encompass a large fraction of the distribution of values that
                            # could reasonably be attributed to the measurand. ExpandUncertValue
                            VarUncertainty = etree.SubElement(VariableValue, 'VarUncertainty')
                            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssesNum')
                            nUncertAssessNum.text = str(1)
                            nExpandUncertValue = etree.SubElement(VarUncertainty, 'nExpandUncertValue')
                            nExpandUncertValue.text = str(vars[0]['uncertainty'])
                        


                if 'properties' in measurements:        
                    for key, props in measurements['properties'].items():
                        if 'elementID' in props[0]:
                            PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
                            nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
                            nPropNumber.text = str(props[0]['elementID'])
                        if 'value' in props[0]:
                            nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
                            nPropValue.text = str(props[0]['value'])
                        
                        if  'numberOfDigits' in props[0]:
                            nPropDigits = etree.SubElement(PropertyValue, 'nPropDigits')
                            nPropDigits.text = str(props[0]['numberOfDigits'])
                        
                        if  'uncertainty' in props[0]:
                            # The combined standard uncertainty ucomb is included only for the quantity designated as the property. 
                            # The combined coverage factor kcomb and the combined expanded uncertainty Ucomb, which also apply only 
                            # to the designated property, are defined through the equation Ucomb = ucomb * kcomb
                            CombinedUncertainty = etree.SubElement(PropertyValue, 'CombinedUncertainty')
                            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssesNum')
                            nCombUncertAssessNum.text = str(1)
                            nCombExpandUncertValue = etree.SubElement(CombinedUncertainty, 'nCombExpandUncertValue')
                            nCombExpandUncertValue.text = str(props[0]['uncertainty'])

        return PureOrMixtureData
        
    def __writeFile(self, dataRepXml):
        convertedString = etree.tostring(dataRepXml, pretty_print=True, xml_declaration=True, encoding="utf-8")
        file = open(self.filename, 'wb')
        file.write(convertedString)
        file.close()