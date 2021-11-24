class ThermoMLTypeError(Exception):
    """Raised when the type of either variable or property isnt matched
    """

    def __init__(self, given_type, expected_type):
        self.given_type = given_type
        self.expected_type = expected_type

    def __str__(self):
        return (
            f"Expected {self.expected_type}, got {self.given_type}."
        )

class ThermoMLSchemaError(Exception):
    """Raised when ThermoML file that schould read in does not follow schema definition

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, tagname):
        """creates ThermoMLSchemaError object

        Args:
            tagname (object): object that does not follow schema definition
        """
        self.tag_name = tagname
    
    def __str__(self):
        """returns a string representation of ThermoMLSchemaError"""
        return(
            f"Problems in {self.tag_name} - tag. Maybe tag name or element name does not follow ThermoML schema definition?"
        )

class ThermoMLMissingIDError(Exception):
    """Raised when a necesarry ID is missing.

    Args:
        Exception ([type]): [description]
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

class ThermoMLNoCompoundError(Exception):
    """Raised when no compound as been specified"""

    def __str__(self):
        """returns a string representation of ThermoMLNoCompoundError
        """
        return(
            f"No compounds have been specified"
        )

class ThermoMLFileFormatError(Exception):
    """Raised when ThermoML file that should be written has no .xml in its name."""
    def __str__(self):
        """returns a string representation of ThermoMLFileFormatError
        """

        return(
            "Please end your new ThermoML file with '.xml'"
        )