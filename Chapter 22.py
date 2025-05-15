# Chapter 22: Working with Databases - SQLAlchemy Example

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(username='alice')
session.add(new_user)
session.commit()