import uuid
from datetime import datetime

from flask import Blueprint
from flask_restx import Api, Resource
from flask_security import auth_token_required, current_user

from app.database import db
from app.database.database import db_session
from app.models import Task, TaskList
from .api_models import gen_api_models
from .api_reqparsers import create_task_list_parser, create_task_parser, edit_task_list_parser, edit_task_parser


# noinspection PyShadowingNames
def get_vac_list_order(current_user):
    list_order = db_session.query(TaskList).filter_by(user_id=current_user.id).count() + 1
    return list_order


authorizations = {
        'apikey': {
                'type': 'apiKey',
                'in':   'header',
                'name': 'Authentication-Token'
        }
}
api_bp = Blueprint('api', __name__, url_prefix='/api/kanban')
api = Api(api_bp, version='1.0', title='API', description='API', doc='/doc/', default_mediatype='application/json',
          authorizations=authorizations, security='apikey')
user_model, task_model, task_list_model = gen_api_models(api)


# TESTING TOKEN : "WyJjMTk0NTZlZmQ1MmY0YWFiYTE3ZWU0MDJlMTNjOGM4ZiJd.Y5GjKg.YjFL2O7sSl_0T4ox9N_fjobe2KI"
@api.route('/user')
class UserInfo(Resource):
    @auth_token_required
    @api.marshal_with(user_model)
    def get(self):
        user = current_user
        return user.__dict__


@api.route('/user/create_task_list')
class CreateTaskList(Resource):
    @auth_token_required
    @api.expect(create_task_list_parser)
    def post(self):
        """
        Create a new task list
        """
        user_id = current_user.id
        new_list_args = create_task_list_parser.parse_args()
        val = TaskList()
        val.name = new_list_args['name']
        val.description = new_list_args['description']
        val.created_at = datetime.now()
        val.updated_at = datetime.now()
        val.user_id = user_id
        val.list_order = get_vac_list_order(current_user)
        db.session.add(val)
        db.session.commit()
        return {'status': 'success'}, 201


@api.route('/user/<task_list_id>/create_task')
class CreateTask(Resource):
    """
    Create a new task
    """

    @auth_token_required
    @api.expect(create_task_parser)
    def post(self, task_list_id):
        new_task_args = create_task_parser.parse_args()
        task_list_id = uuid.UUID(task_list_id)
        user_id = current_user.id
        val = Task()
        val.title = new_task_args['title']
        val.description = new_task_args['description']
        val.created_at = datetime.now()
        val.updated_at = datetime.now()
        val.user_id = user_id
        val.task_list_id = task_list_id
        db.session.add(val)
        db.session.commit()
        return {'status': 'success'}, 201


@api.route('/user/task_lists')
class GetTaskLists(Resource):
    @auth_token_required
    @api.marshal_with(task_list_model)
    def get(self):
        user_id = current_user.id
        task_lists = current_user.task_lists
        return task_lists, 200


@api.route('/user/tasks')
class GetTasks(Resource):
    @auth_token_required
    @api.marshal_with(task_model)
    def get(self):
        user_id = current_user.id
        tasks = current_user.tasks
        return tasks, 200


@api.route('/user/task_lists')
class EditTaskLists(Resource):
    @auth_token_required
    @api.expect(edit_task_list_parser)
    def get(self):
        user_id = current_user.id
        args = edit_task_list_parser.parse_args()
        task_list_id = uuid.UUID(args['task_list_id'])
        task_list = TaskList.query.filter_by(id=task_list_id).first()
        task_list.name = args['name']
        task_list.description = args['description']
        task_list.updated_at = datetime.now()
        db.session.commit()
        return {'status': 'success'}, 201


@api.route('/user/tasks')
class EditTasks(Resource):
    @auth_token_required
    @api.expect(edit_task_parser)
    def get(self):
        user_id = current_user.id
        args = edit_task_parser.parse_args()
        task_id = uuid.UUID(args['task_id'])
        task = Task.query.filter_by(id=task_id).first()
        task.title = args['title']
        task.content = args['content']
        task.updated_at = datetime.now()
        task.completed = args['completed']
        task.deadline = args['deadline']
        db.session.commit()
        return {'status': 'success'}, 201
