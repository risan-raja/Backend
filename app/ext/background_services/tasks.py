# # noinspection PyUnresolvedReferences
# from celery import shared_task
# # noinspection PyUnresolvedReferences
# from .celery_clients import *
# from app.models import *
# from app.database import db
# from coolname import generate_slug
#
#
# def hit():
#     print('hit')
#
#
# # @shared_task(name="create_task_lists")
# @celery.task(name="create_task_lists")
# def create_task_lists(user_id, N):
#     from flask import current_app
#     from app.models import TaskList
#     with current_app.app_context():
#         n_ts = []
#
#         for i in range(N):
#             task_list_name = generate_slug(3)
#             task_list_description = generate_slug(3)
#             ts = TaskList(name=task_list_name,
#                           description=task_list_description,
#                           user_id=user_id)
#             n_ts.append(ts)
#         db.session.add_all(n_ts)
#         db.session.commit()
#         return "done"
#
#
# @celery.task(name="add_this")
# def add(x, y):
#     return x + y
