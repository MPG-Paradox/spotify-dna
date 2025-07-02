import os
import sys
import subprocess
from flask import Flask
from flask_cors import CORS
from config import Config


def install_deps():
    """Install dependencies from requirements.txt if not already."""
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_path])
    except subprocess.CalledProcessError as e:
        print(f'Failed installing requirements: {e}')


install_deps()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    CORS(app)

    from spotify import bp as spotify_bp
    app.register_blueprint(spotify_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
