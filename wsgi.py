from gevent import monkey

monkey.patch_all()


from app import create_app
import warnings

warnings.filterwarnings("ignore")

app = create_app()

app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, threaded=True, load_dotenv=True)
