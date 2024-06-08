import React, { useState } from 'react';
import axios from 'axios';

const GoalForm = () => {
    const [title, setTitle] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/goals', { title });
            setTitle('');
        } catch (error) {
            console.error('Error adding goal:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Enter a goal"
            />
            <button type="submit">Add Goal</button>
        </form>
    );
};

export default GoalForm;
