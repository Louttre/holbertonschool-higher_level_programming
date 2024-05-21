#!/usr/bin/python3
"""Class definition for BaseGeometry"""


class BaseGeometry:
    """This class serves as a base for geometry-related classes"""

    def area(self):
        """Placeholder method for calculating the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
