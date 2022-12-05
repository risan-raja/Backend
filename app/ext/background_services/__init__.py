from celery import Celery
from flask_mailman import Mail

from config import Config

mail = Mail()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL,
                backend=Config.CELERY_RESULT_BACKEND,
                )


@celery.task(name='add_this')
def add(x, y):
    return x + y
