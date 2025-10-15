from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "football"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("database_url")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app=app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    
    return app
