import warnings
#
warnings.filterwarnings("ignore")


from coolname import generate_slug
from app import create_app
from app.database import db
from app.models import *
app = create_app()
app.app_context().push()

u = User.query.all()[0]
for e in range(10):
    ts = TaskList(name=generate_slug(2), description=generate_slug(2), user_id=u.id)

    # print("Current TaskList.list_order : ", ts.list_order)
    db.session.add(ts)
    print(TaskList.get_total_task_lists(u.id))
    # db.session.commit()
