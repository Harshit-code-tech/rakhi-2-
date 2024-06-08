import logo from './logo.svg';
import './App.css';
import React from 'react';
import GoalForm from './components/GoalForm';
import GoalList from './components/GoalList';
import MoodForm from './components/MoodForm';

const App = () => {
    return (
        <div>
            <h1>Rakhi Gift App</h1>
            <GoalForm />
            <GoalList />
            <MoodForm />
        </div>
    );
};

export default App;
