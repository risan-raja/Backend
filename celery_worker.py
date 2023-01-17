#!/usr/bin/env python
from app import create_app

app = create_app()
app.app_context().push()

# noinspection PyUnresolvedReferences
from app import celery

