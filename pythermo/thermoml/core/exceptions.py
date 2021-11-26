'''
File: exceptions.py
Project: core
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

class ThermoMLTypeError(Exception):
    """Raised if the type of either variable or property isnt matched
    """

    def __init__(self, given_type, expected_type):
        self.given_type = given_type
        self.expected_type = expected_type

    def __str__(self):
        return (
            f"Expected {self.expected_type}, got {self.given_type}."
        )

class ThermoMLMissingIDError(Exception):
    """Raised if necessary ID is missing.
    """

    def __init__(self, element):
        """creates ThermoMLMissingIDError

        Args:
            element (object): object that has no ID
        """
        self.element = element
    
    def __str__(self):
        """returns a string representation of ThermoMLMissingIDError
        """
        return(
            f"Please enter an ID for {self.element}."
        )

class ThermoMLFileFormatError(Exception):
    """Raised if ThermoML file that should be written has no .xml in its name."""
    def __str__(self):
        """returns a string representation of ThermoMLFileFormatError
        """

        return(
            "New ThermoML file should end with '.xml'"
        )

class ThermoMLWriterDataReportTypeError(Exception):
    """Raised if type of data report is not readable by ThermoMLWriter."""

    def __init__(self, type):
        """creates ThermoMLWriterDataReportTypeError

        Args:
            type (any): received data report type
        """
        self.type = type

    def __str__(self):
        """string representation of ThermoMLWriterDataReportTypeError."""
        return(
            f"Writer can not read data report. Got {self.type} data report. Please enter data report as DataReport, str or dict"
        )

class ThermoMLQuantityNotFoundError(Exception):
    """Raise if property/variable can not be found in prop/var mapping, or if there are issues with units"""

    def __init__(self, propName:str):
        """creates ThermoMLQuantityNotFoundError

        Args:
            propName (str): name of not founded property
        """
        self.propName = propName
    
    def __str__(self):
        """string representation of ThermoMLQuantityNotFoundError."""
        return(
            f"Defined property/variable: '{self.propName}' could not be found in this version of API. \n Please also check whether unit fits ThermoML - schema definition."
        )