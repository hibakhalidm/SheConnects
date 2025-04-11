import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Button, TextField } from '@mui/material';
import { submitStory } from '../services/api';

const StoryForm = ({ onStorySubmitted }) => {
  const [story, setStory] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await submitStory(story);
      onStorySubmitted(response.data);
      setStory('');
    } catch (err) {
      setError('Failed to submit story. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        multiline
        fullWidth
        rows={4}
        value={story}
        onChange={(e) => setStory(e.target.value)}
        placeholder="Share your story anonymously..."
        error={!!error}
        helperText={error}
        required
      />
      <Button type="submit" variant="contained" sx={{ mt: 2 }}>
        Submit
      </Button>
    </form>
  );
};

StoryForm.propTypes = {
  onStorySubmitted: PropTypes.func.isRequired,
};

export default StoryForm;
