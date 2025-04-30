from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../confing.py')

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.auth_routes import aith_bp
    from .routes.wishlist_routes import wishlist_bp

    app.register_blueprint(aith_bp)
    app.register_blueprint(wishlist_bp)

    return app