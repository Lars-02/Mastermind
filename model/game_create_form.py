from wtforms import Form, BooleanField, StringField, IntegerField
from wtforms.validators import NumberRange, ValidationError, Length, DataRequired


class LessThen(object):
    def __init__(self, fieldname: dict, message: str = None) -> None:
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form: list, field: str) -> None:
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext(f"Invalid field name '{self.fieldname}'."))

        if field.data > other.data:
            message = self.message

            if message is None:
                message = field.gettext(f"Field must be equal to or less then the amount of {self.fieldname}.")

            raise ValidationError(message)


class GameCreateForm(Form):
    name = StringField('Nickname', validators=[DataRequired(), Length(min=4, max=25)])
    colors = IntegerField('Colors', validators=[DataRequired(), NumberRange(min=1, max=12)])
    positions = IntegerField('Positions', validators=[DataRequired(), LessThen('colors'), NumberRange(min=1, max=12)])
    guesses = IntegerField('Guesses', validators=[DataRequired(), NumberRange(min=1, max=20)])
    double_colors = BooleanField('Double colors')
