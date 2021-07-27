from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField , SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length
import us


class ChildRegistration(FlaskForm):
    """ This class is used for registration of child """

    child_firstname = StringField('First Name', validators=[DataRequired('This field is required'), Length(min=1)])
    child_middlename = StringField('Last Name')
    child_lastname = StringField('' , validators=[DataRequired('This field is required')])
    child_dob = DateField('Date of Birth' , validators=[DataRequired()])
    child_gender = SelectField('Gender' , choices=[('M','Male'),('F','Female')] , validators=[DataRequired()])
    address1 = StringField('Address Line 1', validators=[DataRequired('This field is required'), Length(min=1)])
    address2 = StringField('Address Line 2' )
    city = StringField('City', validators=[DataRequired('This field is required'), Length(min=1)])
    state = SelectField('State' , choices= [ (i.abbr,i.name) for i in us.states.STATES])
    zip = IntegerField('Zip', validators=[DataRequired('This field is required'), Length(min=1)])
    submit = SubmitField('Submit')








