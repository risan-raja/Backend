import warnings
from celery import shared_task
from conda_env.cli.main_list import description

warnings.filterwarnings("ignore")

from tests import profiled
from coolname import generate_slug
from app import create_app
from app.models import *
from app.background_tasks.tasks import create_task_lists

app = create_app()
app.app_context().push()
# with profiled():
# u = User.query.all()[0]
new_ts = []
# for e in range(10):
#     ts = TaskList(name=generate_slug(2), description=generate_slug(2), user_id=u.id)
#     new_ts.append(ts)
#     # db.session.add(ts)
#     # print(TaskList.get_total_task_lists(u.id))
# db.session.add_all(new_ts)
# db.session.commit()
# for i in range(100):
# e = add.apply_async(args=(2, 2), ignore_result=True)
# print(u.id)
for i in range(10):
    exec_kwargs = {'user_id': 1, 'N': 100}
    e = create_task_lists.apply_async(kwargs=exec_kwargs, ignore_result=True)
