from flask import Blueprint, render_template, request
from .forms import SubmitForm as SubmitForm

app = Blueprint('main', __name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/write-schedule', methods=('GET', 'POST'))
def write_schedule():
    form = SubmitForm()
    if request.method == 'POST' and form.validate_on_submit():
        print("Aboba")
    return render_template('write-schedule.html')


def register_blueprint(app_blueprint):
    return None