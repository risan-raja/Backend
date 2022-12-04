from flask import Flask, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.middleware.proxy_fix import ProxyFix
from app.ext.security import security
from app.database.database import init_db
from app.ext.cache import cache
from app.ext.celery import celery
from app.ext.sentry import init_sentry
import flask_wtf
from app.ext.security import security, user_datastore, ExtendedRegisterForm, MyMailUtil

# App is behind one proxy that sets the -For and -Host headers.


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")
    ProxyFix(app, x_for=1, x_host=1)
    init_db(app)
    init_sentry(app)
    cache.init_app(app)
    DebugToolbarExtension(app)
    celery.conf.update(app.config)
    flask_wtf.CSRFProtect(app)
    security.init_app(app,
                      datastore=user_datastore,
                      register_form=ExtendedRegisterForm,
                      mail_util=MyMailUtil)

    @app.before_request
    def app_before_request():
        request_path = request.path

        # redirect: example.com/url/ -> example.com/url
        if request_path != "/" and request_path.endswith("/"):
            return redirect(request_path[:-1], 301)

    return app
