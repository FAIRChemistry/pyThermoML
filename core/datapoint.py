from core.functionalities import TypeChecker


class DataPoint(object):

    def __init__(
        self,
        measurementID,
        value,
        propID=None,
        varID=None,
        uncertainty=None
    ) -> None:

        self.measurementID = measurementID
        self.value = value

        if propID:
            self.elementID = propID
        elif varID:
            self.elementID = varID
        else:
            raise TypeError(
                "Neither property or variable ID have been defined.")

        if uncertainty:
            self.uncertainty = uncertainty

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
        self._value = TypeChecker(value, float)

    @property
    def uncertainty(self):
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        self._uncertainty = TypeChecker(uncertainty, float)
