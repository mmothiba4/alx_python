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
    pass
    

class BaseGeometry(metaclass=BaseGeometryMeta):
    """empty class"""
    pass