from flask import Flask

def create_app():
    """Create the Flask application with custom template/static paths."""
    app = Flask(
        __name__,
        template_folder="app/templates",   # 🔥 Tell Flask where to find index.html
        static_folder="app/static"         # (if you're using CSS/JS/images)
    )

    from . import routes
    app.register_blueprint(routes.main_bp)

    return app
