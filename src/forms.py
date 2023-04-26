import this

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, Regexp


class SubmitScheduleForm(FlaskForm):
    submit = SubmitField(label="Подтвердить")
    group_number = StringField(
        label='Номер группы',
        validators=[
            DataRequired(),
            Length(max=2)
        ]
    )
    course_number = StringField(
        label='Номер курса',
        validators=[
            DataRequired(),
            Length(max=2)
        ]
    )
    subgroup_number = StringField(
        label='Номер подгруппы',
        validators=[
            DataRequired(),
            Length(max=2)
        ]
    )


class LoginForm(FlaskForm):
    submit = SubmitField(label="Войти")
    login_field = StringField(
        label="Логин",
        validators=[
            DataRequired(),
            Length(max=10)
        ]
    )
    pass_field = PasswordField(
        label="Пароль",
        validators=[
            DataRequired(),
            Length(max=10)
        ]
    )


class AdminForm(FlaskForm):
    submit = SubmitField(label="Подтвердить")
    file = FileField(
        label="Ссылка на расписание",
        validators=[
            DataRequired()
        ]
    )
