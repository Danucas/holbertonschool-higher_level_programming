#!/usr/bin/python3
"""
This module contains class definition for States
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State table defined by id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """String representation"""
        return self.name
