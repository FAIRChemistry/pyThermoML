# @File          :   datareport.py
# @Last modified :   2022/04/07 23:13:12
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pydantic import BaseModel

from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.core.compound import Compound


class DataReport(BaseModel):
    """
    Class that represents a data report. Basic class of ThermoML - data report.

    Note:
        All entrys of this API refer to http://media.iupac.org/namespaces/ThermoML/ThermoML.xsd 
        ThermoML - schema definition.

    Args:
        title (Optional[str]): Title of a referred paper.
        DOI (Optional[str]): DOI of a referred paper.
        authors (Optional[dict[str, str]]): Dictionary with authors of a referred paper. 
            The keys wont be stored in ThermoML.
        compounds (dict[str, Compound]): Compounds which are used in the data reprot. 
            The keys are stored in the ThermoML .xml file in the <nOrgNum> tag.
        pureOrMixtureData (dict[str, PureOrMixtureData]): PureOrMixtureData elements which are 
            used in data report. The keys are stored in the ThermoML .xml file in the 
            nPureOrMixtureDataNumber tag.
    """

    title: Optional[str]
    DOI: Optional[str]
    authors: Optional[dict[str, str]] = {}
    compounds: dict[str, Compound] = {}
    pureOrMixtureData: dict[str, PureOrMixtureData] = {}

    def addCompound(self, comp: Compound) -> str:
        """adds Compound to data report

        Args:
            comp (Compound): the compound that should be added.

        Raises:
            ThermoMLTypeError: type of compound is not "Compound". The compound wont be added.

        Returns:
            str: ID of added compound
        """
        if comp._type != "comp":
            raise ThermoMLTypeError(
                given_type=comp._type, expected_type="Compound"
            )
            # Add compound to dictionary in DataReport
        else:
            self.compounds[comp.ID] = comp

        return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData: PureOrMixtureData) -> str:
        """adds pureOrMixtureData object to data report.

        Args:
            pureOrMixtureData (PureOrMixtureData): PureOrMixtureData object, 
                that contains experimental information.

        Returns:
            str: Id of added pureOrMixtureData object
        """
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name: str, ID: str) -> 'DataReport':
        """adds authors to data report.

        Args:
            name (str): name of the author
            ID (str): freely selectable ID, to receive information about author.

        Returns:
            DataReport: Returns data report that has been modified.

        Warning:
            The author ID gets lost by writing a ThermoML file.
        """
        if self.authors:
            self.authors[ID] = name
            return self
        else:
            authors = dict()
            authors[ID] = name
            self = DataReport(authors=authors, compounds=self.compounds,
                              pureOrMixtureData=self.pureOrMixtureData)
            return self
    
    def deleteAuthor(self, name: str):
        """removes author from a data report.
        
        Args:
            name (str): name of the author that has to be deleted
        
        Returns:
            DataReport: Returns modified data report.
        
        Note:
            If multiple authors have the same name, everyone will be removed.
        """
        if name in self.authors.values():
            delkeys = list()
            for dataRepKey, dataRepName in self.authors.items():
                if name == dataRepName:
                    delkeys.append(dataRepKey)
            for key in delkeys:
                del self.authors[key]
            
            if not self.authors:
                return DataReport(authors = None, compounds = self.compounds, 
                pureOrMixtureData = self.pureOrMixtureData)
            else:
                return self
        else:
            return self            

    def getPureOrMixtureDataIDs(self) -> list[str]:
        """returns all IDs of pure or mixture entries in the data report.

        Returns:
            IDs (list[str]): List with IDs of pure or mixture data objects.
        """
        IDs = list()
        for ID in self.pureOrMixtureData.keys():
            IDs.append(ID)
        return IDs

    def to_string(self) -> str:
        """returns nice printed string representation of data report object.

        Returns:
            str: string representation
        """

        return self.json(indent=4, exclude_none=True)
