import uuid
from datetime import datetime

from pytz import timezone
from sqlalchemy.ext.orderinglist import ordering_list
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import declarative_base, relationship
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import synonym

from app.database import GUID, db
from . import Base

tz = timezone('Asia/Kolkata')


class TaskList(Base):
    @classmethod
    def get_total_task_lists(cls, user_id):
        return cls.query.filter_by(user_id=user_id).count()

    @property
    def total_tasks(self):
        return self.tasks.count()

    # id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='task_lists')
    tasks = db.relationship(
        'Task',
        back_populates='task_list',
        cascade='all,delete-orphan',
        order_by='Task.order',
        collection_class=ordering_list('order', count_from=0),
        lazy="selectin"
    )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    list_order = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<List %r>' % self.name
