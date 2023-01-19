#!/usr/bin/env python
# from gevent import monkey
# monkey.patch_all()
import warnings
warnings.filterwarnings("ignore")
from app import create_app

app = create_app()
app.app_context().push()

# noinspection PyUnresolvedReferences
from app import celery
