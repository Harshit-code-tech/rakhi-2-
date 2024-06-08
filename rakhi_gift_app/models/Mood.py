# models/Mood.py
from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.getenv('MONGO_URI'))
db = client['rakhi_gift_app']

class Mood:
    def __init__(self, mood, date=None):
        self.mood = mood
        self.date = date or datetime.utcnow()

    def save(self):
        db.moods.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.moods.find())
