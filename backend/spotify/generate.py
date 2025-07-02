import numpy as np
from flask import jsonify, request
from . import bp
from .auth import get_spotify_client
from sentence_transformers import SentenceTransformer, util
import openai
from flask import current_app

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model


def get_track_embeddings(tracks):
    names = [f"{t['name']} {t['artists'][0]['name']}" for t in tracks]
    embeddings = get_model().encode(names, convert_to_tensor=True)
    return embeddings


@bp.route('/api/generate')
def generate_playlist():
    prompt = request.args.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'missing_prompt'}), 400
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'not_authenticated'}), 401

    top = sp.current_user_top_tracks(limit=50)
    tracks = top['items']
    track_embeds = get_track_embeddings(tracks)
    query_embed = get_model().encode(prompt, convert_to_tensor=True)
    scores = util.cos_sim(query_embed, track_embeds)[0]
    ranked_indices = np.argsort(-scores.cpu().numpy())
    ranked_tracks = [tracks[i] for i in ranked_indices[:10]]

    if current_app.config.get('OPENAI_API_KEY'):
        openai.api_key = current_app.config['OPENAI_API_KEY']
        description = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': f'Summarize this playlist: {prompt}'}]
        )
        summary = description.choices[0].message['content']
    else:
        summary = ''

    return jsonify({'tracks': ranked_tracks, 'summary': summary})
