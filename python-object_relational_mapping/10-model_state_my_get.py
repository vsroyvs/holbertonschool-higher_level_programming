#!/usr/bin/python3
'''Module that prints the State object with the name passed as argument'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    name_search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(
            State.name == name_search
            ).first()
    if states:
        print(states.id)
    else:
        print("Not found")
    session.commit()
    session.close()
