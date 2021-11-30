from flask import Flask, send_from_directory # for hosting endpoint
from flask_cors import CORS
import sys

sys.path.append('./src')

from user import user_bp
from search import search_bp
from wishlist import wishlist_bp

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='frontend/build')
    CORS(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(wishlist_bp)

    return app

app = create_app()

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/<path>")
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

def serve_app():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    serve_app()
