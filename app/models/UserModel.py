from datetime import datetime

from flask_security import RoleMixin, UserMixin
import uuid
from app.database import GUID, db
from . import Base


class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))


class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(db.String(255))


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role',
                            secondary='roles_users',
                            backref=db.backref('user', lazy='dynamic'))
    task_lists = db.relationship('TaskList', backref='user', lazy=True)
    tasks = db.relationship('Task', backref='user', lazy=True)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.utcnow)
    current_login_ip = db.Column(db.String(100))
    last_login_ip = db.Column(db.String(100))
    confirmed_at = db.Column(db.DateTime())

    # dob = db.Column(db.DateTime, nullable=True)

    def get_security_payload(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'active': self.active,
            'confirmed_at': self.confirmed_at,
        }
