import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

export const submitStory = (story) => API.post('/submit_story', { story });
export const getMatches = (userId) => API.get(`/get_matches?user_id=${userId}`);