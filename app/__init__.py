from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "football"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cool_user:1234@localhost:5432/cool_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app=app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    
    return app
