from flask import Blueprint, request, jsonify
from rakhi_gift_app.models.Mood import Mood
from rakhi_gift_app.services.recommendation_service import get_recommendations
from rakhi_gift_app.utils.config import use_ai
from rakhi_gift_app.services.aiRecommendationService import get_ai_recommendations

mood_routes = Blueprint('moods', __name__)


@mood_routes.route('/', methods=['POST'])
def add_mood():
    data = request.get_json()
    mood = Mood(mood=data['mood'])
    mood.save()
    recommendations = get_ai_recommendations(data['mood']) if use_ai else get_recommendations(data['mood'])
    return jsonify(message="Mood recorded successfully!", recommendations=recommendations), 201


@mood_routes.route('/', methods=['GET'])
def get_moods():
    moods = Mood.get_all()
    return jsonify(moods), 200
