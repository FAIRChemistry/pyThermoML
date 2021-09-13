import json


class Compound(object):

    def __init__(
        self,
        ID,
        standardInchI,
        standardInchIKey,
        smiles,
        commonName
    ) -> None:

        self.__type = "comp"
        self.ID = ID
        self.standardInchI = standardInchI
        self.standardInchIKey = standardInchIKey
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
    def standardInchI(self):
        return self._standardInchI

    @standardInchI.setter
    def standardInchI(self, standardInchI):
        self._standardInchI = standardInchI

    @property
    def standardInchIKey(self):
        return self._standardInchIKey

    @standardInchIKey.setter
    def standardInchIKey(self, standardInchIKey):
        self._standardInchIKey = standardInchIKey

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
