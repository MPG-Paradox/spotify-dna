from flask import jsonify, request
from . import bp
from .auth import get_spotify_client


@bp.route('/api/top-artists')
def top_artists():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401
    results = sp.current_user_top_artists(limit=20)
    return jsonify(results)


@bp.route('/api/top-tracks')
def top_tracks():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401
    results = sp.current_user_top_tracks(limit=20)
    return jsonify(results)


@bp.route('/api/audio-features')
def audio_features():
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401
    ids = request.args.getlist('ids')
    if not ids:
        return jsonify({'error': 'missing_ids'}), 400
    features = sp.audio_features(tracks=ids)
    return jsonify(features)
