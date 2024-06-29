#!/usr/bin/python3
"""Deletes all State objects with a name containing "a"
    from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_to_delete:
        session.delete(state)
    session.commit()
    session.close()
