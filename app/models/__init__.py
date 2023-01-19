from sqlalchemy import event
from sqlalchemy.orm import Session
# from celery import shared_task
from app.ext.background_services import celery
from sqlalchemy.util.langhelpers import symbol

# noinspection PyUnresolvedReferences
from app.database.base_model import BaseModel as Base
from .TaskListModel import TaskList
from .TaskModel import Task
from .UserModel import Role, User


# Session = sessionmaker()
#
# @event.listens_for(Base, "init", propagate=True, retval=True)
# def intercept_init(instance, args, kwargs):
#     pass
#     # print("new transient: %s" % instance)
#     # assert type(instance) is TaskList
#
#     # print(instance.__dict__)
#
#
# @event.listens_for(TaskList.list_order, "init_scalar", propagate=True, retval=True)
# def intercept_init(target, dict_, value):
#     print("initialization Hijacked")
#     print(target, dict_, value)
#     value = TaskList.get_total_task_lists(target.user_id) + 1
#     target.list_order = value
#     # dict_['list_order'] = value
#     # print("new transient: %s" % instance)
#     # assert type(instance) is TaskList
#     # print(instance.__dict__)
#     return value
#
#



@event.listens_for(TaskList.list_order, 'set', retval=False)
def receive_set(target, value, oldvalue, initiator):
    print("setting Hijacked")
    if oldvalue == symbol('NO_VALUE'):
        print("setting Hijacked")  # value = TaskList.get_total_task_lists(target.user_id) + 1  # return value


def hit():
    print("hit")


def get_list_order(user_id):
    return TaskList.get_total_task_lists(user_id) + 1


# @event.listens_for(TaskList, 'before_insert', retval=True)
# def receive_before_insert(mapper, connection, target):
#     """listen for the 'before_insert' event"""
#     val = get_list_order(target.user_id)
#     target.__dict__['list_order'] = val
#     return val


@event.listens_for(TaskList, 'before_insert', retval=True, )
def receive_before_insert(mapper, connection, target):
    """listen for the 'before_insert' event"""
    # hit()
    # val = None
    val = get_list_order(target.user_id)
    # print(target.user.task_lists)
    # print(val)
    # print("before_insert", mapper, connection, target)
    target.__dict__['list_order'] = val
    return val


@event.listens_for(Session, 'before_flush')
def receive_before_flush(session, flush_context, instances):
    "listen for the 'before_flush' event"
    # print("before_flush", session, flush_context, instances)
    pass
