#!/usr/bin/python3
"""
This script defines a State class and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): name of the MySQL 
        id (sqlalchemy.Integer): state's id
        name (sqlalchemy.String): state's name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
