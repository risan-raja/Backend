from flask import Flask, redirect, request
from flask import current_app, g
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.middleware.proxy_fix import ProxyFix
from app.ext.security import security
from app.database.database import init_db
from app.ext.cache import cache
from app.ext.cors import cors
from app.ext.background_services import celery, mail
from app.ext.sentry import init_sentry
import flask_wtf
from app.ext.security import security, user_datastore, ExtendedRegisterForm, MyMailUtil

# App is behind one proxy that sets the -For and -Host headers.


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")
    # ProxyFix(app,x_for=1,x_host=1,)
    init_db(app)
    mail.init_app(app)
    cors.init_app(app, resources={r'/*': {'origins': '*'}, r'/api/*': {'origins': '*'}})
    # init_sentry(app)
    cache.init_app(app)
    # DebugToolbarExtension(app)
    flask_wtf.CSRFProtect(app)
    security.init_app(app,
                      datastore=user_datastore,
                      confirm_register_form=ExtendedRegisterForm,
                      mail_util_cls=MyMailUtil)
    celery.conf.update(app.config)

    return app
