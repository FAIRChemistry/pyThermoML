import pandas as pd
import numpy as np

from typing import Optional
from pydantic import BaseModel

from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.core.compound import Compound


class DataReport(BaseModel):

    title: Optional[str]
    DOI: Optional[str]
    authors: dict[str, str] = {}
    compounds: dict[str, Compound] = {}
    pureOrMixtureData: dict[str, PureOrMixtureData] = {}

    def addCompound(self, comp: Compound) -> str:
        """adds compund to DataReport returns ID"""
        if comp._type != "comp":
            raise ThermoMLTypeError(
                given_type=comp._type, expected_type="Compound"
            )
            # Add compound to dictionary in DataReport
        self.compounds[comp.ID] = comp

        return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData):
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name: str, ID: str):
        self.authors[ID] = name

    def getAuthor(self, ID):
        try:
            return self.authors[ID]
        except KeyError:
            raise KeyError(
                f"Author with ID {ID} does not exist"
            )

    def getCompound(self, ID):
        try:
            return self.compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound with ID {ID} does not exist."
            )

    def getPureOrMixtureData(self, ID: str) -> PureOrMixtureData:
        if ID is not None:
            try:
                return self.pureOrMixtureData[ID]
            except KeyError:

                raise KeyError(
                    f"PureOrMixtureData with ID {ID} does not exist."
                )

        # DANGEROUS!
        else:
            try:
                print("used pure or mixture data key = ID")
                return self.pureOrMixtureData["ID"]

            except KeyError:
                raise KeyError("Please enter key of pure or mixture Data")

    def getAuthorList(self):
        return self._getElementList(self.authors)

    def getCompoundList(self):
        return self._getElementList(self.compounds)

    def getPureOrMixtureDataList(self):
        return self._getElementList(self.pureOrMixtureData)

    def _getElementList(self, dictionary: dict) -> list[str]:
        return list(dictionary.keys())

    def getPureOrMixtureDataIDs(self) -> list:
        """returns list with keys used in DataReport"""
        return list(self.pureOrMixtureData.keys())
