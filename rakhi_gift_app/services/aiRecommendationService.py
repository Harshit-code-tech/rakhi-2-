ai_recommendations = {
    'happy': [
        "Join a dance class",
        "Plan a trip",
        "Volunteer for a cause"
    ],
    'sad': [
        "Try painting",
        "Write a letter to a loved one",
        "Cook a new recipe"
    ],
    'anxious': [
        "Meditate for 10 minutes",
        "Go for a run",
        "Practice mindfulness"
    ]
}

def get_ai_recommendations(mood):
    return ai_recommendations.get(mood, [])
