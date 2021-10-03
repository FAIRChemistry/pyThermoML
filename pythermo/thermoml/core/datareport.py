from pythermo.thermoml.core.functionalities import TypeChecker
from pythermo.thermoml.core import PureOrMixtureData

import json


class DataReport(object):
    def __init__(
        self,
        title=None,
        DOI=None,
        *authors
    ) -> None:
        '''
        Object describing a DataReport.

        Args:
            String title: Title of referred paper
            String DOI: DOI of referred
            *String authors: Authors of referred paper
        '''
        if title is not None:
            self.title = title
        if DOI is not None:
            self.DOI = DOI

        self._authors = dict()

        self.compounds = dict()
        self.pureOrMixtureData = dict()

        authorID = 0
        for name in authors:
            self._authors['_author' + str(authorID)] = name
            authorID += 1

    def __str__(self):
        return self.toJSON()

    def toJSON(self, d=False):
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

    def addCompound(self, comp):
        if comp.dataType == "comp":

            # Add compound to dictionary in DataReport
            self.compounds[comp.ID] = comp

            return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData):
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    @property
    def compounds(self):
        return self._compounds
    
    @compounds.setter
    def compounds(self, compounds):
        self._compounds = TypeChecker(compounds, dict)

    def getCompound(self, ID):
        try:
            return self._compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound wit ID {ID} does not exist."
            )
        
    def getCompoundList(self):
        return [
            compoundInstance for compoundInstance in self._compounds.values()
        ]
    
    @property
    def pureOrMixtureData(self):
        return self._pureOrMixtureData

    @pureOrMixtureData.setter
    def pureOrMixtureData(self, pureOrMixtureData):
        self._pureOrMixtureData = TypeChecker(
            pureOrMixtureData, dict
        )

    def getPureOrMixtureData(self, ID=None):
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

    # TODO: multiple authors
