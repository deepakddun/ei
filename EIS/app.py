from EIS.EISApp import create_app
from flask import session
import random

if __name__ == '__main__':
    app = create_app()

    app.run(debug=True,threaded=True)
