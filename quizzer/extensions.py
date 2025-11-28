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

# Initialize Pusher client only if credentials are available
if Config.PUSHER_APP_ID and Config.PUSHER_APP_ID != 'placeholder':
    pusher_client = pusher.Pusher(
        app_id=Config.PUSHER_APP_ID,
        key=Config.PUSHER_KEY,
        secret=Config.PUSHER_SECRET,
        cluster=Config.PUSHER_CLUSTER,
        ssl=True
    )
else:
    # Mock pusher client for local development
    class MockPusher:
        def trigger(self, *args, **kwargs):
            print(f"[MockPusher] trigger called with: {args}, {kwargs}")
    pusher_client = MockPusher()






