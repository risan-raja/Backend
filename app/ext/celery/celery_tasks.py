from flask_mailman import EmailMultiAlternatives
from flask import current_app
from . import celery


@celery.task(name='app.send_email')
def send_flask_mail(**kwargs):
    with current_app.app_context():
        with app.extensions['mailman'].get_connection() as connection:
            html = kwargs.pop("html", None)
            msg = EmailMultiAlternatives(**kwargs, connection=connection)
            if html:
                msg.attach_alternative(html, "text/html")
            msg.send()
