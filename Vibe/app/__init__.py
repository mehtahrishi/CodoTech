from flask import Flask

def create_app():
    """Create a minimal Flask application."""
    app = Flask(__name__)

    # No database or complex config needed anymore
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main_bp)

    return app