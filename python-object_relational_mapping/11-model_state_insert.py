#!/usr/bin/python3
"""Modules for sqlalchemy"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    mysql = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(mysql.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
