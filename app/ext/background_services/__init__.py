from celery import Celery
from flask_mailman import Mail

from config import Config

mail = Mail()
celery = Celery(
    __name__, broker=Config.CELERY_CONFIG['broker_url'], backend=Config.CELERY_CONFIG['result_backend']
)


@celery.task(name="add_this")
def add(x, y):
    return x + y
