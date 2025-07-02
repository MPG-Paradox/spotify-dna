import React, { useState } from 'react';
import { generatePlaylist } from '../services/api';

function GeneratePlaylist() {
  const [prompt, setPrompt] = useState('');
  const [playlist, setPlaylist] = useState([]);
  const [summary, setSummary] = useState('');

  const handleGenerate = () => {
    generatePlaylist(prompt).then(res => {
      setPlaylist(res.data.tracks);
      setSummary(res.data.summary);
    }).catch(console.error);
  };

  return (
    <div>
      <h2>Generate Playlist</h2>
      <input value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Describe your vibe" />
      <button onClick={handleGenerate}>Generate</button>
      {summary && <p>{summary}</p>}
      <ol>
        {playlist.map(t => <li key={t.id}>{t.name} - {t.artists[0].name}</li>)}
      </ol>
    </div>
  );
}

export default GeneratePlaylist;
