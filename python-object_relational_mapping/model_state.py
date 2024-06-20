from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+pymysql://username:password@localhost:3306/database_name')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
new_state = State(name='California')
session.add(new_state)
session.commit()
session.close()
