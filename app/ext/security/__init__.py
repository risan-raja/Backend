from flask_security import SQLAlchemyUserDatastore, Security
from flask_security import UserDatastore, MailUtil,RegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

from app.database.database import db_session
from app.ext.celery.celery_tasks import send_flask_mail
from app.models import Role, User
from app.database import db

class MyMailUtil(MailUtil):
    def send_mail(self, template, subject, recipient, sender, body, html, user, **kwargs):
        send_flask_mail.delay(
            subject=subject,
            from_email=sender,
            to=[recipient],
            body=body,
            html=html,
        )


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [Optional()])


security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
