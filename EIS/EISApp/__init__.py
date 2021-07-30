from flask import Flask
from flask_redis import FlaskRedis

redis_client = FlaskRedis()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "JWqNdK-NtLtsMZVNzJHEg530Fi36v6V7DUTCOUBFB1E"

    from EIS.EISApp.child.routes import child
    from EIS.EISApp.main.routes import main

    app.register_blueprint(child)
    app.register_blueprint(main)

    REDIS_URL = "redis://localhost:6379/0"

    redis_client.init_app(app)

    return app
