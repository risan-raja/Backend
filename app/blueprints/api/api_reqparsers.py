from datetime import datetime

from coolname import generate_slug
from flask_restx import reqparse
from flask_restx.inputs import boolean, datetime_from_iso8601

from app.database.database import db_session
from app.models import TaskList


# session = db_session()
def get_vac_list_order(user):
    return db_session.query(TaskList).filter_by(user_id=user.id).count() + 1


# noinspection DuplicatedCode
class ApiReqParsers(object):
    @property
    def create_task_list_parser(self):
        _create_task_list_parser = reqparse.RequestParser()
        _create_task_list_parser.add_argument(
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
        _create_task_list_parser.add_argument(
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
        _create_task_list_parser.add_argument(
            name='updated_at',
            required=False,
            type=datetime_from_iso8601,
            location='json',
            help='Last Updated Time of the Task List',
            store_missing=True,
            nullable=True,
            default=datetime.utcnow()
        )
        _create_task_list_parser.add_argument(
            name='list_order',
            required=False,
            type=int,
            location='json',
            help='Task List Index',
            store_missing=False,
            nullable=True,
        )
        return _create_task_list_parser

    @property
    def create_task_parser(self):
        _create_task_parser = reqparse.RequestParser()
        _create_task_parser.add_argument(
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
        _create_task_parser.add_argument(
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
        _create_task_parser.add_argument(
            name='deadline',
            required=False,
            type=datetime_from_iso8601,
            location='json',
            help='Deadline of the Task',
            store_missing=False,
            nullable=True
        )
        _create_task_parser.add_argument(
            name='completed',
            required=False,
            type=boolean,
            location='json',
            help='Completed status of the Task',
            store_missing=True,
            nullable=False,
            default=False
        )
        _create_task_parser.add_argument(
            name='updated_at',
            required=False,
            type=datetime_from_iso8601,
            location='json',
            help='Last Date Modified of the Task',
            store_missing=False,
            nullable=True,
            default=datetime.utcnow()
        )
        _create_task_parser.add_argument(
            name='order',
            required=False,
            type=int,
            location='json',
            help='Task Index',
            store_missing=False,
            nullable=False,
        )
        return _create_task_parser

    @property
    def edit_task_list_parser(self):
        _edit_task_list_parser = self.create_task_list_parser.copy()
        _edit_task_list_parser.add_argument(
            name='id',
            required=True,
            type=int,
            location='json',
            help='ID of the Task List')
        _edit_task_list_parser.replace_argument(
            name='name',
            required=False,
            type=str,
            location='json',
            help='Name of the Task List',
        )
        return _edit_task_list_parser

    @property
    def edit_task_parser(self):
        _edit_task_parser = self.create_task_parser.copy()
        _edit_task_parser.add_argument(
            name='id',
            required=True,
            type=int,
            location='json',
            help='ID of the Task')
        _edit_task_parser.replace_argument('order', required=False, location='json')
        _edit_task_parser.replace_argument('title', required=False, location='json')
        return _edit_task_parser

    @property
    def delete_task_parser(self):
        _delete_task_parser = reqparse.RequestParser()
        _delete_task_parser.add_argument(
            name='id',
            required=True,
            type=int,
            location='json',
            help='ID of the Task')
        return _delete_task_parser

    @property
    def delete_task_list_parser(self):
        _delete_task_list_parser = reqparse.RequestParser()
        _delete_task_list_parser.add_argument(
            name='id',
            required=True,
            type=int,
            location='json',
            help='ID of the Task List')
        _delete_task_list_parser.add_argument("delete_with_transfer", type=bool, required=True,
                                              location='json',
                                              help="Delete task")
        _delete_task_list_parser.add_argument("transfer_to", type=str, required=False,
                                              location='json',
                                              help="Transfer task to another list")
        return _delete_task_list_parser
