#!/usr/bin/python3
"""BaseGeometry class Module"""


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