from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
import os.path


class Config:
    BASE_FIR = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = 'we4fh%gc_za:*8G5V=fbv'


app = Flask(__name__)
app.config.from_object(Config)
mod = Blueprint('app', __name__)
csrf = CSRFProtect(app)