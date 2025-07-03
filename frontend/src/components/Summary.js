import React, { useEffect, useState } from 'react';
import { getSummary } from '../services/api';

function Summary() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getSummary().then(res => setData(res.data)).catch(console.error);
  }, []);

  if (!data) return null;

  return (
    <div>
      <h2>Your Listening Summary</h2>
      {data.summary && <p>{data.summary}</p>}
      <h3>Top Artists</h3>
      <ol>
        {data.top_artists.map(a => <li key={a}>{a}</li>)}
      </ol>
      <h3>Top Tracks</h3>
      <ol>
        {data.top_tracks.map(t => <li key={t}>{t}</li>)}
      </ol>
    </div>
  );
}

export default Summary;
