#!/usr/bin/python3
"""model:state: contains the class definition of state. 
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base)
    """The base class state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128),nullable=False)
