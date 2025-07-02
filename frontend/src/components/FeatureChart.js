import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

function FeatureChart({ features }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!features || features.length === 0) return;
    const ctx = canvasRef.current.getContext('2d');
    const labels = ['danceability', 'energy', 'valence', 'tempo'];
    const data = labels.map(l => features.reduce((sum, f) => sum + f[l], 0) / features.length);
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels,
        datasets: [{ label: 'Avg Features', data, backgroundColor: 'rgba(75,192,192,0.6)' }]
      }
    });
  }, [features]);

  return <canvas ref={canvasRef} />;
}

export default FeatureChart;
