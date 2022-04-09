# @File          :   pureOrMixtureData.py
# @Last modified :   2022/04/09 18:57:31
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Union, Any, TYPE_CHECKING, Optional
from dataclasses import dataclass
from pydantic import BaseModel, validate_arguments, validator

from pythermo.thermoml.props.propertyBase import PropertyBase
from pythermo.thermoml.vars.variableBase import VariableBase
from pythermo.thermoml.core.measurement import Measurement
from pythermo.thermoml.core.datapoint import DataPoint
from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.utils import type_checking

if TYPE_CHECKING:  # pragma: no cover
    static_check_init_args = dataclass
else:
    static_check_init_args = type_checking


@static_check_init_args
class PureOrMixtureData(BaseModel):
    """class representing experimental/simulated pure or mixture data

    Args:
        ID (str): user specified ID. Stored in ThermoML .xml in nPureOrMixtureDataNumber tag.
        compiler (str): The name of the person who compiled the data contained in the ThermoML file.
        comps (list[str]): used Compounds
        properties (dict[str, PropertyBase]): dictionary of properties used in pureOrMixtureData. (Key: pID, Value: Property)
        variables (dict[str, VariableBase]): dictionary of variables used in pureOrMixtureData. (Key: vID, Value: Variable)
        measurements (dict[str, Measurement]): dictionary of measurements of pureOrMixtureData. (Key: measID, Value: Measurement)           

    """
    
    ID: str
    compiler: str
    comps: list[str] = []
    properties: dict[str, PropertyBase] = {}
    variables: dict[str, VariableBase] = {}
    measurements: dict[str, Measurement] = {}

    @validator("ID", always=True)
    @classmethod
    def validate_ID_string(cls, ID: str):
        """user specified ID of pure or mixture data has to be determined in the following pattern: 'pom[digit/s]'.

        Args:
            ID (str): user specified ID

        Raises:
            TypeError: ID does not match expected pattern.

        Returns:
            str: ID
        """
        if ID.startswith("pom"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'pom[digit/s]'"
            )

    def addProperty(self, prop: PropertyBase) -> str:
        """adds a property to pureOrMixture data

        Args:
            prop (PropertyBase): the respective property is inherited from PropertyBase

        Raises:
            ThermoMLTypeError: If property is no well defined property

        Returns:
            str: user specified ID of property
        """
        if prop._type != "Property":
            raise ThermoMLTypeError(
                given_type=prop._type, expected_type="Property"
            )

        # Add property to dicitonary
        self.properties[prop.ID] = prop

        return prop.ID

    def addVariable(self, variable: VariableBase) -> str:
        """adds a variable to pureOrMixture data

        Args:
            variable (VariableBase): the respective variable is inherited from VariableBase

        Raises:
            ThermoMLTypeError: If variable is no well defined variable

        Returns:
            str: user sepcified ID of variable
        """
        if variable._type != "Variable":
            raise ThermoMLTypeError(
                given_type=variable._type, expected_type="Variable"
            )

        # Add variable to dicitonary
        self.variables[variable.ID] = variable

        return variable.ID

    def addMeasurement(self, dataPoints: list[DataPoint]) -> None:
        """creates a new object of type Measurement, adds measurement to pureOrMxiture data. 
        One measurement consists of multiple datapoints which contain experimental/simulation data of property/variable, 
        with the same meausrement ID.

        Args:
            dataPoints (list[DataPoint]): List of datapoints that should be added to pureOrMixtureData.
        """
        for dataPoint in dataPoints:

            measurementID = dataPoint.measurementID
            if measurementID not in self.measurements.keys():
                self.measurements[measurementID] = Measurement(
                    ID=measurementID
                )
            self.measurements[measurementID].addDataPoint(dataPoint, self)
    
    
    def getMeasurementByValues(self, val1:tuple[str, float], val2:tuple[str, float]=None) -> 'DataReport':
        """With this function property values of specific variable values can be found. 
        
        One or two variable IDs and values must be stored in a tuple.

        Args:
            val1 (tuple[str, float]): First entry: ID of searched variable, value of searched variable.
            val2 (tuple[str, float], optional): Optionally a second variable can be added. 

        Returns:
            PureOrMixtureData: The new created PureOrMixtureData object containing only the measurements 
                with specified variable values.
            
        """

        conditionedPOM = PureOrMixtureData(ID=self.ID, compiler=self.compiler, comps=self.comps, 
            properties=self.properties, variables = self.variables, measurements=dict())

        def __addMeasToPOM__(measValue, conditionedPOM):
            dp = measValue.getDataPointList()
            conditionedPOM.addMeasurement(dp)
            
        if not val2:
            for measID, measValue in self.measurements.items():
                for varID, values in measValue.variables.items():
                    if val1[0] == varID and values.value == val1[1]:
                        __addMeasToPOM__(measValue=measValue, conditionedPOM=conditionedPOM)
        elif val2:
            for measID, measValue in self.measurements.items():
                for varID, values in measValue.variables.items():
                    if val1[0] in measValue.variables.keys() and val2[0] in measValue.variables.keys():
                        if measValue.variables[val1[0]].value == val1[1] and measValue.variables[val2[0]].value == val2[1]:
                            __addMeasToPOM__(measValue=measValue, conditionedPOM=conditionedPOM)    
        
        if conditionedPOM.measurements:
            print("At least one matching measurement could be found.")
        else:
            print("No matching measurement could be found. No measurement entrys in returned pure or mixture data")

        return conditionedPOM

                


    def getMeasurement(self, ID: str) -> Measurement:
        """Returns measurement with given measurementID.

        Args:
            ID (str): The user specified ID of measurement

        Raises:
            KeyError: measurement with ID does not exist

        Returns:
            Measurement: object of type Measurement
        """
        try:
            
            return self.measurements[ID]
        except KeyError:

            raise KeyError(
                f"Measurement with ID {ID} does not exist."
            )
            
    def getMeasurementsList(self) -> list[Measurement]:
        """Returns list of measurements in pureOrMixtureData.

        Returns:
            list[Measurement]: list of measurements
        """
        return list(self.measurements.values())

    @validate_arguments
    def getPOMProperty(self, propertyID: str):
        """returns property with ID propertyID, that is used in pureOrMixtureData.

        Args:
            propertyID (str): ID of property

        Returns:
            PropertyBase: object with type inherited from PropertyBase.
        """
        return self._getElement(
            propertyID,
            self.properties,
        )

    @validate_arguments
    def getPOMVariable(self, variableID: str):
        """returns variable with ID variableID, that is used in pureOrMixtureData.

        Args:
            variableID (str): ID of variable

        Returns:
            VariableBase: object with type inherited from VariableBase.
        """
        return self._getElement(
            variableID,
            self.variables,
        )

    @validate_arguments
    def getMoleFractionIDs(self) -> dict[str, str]:
        """returns dictionary with compoundID <-> moleFraction assignment.

        Returns:
            dict: keys: compoundIDs, values: moleFraction IDs
        """
        moleFracCompound = dict()

        for key in self.comps:

            for value in self.variables:
                try:
                    if self.getPOMVariable(value).compoundID == key:
                        moleFracCompound[key] = value

                except AttributeError:
                    continue
        return moleFracCompound
    

    def to_string(self) -> str:
        """returns nice printed string representation of pureOrMixtureData object.

        Returns:
            str: string representation
        """

        return self.json(indent=4, exclude_none=True)


    def _getElement(
        self,
        elementID: str,
        dictionary: Union[dict[str, VariableBase],
                          dict[str, PropertyBase]]
    ):
        try:
            
            return dictionary[elementID]
        except KeyError:
            raise KeyError(
                f"{elementID} is not defined yet."
            )

