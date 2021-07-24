import json
from props.propertyBase import PropertyBase

class Compound(object):

    def __init__(
        self,
        ID,
        standardInchi,
        standardInchiKey,
        smiles,
        commonName
    ) -> None:

        self.__type = "comp"
        self.ID = ID
        self.standardInchi = standardInchi
        self.standardInchiKey = standardInchiKey
        self.smiles = smiles
        self.commonName = commonName


    def __str__(self):
        return json.dumps(
            self.__dict__,
            indent=4
        )
    
    @property
    def dataType(self):
        return self.__type
    
    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def standardInchi(self):
        return self._standardInchi
    
    @standardInchi.setter
    def standardInchi(self, standardInchi):
        self._standardInchi = standardInchi
    
    @property
    def standardInchiKey(self):
        return self._standardInchiKey
    
    @standardInchiKey.setter
    def standardInchiKey(self, standardInchiKey):
        self._standardInchiKey = standardInchiKey
    
    @property
    def commonName(self):
        return self._commonName

    @commonName.setter
    def commonName(self, commonName):
        self._commonName = commonName

    @property
    def smiles(self):
        return self._smiles
    
    @smiles.setter
    def smiles(self, smiles):
        self._smiles = smiles
