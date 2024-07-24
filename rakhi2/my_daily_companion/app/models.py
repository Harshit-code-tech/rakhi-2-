# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_daily_companion.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MoodEntry(Base):
    __tablename__ = 'mood_entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    mood = Column(String)
    date = Column(Date)

class DailyGoal(Base):
    __tablename__ = 'daily_goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    goal = Column(String)
    status = Column(String)

Base.metadata.create_all(engine)
