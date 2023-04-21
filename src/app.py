import os
import re

from werkzeug.utils import secure_filename
from app_config import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SubmitScheduleForm, AdminForm, AdminSettingsForm
from model import *
import schedule


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/admin', methods=('GET', 'POST'))
def admin():
    form = AdminForm()
    login_db = db.session.query(Admin).first().login
    pass_db = db.session.query(Admin).first().password
    if request.method == 'POST' and form.validate_on_submit():
        login = form.login_field.data
        password = form.pass_field.data

        if login == login_db and pass_db == password:
            return redirect(url_for('admin_settings'))
        else:
            flash("Неверный логин или пароль")
    return render_template('admin_login.html', form=form)


@app.route('/admin/settings', methods=('GET', 'POST'))
def admin_settings():
    form = AdminSettingsForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = form.file.data
        if re.match("^\S*.xls$", file.filename):
            file.filename = "schedule.xls"
            file.save(
                os.path.join(
                    os.path.abspath(
                        os.path.dirname(__file__)
                    ), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)
                )
            )
            flash("Файл был загружен")
        else:
            flash("Ошибка при загрузке")
    return render_template('admin-settings.html', form=form)


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
