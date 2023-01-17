reload = False
preload = True

workers = 12
worker_class = 'gevent'
worker_connections = 1000
timeout = 30
keepalive = 2
bind = '0.0.0.0:8000'
backlog = 2048
loglevel = 'error'
wsgi_app = 'pywsgi:app'
