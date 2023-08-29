#!/usr/bin/python3
'''Module that lists all State objects that contain the letter a'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(
            State.name.ilike('%a%')
            )
    for state in states:
        print(f"{state.id}: {state.name}")
    session.commit()
    session.close()
