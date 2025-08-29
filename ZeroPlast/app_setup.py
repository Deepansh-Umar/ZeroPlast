from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import DevConfig

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_obj=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    return app
