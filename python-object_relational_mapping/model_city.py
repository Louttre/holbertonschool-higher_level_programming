#!/usr/bin/python3
"""class definition of a State and an instance"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State
Base = declarative_base()


class City(Base):
    """state class"""

    __tablename__ = "cities"

    id = Column(
                Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
