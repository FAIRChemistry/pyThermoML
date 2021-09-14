from typing import Type
from pythermo.thermoml.core.functionalities import TypeChecker
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
                    jsonDict[key] = dict()

                    for ID, item in value.items():
                        try:
                            jsonDict[key][ID] = item.toJSON(d=True)
                        except AttributeError:
                            jsonDict[key][ID] = item

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
