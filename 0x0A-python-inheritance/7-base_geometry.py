#!/usr/bin/python3
"""Base Geometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Args:
            name (str): given name
            value (int): given int

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
