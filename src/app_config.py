from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import os.path


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SECRET_KEY = 'we4fh%gc_za:*8G5V=fbv'
    UPLOAD_DIR = './upload'
    ALLOWED_EXTENSIONS = {'xls'}
    MAX_WEIGHT = 1000


app = Flask(__name__)
app.config["SQLALCHEMY_ECHO"] = True
app.config.from_object(Config())
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_DIR
app.config['MAX_CONTENT_PATH'] = Config.MAX_WEIGHT
mod = Blueprint('app', __name__)
db = SQLAlchemy(app=app, session_options={'autoflush': False})
csrf = CSRFProtect(app)
