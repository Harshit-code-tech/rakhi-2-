# models/Prediction.py
from pymongo import MongoClient
from datetime import datetime

client = MongoClient(
    'mongodb+srv://harshitghosh7:rakhi@cluster0.5vlwifq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['rakhi_gift_app']


class Prediction:
    def __init__(self, recommendation, date=None):
        self.recommendation = recommendation
        self.date = date or datetime.utcnow()

    def save(self):
        db.predictions.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.predictions.find())
