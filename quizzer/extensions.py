# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
import pusher
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from quizzer.settings import Config

api = Api(prefix='/api/v1')
migrate = Migrate()
db = SQLAlchemy()

pusher_client = pusher.Pusher(
  app_id=Config.PUSHER_APP_ID,
  key=Config.PUSHER_KEY,
  secret=Config.PUSHER_SECRET,
  cluster=Config.PUSHER_CLUSTER,
  ssl=True
)






