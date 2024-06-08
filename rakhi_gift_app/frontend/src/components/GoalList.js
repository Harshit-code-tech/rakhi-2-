import React, { useEffect, useState } from 'react';
import axios from 'axios';

const GoalList = () => {
    const [goals, setGoals] = useState([]);

    useEffect(() => {
        const fetchGoals = async () => {
            try {
                const response = await axios.get('http://localhost:5000/goals');
                setGoals(response.data);
            } catch (error) {
                console.error('Error fetching goals:', error);
            }
        };
        fetchGoals();
    }, []);

    return (
        <ul>
            {goals.map((goal) => (
                <li key={goal._id}>{goal.title}</li>
            ))}
        </ul>
    );
};

export default GoalList;
