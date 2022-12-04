from app.database import GUID, db
from . import Base
import uuid
class Task(Base):
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    task_list_id = db.Column(db.Integer, db.ForeignKey('task_list.id'), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.title
