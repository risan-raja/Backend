from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from .base_model import BaseModel as Base
from app.database.base_query import BaseQuery
from config import Config


db_engine = create_engine(
        Config.SQLALCHEMY_DATABASE_URI,
        echo=Config.SQLALCHEMY_ENGINE_ECHO
    )
# create empty session for future usage
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False))

# user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
db = SQLAlchemy(session_options={"autocommit": True,"autoflush": False},
                model_class=Base,
                query_class=BaseQuery,)


def init_db(app):
    # noinspection PyShadowingNames
    engine = create_engine(
        app.config.get("SQLALCHEMY_DATABASE_URI"),
        echo=app.config.get("SQLALCHEMY_ENGINE_ECHO")
    )

    db_session.configure(
        bind=engine,
        autocommit=app.config.get("SQLALCHEMY_AUTOCOMMIT"),
        autoflush=app.config.get("SQLALCHEMY_AUTOFLUSH"),
        query_cls=BaseQuery
    )
    db.init_app(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    import app.models

    Base.metadata.create_all(bind=engine)

