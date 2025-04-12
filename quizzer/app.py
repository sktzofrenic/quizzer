# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template, session, url_for, redirect, request

"""Register Flask blueprints."""
from quizzer.public import public_views
from quizzer.extensions import api

from flask_sslify import SSLify
from flask_cors import CORS

from quizzer.settings import Config


def create_app(config_object=Config):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    CORS(app)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)

    if config_object.ENV == 'PROD':
        SSLify(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    api.init_app(app)
    return None

def register_commands(app):
    """Register Click commands."""

def register_blueprints(app):
    app.register_blueprint(public_views)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        print(error)
        error_code = getattr(error, 'code', 500)
        if error_code == 401:
            return redirect(url_for('auth.login'))
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

