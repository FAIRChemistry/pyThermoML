from pythermo.thermoml.tools.readTools import ThermoMLReader
from pyDaRUS import Citation, Dataset, EngMeta
from pyDaRUS.metadatablocks.citation import SubjectEnum, IdType
from pyDaRUS.metadatablocks.engMeta import DataGeneration


class ThermoMLDaRUSHandler(object):
    """Class providing functionalities to upload/download ThermoML 
    files to DaRUS (data repository of the university of Stuttgart)
    """

    def uploadToDaRUS(self, local_path:str, dv_path:str, dv_name:str) -> str:
        """uploads ThermoML file to DaRUS

        Warning: Please note, that the interface easyDataverse will infer the DATAVERSE_URL as well as 
        DATAVERSE_API_TOKEN from your environment variables. 
        Thus, please make sure these are available at runtim.

        Args:
            local_path (str): local path to ThermoML file
            dv_path (str): path of ThermoML file, that should be stored DaRUS dataverse
            dv_name (str): name of datavarese in DaRUS
        
        Returns:
            str: ID of uploaded dataset. Needed for accessing dataset and download it from DaRUS
        """

        reader = ThermoMLReader(path=local_path)
        dataReport = reader.readFromThermoMLFile()

        dataset = Dataset()
        citation = Citation()
        

        # citation meta data extracted from ThermoML file
        citation.add_description(text=f"Partial or complete data integration of dataset from {dataReport.title}")
        citation.title = dataReport.title
        citation.subject = [SubjectEnum.chemistry]

        citation.add_related_publication(id_type = IdType.doi, id_number = dataReport.DOI)
            
        for author in dataReport.authors.values():

            citation.add_author(name=author)

            # NOTE Email is necessary for DaRUS, but currently dummy values because mail
            # can not be stored in ThermoML files
            citation.add_contact(name=author, email="mail@author.de")
        
        dataset.add_metadatablock(citation)

        # eng meta data extracted from ThermoML file
        for pom in dataReport.pureOrMixtureData.values():
            for prop in pom.properties.values():
                if prop.method == "simulation":
                    method = "simulation"
                elif prop.method == "experiment":
                    method = "experiment"
        
        # TODO distinguish exp/sim
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
    
        # If we want to store each value in engMeta
        """
        for pom in dataReport.pureOrMixtureData.values():
            for meas in pom.measurements.values():
                for prop in meas.properties.keys():
                    propName = pom.getPOMProperty(prop).propName
                    unit = pom.getPOMProperty(prop).unit
                    value = meas.getProperty(prop).value
                    if meas.getProperty(prop).uncertainty != None:
                        error = meas.getProperty(prop).uncertainty
                        error_description = "stadard deviation"
                        engMeta.add_measured_variables(
                            name = propName,
                            unit = unit,
                            error = error,
                            error_description = error_description,
                            minimum_value = value,
                            maximum_value = value,
                        )
                    else:
                        engMeta.add_measured_variables(
                            name = propName,
                            unit = unit,
                            minimum_value = value,
                            maximum_value = value,
                    )
                for var in meas.variables.keys():
                    varName = pom.getPOMVariable(var).varName
                    unit = pom.getPOMVariable(var).unit
                    value = meas.getVariable(var).value

                    engMeta.add_controlled_variables(
                        name = varName,
                        unit = unit,
                        value = value
                    )
        """

        dataset.add_metadatablock(engMeta)
        dataset.add_file(dv_path=dv_path, local_path=local_path)

        p_id = dataset.upload(dataverse_name=dv_name)

        return p_id
    
    def downloadFromDaRUS(self, p_id:str, filedir:str) -> None:
        """Retrieve a dataset from dataverse by using PID

        Args:
            p_id (str): PID of dataset in dataverse
            filedir (str): local path in which dataset should be stored
        """
        dataset = Dataset.from_dataverse_doi(p_id, filedir)
        
