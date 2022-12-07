from app import create_app

app = create_app()

app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=8080,
            threaded=True,
            load_dotenv=True)
