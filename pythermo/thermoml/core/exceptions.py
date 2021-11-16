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
        