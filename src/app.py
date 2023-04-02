import os

from app_config import app
from flask import Flask, render_template, request
from forms import SubmitScheduleForm
import schedule


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/write-schedule', methods=('GET', 'POST'))
def write_schedule():
    form = SubmitScheduleForm()
    if request.method == 'POST' and form.validate_on_submit():
        course_number = int(form.course_number.data)
        group_number = int(form.group_number.data)
        subgroup_number = int(form.subgroup_number.data)
        schedule.process(course_number, group_number, subgroup_number)
        os.remove('resources/token.json')
    return render_template('write-schedule.html', form=form)
