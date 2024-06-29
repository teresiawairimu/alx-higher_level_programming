#!/usr/bin/python3
"""class definition of a city class and Base instance for SQLAlchemy ORM"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """City class which links to the MYSQL table 'cities'"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
