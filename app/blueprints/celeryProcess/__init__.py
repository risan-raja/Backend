from flask import Blueprint, current_app
from app.ext.celery import celery

celeryTasks = Blueprint('celeryTasks', __name__)

"""
Celery Tasks
"""


@celery.task
def create_user(args, pnorm):
    """
    Create a user with the given arguments.
    param args: first_name, last_name, email, username
    :type args: Dict[str, str]
    :param pnorm: password
    :type pnorm: str
    """
    with current_app.app_context():
        user_datastore.create_user(
            first_name=args['first_name'],
            last_name=args['last_name'],
            email=args['email'],
            password=hash_password(pnorm))
        user_datastore.commit()


@celery.task(name='app.send_email')
def send_flask_mail(**kwargs):
    with current_app.app_context():
        with app.extensions['mailman'].get_connection() as connection:
            html = kwargs.pop("html", None)
            msg = EmailMultiAlternatives(**kwargs, connection=connection)
            if html:
                msg.attach_alternative(html, "text/html")
            msg.send()


@celery.task
def test_celery():
    """
    Test Celery
    """

    with current_app.app_context():
        msg = EmailMessage('Hello',
                           'Body goes here',
                           'risan.raja@outlook.com',
                           ['op3ntrap@gmail.com'], )
        # app.extensions['mailman'].send(msg)
        msg.send()
    print("Celery is working")
