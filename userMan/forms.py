from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email=StringField(label='Email Adress:', validators=[Email(), DataRequired()])
    firstName=StringField(label='First Name:', validators=[DataRequired()])
    lastName=StringField(label='Last Name:', validators=[DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LogInForm(FlaskForm):
    usernameL = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    passwordL = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    submitL = SubmitField(label='Log In')