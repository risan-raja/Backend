import uuid
from datetime import datetime
from gevent import monkey
monkey.patch_all()
from flask import Blueprint, jsonify
from flask import current_app
from flask import request
from flask_restx import Api, Resource
from flask_security import auth_token_required, current_user, logout_user

from app.database import db
from app.ext.cache import cache
from app.models import Task, TaskList
from .api_models import gen_api_models
from .api_reqparsers import ApiReqParsers


def convert_string_to_datetime(date):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")


authorizations = {
        "apikey": {"type": "apiKey", "in": "header", "name": "Authentication-Token"}
}
api_bp = Blueprint("api", __name__, url_prefix="/api/kanban")
api = Api(
    api_bp,
    version="1.0",
    title="API",
    description="API",
    doc="/doc/",
    default_mediatype="application/json",
    authorizations=authorizations,
    security="apikey",
)
user_model, task_model, task_list_model, resource_model = gen_api_models(api)


# noinspection PyMethodMayBeStatic
@api.route("/user/logout")
class UserLogout(Resource):
    def get(self):
        logout_user()
        return "Logged out"

    def post(self):
        logout_user()
        return "Logged out"


@api.route("/user")
class UserInfo(Resource):
    @auth_token_required
    @api.marshal_with(user_model)
    def get(self):
        user = current_user
        return user.__dict__


req_parsers = ApiReqParsers()


@api.route("/user/task_lists")
class TaskListApi(Resource):

    @auth_token_required
    @api.expect(req_parsers.create_task_list_parser)
    def post(self):
        """
        Create a new task list
        """
        new_task_list = req_parsers.create_task_list_parser.parse_args()
        user_id = current_user.id
        val = TaskList()
        val.name = new_task_list["name"]
        val.description = new_task_list["description"]
        val.created_at = datetime.utcnow()
        val.updated_at = new_task_list["updated_at"]
        val.user_id = user_id
        val.list_order = new_task_list["list_order"]
        db.session.add(val)
        db.session.commit()
        return {"status": "success"}, 201

    @auth_token_required
    @api.marshal_with(task_list_model)
    def get(self):
        user_id = current_user.id
        task_lists = current_user.task_lists
        return task_lists, 200

    @auth_token_required
    @api.expect(req_parsers.edit_task_list_parser)
    def put(self):
        user_id = current_user.id
        args = req_parsers.edit_task_list_parser.parse_args()
        task_list_id = args["task_list_id"]
        # task_list = TaskList.query.filter_by(id=task_list_id).first()
        task_list = TaskList.query.get(task_list_id)
        task_list.name = args["name"]
        task_list.description = args["description"]
        task_list.order = args["list_order"]
        task_list.updated_at = datetime.now()
        db.session.commit()
        return {"status": "success"}, 201

    @auth_token_required
    @api.expect(req_parsers.delete_task_list_parser)
    def delete(self, task_list_id):
        user_id = current_user.id
        args = req_parsers.delete_task_list_parser.parse_args()
        task_list_id = task_list_id
        task_list = TaskList.query.get(task_list_id)
        if args["delete_with_transfer"]:
            transfer_to = args["transfer_to"]
            transfer_list = TaskList.query.filter_by(id=transfer_to).first()
            tasks = task_list.tasks
            for task in tasks:
                transfer_list.tasks.append(task)
            db.session.commit()
        db.session.delete(task_list)
        db.session.commit()
        return {"status": "success"}, 204


def get_task(task_id):
    with current_app.app_context():
        t = Task.query.get(task_id)
    return t


from .dfs import DATA


@api.route("/user/tasks/<task_id>")
class GTask(Resource):
    # @auth_token_required
    # @api.marshal_with(task_model)
    # @cache.cached(timeout=1)
    # @auth_token_required
    def get(self, task_id: str):
        task_id = task_id
        e = Task.query.all()
        t = TaskList.query.all()
        return "Task.query.get(task_id)"
        # return get_task(task_id)


@api.route("/user/tasks")
class TaskApi(Resource):

    @auth_token_required
    @api.expect(req_parsers.create_task_parser)
    def post(self, task_list_id):
        new_task_args = req_parsers.create_task_parser.parse_args()
        task_list_id = task_list_id
        user_id = current_user.id
        val = Task()
        val.title = new_task_args["title"]
        val.description = new_task_args["description"]
        val.created_at = datetime.now()
        val.updated_at = datetime.now()
        val.user_id = user_id
        val.task_list_id = task_list_id
        val.order = new_task_args["order"]
        db.session.add(val)
        db.session.commit()
        return {"status": "success"}, 201

    @auth_token_required
    @api.marshal_with(task_model)
    def get(self):
        user_id = current_user.id
        tasks = current_user.tasks
        return tasks, 200

    @auth_token_required
    @api.expect(req_parsers.delete_task_parser)
    def delete(self):
        """
        Delete a task
        """
        user_id = current_user.id
        delete_task_args = req_parsers.delete_task_parser.parse_args()
        task_id = delete_task_args["id"]
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return {"status": "success"}, 204

    @auth_token_required
    @api.expect(req_parsers.edit_task_parser)
    def put(self):
        user_id = current_user.id
        args = req_parsers.edit_task_parser.parse_args()
        task_id = args["id"]
        task = Task.query.get(task_id)
        task.updated_at = datetime.now()
        edited_fields = request.get_json()
        try:
            edited_fields.pop("id")
        except KeyError:
            return {"status": "error", "message": "No id provided"}, 400
        for key in edited_fields:
            if key == "deadline":
                # task[key] = convert_string_to_datetime(edited_fields[key])
                setattr(task, key, convert_string_to_datetime(edited_fields[key]))
            else:
                # task[key] = edited_fields[key]
                setattr(task, key, edited_fields[key])
        db.session.commit()
        return {"status": "success"}, 201


@api.route("/user/sync")
class UpdateUser(Resource):
    @staticmethod
    def update_user(payload):
        for task_list in payload["task_lists"]:
            task_list_db = TaskList.query.get(id=task_list["id"])
            for task in task_list["tasks"]:
                task_db = Task.query.get(id=task["id"])
                task_db.completed = task["completed"]
                task_db.deadline = convert_string_to_datetime(task["deadline"])
                task_db.title = task["title"]
                task_db.content = task["content"]
                task_db.updated_at = task["updated_at"]
                task_db.order = task["order"]
                db.session.commit()
            task_list_db.name = task_list["name"]
            task_list_db.description = task_list["description"]
            task_list_db.list_order = task_list["list_order"]
            task_list_db.updated_at = task_list["updated_at"]

    # noinspection PyBroadException
    @auth_token_required
    def post(self):
        user_db = request.get_json()
        try:
            self.update_user(payload=user_db)
        # noinspection PyBroadException
        except:
            return {"status": "error", "message": "Error updating user"}, 400
        return {"status": "success"}, 201
