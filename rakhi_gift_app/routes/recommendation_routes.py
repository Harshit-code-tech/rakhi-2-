from flask import Blueprint, request, jsonify
from rakhi_gift_app.models.Prediction import Prediction
from rakhi_gift_app.services.aiRecommendationService import get_ai_recommendations

recommendation_routes = Blueprint('recommendations', __name__)

@recommendation_routes.route('/', methods=['POST'])
def add_recommendation():
    data = request.get_json()
    mood = data['mood']
    recommendations = get_ai_recommendations(mood)
    prediction = Prediction(mood=mood, recommendations=recommendations)
    prediction.save()
    return jsonify(message="Recommendation added successfully!", recommendations=recommendations), 201

@recommendation_routes.route('/', methods=['GET'])
def get_recommendations():
    predictions = Prediction.get_all()
    return jsonify(predictions), 200