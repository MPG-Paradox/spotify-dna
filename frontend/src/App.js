import React from 'react';
import Dashboard from './components/Dashboard';
import GeneratePlaylist from './components/GeneratePlaylist';

function App() {
  return (
    <div className="App">
      <h1>Your Spotify DNA</h1>
      <Dashboard />
      <GeneratePlaylist />
    </div>
  );
}

export default App;
