import flask_wtf
from flask import Flask
from flask_migrate import Migrate
from app.blueprints.api import api_bp
from app.database import db
from app.database.database import init_db
from app.ext.background_services import celery, mail, make_celery
from app.ext.cache import cache
from app.ext.cors import cors
from app.ext.security import ExtendedRegisterForm, MyMailUtil, security, user_datastore
from app.ext.security import security
from app.ext.sentry import init_sentry


# App is behind one proxy that sets the -For and -Host headers.


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")
    init_db(app)
    Migrate(app, db)
    mail.init_app(app)
    cors.init_app(
        app,
        resources={
            r"/*": {
                "origins": [
                    "0.0.0.0",
                    "localhost",
                    "192.168.29.74",
                    "192.168.29.65",
                    "127.0.0.1",
                ]
            }
        },
    )
    # init_sentry(app)
    cache.init_app(app)
    # DebugToolbarExtension(app)
    flask_wtf.CSRFProtect(app)
    security.init_app(
        app,
        datastore=user_datastore,
        confirm_register_form=ExtendedRegisterForm,
        mail_util_cls=MyMailUtil,
    )
    # celery.conf.update(app.config)
    celery = make_celery(app)
    app.register_blueprint(api_bp)

    return app
