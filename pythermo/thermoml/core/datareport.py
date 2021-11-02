
from pythermo.thermoml.core.functionalities import TypeChecker
from pythermo.thermoml.core import PureOrMixtureData, compound

import json


class DataReport(object):
    def __init__(
        self,
        title=None,
        DOI=None,
        authors=None,
    ) -> None:
        '''
        Object describing a DataReport.

        Args:
            String title: Title of referred paper
            String DOI: DOI of referred
            List authors: Authors of referred paper
        '''
        
        
        if title is not None:
            self.title = TypeChecker(title, str)
        if DOI is not None:
            self.DOI = TypeChecker(DOI, str)

        self.authors = dict()
        self.compounds = dict()
        self.pureOrMixtureData = dict()

        if authors is not None:
            try:
                for key, value in authors.items():
                    self.authors[key] = value
            except AttributeError:
                raise AttributeError(
                    f"authors should be stored in a dict"
                )
    
    def __str__(self) -> str:
        return self.toJSON()

    def toJSON(self, d=False) -> str:
        '''retunrs json formatted string representation of DataReport class'''
        
        def transformAttributes(self):
            
            jsonDict = dict()
            for key, value in self.__dict__.items():
                
                if isinstance(value, dict):
                    jsonDict[key.replace('_', '')] = dict()

                    for ID, item in value.items():
                        try:
                            jsonDict[key.replace(
                                '_', '')][ID] = item.toJSON(d=True)
                        except AttributeError:
                            jsonDict[key.replace('_', '')][ID] = item

                else:
                    jsonDict[key.replace('_', '')] = value

            return jsonDict

        if d:
            return transformAttributes(self)

        else:
            return json.dumps(
                self,
                default=transformAttributes,
                indent=4
            )

    def addCompound(self, comp) -> str:
        """adds compund to DataReport returns ID"""
        if comp.dataType == "comp":

            # Add compound to dictionary in DataReport
            self.compounds[comp.ID] = comp

            return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData):
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name, ID):
        self.authors[ID] = name

        return ID

    def getAuthor(self, ID):
        try:
            return self._authors[ID]
        except KeyError:
            raise KeyError(
                f"Author with ID {ID} does not exist"
            )
    
    def getAuthorList(self):
        return [
            authorInstance for authorInstance in self._authors.values()
        ]

    def getCompound(self, ID):
        try:
            return self._compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound with ID {ID} does not exist."
            )
        
    def getCompoundList(self):
        return [
            compoundInstance for compoundInstance in self._compounds.values()
        ]
    
    def getCompDict(self) -> dict:
        """returns dictionary with ID (key) of compound (value) used in dataReport"""
        compoundDict = dict()
        for value in self._compounds.values():
            compoundDict[value.ID] = value
        return compoundDict

    def getPureOrMixtureData(self, ID=None) -> PureOrMixtureData:
        if ID is not None:
            try:
                return self._pureOrMixtureData[ID]
            except KeyError:
                
                raise KeyError(
                    f"PureOrMixtureData with ID {ID} does not exist."
                )
        
        #DANGEROUS!
        else:
            try:
                print("used pure or mixture data key = ID")
                return self._pureOrMixtureData["ID"]
                
            except KeyError:
                raise KeyError(f"Please enter key of pure or mixture Data")

    def getPureOrMixtureDataList(self):
        return [
            pureOrMixtureDataInstance
            for pureOrMixtureDataInstance in self._pureOrMixtureData.values()

    ]

    def getPureOrMixtureDataIDs(self) -> list:
        """returns list with keys used in DataReport"""
        keys = list()
        for key in self._pureOrMixtureData.keys():
            keys.append(key)
        return keys
    

    @property
    def compounds(self):
        return self._compounds
    
    @compounds.setter
    def compounds(self, compounds):
        self._compounds = TypeChecker(compounds, dict)

    @property
    def authors(self):
        return self._authors
    
    @authors.setter
    def authors(self, authors):
        self._authors = TypeChecker(authors, dict)

    @property
    def pureOrMixtureData(self):
        return self._pureOrMixtureData

    @pureOrMixtureData.setter
    def pureOrMixtureData(self, pureOrMixtureData):
        self._pureOrMixtureData = TypeChecker(
            pureOrMixtureData, dict
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = TypeChecker(title, str)

    @property
    def DOI(self):
        return self._DOI

    @DOI.setter
    def DOI(self, DOI):
        self._DOI = TypeChecker(DOI, str)
