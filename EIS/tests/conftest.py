from EIS.EISApp import create_app
import pytest
from flask_sqlalchemy import SQLAlchemy
import os
import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    DB_CONN = "mysql+mysqlconnector://d1105:Password123@localhost:3306/dev"
except KeyError:
    raise KeyError('TEST_DATABASE_URL not found. You must export a database ' +
                   'connection string to the environmental variable ' +
                   'TEST_DATABASE_URL in order to run tests.')
else:
    DB_OPTS = sa.engine.url.make_url(DB_CONN).translate_connect_args()

Session = sessionmaker()

@pytest.fixture(scope='session')
def connection(request):
    '''
    Create a Postgres database for the tests, and drop it when the tests are done.
    '''
    pg_host = DB_OPTS.get("host")
    pg_port = DB_OPTS.get("port")
    pg_user = DB_OPTS.get("username")
    pg_pass = DB_OPTS.get("password")
    pg_db = DB_OPTS["database"]
    print(pg_host, pg_port, pg_user, pg_pass, pg_db)

    engine = create_engine(DB_CONN)
    connection =  engine.connect()

    return connection


@pytest.fixture(scope='session')
def app(connection):
    """
    create flask application object

    """
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    return app


@pytest.fixture(scope='session')
def _db(app):
    '''
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    '''
    db = SQLAlchemy(app=app)
    return db



