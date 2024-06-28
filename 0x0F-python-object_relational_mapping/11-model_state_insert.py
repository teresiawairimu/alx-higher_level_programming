#!/usr/bin/python3
"""Add the State object 'Louisiana'
    to the database hbtn_0e_6_usa
    print the new states.id after creation
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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(f"{new_state.id}")
    session.close()
