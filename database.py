from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def CreateUser(name,last_topic,last_essay):
  user_object = User(
    name = name,
    last_topic = last_topic,
    last_essay = last_essay,
  )
  session.add(user_object)
  session.commit()
def get_users():
    users = session.query(User).all()
    for user in users:
        print(user.name)
        print(user.last_topic)
        print(user.last_essay)