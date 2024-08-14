# kivy_models.py
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


from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood}"


Base.metadata.create_all(engine)
