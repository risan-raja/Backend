from app import create_app

app = create_app()

app.app_context().push()


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(load_dotenv=True)
