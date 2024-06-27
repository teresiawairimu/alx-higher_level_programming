#!/usr/bin/python3
"""class definition of a state class and Base instance for SQLAlchemy ORM"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class which links to the MYSQL table 'states'"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
        import sys
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
        Base.metadata.create_all(engine)
