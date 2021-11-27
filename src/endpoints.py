from flask import Flask # for hosting endpoint
from flask_cors import CORS

from user import user_bp
from search import search_bp
from wishlist import wishlist_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(wishlist_bp)

    return app

def main():
    app = create_app()
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
