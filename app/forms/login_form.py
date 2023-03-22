from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import InputRequired, Email, ValidationError
from app.models import User


def password_matches(form, field):
  password = field.data
  email = form.data['email']
  user = User.query.filter(User.email == email).first()
  if not user:
    raise ValidationError('Invalid login.')
  if not user.check_password(password):
    raise ValidationError('Invalid login.')



class LoginForm(FlaskForm):
  email = EmailField('email', validators=[InputRequired(), Email()])
  password = PasswordField('password', validators=[InputRequired(), password_matches])
  


  