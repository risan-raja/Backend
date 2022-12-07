from flask import Blueprint
from flask_restx import Api, Resource
from flask_restx import fields
from flask_security import auth_token_required, current_user, login_required
from app.models import TaskList, Task

"""
## USER DATA MODEL
data = {'email':                                      'op3ntrap@gmail.com',
        'last_login_at':                              datetime.datetime(2022, 12, 7, 14, 33, 31, 832489),
        'login_count':                                14,
        'active':                                     True,
        'created_at':                                 datetime.datetime(2022, 12, 7, 11, 28, 3, 991610),
        'last_login_ip':                              '127.0.0.1',
        'first_name':                                 'Risan',
        'last_name':                                  'Raja',
        'current_login_at':                           datetime.datetime(2022, 12, 7, 15, 55, 22, 803025),
        'current_login_ip':                           '127.0.0.1',
        'confirmed_at':                               datetime.datetime(2022, 12, 7, 11, 28, 21, 78423), 
        }
"""

api_bp = Blueprint('api', __name__, url_prefix='/api/kanban')
api = Api(api_bp, version='1.0', title='API', description='API', doc='/doc/')

user_model = api.model('User', {
        'email':            fields.String(required=True, description='The user email address'),
        'last_login_at':    fields.DateTime(required=True, description='The last login date'),
        'login_count':      fields.Integer(required=True, description='The login count'),
        'active':           fields.Boolean(required=True, description='The user active status'),
        'created_at':       fields.DateTime(required=True, description='The user creation date'),
        'last_login_ip':    fields.String(required=True, description='The last login IP'),
        'first_name':       fields.String(required=True, description='The user first name'),
        'last_name':        fields.String(required=True, description='The user last name'),
        'current_login_at': fields.DateTime(required=True, description='The current login date'),
        'current_login_ip': fields.String(required=True, description='The current login IP'),
        'confirmed_at':     fields.DateTime(required=True, description='The user confirmation date'),
})
task_list_model = api.model('TaskList', {
        'title':      fields.String(required=True, description='The task list title'),
        'created_at': fields.DateTime(required=True, description='The task list creation date'),
        'updated_at': fields.DateTime(required=True, description='The task list update date'),
        'description':  fields.String(required=True, description='The task list description'),
})
task_model = api.model('Task', {
        'title':        fields.String(required=True, description='The task title'),
        'content':      fields.String(required=True, description='The task content'),
        'deadline':     fields.DateTime(required=True, description='The task deadline'),
        'completed':    fields.Boolean(required=True, description='The task completed status'),
        'created_at':   fields.DateTime(required=True, description='The task creation date'),
        'updated_at':   fields.DateTime(required=True, description='The task update date'),
        'task_list_id': fields.Integer(required=True, description='The task task list id'),
})


@api.route('/user')
class UserInfo(Resource):
    @login_required
    @auth_token_required
    @api.marshal_with(user_model)
    def post(self):
        user = current_user
        return user.__dict__


@api.route('/create_task_list')
class TaskList(Resource):
    @api.expect(task_list_model)
    @login_required
    def get(self):
        """
        Create a new task list
        """
        user_id = current_user.id
        new_list = TaskList(
            name=api.payload['title'],
            description=api.payload['description'],
            user_id=user_id
        )



def create_task():
    pass
