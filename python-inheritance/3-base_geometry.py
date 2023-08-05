#!/usr/bin/python3
"""
Define an empty class BaseGeometry
"""


class BaseGeometry:
    """
    Base geometry's meta class
    """
    pass


    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    

class BaseGeometry(BaseGeometry=BaseGeometryMeta):
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
