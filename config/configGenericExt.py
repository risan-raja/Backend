from dataclasses import dataclass
from zxcvbn import zxcvbn
from flask_security.utils import uia_email_mapper

REDIS_URL = "redis://opla:ZnnfZ6EssaXW7Yq$@redis-19917.c240.us-east-1-3.ec2.cloud.redislabs.com:19917"


@dataclass
class FlaskExtConfig(object):
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://opla:ZnnfZ6EssaXW7Yq$@redis-19917.c240.us-east-1-3.ec2.cloud.redislabs.com:19917/0"
    CACHE_DEFAULT_TIMEOUT = 300
    SENTRY_DSN = "https://6c78492f0dbe4db4b230b93949916cdd@o4504245195898880.ingest.sentry.io/4504245201469443"

    CELERY_CONFIG = {
            "broker_url":     REDIS_URL,
            "result_backend": REDIS_URL,
    }
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

    accept_content = ["json"]
    task_serializer = "json"
    result_serializer = "json"

    MAIL_SERVER = "smtp-mail.outlook.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "risan.raja@outlook.com"
    MAIL_PASSWORD = ":R?#5r5ZyCy7B)C"
    MAIL_DEFAULT_SENDER = "risan.raja@outlook.com"

    CORS_ALLOW_HEADERS = "*"
    CORS_ALWAYS_SEND = True
    CORS_AUTOMATIC_OPTIONS = True
    CORS_EXPOSE_HEADERS = None
    CORS_INTERCEPT_EXCEPTIONS = True
    CORS_MAX_AGE = None
    CORS_METHODS = ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"]
    CORS_ORIGINS = "*"
    CORS_RESOURCES = r"/*"
    CORS_SEND_WILDCARD = False
    CORS_SUPPORTS_CREDENTIALS = False
    CORS_VARY_HEADER = True
