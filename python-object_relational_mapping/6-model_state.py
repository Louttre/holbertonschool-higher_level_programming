from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/hbtn_0e_0_usa')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
new_state = State(name='California')
session.add(new_state)
session.commit()
session.close()
