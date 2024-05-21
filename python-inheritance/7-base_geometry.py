#!/usr/bin/python3
"""Class definition for BaseGeometry"""


class BaseGeometry:
    """This class serves as a base for geometry-related classes"""

    def area(self):
        """Placeholder method for calculating the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
