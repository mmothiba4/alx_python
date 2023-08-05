#!/usr/bin/python3
"""Square class Module
"""


class BaseGeometry():
    """BaseGeometry class"""

class BaseGeometryMeta(type): 
   
    """BaseGeometry's meta class"""
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    """empty class"""
    pass


class BaseGeometry(metaclass=BaseGeometryMeta):
    """BaseGeometry metaclass"""
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    """empty class"""
    pass

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)