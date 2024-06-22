#!/usr/bin/python3
"""fetches cities with letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database),
        pool_pre_ping=True
        )
    session = Session(engine)
    a_letter = '%a%'
    eachState = session.query(State).filter(
        State.name.like(a_letter)).order_by(State.id)
    for eachCity in eachState:
        print("{}: {}".format(eachCity.id, eachCity.name))
    session.close()
