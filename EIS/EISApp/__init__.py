from flask import Flask

def create_app():

    app = Flask(__name__)
    app.secret_key = "JWqNdK-NtLtsMZVNzJHEg530Fi36v6V7DUTCOUBFB1E"

    from EIS.EISApp.child.routes import child

    app.register_blueprint(child)

    return app

