from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class User(Base):
  __tablename__ = 'Users'
  id = Column(Integer,primary_key = True)
  name = Column(String)
  last_topic = Column(String)
  last_essay = Column(String)