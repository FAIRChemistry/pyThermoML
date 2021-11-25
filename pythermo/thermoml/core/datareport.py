from typing import Optional
from pydantic import BaseModel

from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.core.compound import Compound


class DataReport(BaseModel):
    """class that represents a data report. Basic soft data of ThermoML file"""
    title: Optional[str]
    DOI: Optional[str]
    authors: dict[str, str] = {}
    compounds: dict[str, Compound] = {}
    pureOrMixtureData: dict[str, PureOrMixtureData] = {}

    def addCompound(self, comp: Compound) -> str:
        """adds Compound to data report

        Args:
            comp (Compound): the compound that should be added.

        Raises:
            ThermoMLTypeError: When type of compound is not "Compound". The compound wont be added.

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
            pureOrMixtureData (PureOrMixtureData): PureOrMixtureData object, that contains experimental information.

        Returns:
            str: Id of added pureOrMixtureData object
        """
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name: str, ID: str):
        """adds authors to data report. Basic

        Args:
            name (str): name of the author
            ID (str): freely selectable ID, to receive information about author.
        """
        self.authors[ID] = name

    def getAuthor(self, ID: str):
        """returns author with given author ID.

        Args:
            ID (str): The user specified ID of the author. When used with a data Report objcet which was read in by ThermoML Reader,
            be aware that user specified IDs will be deleted. Information about IDs via dataReport.authors

        Raises:
            KeyError: When author with respective ID does not exist.

        Returns:
            str: name of the author
        """
        try:
            return self.authors[ID]
        except KeyError:
            raise KeyError(
                f"Author with ID {ID} does not exist"
            )

    def getCompound(self, ID: str) -> Compound:
        """returns compound with given compound ID.

        Args:
            ID (str): The user specified ID of the compound.

        Raises:
            KeyError: When data report does not contain compound with respective ID.

        Returns:
            Compound: compound object with respective ID.
        """
        try:
            return self.compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound with ID {ID} does not exist."
            )

    def getPureOrMixtureData(self, ID: str) -> PureOrMixtureData:
        """retunrs pure or mixture data with given pure or mixture data ID.

        Args:
            ID (str): The user specified ID of pureOrMixtureData 

        Raises:
            KeyError: [description]

        Returns:
            PureOrMixtureData: [description]
        """
        try:
            return self.pureOrMixtureData[ID]
        except KeyError:

            raise KeyError(
                f"PureOrMixtureData with ID {ID} does not exist."
            )
