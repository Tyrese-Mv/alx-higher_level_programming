#!/usr/bin/python3
"""defining table using SQL alchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State class

    Args:
        Base (class): base class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
