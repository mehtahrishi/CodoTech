# app/__init__.py
import os
from flask import Flask

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, '..', 'templates'),
        static_folder=os.path.join(base_dir, '..', 'static')
    )
    from . import routes
    app.register_blueprint(routes.main_bp)
    return app
