import axios from 'axios';

const api = axios.create({
  baseURL: '/' // same origin
});

export const getTopArtists = () => api.get('/api/top-artists');
export const getTopTracks = () => api.get('/api/top-tracks');
export const getAudioFeatures = (ids) => api.get('/api/audio-features', { params: { ids } });
export const getRecommend = () => api.get('/api/recommend');
export const generatePlaylist = (prompt) => api.get('/api/generate', { params: { prompt } });
export const getSummary = () => api.get('/api/summary');

export default api;
