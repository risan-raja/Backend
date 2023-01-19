from celery import Celery
from .celery_clients import *
from .tasks import *
from flask_mailman import Mail

from config import Config

mail = Mail()



