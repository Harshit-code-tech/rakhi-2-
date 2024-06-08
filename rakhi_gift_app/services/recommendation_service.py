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

def get_recommendations(mood):
    return habits.get(mood, [])
