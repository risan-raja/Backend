from datetime import datetime
from flask import current_app
from coolname import generate_slug
from flask_restx import reqparse
from flask_restx.inputs import boolean, datetime_from_iso8601
from app.database.database import db_session
from app.models import TaskList, Task

# with current_app.app_context():
create_task_list_parser = reqparse.RequestParser()
create_task_list_parser.add_argument(
    name='name',
    default=generate_slug(3),
    required=True,
    type=str,
    location='json',
    help='Name of the Task List',
    case_sensitive=True,
    store_missing=True,
    trim=True,
    nullable=False
)
create_task_list_parser.add_argument(
    name='description',
    required=False,
    type=str,
    location='json',
    help='Description of the Task List',
    case_sensitive=False,
    store_missing=False,
    trim=True,
    nullable=True
)
create_task_list_parser.add_argument(
    name='updated_at',
    required=False,
    type=datetime_from_iso8601,
    location='json',
    help='Last Updated Time of the Task List',
    store_missing=False,
    nullable=True,
    default=datetime.utcnow()
)
create_task_list_parser.add_argument(
    name='list_order',
    required=True,
    type=int,
    location='json',
    help='Task List Index',
    store_missing=False,
    nullable=False,

)
create_task_parser = reqparse.RequestParser()
create_task_parser.add_argument(
    name='title',
    default=generate_slug(3),
    required=True,
    type=str,
    location='json',
    help='Title of the Task',
    case_sensitive=False,
    store_missing=True,
    trim=True,
    nullable=False
)
create_task_parser.add_argument(
    name='content',
    required=False,
    type=str,
    location='json',
    help='Content of the Task',
    case_sensitive=False,
    store_missing=False,
    trim=True,
    nullable=True
)
create_task_parser.add_argument(
    name='deadline',
    required=False,
    type=datetime_from_iso8601,
    location='json',
    help='Deadline of the Task',
    store_missing=False,
    nullable=True
)
create_task_parser.add_argument(
    name='completed',
    required=False,
    type=boolean,
    location='json',
    help='Completed status of the Task',
    store_missing=True,
    nullable=False
)
create_task_parser.add_argument(
    name='updated_at',
    required=False,
    type=datetime_from_iso8601,
    location='json',
    help='Last Date Modified of the Task',
    store_missing=False,
    nullable=True,
    default=datetime.utcnow()
)
create_task_parser.add_argument(
    name='order',
    required=True,
    type=int,
    location='json',
    help='Task Index',
    store_missing=False,
    nullable=False
)

edit_task_list_parser = create_task_list_parser.copy()
edit_task_list_parser.add_argument(
    name='id',
    required=True,
    type=str,
    location='json',
    help='ID of the Task List')

edit_task_parser = create_task_parser.copy()
edit_task_parser.add_argument(
    name='id',
    required=True,
    type=str,
    location='json',
    help='ID of the Task')

