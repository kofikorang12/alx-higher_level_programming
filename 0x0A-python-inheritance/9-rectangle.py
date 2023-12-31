#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Attributes:
        width (int): the rect width
        height (int): the rect height
    """
    def __init__(self, width, height):
        """Initializer

        Args:
            width (int): the rect width
            height (int): the rect height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Humain reading representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
