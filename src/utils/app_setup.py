from flask import Flask
from flask_cors import CORS

def create_flask_app():
    """Flask Setup"""
    app = Flask(__name__)
    cors = CORS(app)

    return app