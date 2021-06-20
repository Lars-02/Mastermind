from wtforms import Form, BooleanField, StringField, validators, IntegerField
from wtforms.validators import NumberRange, ValidationError


class LessThen(object):
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data > other.data:
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.gettext('Field must be equal or lower to %(other_name)s.')

            raise ValidationError(message % d)


class GameCreateForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    colors = IntegerField('Colors', [validators.NumberRange(min=1, max=12)])
    positions = IntegerField('Positions', validators=[LessThen('colors'), NumberRange(min=1, max=12)])
    guesses = IntegerField('Guesses', [validators.NumberRange(min=1, max=30)])
    double_colors = BooleanField('Double colors')
