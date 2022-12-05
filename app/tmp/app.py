from flask import Flask, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.middleware.proxy_fix import ProxyFix

from app.database.database import init_db
from app.ext.cache import cache
from app.ext.background_services import celery
from app.ext.sentry import init_sentry


# App is behind one proxy that sets the -For and -Host headers.


def init_configuration(app):
    """
    Load the default configuration
    """
    app.config.from_object("config.Config")


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    init_configuration(app)
    app.config.from_object("config.Config")

    ProxyFix(app, x_for=1, x_host=1)

    init_db(app)
    init_sentry(app)

    cache.init_app(app)
    DebugToolbarExtension(app)

    @app.before_request
    def app_before_request():
        request_path = request.path

        # redirect: example.com/url/ -> example.com/url
        if request_path != "/" and request_path.endswith("/"):
            return redirect(request_path[:-1], 301)

    celery.conf.update(app.config)
    return app
