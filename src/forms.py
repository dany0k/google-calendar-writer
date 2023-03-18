from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SubmitForm(FlaskForm):
    submit = SubmitField(label="Submit")
    group_number = StringField(
        label='Номер группы',
        validators=[
            DataRequired(),
            Length(max=20)
        ]
    )
    course_number = StringField(
        label='Номер курса',
        validators=[
            DataRequired(),
            Length(max=20)
        ]
    )