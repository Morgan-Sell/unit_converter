from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired

from src.config import LENGTH_UNIT_CHOICES


class LengthForm(FlaskForm):
    length = DecimalField("Enter length to convert:", validators=[DataRequired()])
    from_unit = SelectField(
        "Unit to convert from:",
        choices=LENGTH_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    to_unit = SelectField(
        "Unit to convert to:", choices=LENGTH_UNIT_CHOICES, validators=[DataRequired()]
    )
    convert = SubmitField(label="Convert")
