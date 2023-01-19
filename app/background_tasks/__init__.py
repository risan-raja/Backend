# noinspection PyUnresolvedReferences
from gevent import monkey

monkey.patch_all()

from .tasks import celery
