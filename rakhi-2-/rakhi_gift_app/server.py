from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load environment variables
MONGO_URI = os.getenv('MONGO_URI')

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.rakhiApp


@app.route('/goals', methods=['POST'])
def add_goal():
    data = request.json
    db.goals.insert_one(data)
    return jsonify({'message': 'Goal added successfully'}), 201


@app.route('/goals', methods=['GET'])
def get_goals():
    goals = list(db.goals.find({}, {'_id': 0}))
    return jsonify(goals), 200


@app.route('/moods', methods=['POST'])
def add_mood():
    data = request.json
    db.moods.insert_one(data)
    # Placeholder for recommendations
    recommendations = ["Read a book", "Go for a walk"]
    return jsonify({'recommendations': recommendations}), 201


if __name__ == '__main__':
    app.run(debug=True)
