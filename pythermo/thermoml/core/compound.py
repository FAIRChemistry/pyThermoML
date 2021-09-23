import json


class Compound(object):

    def __init__(
        self,
        ID,
        standardInchI=None,
        standardInchIKey=None,
        smiles=None,
        commonName=None
    ) -> None:

        if standardInchI is not None:
            self.standardInchI = standardInchI

        if standardInchIKey is not None:
            self.standardInchIKey = standardInchIKey

        if smiles is not None:
            self.smiles = smiles

        if commonName is not None:
            self.commonName = commonName

        self.__type = "comp"
        self.ID = ID

    def __str__(self):
        return self.toJSON()

    def toJSON(self, d=False):

        def transformAttributes(self):
            jsonData = dict()

            for key, value in self.__dict__.items():
                jsonData[key.replace('_','')] = value

            return jsonData

        if d:
            return transformAttributes(self)
        else:
            return json.dumps(
                self,
                default=transformAttributes,
                indent=4,
                sort_keys=True
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
