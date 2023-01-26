# @File          :   writeTools.py
# @Last modified :   2022/04/09 19:29:12
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from textwrap import indent
import lxml.etree as etree
from pythermo.thermoml.core import DataReport
from pydantic import BaseModel
from typing import Optional
import json


class ThermoMLWriter(BaseModel):
    """Class providing functionalities for writing ThermoML file.

    Args:
        folder_thermoML_files (str): name of the ThermoML file that should be written.
        folder_json_files (str): name of the json files that should be written.
    """

    folder_thermoML_files: Optional[str]
    folder_json_files: Optional[str]
    _attr_qname: etree.QName = etree.QName(
        "http://www.w3.org/2001/XMLSchema-instance", "schemaLocation"
    )
    _nsmap: dict[str, str] = {
        None: "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }

    def writeJSON(self, dataReport: DataReport, filename: str) -> None:
        """writes pyThermoML readable .json file.

        Args:
            dataReport (DataReport): Dataset that schould be converted into .json file.
            filename (str): name of the .json file
        """
        json_string = dataReport.to_string()
        print(type(json_string))
        with open(f"{self.folder_json_files}{filename}", "w") as file:
            file.write(json_string)

    def writeThermo(self, dataReport: DataReport, filename: str) -> None:
        """writes ThermoML file to entered filename, by checking wheter key is in data report dictionary and by writing entry possibly to respective ThermoML tag.

        Args:
            dataReport (DataReport): Dataset that should be written into ThermoML file
            filename (str): filename of new ThermoML file
        """
        dataRepXml = etree.Element(
            "DataReport",
            {self._attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"},
            nsmap=self._nsmap,
        )
        dataReport = dataReport.dict(exclude_none=True)
        dataRepXml = self.__createVersion(dataRepXml)
        dataRepXml = self.__createCitation(dataReport, dataRepXml)
        dataRepXml = self.__createCompound(dataReport, dataRepXml)
        dataRepXml = self.__createPureOrMixtureData(dataReport, dataRepXml)

        self.__writeFile(dataRepXml, filename)

    def __writeFile(self, dataRepXml: etree._Element, filename):
        convertedString = etree.tostring(
            dataRepXml, pretty_print=True, xml_declaration=True, encoding="utf-8"
        )
        file = open(f"{self.folder_thermoML_files}{filename}", "wb")
        file.write(convertedString)
        file.close()

    def __createVersion(self, dataRepXml: etree._Element) -> etree._Element:

        Version = etree.SubElement(dataRepXml, "Version")
        nVersionMajor = etree.SubElement(Version, "nVersionMajor")
        nVersionMajor.text = "4"
        nVersionMinor = etree.SubElement(Version, "nVersionMinor")
        nVersionMinor.text = "0"

        return dataRepXml

    def __createCitation(
        self, dataRep: DataReport, dataRepXml: etree._Element
    ) -> etree._Element:
        if "title" not in dataRep and "DOI" not in dataRep and dataRep["authors"] == {}:
            return dataRepXml
        else:
            Citation = etree.SubElement(dataRepXml, "Citation")
            if "title" in dataRep:
                sTitle = etree.SubElement(Citation, "sTitle")
                sTitle.text = dataRep["title"]
            if "authors" in dataRep:
                for key in dataRep["authors"].keys():
                    sAuthor = etree.SubElement(Citation, "sAuthor")
                    sAuthor.text = dataRep["authors"][key]
            if "DOI" in dataRep:
                sDOI = etree.SubElement(Citation, "sDOI")
                sDOI.text = dataRep["DOI"]

            return dataRepXml

    def __createCompound(
        self, dataRep: DataReport, dataRepXml: etree._Element
    ) -> etree._Element:

        if "compounds" in dataRep:
            for key, value in dataRep["compounds"].items():

                Compound = etree.SubElement(dataRepXml, "Compound")
                RegNum = etree.SubElement(Compound, "RegNum")
                nOrgNum = etree.SubElement(RegNum, "nOrgNum")
                nOrgNum.text = str(key)

                # subjson = dataRep['compounds']
                if "standardInchI" in value:
                    sstandardInchI = etree.SubElement(Compound, "sStandardInChI")
                    sstandardInchI.text = value["standardInchI"]

                if "standardInchIKey" in value:
                    sstandardInchIKey = etree.SubElement(Compound, "sStandardInChIKey")
                    sstandardInchIKey.text = value["standardInchIKey"]

                if "commonName" in value:
                    sCommonName = etree.SubElement(Compound, "sCommonName")
                    sCommonName.text = value["commonName"]

                if "smiles" in value:
                    sSmiles = etree.SubElement(Compound, "sSmiles")
                    sSmiles.text = value["smiles"]

        return dataRepXml

    def __createPureOrMixtureData(
        self, dataRep: DataReport, dataRepXml: etree._Element
    ) -> etree._Element:

        if "pureOrMixtureData" in dataRep:
            for key, value in dataRep["pureOrMixtureData"].items():
                PureOrMixtureData = etree.SubElement(dataRepXml, "PureOrMixtureData")

                # ID of respective PureOrMixtureData
                nPureOrMixtureDataNumber = etree.SubElement(
                    PureOrMixtureData, "nPureOrMixtureDataNumber"
                )
                nPureOrMixtureDataNumber.text = str(key)

                sCompiler = etree.SubElement(PureOrMixtureData, "sCompiler")
                sCompiler.text = value["compiler"]
                PureOrMixtureData = self.__createComponents(value, PureOrMixtureData)
                PureOrMixtureData = self.__createProperties(value, PureOrMixtureData)
                PureOrMixtureData = self.__createVariables(value, PureOrMixtureData)
                PureOrMixtureData = self.__createDatapoints(value, PureOrMixtureData)

        return dataRepXml

    def __createComponents(
        self, pureOrMixtureDict: dict, PureOrMixtureData: etree._Element
    ) -> etree._Element:
        # Declaration of components
        if "comps" in pureOrMixtureDict:
            for comp in pureOrMixtureDict["comps"]:
                Component = etree.SubElement(PureOrMixtureData, "Component")
                RegNum = etree.SubElement(Component, "RegNum")
                nOrgNum = etree.SubElement(RegNum, "nOrgNum")
                nOrgNum.text = str(comp)
        return PureOrMixtureData

    def __createProperties(
        self, pureOrMixtureDict: dict, PureOrMixtureData: etree._Element
    ) -> etree._Element:
        if "properties" in pureOrMixtureDict:
            for key, value in pureOrMixtureDict["properties"].items():
                Property = etree.SubElement(PureOrMixtureData, "Property")
                nPropNumber = etree.SubElement(Property, "nPropNumber")
                nPropNumber.text = str(key)
                PropertyMethodID = etree.SubElement(Property, "Property-MethodID")

                if "propName" in value:
                    PropertyGroup = etree.SubElement(PropertyMethodID, "PropertyGroup")
                    propertyGroupName = etree.SubElement(
                        PropertyGroup, value["propGroup"]
                    )
                    ePropName = etree.SubElement(propertyGroupName, "ePropName")
                    ePropName.text = value["propName"] + ", " + value["unit"]

                # not used in ThermoML schema definition
                if "method" in value:
                    eMethodName = etree.SubElement(propertyGroupName, "eMethodName")
                    eMethodName.text = value["method"]

                if "compoundID" in value:
                    RegNum = etree.SubElement(PropertyMethodID, "RegNum")
                    nOrgNum = etree.SubElement(RegNum, "nOrgNum")
                    nOrgNum.text = str(value["compoundID"])
                PropUncertainty = etree.SubElement(Property, "PropUncertainty")
                nCombUncertAssessNum = etree.SubElement(
                    PropUncertainty, "nUncertAssessNum"
                )

                # one uncertainty for each property
                nCombUncertAssessNum.text = str(1)
        return PureOrMixtureData

    def __createVariables(
        self, pureOrMixtureDict: dict, PureOrMixtureData: etree._Element
    ) -> etree._Element:
        if "variables" in pureOrMixtureDict:
            for key, value in pureOrMixtureDict["variables"].items():
                Variable = etree.SubElement(PureOrMixtureData, "Variable")
                nVarNumber = etree.SubElement(Variable, "nVarNumber")
                nVarNumber.text = str(key)
                VariableID = etree.SubElement(Variable, "VariableID")
                VariableType = etree.SubElement(VariableID, "VariableType")

                if "varType" in value:
                    varName = etree.SubElement(VariableType, value["varType"])
                    if "unit" in value:
                        if len(value["unit"]) >= 1:
                            if "varName" in value:
                                varName.text = value["varName"] + ", " + value["unit"]
                        # e.g component Composition
                        else:
                            if "varName" in value:
                                varName.text = value["varName"]

                if "compoundID" in value:
                    RegNum = etree.SubElement(VariableID, "RegNum")
                    nOrgNum = etree.SubElement(RegNum, "nOrgNum")
                    nOrgNum.text = str(value["compoundID"])

                VarUncertainty = etree.SubElement(Variable, "VarUncertainty")
                nUncertAssessNum = etree.SubElement(VarUncertainty, "nUncertAssessNum")
                # one uncertainty for each variable
                nUncertAssessNum.text = str(1)
        return PureOrMixtureData

    def __createDatapoints(
        self, pureOrMixtureDict: dict, PureOrMixtureData: etree._Element
    ) -> etree._Element:
        if "measurements" in pureOrMixtureDict:
            for measKey, measurements in pureOrMixtureDict["measurements"].items():
                NumValues = etree.SubElement(
                    PureOrMixtureData, "NumValues", ID=str(measKey)
                )

                if "variables" in measurements:
                    for dataPointKey in measurements["variables"].values():

                        if "elementID" in dataPointKey:
                            # in if clause because elementID is mandatory else raise Error
                            VariableValue = etree.SubElement(NumValues, "VariableValue")
                            nVarNumber = etree.SubElement(VariableValue, "nVarNumber")
                            nVarNumber.text = str(dataPointKey["elementID"])
                        if "value" in dataPointKey:
                            nVarValue = etree.SubElement(VariableValue, "nVarValue")
                            nVarValue.text = str(dataPointKey["value"])

                        if "numberOfDigits" in dataPointKey:
                            nVarDigits = etree.SubElement(VariableValue, "nVarDigits")
                            nVarDigits.text = str(dataPointKey["numberOfDigits"])

                        if "uncertainty" in dataPointKey:
                            VarUncertainty = etree.SubElement(
                                VariableValue, "VarUncertainty"
                            )
                            nUncertAssessNum = etree.SubElement(
                                VarUncertainty, "nUncertAssessNum"
                            )
                            nUncertAssessNum.text = str(1)
                            nStdUncertValue = etree.SubElement(
                                VarUncertainty, "nStdUncertValue"
                            )
                            nStdUncertValue.text = str(dataPointKey["uncertainty"])

                if "properties" in measurements:
                    for dataPointKey in measurements["properties"].values():

                        if "elementID" in dataPointKey:
                            # in if clause because elementID is mandatory else raise Error
                            PropertyValue = etree.SubElement(NumValues, "PropertyValue")
                            nPropNumber = etree.SubElement(PropertyValue, "nPropNumber")
                            nPropNumber.text = str(dataPointKey["elementID"])
                        if "value" in dataPointKey:
                            nPropValue = etree.SubElement(PropertyValue, "nPropValue")
                            nPropValue.text = str(dataPointKey["value"])

                        if "numberOfDigits" in dataPointKey:
                            nPropDigits = etree.SubElement(PropertyValue, "nPropDigits")
                            nPropDigits.text = str(dataPointKey["numberOfDigits"])

                        if "uncertainty" in dataPointKey:
                            PropUncertainty = etree.SubElement(
                                PropertyValue, "PropUncertainty"
                            )
                            nCombUncertAssessNum = etree.SubElement(
                                PropUncertainty, "nUncertAssessNum"
                            )
                            nCombUncertAssessNum.text = str(1)
                            nCombExpandUncertValue = etree.SubElement(
                                PropUncertainty, "nStdUncertValue"
                            )
                            nCombExpandUncertValue.text = str(
                                dataPointKey["uncertainty"]
                            )

        return PureOrMixtureData
