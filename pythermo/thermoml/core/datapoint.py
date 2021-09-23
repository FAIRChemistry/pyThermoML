from pythermo.thermoml.core.functionalities import TypeChecker
import json

class DataPoint(object):

    def __init__(
        self,
        measurementID,
        value,
        propID=None,
        varID=None,
        uncertainty=None,
        numberOfDigits=None
    ) -> None:


        self.measurementID = measurementID
        self.value = value
        

        if propID:
            self.elementID = propID
            self.__type = "prop"
        elif varID:
            self.elementID = varID
            self.__type = "var"
        else:
            raise TypeError(
                "Neither property or variable ID have been defined.")

        if uncertainty:
            self.uncertainty = uncertainty
        
        if numberOfDigits:
            self.numberOfDigits = numberOfDigits


    def __str__(self):
        return self.toJSON()

    def toJSON(self):
        
        def transformAttributes(self):

            jsonDict = dict()
            for key, value in self.__dict__.items():

                try:
                    jsonDict[key.replace('_','')] = value
                except TypeError:
                    jsonDict[key.replace('_','')] = str(value)

            return jsonDict

        return json.dumps(
            self,
            default=transformAttributes,
            indent=4
        )
    
    @property
    def elementID(self):
        return self._elementID

    @elementID.setter
    def elementID(self, elementID):
        self._elementID = TypeChecker(elementID, str)

    @property
    def measurementID(self):
        return self._measurementID

    @measurementID.setter
    def measurementID(self, measurementID):
        self._measurementID = TypeChecker(measurementID, str)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = TypeChecker(value, float)
        except TypeError:
            self._value = TypeChecker(value, int)
        

    @property
    def uncertainty(self):
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        try:
            self._uncertainty = TypeChecker(uncertainty, float)
        except TypeError:
            self._uncertainty = "NG"

    @property
    def dataType(self):
        return self.__type
    
    @property
    def numberOfDigits(self):
        return self._numberOfDigits
    
    @numberOfDigits.setter
    def numberOfDigits(self, numberOfDigits):
        self._numberOfDigits = TypeChecker(numberOfDigits, int)
        