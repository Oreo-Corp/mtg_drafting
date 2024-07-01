import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from app.config import Config
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

# Importing blueprints


# For debugging purposes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    CORS(app)

    from app.main.routes import bp as main_bp
    from app.errors.handlers import bp as errors_bp
    from app.posts.routes import bp as posts_bp
    from app.users.routes import bp as users_bp
    from app.drafts.routes import bp as drafts_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(posts_bp, url_prefix='/api/posts')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(drafts_bp, url_prefix='/api/drafts')

    return app