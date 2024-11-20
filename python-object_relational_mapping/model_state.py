#!/usr/bin/python3
"""Modules for sqlalchemy"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql:///:memory:', echo=True)
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

