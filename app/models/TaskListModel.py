from app.database import GUID, db
from . import Base
import uuid
from datetime import datetime
from pytz import timezone

tz = timezone('Asia/Kolkata')


class TaskList(Base):
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=True)
    user_id = db.Column(GUID, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='task_list', cascade='all,delete', lazy=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    list_order = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<List %r>' % self.name

