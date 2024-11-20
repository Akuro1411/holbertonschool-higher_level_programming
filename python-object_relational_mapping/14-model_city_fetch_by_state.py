#!/usr/bin/python3
"""Modules for sqlalchemy"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    mysql = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(mysql.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    # You shouldn't write on clause,
    # because there 1 foreign key and orm know how to join tables.
    rows = session.query(State, City).join(City).all()
    for s, c in rows:
        print(f"{s.name}: ({c.id}) {c.name}")
