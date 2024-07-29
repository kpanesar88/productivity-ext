# backend/app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    # app._static_folder = '/ProductivityExtension/Backend/app/static'
    
    # Register blueprints (if any)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
