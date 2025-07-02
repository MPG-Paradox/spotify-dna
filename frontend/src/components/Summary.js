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
      <h2>Your Music Taste</h2>
      {data.summary && <p>{data.summary}</p>}
      <h3>Top Genres</h3>
      <ul>
        {data.top_genres.map(g => (
          <li key={g}>{g}</li>
        ))}
      </ul>
    </div>
  );
}

export default Summary;
