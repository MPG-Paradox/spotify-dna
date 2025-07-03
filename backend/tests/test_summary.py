import os
import sys
import types
from unittest.mock import patch, MagicMock

import pytest

# Ensure backend directory is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Prepare fake packages to satisfy optional dependencies
fake_sklearn = types.ModuleType('sklearn')
fake_sklearn.__path__ = []
sys.modules.setdefault('sklearn', fake_sklearn)
sys.modules.setdefault('sklearn.neighbors', MagicMock())
sys.modules.setdefault('sentence_transformers', MagicMock())
sys.modules.setdefault('torch', MagicMock())

class FakeSpotify:
    def current_user_top_tracks(self, limit=10):
        return {
            'items': [
                {'name': 'Song1', 'artists': [{'name': 'Artist1'}]},
                {'name': 'Song2', 'artists': [{'name': 'Artist2'}]}
            ]
        }

    def current_user_top_artists(self, limit=10):
        return {
            'items': [
                {'name': 'Artist1'},
                {'name': 'Artist2'}
            ]
        }


def create_test_app():
    with patch('subprocess.check_call'):
        from app import create_app
        return create_app()


def test_summary_response_structure():
    app = create_test_app()
    with app.test_client() as client:
        with patch('spotify.analysis.get_spotify_client', return_value=FakeSpotify()):
            response = client.get('/api/summary')
            assert response.status_code == 200
            data = response.get_json()
            assert 'top_artists' in data
            assert 'top_tracks' in data
            assert 'summary' in data
            assert data['top_artists'] == ['Artist1', 'Artist2']
            assert data['top_tracks'] == ['Song1 - Artist1', 'Song2 - Artist2']
            assert isinstance(data['summary'], str)
