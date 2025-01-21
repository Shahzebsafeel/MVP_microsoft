import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [skill, setSkill] = useState('');
  const [recommendation, setRecommendation] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/recommend', { skill });
      setRecommendation(response.data.recommendation);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  return (
    <div className="App">
      <h1>AI CareerMentor</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter a skill:
          <input
            type="text"
            value={skill}
            onChange={(e) => setSkill(e.target.value)}
            placeholder="e.g., Python, HTML"
          />
        </label>
        <button type="submit">Get Career Recommendation</button>
      </form>
      {recommendation && <p>{recommendation}</p>}
    </div>
  );
}

export default App;
