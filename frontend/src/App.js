import React from 'react';
import Dashboard from './components/Dashboard';
import GeneratePlaylist from './components/GeneratePlaylist';
import Summary from './components/Summary';

function App() {
  return (
    <div className="App">
      <h1>Your Spotify DNA</h1>
      <a href="/login">Login with Spotify</a>
      <Summary />
      <Dashboard />
      <GeneratePlaylist />
    </div>
  );
}

export default App;
