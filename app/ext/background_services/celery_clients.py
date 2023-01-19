from celery import Celery
from config import Config


celery = Celery(
    __name__, broker=Config.CELERY_CONFIG['broker_url'], backend=Config.CELERY_CONFIG['result_backend']
)


def make_celery(app):
    global celery
    celery = Celery(app.import_name)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    # noinspection PyPropertyAccess
    celery.Task = ContextTask
    return celery

