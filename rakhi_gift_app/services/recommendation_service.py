habits = {
    'happy': [
        "Go for a walk",
        "Call a friend",
        "Read a book"
    ],
    'sad': [
        "Watch a funny movie",
        "Listen to uplifting music",
        "Write in a journal"
    ],
    'anxious': [
        "Practice deep breathing",
        "Do some yoga",
        "Take a relaxing bath"
    ]
}

# services/recommendation_service.py
def get_recommendations(mood):
    # Basic example of mood-based recommendations
    recommendations = {
        'happy': ['Keep smiling!', 'Spread the joy!'],
        'sad': ['It\'s okay to feel sad sometimes.', 'Talk to a friend.'],
        'anxious': ['Take deep breaths.', 'Go for a walk.']
    }
    return recommendations.get(mood, ['Stay positive!'])
