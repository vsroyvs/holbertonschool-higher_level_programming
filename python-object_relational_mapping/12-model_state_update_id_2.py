#!/usr/bin/python3
'''Module that changes the name of a State object from the database'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    session.query(State).filter(
            State.id == 2
    ).update(
            {
                State.name: 'New Mexico'
            }
            )
    session.commit()
    session.close()
