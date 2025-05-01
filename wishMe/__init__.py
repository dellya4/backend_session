from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('wishMe.config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from datetime import timedelta
    app.permanent_session_lifetime = timedelta(minutes=30)

    login_manager.login_view = 'auth.login'

    from .routes.auth_routes import auth_bp
    from .routes.wishlist_routes import wishlist_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(wishlist_bp, url_prefix='/')

    return app
