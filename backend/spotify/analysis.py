import openai
from flask import jsonify, current_app
from . import bp
from .auth import get_spotify_client


@bp.route('/api/summary')
def summary():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401

    top_tracks = sp.current_user_top_tracks(limit=10)['items']
    top_artists = sp.current_user_top_artists(limit=10)['items']

    track_names = [f"{t['name']} - {t['artists'][0]['name']}" for t in top_tracks]
    artist_names = [a['name'] for a in top_artists]

    summary_text = ''
    if current_app.config.get('OPENAI_API_KEY'):
        openai.api_key = current_app.config['OPENAI_API_KEY']
        prompt = (
            'Summarize this user\'s music taste using the following artists and tracks: '
            f"Artists: {', '.join(artist_names[:5])}. Tracks: {', '.join(track_names[:5])}"
        )
        result = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        summary_text = result.choices[0].message['content']

    return jsonify({'top_artists': artist_names, 'top_tracks': track_names, 'summary': summary_text})
