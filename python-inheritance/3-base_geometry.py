#!/usr/bin/python3
"""
Define an empty class BaseGeometry
"""


class BaseGeometryMeta(type):
    """
    Empty class
    """
    pass
    
"""Description of the object"""
    
bg = BaseGeometry()

print(dir(bg))

print()

print(dir(BaseGeometry))
