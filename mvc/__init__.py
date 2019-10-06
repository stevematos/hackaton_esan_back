from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
# import extensions
from mvc.config import DATABASES_CONFIG
import argparse


from os import environ

blueprints = None
db = None
ma = None


def init_blueprints(app):
    for bp in blueprints:
        app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extract', help='fuente de extraccion', required=True)

    args = parser.parse_args()

    config_extract = args.extract

    config_database = None

    if config_extract:
        config_database = DATABASES_CONFIG[config_extract]

    app.config.from_object(config_database)
    global db, ma, blueprints
    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    from mvc.controllers import tablero

    blueprints = (tablero,)
    init_blueprints(app)
    cors=CORS(app, resources={r"*": {"origins": "*"}})
    return app
    # init_extensions(app)
    # init_other(app)

# def init_extensions(app):
#    pass

# def init_other(app):
#     pass
