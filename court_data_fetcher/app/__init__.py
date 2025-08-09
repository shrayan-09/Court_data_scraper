from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev")

    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
