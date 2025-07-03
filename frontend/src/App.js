import React from 'react';
import Dashboard from './components/Dashboard';
import Summary from './components/Summary';
import GeneratePlaylist from './components/GeneratePlaylist';

function App() {
  return (
    <div className="App">
      <h1>Your Spotify DNA</h1>
      <a href="/login">Login with Spotify</a>
      <Dashboard />
      <Summary />
      <GeneratePlaylist />
    </div>
  );
}

export default App;
