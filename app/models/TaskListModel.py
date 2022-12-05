from app.database import GUID, db
from . import Base
import uuid


class TaskList(Base):
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='task_list', lazy=True)

    def __repr__(self):
        return '<List %r>' % self.name
