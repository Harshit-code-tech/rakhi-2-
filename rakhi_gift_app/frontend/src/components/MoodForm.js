import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MoodForm = () => {
    const [mood, setMood] = useState('');
    const [recommendations, setRecommendations] = useState([]);
    const [allGoalsCompleted, setAllGoalsCompleted] = useState(false);

    useEffect(() => {
        const checkGoals = async () => {
            try {
                const response = await axios.get('http://localhost:5000/goals');
                const goals = response.data;
                const allCompleted = goals.every(goal => goal.completed);
                setAllGoalsCompleted(allCompleted);
            } catch (error) {
                console.error('Error checking goals:', error);
            }
        };
        checkGoals();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/moods', { mood });
            setMood('');
            setRecommendations(response.data.recommendations);
        } catch (error) {
            console.error('Error adding mood:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={mood}
                    onChange={(e) => setMood(e.target.value)}
                    placeholder="Enter your mood"
                />
                <button type="submit">Add Mood</button>
            </form>
            <div>
                <h3>Recommendations:</h3>
                <ul>
                    {recommendations.map((rec, index) => (
                        <li key={index}>{rec}</li>
                    ))}
                </ul>
            </div>
            <div>
                {allGoalsCompleted ? (
                    <div>
                        <h3>Congratulations! You've completed all your goals!</h3>
                        <img src="path_to_your_rakhi_image" alt="Rakhi Gift" />
                    </div>
                ) : (
                    <h3>Keep trying! You can complete all your goals!</h3>
                )}
            </div>
        </div>
    );
};

export default MoodForm;
