#!/usr/bin/python3
'''Module that contains the class definition pf a State'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    '''State Model'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    pass
