from dataclasses import dataclass
# TODO - remove development config

@dataclass
class AppBaseConfig(object):
    DEBUG = True
    IS_PRODUCTION = False
    JSON_SORT_KEYS = False
    FLASK_STRICT_SLASHES = False
    PREFERRED_URL_SCHEME = "http"
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = "65f639cff0ba3b459a800d6deaed666d56f7489697b275dded8ac5f83cf1e42d"
    



