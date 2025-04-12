# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_restful import Api
import pusher

api = Api(prefix='/api/v1')

pusher_client = pusher.Pusher(
  app_id='677956',
  key='c94fbf647eaf623c10ba',
  secret='0f879745e026ddfc0dbd',
  cluster='us2',
  ssl=True
)






