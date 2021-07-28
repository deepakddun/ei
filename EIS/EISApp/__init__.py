from flask import Flask


def create_app():
    app = Flask(__name__,template_folder="templates")
    app.secret_key = "JWqNdK-NtLtsMZVNzJHEg530Fi36v6V7DUTCOUBFB1E"

    from EIS.EISApp.child.routes import child
    from EIS.EISApp.main.routes import main

    app.register_blueprint(child)
    app.register_blueprint(main)

    return app
