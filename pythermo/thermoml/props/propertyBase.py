'''
File: propertyBase.py
Project: props
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''


from pydantic import BaseModel, validator
from pydantic.fields import PrivateAttr
from typing import Optional


class PropertyBase(BaseModel):
    """
    Base class for properties. Fore more information visit ThermoMLSchema definition.

        Args:
            propName (str): Name of the property. Determined in child classes.
            propGroup (str): Name of belonging property group. Determined in child classes.
            ID (str): User specified property ID. Will be stored in nPropNumber tag in ThermoML .xml
            unit (str): Unit of property. Determined in child classes.
            method (str): Method used to obtain experimental/simulation data. Please enter "experiment" for experimental data and "simulation" for simulation data.
            compoundID (str, optional): ID of reffered compound
            _type (str): Type of property. Default is "Property"
    """
    propName: str
    propGroup: str
    ID: str
    unit: str
    method: str
    compoundID: Optional[str] = None
    _type: str = PrivateAttr(default="Property")

    @validator("ID", always=True)
    @classmethod
    def validate_ID_string(cls, ID:str) -> str:
        """user specified ID of property has to be in the following pattern: 'p[digit/s]'.

        Args:
            ID (str): user specified ID

        Raises:
            TypeError: When ID does not match expected pattern.

        Returns:
            str: ID
        """
        if ID.startswith("p"):
            return ID
        else:
            raise TypeError(
                "ID does not match the expected pattern of 'p[digit/s]'"
            )

    @validator("method", always=True)
    @classmethod
    def validate_method_string(cls, method: str) -> str:
        """user specified method name has to be simulation, experiment, or other.

        Args:
            method (str): user specified method name

        Raises:
            TypeError: method name does not match

        Returns:
            str: method
        """
        if method == "simulation":
            return method
        
        elif method == "experiment":
            return method
        
        elif method == "other":
            return method
        
        else:
            raise TypeError(
                "Please define whether data was obtained by 'experiment', 'simulation' or 'other'"
        )