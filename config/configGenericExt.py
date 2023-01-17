from dataclasses import dataclass

REDIS_URL = "redis://default:passme@localhost:6379/5"


@dataclass
class FlaskExtConfig(object):
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://default:passme@localhost:6379/1"
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_KEY_PREFIX = "FCACHE_"

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
