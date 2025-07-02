from collections import Counter
from flask import jsonify, current_app
from . import bp
from .auth import get_spotify_client
import openai

@bp.route('/api/summary')
def summary():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401

    top_tracks = sp.current_user_top_tracks(limit=50)
    track_ids = [t['id'] for t in top_tracks['items']]
    features = sp.audio_features(track_ids)
    feature_keys = ['danceability', 'energy', 'valence', 'tempo']
    avg = {k: float(sum(f[k] for f in features if f) / len(features)) for k in feature_keys}

    top_artists = sp.current_user_top_artists(limit=20)
    genres = [g for a in top_artists['items'] for g in a.get('genres', [])]
    top_genres = [g for g, _ in Counter(genres).most_common(5)]

    summary_text = ''
    if current_app.config.get('OPENAI_API_KEY'):
        openai.api_key = current_app.config['OPENAI_API_KEY']
        prompt = f"User's top genres: {', '.join(top_genres)}. Avg features: {avg}. Summarize their taste in two sentences."
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        summary_text = resp.choices[0].message['content']

    return jsonify({'averages': avg, 'top_genres': top_genres, 'summary': summary_text})
