from flask import Flask
from app.config import Config  # Import configuration

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')  
    app.config.from_object(Config)  # Load configuration

    from app.routes import main  # Import Blueprint from routes.py
    app.register_blueprint(main)  # Register Blueprint

    return app
