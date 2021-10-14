from flask import Flask

import os

from .api import user


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        print(f'Instance path = {app.instance_path}')
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add blueprints
    app.register_blueprint(user.bp)

    return app
