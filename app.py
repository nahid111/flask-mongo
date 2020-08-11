import os
from dotenv import load_dotenv
from flask import Flask
from app_extensions import db
from controllers.parents import parents_module
from controllers.children import children_module

# load dotenv in the base root
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    if settings_override:
        app.config.update(settings_override)

    # Register Controller Blueprints
    app.register_blueprint(parents_module, url_prefix='/api/v1/parents')
    app.register_blueprint(children_module, url_prefix='/api/v1/children')

    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)

    return None

