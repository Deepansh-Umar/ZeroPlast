import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-dev-dev")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///zeroplast.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config): DEBUG = True
class ProdConfig(Config): DEBUG = False
