from flask import Blueprint

bp = Blueprint('spotify', __name__)

from . import auth, ingest, recommend, generate  # noqa: F401
