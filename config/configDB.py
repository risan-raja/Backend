from dataclasses import dataclass
import os

DB_PATH = os.getcwd().replace("/config", "") + "/instance/db.sqlite3"


@dataclass
class configDB(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_AUTOCOMMIT = False
    SQLALCHEMY_AUTOFLUSH = False
    SQLALCHEMY_ENGINE_ECHO = True
    
