# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from quizzer.app import create_app
from quizzer.settings import Config, ProdConfig

CONFIG = Config if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

