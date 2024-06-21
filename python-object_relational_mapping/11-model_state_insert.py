#!/usr/bin/python3
"""module"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    l1 = sys.argv[1]
    l2 = sys.argv[2]
    l3 = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{l1}:{l2}@localhost:3306/{l3}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()
