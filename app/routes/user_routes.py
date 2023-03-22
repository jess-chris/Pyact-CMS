from flask import Blueprint
from flask_login import login_required, current_user
from app.models import User

user_routes = Blueprint('profile', __name__)

@user_routes.route('/')
@login_required
def profile():
  if current_user.is_authenticated:
    return current_user.to_dict()
  return {'errors': ['Unauthorized']}

