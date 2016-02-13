from wtforms import StringField, SubmitField, Form, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class PersonForm(Form):
    name = StringField('Enter the Name', validators=[DataRequired()])
    email = EmailField("Enter the Email", validators=[DataRequired, Email])
    contact = StringField("Contact Number", validators=[DataRequired])
    city = StringField("Enter City", validators=[DataRequired])
    company = StringField("Company Name", validators=[DataRequired])
    submit = SubmitField('Submit')