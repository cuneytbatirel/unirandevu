from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    phonenumber = StringField('Phone Number', validators =[DataRequired(), Length(min = 10, max = 13)])
    firstname = StringField('First Name', validators =[DataRequired(), Length(min = 2, max = 20)])
    lastname = StringField('Last Name', validators =[DataRequired(), Length(min = 2, max = 30)])
    title = StringField('Title', validators =[DataRequired()])
    university = StringField('University', validators =[DataRequired()])
    city = StringField('City', validators =[DataRequired()])
    department = StringField('Department', validators =[DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    passwordconfirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DeleteDForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Delete')

class DeleteUForm(FlaskForm):
    title = StringField('Name', validators = [DataRequired()])
    city = StringField('City', validators = [DataRequired()])
    submit = SubmitField('Delete')

