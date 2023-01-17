# https://flask.palletsprojects.com/en/2.1.x/config/#builtin-configuration-values
class DevelopmentConfig(object):
    DEBUG = True
    IS_PRODUCTION = False
    SERVER_NAME = "127.0.0.1:8000"
    PREFERRED_URL_SCHEME = "http"
    DEBUG_TB_ENABLED = True
    TEMPLATES_AUTO_RELOAD = True
