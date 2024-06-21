#!/usr/bin/python3
"""module"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine(
    f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
    pool_pre_ping=True
)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).order_by(State.id.asc()).all()
for state in states:
    print(f"{state.id}: {state.name}")
session.close()

if __name__ == "__main__":
    main()
