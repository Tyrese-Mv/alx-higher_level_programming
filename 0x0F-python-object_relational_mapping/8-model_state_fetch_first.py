#!/usr/bin/python3
"""fetches first city"""
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
    eachState = session.query(State).order_by(State.id).first()
    if eachState is None:
        print("Nothing")
    else:
        print("{}: {}".format(eachState.id, eachState.name))
    session.close()
