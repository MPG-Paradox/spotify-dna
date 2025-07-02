import React, { useEffect, useState } from 'react';
import { getTopArtists, getTopTracks, getAudioFeatures } from '../services/api';
import TopList from './TopList';
import FeatureChart from './FeatureChart';

function Dashboard() {
  const [artists, setArtists] = useState([]);
  const [tracks, setTracks] = useState([]);
  const [features, setFeatures] = useState([]);

  useEffect(() => {
    getTopArtists().then(res => setArtists(res.data.items)).catch(console.error);
    getTopTracks().then(res => {
      setTracks(res.data.items);
      const ids = res.data.items.map(t => t.id);
      getAudioFeatures(ids).then(fr => setFeatures(fr.data)).catch(console.error);
    }).catch(console.error);
  }, []);

  return (
    <div>
      <TopList title="Top Artists" items={artists} />
      <TopList title="Top Tracks" items={tracks} />
      <FeatureChart features={features} />
    </div>
  );
}

export default Dashboard;
