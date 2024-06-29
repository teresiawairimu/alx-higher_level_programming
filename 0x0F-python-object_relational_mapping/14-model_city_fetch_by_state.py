#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_6_usa
    Results must be sorted in ascending order by cities.id
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
