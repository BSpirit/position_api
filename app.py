"""ConnexionApp and SQLAlchemy objects instantiation"""

from connexion import FlaskApp
import os
from config import app_config
from flask_sqlalchemy import SQLAlchemy


connexion_app: FlaskApp = FlaskApp(__name__)
connexion_app.app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
db: SQLAlchemy = SQLAlchemy(connexion_app.app)
