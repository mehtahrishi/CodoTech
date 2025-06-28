from flask import Flask
import os

def create_app():
    """Create a minimal Flask application."""
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "static")
    )

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main_bp)

    return app
