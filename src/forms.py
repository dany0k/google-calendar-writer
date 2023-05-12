from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange


class SubmitScheduleForm(FlaskForm):
    submit = SubmitField(label="Подтвердить")
    course_number = IntegerField(
        label='Номер курса',
        render_kw={"placeholder": "Номер курса"},
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10)
        ]
    )
    group_number = IntegerField(
        label='Номер группы',
        render_kw={"placeholder": "Номер группы"},
        validators=[
            DataRequired(),
            NumberRange(min=1, max=11)
        ]
    )
    subgroup_number = IntegerField(
        label='Номер подгруппы',
        render_kw={"placeholder": "Номер подгруппы"},
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10)
        ]
    )
    week_amount = IntegerField(
        label="Количество недель",
        render_kw={"placeholder": "Количество заполняемых недель"},
        validators=[
            DataRequired(),
            NumberRange(min=1, max=20)
        ]
    )


class LoginForm(FlaskForm):
    submit = SubmitField(label="Войти")
    login_field = StringField(
        label="Логин",
        render_kw={"placeholder": "Логин"},
        validators=[
            DataRequired(),
            Length(max=10)
        ]
    )
    pass_field = PasswordField(
        label="Пароль",
        render_kw={"placeholder": "Пароль"},
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
