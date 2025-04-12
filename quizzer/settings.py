import os


class Config(object):
    ENV = 'DEV'
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(APP_DIR, 'app.db')


class ProdConfig(Config):
    ENV = 'DEV'

class TestConfig(Config):
    ENV = 'DEV'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 

