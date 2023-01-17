import flask_restx
from flask_restx import fields


def gen_api_models(api):
    """
    Generate API Models for Flask-RESTX
    :@param api: Flask-RESTX API
    :@return: User Model, Task Model, Task List Model, Resource Model
    """
    user_model = api.model(
        "User",
        {
            "email": fields.String(required=True, description="The user email address"),
            "last_login_at": fields.DateTime(
                required=True, description="The last login date"
            ),
            "login_count": fields.Integer(required=True, description="The login count"),
            "active": fields.Boolean(
                required=True, description="The user active status"
            ),
            "created_at": fields.DateTime(
                required=True, description="The user creation date"
            ),
            "last_login_ip": fields.String(
                required=True, description="The last login IP"
            ),
            "first_name": fields.String(
                required=True, description="The user first name"
            ),
            "last_name": fields.String(required=True, description="The user last name"),
            "current_login_at": fields.DateTime(
                required=True, description="The current login date"
            ),
            "current_login_ip": fields.String(
                required=True, description="The current login IP"
            ),
            "confirmed_at": fields.DateTime(
                required=True, description="The user confirmation date"
            ),
            "offline_db": fields.Boolean(
                required=True, description="The user offline database status"
            ),
        },
    )
    task_model = api.model(
        "Task",
        {
            "title": fields.String(required=True, description="The task title"),
            "order": fields.Integer(required=True, description="The task index"),
            "content": fields.String(required=True, description="The task content"),
            "deadline": fields.DateTime(required=True, description="The task deadline"),
            "completed": fields.Boolean(
                required=True, description="The task completed status"
            ),
            "created_at": fields.DateTime(
                required=True, description="The task creation date"
            ),
            "updated_at": fields.DateTime(
                required=True, description="The task update date"
            ),
            "task_list_id": fields.String(
                required=True, description="The task task list id"
            ),
            "id": fields.Integer(required=True, description="The task id"),
        },
    )
    task_list_model = api.model(
        "TaskList",
        {
            "id": fields.Integer(required=True, description="The task list id"),
            "name": fields.String(required=True, description="The task list name"),
            "description": fields.String(
                required=True, description="The task list description"
            ),
            "list_order": fields.Integer(
                required=True, description="The task list index"
            ),
            "created_at": fields.DateTime(
                required=True, description="The task list creation date"
            ),
            "updated_at": fields.DateTime(
                required=True, description="The task list update date"
            ),
            "tasks": fields.List(fields.Nested(task_model)),
        },
    )
    resource_fields = api.model(
        "Resource",
        {
            "name": fields.String,
        },
    )
    # task_list_task_model = api.model('TaskListTask', {'id': fields.String(required=True, description='The task id'),})

    return user_model, task_model, task_list_model, resource_fields
