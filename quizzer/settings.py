import os
from dotenv import load_dotenv

load_dotenv(override=True)
print('Loading environment variables from .env file')


class Config(object):
    ENV = 'DEV'
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    PUSHER_APP_ID = os.environ.get('PUSHER_APP_ID')
    PUSHER_KEY = os.environ.get('PUSHER_KEY')
    PUSHER_SECRET = os.environ.get('PUSHER_SECRET')
    PUSHER_CLUSTER = os.environ.get('PUSHER_CLUSTER')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

class ProdConfig(Config):
    ENV = 'DEV'

class TestConfig(Config):
    ENV = 'DEV'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 

