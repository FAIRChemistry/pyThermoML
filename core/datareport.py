import json

class DataReport(object):

    def __init__(
        self,
        title,
        DOI,
        *authors,
    ) -> None:

        self.title = title
        self.DOI = DOI
        self._authors = dict()

        self.compounds = dict()
        self.pureOrMixtureData = dict()

        authorID = 0
        for name in authors:
            self._authors['_author' + str(authorID)] = name
            authorID += 1
    def __str__(self):
        
        def transformAttributes(self):
            
            jsonDict = dict()
            for key, value in self.__dict__.items():

                try:
                    jsonDict[key] = value
                except TypeError:
                    jsonDict[key] = str(value)

            return jsonDict

        return json.dumps(
            self,
            default=transformAttributes,
            indent=4
        )
    
    def toJSON(self):
        jsonDict = dict()
        for key, value in self.__dict__.items():

            try:
                jsonDict[key] = value
            except TypeError:
                jsonDict[key] = str(value)

        return jsonDict


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
        self._title = title
    
    @property
    def DOI(self):
        return self._DOI
    
    @DOI.setter
    def DOI(self, DOI):
        self._DOI = DOI
    
    # TODO: getter/setter for authors 