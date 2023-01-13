import uuid
# from datetime import datetime
from datetime import datetime
from datetime import timedelta

from app.database import GUID, db
from . import Base


class Task(Base):
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    title = db.Column(db.Text, unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=True)
    deadline = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow() + timedelta(days=1)
    )
    completed = db.Column(db.Boolean, nullable=False, default=False)
    task_list_id = db.Column(GUID,
                             db.ForeignKey('task_list.id'),
                             nullable=True)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.utcnow())
    updated_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.utcnow())
    user_id = db.Column(GUID, db.ForeignKey('user.id'), nullable=True)
    order = db.Column(db.Integer, nullable=True)
    user = db.relationship('User', back_populates='tasks')
    task_list = db.relationship('TaskList', back_populates='tasks')

    def __repr__(self):
        return '<Task %r>' % self.title
