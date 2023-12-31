#!/usr/bin/python3
"""
Define an empty class BaseGeometry
"""


class BaseGeometry:
    """
    Empty class
    """
    pass

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