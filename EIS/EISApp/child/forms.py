from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FormField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import DateField
import us


class ChildRegistration(FlaskForm):
    """ This class is used for registration of child """

    child_firstname = StringField('First Name', validators=[DataRequired('This field is required'), Length(min=1)])
    child_middlename = StringField('Middle Name')
    child_lastname = StringField('Last Name', validators=[DataRequired('This field is required')])
    child_dob = DateField('Date of Birth', validators=[DataRequired()])
    child_gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Next')


class ChildAddress(FlaskForm):
    address1 = StringField('Address Line 1', validators=[DataRequired('This field is required')])
    address2 = StringField('Address Line 2')
    county = StringField('County')
    city = StringField('City', validators=[DataRequired('This field is required')])
    state = SelectField('State', choices=[(i.abbr, i.name) for i in us.states.STATES])
    zip = IntegerField('Zip', validators=[DataRequired('This field is required')])
    submit = SubmitField('Next')


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[DataRequired()])
    area_code = IntegerField('Area Code', validators=[DataRequired()])
    number = StringField('Number')


class FamilyInformation(FlaskForm):
    mother_firstname = StringField('Mother FirstName', validators=[DataRequired('This field is required')])
    mother_last_name = StringField('Mother LastName')
    father_first_name = StringField('Father FirstName',
                                    validators=[DataRequired('This field is required')])
    father_last_name = StringField('Father LastName')
    phone_number = FormField(TelephoneForm)
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Next')


class DiagnosisInformation(FlaskForm):
    details = TextAreaField('Detailed Diagnosis Information', validators=[DataRequired()])
    submit = SubmitField('Submit')
