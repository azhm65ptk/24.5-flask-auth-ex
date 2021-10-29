from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    '''form for user to register'''
    username=StringField('Username', validators=[InputRequired(), Length(min=1, max=20)])
    password=PasswordField('Password', validators=[InputRequired(), Length(min=6, max=55)])
    

class SignupForm(FlaskForm):
    '''form for user login'''
    username=StringField('Username', validators=[InputRequired(), Length(min=1, max=20)])
    password=PasswordField('Password', validators=[InputRequired(), Length(min=6, max=55)])
    email=StringField('Email', validators=[InputRequired(), Length( max=50)])
    first_name=StringField('First Name', validators=[InputRequired(), Length( max=30)])
    last_name=StringField('Last Name', validators=[InputRequired(), Length( max=30)])

class DeleteForm(FlaskForm):
    '''Delete Form'''