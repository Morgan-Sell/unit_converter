from src.config import LENGTH_UNIT_CHOICES
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LengthForm(FlaskForm):
    length = DecimalField("Enter length to convert:", validators=[DataRequired()])
    from_unit = SelectField(
        "Unit to convert from:",
        choices=LENGTH_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    to_unit = SelectField(
        "Unit to convert to:",
        choices=LENGTH_UNIT_CHOICES,
        validators=[DataRequired()]
    )
    convert = SubmitField(label="Convert")
