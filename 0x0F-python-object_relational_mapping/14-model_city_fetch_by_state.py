#!/usr/bin/python3
"""
Lists all states in ascending order
"""


from sqlalchemy import *
import warnings
from sqlalchemy import exc as sa_exc
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb:' +
                           '//{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    #Base.metadata.reflect(bind=engine)
    #for table in reversed(Base.metadata.sorted_tables):
    #    print(table)
    #for model in states:
    #    print('{}: {}'.format(model[1].name, model[0]))

if __name__ == '__main__':
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        main()
