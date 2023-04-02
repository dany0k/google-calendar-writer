from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


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
