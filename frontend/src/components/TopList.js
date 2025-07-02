import React from 'react';

function TopList({ title, items }) {
  return (
    <div>
      <h2>{title}</h2>
      <ol>
        {items && items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ol>
    </div>
  );
}

export default TopList;
