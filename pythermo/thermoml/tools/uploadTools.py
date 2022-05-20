# @File          :   uploadTools.py
# @Last modified :   2022/04/09 19:29:00
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import List
from pythermo.thermoml.tools.readTools import ThermoMLReader
from pythermo.thermoml.core.datareport import DataReport
from pyDaRUS import Citation, Dataset, EngMeta
from pyDaRUS.metadatablocks.citation import SubjectEnum, IdType, Contact
from pyDaRUS.metadatablocks.engMeta import DataGeneration

from pydantic import BaseModel

class ThermoMLDaRUSHandler(BaseModel):
    """Class providing functionalities to upload/download ThermoML 
    files to DaRUS (data repository of the university of Stuttgart)

    Args:
        folder_thermoML_files(str): path to folder that contains thermoML files
    """
    folder_thermoML_files: str
    
    def uploadToDaRUS(self, thermoML_filename:str, dv_path:str, dv_name:str, title:str, subject:SubjectEnum, description:str, contact_name:str, contact_mail:str) -> str:
        """uploads ThermoML file to DaRUS

        Warning: Please note, that the interface easyDataverse will infer the DATAVERSE_URL as well as 
        DATAVERSE_API_TOKEN from your environment variables. 
        Thus, please make sure these are available at runtime.

        Args:
            thermoML_filename (str): name of the locally stored thermoML file
            dv_path (str): path of ThermoML file, that should be stored DaRUS dataverse
            dv_name (str): name of datavarese in DaRUS
            title (str): title of the file that should be uploaded to DaRUS
            subject (SubjectEnum): Subject of the dataset e. g. chemistry
            description (str): A summary describing the purpose of the dataset
            contact_name (str): Contact for this Dataset
            contact_mail (str): Mail of contact person
        
        Returns:
            str: ID of uploaded dataset. Needed for accessing dataset and download it from DaRUS
        """

    
        reader = ThermoMLReader(folder_thermoML_files=self.folder_thermoML_files)
        dataReport = reader.readFromThermoMLFile(filename=thermoML_filename)

        dataset = Dataset()
        citation = Citation()
        

        # citation meta data extracted from ThermoML file
        citation.add_description(text=description)
        
        citation.title = title
        citation.subject = subject
        citation.kind_of_data = ["ThermoML file"]

        citation.add_related_publication(id_type = IdType.doi, id_number = dataReport.DOI)
            
        for author in dataReport.authors.values():
            citation.add_author(name=author)
        
        citation.add_contact(name=contact_name, email=contact_mail)
        
        dataset.add_metadatablock(citation)

        # eng meta data extracted from ThermoML file
        for pom in dataReport.pureOrMixtureData.values():
            if pom.compiler:
                citation.add_producer(name=pom.compiler)
            for prop in pom.properties.values():
                if prop.method == "simulation":
                    method = "simulation"
                elif prop.method == "experiment":
                    method = "experiment"
        
    
        engMeta = EngMeta()
        if method == "simulation":
            engMeta.data_generation = [DataGeneration.simulation]
        elif method == "experiment":
            engMeta.data_generation = [DataGeneration.experiment]

        # just prop/vars not values in engMeta
        for pom in dataReport.pureOrMixtureData.values():
            for prop in pom.properties.values():
                if prop.compoundID:
                    compName = dataReport.compounds[prop.compoundID].commonName
                    propName = f"{prop.propName} of {compName}" 
                    unit = prop.unit
                else:
                    propName = prop.propName
                    unit = prop.unit
                engMeta.add_measured_variables(name=propName, unit=unit)

            for var in pom.variables.values():
                if var.compoundID:
                    compName = dataReport.compounds[var.compoundID].commonName
                    varName = f"{var.varName} of {compName}" 
                    unit = var.unit
                else:
                    varName = var.varName
                    unit = var.unit
                engMeta.add_controlled_variables(name=varName, unit = unit)

        dataset.add_metadatablock(engMeta)
        dataset.add_file(dv_path=dv_path, local_path=f"{self.folder_thermoML_files}{thermoML_filename}")

        p_id = dataset.upload(dataverse_name=dv_name)

        return p_id
    
    def downloadFromDaRUS(self, p_id:str, filename:str) -> DataReport:
        """Retrieve a dataset from dataverse by using PID

        Args:
            p_id (str): PID of dataset in dataverse
            filename (str): local name of ThermoML file

        Returns:
            DataReport: _description_
        """
        dataset = Dataset.from_dataverse_doi(doi=p_id, filedir=self.folder_thermoML_files)
        return ThermoMLReader(folder_thermoML_files=self.folder_thermoML_files).readFromThermoMLFile(filename=filename)

