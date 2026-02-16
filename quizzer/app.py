# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, redirect, render_template, request, session, url_for

"""Register Flask blueprints."""
from flask_cors import CORS
from flask_sslify import SSLify
from werkzeug.middleware.proxy_fix import ProxyFix

from quizzer.api.resources import PollsAdminApi, PollsApi, VerseGameApi
from quizzer.extensions import api, db, migrate
from quizzer.public import public_views
from quizzer.settings import Config


def create_app(config_object=Config):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
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
    db.init_app(app)
    migrate.init_app(app, db)
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

