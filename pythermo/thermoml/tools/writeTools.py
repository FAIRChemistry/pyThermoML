'''
File: writeTools.py
Project: tools
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

import lxml.etree as etree
from pythermo.thermoml.core import DataReport
import json
from pydantic import BaseModel, validator
from typing import  Union
from pythermo.thermoml.core.exceptions import ThermoMLFileFormatError, ThermoMLWriterDataReportTypeError
from pydantic.json import pydantic_encoder
from pathlib import Path
from pythermo.thermoml.tools.readTools import ThermoMLReader

class ThermoMLWriter(BaseModel):
    """Class providing functionalities for writing ThermoML file.

        Args:
            dataRep (dict): dictionary representation of data report.
            filename (str): name of the ThermoML file that should be written.
            _attr_qname (etree.Qname): .xml schema attributes
            _nsmap (dict[str, str]): mapping of ThermoML schema definition
    """
        

    dataRep: Union[DataReport, dict, str]
    filename: str
    _attr_qname: etree.QName = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    _nsmap: dict[str, str] = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    
    @validator('dataRep', always=True)
    @classmethod
    def check_dataReport(cls, dataRep:Union[DataReport, dict, str]) -> dict:
        """converts entered dataReport into iterable dictionary

        Args:
            dataRep (Union[DataReport, dict, str]): entered dataReport. Can be either filename to .json data report or DataReport object

        Raises:
            ThermoMLWriterDataReportTypeError: entered dataReport is no DataReport/.json

        Returns:
            dict: iterable dataReport dict
        """
        if type(dataRep) is DataReport:
            return dataRep.dict(exclude_none=True)
        elif type(dataRep) is str:
            reader = ThermoMLReader(path=dataRep)
            dataRep = reader.readFromJSON()
            return dataRep.dict(exclude_none=True)
        else:
            raise ThermoMLWriterDataReportTypeError(type=dataRep)

    
    @validator('filename', always=True)
    @classmethod
    def check_filename(cls, filename:str):
        """Checks whether filename has been entered correctly.

        Args:
            filename (str): filename of new ThermoML (.xml) file

        Raises:
            TypeError: filename no string
            ThermoMLFileFormatError: filename does not end with ".xml"

        Returns:
            str: entered filename
        """
        if type(filename) is not str:
            raise TypeError('filename must be a string')
        elif ".xml" not in filename:
            raise ThermoMLFileFormatError()
        else:
            return filename
    
    
    
    def writeThermo(self):
        """writes ThermoML file to entered filename, by basically checking wheter key is in data report dictionary and by writing entry possibly to respective ThermoML tag.
        """
        dataRepXml = etree.Element("DataReport", {self._attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=self._nsmap)
        
        dataRepXml = self.__createVersion(dataRepXml)
        dataRepXml = self.__createCitation(dataRepXml)
        dataRepXml = self.__createCompound(dataRepXml)
        dataRepXml = self.__createPureOrMixtureData(dataRepXml)

        self.__writeFile(dataRepXml)

    def __writeFile(self, dataRepXml:etree._Element):
        convertedString = etree.tostring(dataRepXml, pretty_print=True, xml_declaration=True, encoding="utf-8")
        file = open(self.filename, 'wb')
        file.write(convertedString)
        file.close()
    
    def __createVersion(self, dataRepXml:etree._Element) -> etree._Element:
        
        Version = etree.SubElement(dataRepXml, 'Version')
        nVersionMajor = etree.SubElement(Version, 'nVersionMajor')
        nVersionMajor.text = '4'
        nVersionMinor = etree.SubElement(Version, 'nVersionMinor')
        nVersionMinor.text = '0'

        return dataRepXml

    def __createCitation(self, dataRepXml:etree._Element) -> etree._Element:
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

    def __createCompound(self, dataRepXml:etree._Element) -> etree._Element:
        
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

    def __createPureOrMixtureData(self, dataRepXml:etree._Element) -> etree._Element:
        
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

    def __createComponents(self, pureOrMixtureDict:dict, PureOrMixtureData:etree._Element)-> etree._Element:
        # Declaration of components
        if 'comps' in pureOrMixtureDict:
            for comp in pureOrMixtureDict['comps']:
                Component = etree.SubElement(PureOrMixtureData, 'Component')
                RegNum = etree.SubElement(Component, 'RegNum')
                nOrgNum = etree.SubElement(RegNum, 'nOrgNum')
                nOrgNum.text = comp
        return PureOrMixtureData

    def __createProperties(self, pureOrMixtureDict:dict, PureOrMixtureData:etree._Element) -> etree._Element:
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
                
                # one uncertainty for each property
                nCombUncertAssessNum.text = str(1)
        return PureOrMixtureData

    def __createVariables(self, pureOrMixtureDict:dict, PureOrMixtureData:etree._Element) -> etree._Element:
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

    def __createDatapoints(self, pureOrMixtureDict:dict, PureOrMixtureData:etree._Element) -> etree._Element:
        if 'measurements' in pureOrMixtureDict:
            for measKey, measurements in pureOrMixtureDict['measurements'].items():
                NumValues = etree.SubElement(PureOrMixtureData, 'NumValues', ID=str(measKey))

                if 'variables' in measurements:
                    for dataPointKey in measurements['variables'].values():

                        if 'elementID' in dataPointKey:
                            # in if clause because elementID is mandatory else raise Error
                            VariableValue = etree.SubElement(NumValues, 'VariableValue')
                            nVarNumber = etree.SubElement(VariableValue, 'nVarNumber')
                            nVarNumber.text = str(dataPointKey['elementID'])
                        if 'value' in dataPointKey:
                            nVarValue = etree.SubElement(VariableValue, 'nVarValue')
                            nVarValue.text = str(dataPointKey['value'])
                        
                        if 'numberOfDigits' in dataPointKey:
                            nVarDigits = etree.SubElement(VariableValue, 'nVarDigits')
                            nVarDigits.text = str(dataPointKey['numberOfDigits'])
                        
                        if  'uncertainty' in dataPointKey:
                            VarUncertainty = etree.SubElement(VariableValue, 'VarUncertainty')
                            nUncertAssessNum = etree.SubElement(VarUncertainty, 'nUncertAssesNum')
                            nUncertAssessNum.text = str(1)
                            nExpandUncertValue = etree.SubElement(VarUncertainty, 'nExpandUncertValue')
                            nExpandUncertValue.text = str(dataPointKey['uncertainty'])
                        


                if 'properties' in measurements:        
                    for dataPointKey in measurements['properties'].values():
                        
                        if 'elementID' in dataPointKey:
                            # in if clause because elementID is mandatory else raise Error
                            PropertyValue = etree.SubElement(NumValues, 'PropertyValue')
                            nPropNumber = etree.SubElement(PropertyValue, 'nPropNumber')
                            nPropNumber.text = str(dataPointKey['elementID'])
                        if 'value' in dataPointKey:
                            nPropValue = etree.SubElement(PropertyValue, 'nPropValue')
                            nPropValue.text = str(dataPointKey['value'])
                        
                        if  'numberOfDigits' in dataPointKey:
                            nPropDigits = etree.SubElement(PropertyValue, 'nPropDigits')
                            nPropDigits.text = str(dataPointKey['numberOfDigits'])
                        
                        if  'uncertainty' in dataPointKey:
                            CombinedUncertainty = etree.SubElement(PropertyValue, 'CombinedUncertainty')
                            nCombUncertAssessNum = etree.SubElement(CombinedUncertainty, 'nCombUncertAssesNum')
                            nCombUncertAssessNum.text = str(1)
                            nCombExpandUncertValue = etree.SubElement(CombinedUncertainty, 'nCombExpandUncertValue')
                            nCombExpandUncertValue.text = str(dataPointKey['uncertainty'])

        return PureOrMixtureData
    