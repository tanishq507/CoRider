from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from app.config import Config
from app.routes import api_bp, main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    api = Api(app)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    api.register_blueprint(api_bp)
    
    return app