'''
File: datareport.py
Project: core
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from typing import Optional
from pydantic import BaseModel

from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.core.compound import Compound


class DataReport(BaseModel):
    """
    Class that represents a data report. Basic class of ThermoML - data report.

    Note:
        All entrys of this API refer to http://media.iupac.org/namespaces/ThermoML/ThermoML.xsd ThermoML - schema definition.

    Args:
        title (Optional[str]): Title of a referred paper.
        DOI (Optional[str]): DOI of a referred paper.
        authors (dict[str, str]): Dictionary with authors of a referred paper. The keys wont be stored in ThermoML.
        compounds (dict[str, Compound]): Compounds which are used in data reprot. The keys are stored in the ThermoML .xml file in the nOrgNum tag.
        pureOrMixtureData (dict[str, PureOrMixtureData]): PureOrMixtureData elements which are used in data report. The keys are stored in the ThermoML .xml file in the nPureOrMixtureDataNumber tag.

    """
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
        """returns pure or mixture data with given pure or mixture data ID.

        Args:
            ID (str): The user specified ID of pureOrMixtureData 

        Raises:
            KeyError: pure or mixture data with ID does not exist

        Returns:
            PureOrMixtureData: object of type PureOrMixtureData with respective ID
        """
        try:
            return self.pureOrMixtureData[ID]
        except KeyError:

            raise KeyError(
                f"PureOrMixtureData with ID {ID} does not exist."
            )
