from flask import Flask, g
import redis
from flask_session import Session
import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler = logging.StreamHandler()
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)
key = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "JWqNdK-NtLtsMZVNzJHEg530Fi36v6V7DUTCOUBFB1E"

    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')
    server_session = Session(app)

    from EIS.EISApp.child.routes import child
    from EIS.EISApp.main.routes import main

    app.register_blueprint(child)
    app.register_blueprint(main)
    logger.info("Inside create app")
    return app
