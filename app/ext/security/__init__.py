from flask import current_app
from flask_mailman import EmailMultiAlternatives
from flask_security import MailUtil, RegisterForm
from flask_security import SQLAlchemyUserDatastore, Security
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

from app.database.database import db
from app.ext.background_services import celery
from app.models import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField(
        "First Name",
        [
            DataRequired(
                message="Invalid First Name : Please provide a valid First Name"
            )
        ],
    )
    last_name = StringField("Last Name", [Optional()])


@celery.task(name="security.send_email")
def send_flask_mail(**kwargs):
    with current_app.app_context():
        with current_app.extensions["mailman"].get_connection() as connection:
            html = kwargs.pop("html", None)
            msg = EmailMultiAlternatives(connection=connection, **kwargs)
            if html:
                msg.attach_alternative(html, "text/html")
            msg.send()


class MyMailUtil(MailUtil):
    def send_mail(
        self, template, subject, recipient, sender, body, html, user, **kwargs
    ):
        return send_flask_mail.apply_async(
            kwargs={
                "subject": subject,
                "from_email": sender,
                "to": [recipient],
                "body": body + "this is by celery",
                "html": html,
            }
        )


security = Security()
