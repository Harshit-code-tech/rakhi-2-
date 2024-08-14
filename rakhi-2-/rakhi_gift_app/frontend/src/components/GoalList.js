import React, {useEffect, useState} from 'react';
import axios from 'axios';

const GoalList = () => {
    const [goals, setGoals] = useState([]);
    const backendUrl = process.env.REACT_APP_BACKEND_URL;

    useEffect(() => {
        const fetchGoals = async () => {
            try {
                const response = await axios.get(`${backendUrl}/goals`);
                setGoals(response.data);
            } catch (error) {
                console.error('Error fetching goals:', error);
            }
        };
        fetchGoals();
    }, [backendUrl]);

    return (
        <ul>
            {goals.map((goal) => (
                <li key={goal._id}>{goal.title}</li>
            ))}
        </ul>
    );
};

export default GoalList;
