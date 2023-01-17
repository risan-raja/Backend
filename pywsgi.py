# ./flask_app/pywsgi.py
from gevent import monkey

monkey.patch_all()

from wsgi import app

app.app_context().push()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, threaded=True, load_dotenv=True)


# gunicorn --worker-class gevent 9 --threads 2 wsgi:app --bind 0.0.0.0:8000 --preload --reload &
