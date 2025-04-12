# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
import pusher
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api(prefix='/api/v1')

db = SQLAlchemy()

pusher_client = pusher.Pusher(
  app_id='677956',
  key='c94fbf647eaf623c10ba',
  secret='0f879745e026ddfc0dbd',
  cluster='us2',
  ssl=True
)






