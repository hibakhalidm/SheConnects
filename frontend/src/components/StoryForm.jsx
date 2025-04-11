import React, { useState } from 'react';
import PropTypes from 'prop-types';
import axios from '../services/api';

const StoryForm = ({ onStorySubmitted }) => {
  const [story, setStory] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/stories', { story });
      onStorySubmitted(response.data);
      setStory('');
    } catch (err) {
      setError('Failed to submit story. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={story}
        onChange={(e) => setStory(e.target.value)}
        placeholder="Share your story..."
        required
      />
      <button type="submit">Submit</button>
      {error && <p>{error}</p>}
    </form>
  );
};

StoryForm.propTypes = {
  onStorySubmitted: PropTypes.func.isRequired,
};

export default StoryForm;
