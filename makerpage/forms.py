from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email
from makerpage.models import QuoteForm

class QuotePage(FlaskForm):

    quotedisplay = TextAreaField('Quote')
    rating = SelectField(u'Is it good', choices=[], coerce=int)
    submit = SubmitField('Submit')