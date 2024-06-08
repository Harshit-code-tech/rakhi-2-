# server.py
from flask import Flask, request, jsonify
from models.Goal import Goal
from models.Mood import Mood
from models.Prediction import Prediction

app = Flask(__name__)

@app.route('/goals', methods=['POST'])
def add_goal():
    data = request.json
    goal = Goal(title=data['title'])
    goal.save()
    return jsonify({'message': 'Goal added successfully'}), 201

@app.route('/goals', methods=['GET'])
def get_goals():
    goals = Goal.get_all()
    return jsonify(goals), 200

@app.route('/moods', methods=['POST'])
def add_mood():
    data = request.json
    mood = Mood(mood=data['mood'])
    mood.save()
    from services.recommendation_service import get_recommendations
    recommendations = get_recommendations(data['mood'])
    return jsonify({'recommendations': recommendations}), 201

@app.route('/moods', methods=['GET'])
def get_moods():
    moods = Mood.get_all()
    return jsonify(moods), 200

@app.route('/predictions', methods=['POST'])
def add_prediction():
    data = request.json
    prediction = Prediction(recommendation=data['recommendation'])
    prediction.save()
    return jsonify({'message': 'Prediction added successfully'}), 201

@app.route('/predictions', methods=['GET'])
def get_predictions():
    predictions = Prediction.get_all()
    return jsonify(predictions), 200

if __name__ == '__main__':
    app.run(debug=True)
