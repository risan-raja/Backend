from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker

from app.database.base_query import BaseQuery
from config import Config
from .base_model import BaseModel as Base

db_engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI, echo=Config.SQLALCHEMY_ENGINE_ECHO
)
# create empty session for future usage
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False))

# user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
db = SQLAlchemy(
    session_options={"autocommit": False, "autoflush": False},
    model_class=Base,
    query_class=BaseQuery,
)


def init_db(app):
    # noinspection PyShadowingNames
    engine = create_engine(
        app.config.get("SQLALCHEMY_DATABASE_URI"),
        echo=app.config.get("SQLALCHEMY_ENGINE_ECHO"),
        # isolation_level=1
    )

    @event.listens_for(engine, "connect")
    def do_connect(dbapi_connection, connection_record):
        # disable pysqlite's emitting of the BEGIN statement entirely.
        # also stops it from emitting COMMIT before any DDL.
        dbapi_connection.isolation_level = None

    @event.listens_for(engine, "begin")
    def do_begin(conn):
        # emit our own BEGIN
        conn.exec_driver_sql("BEGIN EXCLUSIVE")

    db_session.configure(
        bind=engine,
        autocommit=app.config.get("SQLALCHEMY_AUTOCOMMIT"),
        autoflush=app.config.get("SQLALCHEMY_AUTOFLUSH"),
        query_cls=BaseQuery,
    )
    db.init_app(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    Base.metadata.create_all(bind=engine)


"""
gunicorn --worker-class gevent -w 9 pywsgi:app --bind 0.0.0.0:8000 --preload --reload &
"""
