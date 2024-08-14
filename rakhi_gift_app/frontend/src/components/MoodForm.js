import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MoodForm = () => {
    const [mood, setMood] = useState('');
    const [recommendations, setRecommendations] = useState([]);
    const [allGoalsCompleted, setAllGoalsCompleted] = useState(false);
    const backendUrl = process.env.REACT_APP_BACKEND_URL;

    useEffect(() => {
        const checkGoals = async () => {
            try {
                const response = await axios.get(`${backendUrl}/goals`);
                const goals = response.data;
                const allCompleted = goals.every(goal => goal.completed);
                setAllGoalsCompleted(allCompleted);
            } catch (error) {
                console.error('Error checking goals:', error);
            }
        };
        checkGoals();
    }, [backendUrl]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${backendUrl}/moods`, { mood });
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
                        <img src={`${process.env.PUBLIC_URL}/images/rakhi_gift.png`} alt="Rakhi Gift" />
                    </div>
                ) : (
                    <h3>Keep trying! You can complete all your goals!</h3>
                )}
            </div>
        </div>
    );
};

export default MoodForm;
