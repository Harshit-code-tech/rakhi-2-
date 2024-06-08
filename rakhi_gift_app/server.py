from flask import Flask
from flask_cors import CORS
from routes.goal_routes import goal_routes
from routes.mood_routes import mood_routes
from routes.recommendation_routes import recommendation_routes

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(goal_routes, url_prefix='/goals')
app.register_blueprint(mood_routes, url_prefix='/moods')
app.register_blueprint(recommendation_routes, url_prefix='/recommendations')

@app.route('/')
def home():
    return "Welcome to the Rakhi Gift App!"

if __name__ == '__main__':
    app.run(debug=True)
