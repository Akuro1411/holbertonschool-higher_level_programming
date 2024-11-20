#!/usr/bin/python3
"""Modules for sqlalchemy"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base


class City(Base):
    """City mapped class"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
