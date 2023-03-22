import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, ValidationError, Length, EqualTo
from app.models import User

def username_exists(form, field):
  username = User.query.filter(User.username == form.data['username']).first()
  
  if username:
    raise ValidationError('Username is already in use.')
  
def email_exists(form, field):
  user_email = User.query.filter(User.email == form.data['email']).first()
  
  if user_email:
    raise ValidationError('Email address is already in use.')
  
def valid_password(form, field):
  password = form.data['password']
  
  upper_match = re.search(r'([A-Z])*', password)
  number_match = re.search(r'([0-9])\d*', password)
  special_match = re.search(r'([!@#$%^&*()-+?/\><~])', password)
  
  if not upper_match:
    raise ValidationError('Password must include at least 1 upper case character.')
  
  if not number_match:
    raise ValidationError('Password must include at least 1 number.')
  
  if not special_match:
    raise ValidationError('Password must include at least 1 special character.')
  
  
class SignUpForm(FlaskForm):
  username = StringField('username', validators=[InputRequired(), username_exists, Length(min=3, max=40)])
  email = EmailField('email', validators=[InputRequired(), Email(), email_exists])
  password = PasswordField('password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, message='Password must be at least 8 characters long.'), valid_password])
  confirm = PasswordField('password', validators=[InputRequired()])