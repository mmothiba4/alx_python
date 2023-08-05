#!/usr/bin/python3
"""
Description of the module
"""


class BaseGeometryMeta(type):
    """
    Base geometry's meta class
    """


    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    

class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    Description of the class
    """

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    
    a = BaseGeometry()

    print(dir(a))

    print()
    
    print(dir(BaseGeometry))
