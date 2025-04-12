import os
from dotenv import load_dotenv

load_dotenv(override=True)
print('Loading environment variables from .env file')


class Config(object):
    ENV = 'DEV'
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    SECRET_KEY = '2[U}n*asUv)_xa%6f)aEKW`w,C9Fha69L'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://usr_ff1c8f2e:pw_179d425cac6a443c93a8ea96a958c92b@localhost:5432/db_cdb416a2'


class ProdConfig(Config):
    ENV = 'DEV'

class TestConfig(Config):
    ENV = 'DEV'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 

