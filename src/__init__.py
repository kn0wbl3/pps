from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from src import models
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

db = SQLAlchemy()


def create_app():
    logger.debug("test")
    app = Flask(__name__)
    app.secret_key = os.getenv("HASH")

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase"
    )
    # Disable track modifications for performance
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from src.views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app
