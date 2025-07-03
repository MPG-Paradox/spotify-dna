from flask import Blueprint

bp = Blueprint('spotify', __name__)

from . import auth, ingest, recommend, generate, analysis  # noqa: F401
