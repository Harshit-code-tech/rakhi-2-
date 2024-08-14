from flask import Blueprint, request, jsonify
from rakhi_gift_app.models.Goal import Goal

goal_routes = Blueprint('goals', __name__)


@goal_routes.route('/', methods=['POST'])
def add_goal():
    data = request.get_json()
    goal = Goal(title=data['title'])
    goal.save()
    return jsonify(message="Goal added successfully!"), 201


@goal_routes.route('/', methods=['GET'])
def get_goals():
    goals = Goal.get_all()
    return jsonify(goals), 200
