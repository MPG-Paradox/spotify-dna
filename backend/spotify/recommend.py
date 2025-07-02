import numpy as np
from flask import jsonify
from sklearn.neighbors import NearestNeighbors
from . import bp
from .auth import get_spotify_client


@bp.route('/api/recommend')
def recommend():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401

    top = sp.current_user_top_tracks(limit=20)
    track_ids = [t['id'] for t in top['items']]
    features = sp.audio_features(track_ids)
    feats = np.array([[
        f['danceability'], f['energy'], f['loudness'], f['speechiness'],
        f['acousticness'], f['instrumentalness'], f['liveness'], f['valence'],
        f['tempo']
    ] for f in features if f])

    nn = NearestNeighbors(n_neighbors=5, metric='euclidean')
    nn.fit(feats)
    distances, indices = nn.kneighbors(feats)

    recs = []
    for idxs in indices:
        for i in idxs:
            recs.append(top['items'][i])
    # simple unique
    seen = set()
    unique_recs = []
    for r in recs:
        if r['id'] not in seen:
            unique_recs.append(r)
            seen.add(r['id'])
    return jsonify({'tracks': unique_recs})
