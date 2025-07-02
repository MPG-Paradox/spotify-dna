from flask import current_app, session, redirect, request, url_for
from . import bp
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_oauth():
    return SpotifyOAuth(
        client_id=current_app.config['SPOTIFY_CLIENT_ID'],
        client_secret=current_app.config['SPOTIFY_CLIENT_SECRET'],
        redirect_uri=current_app.config['SPOTIFY_REDIRECT_URI'],
        scope=current_app.config['SPOTIFY_SCOPE'],
    )


def get_spotify_client():
    token_info = session.get('token_info')
    if not token_info:
        return None
    if get_spotify_oauth().is_token_expired(token_info):
        token_info = get_spotify_oauth().refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info
    return spotipy.Spotify(auth=token_info['access_token'])


@bp.route('/login')
def login():
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@bp.route('/callback')
def callback():
    sp_oauth = get_spotify_oauth()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code, as_dict=True)
    session['token_info'] = token_info
    return redirect(url_for('spotify.me'))


@bp.route('/me')
def me():
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('spotify.login'))
    me_info = sp.current_user()
    return me_info
