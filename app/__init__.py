import os
from flask import Flask, render_template, request, session, redirect, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from .config import Config
from .models import db, User
from .routes.user_routes import user_routes
from .routes.auth_routes import auth_routes

app = Flask(__name__, static_folder='../build', static_url_path='/')

base_url = 'pyact-cms'

login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
  
app.config.from_object(Config)
  
app.register_blueprint(user_routes, url_prefix=f"/{base_url}/profile")
app.register_blueprint(auth_routes, url_prefix=f"/{base_url}/auth")
db.init_app(app)
Migrate(app, db)
  
  
CORS(app)  
  

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route(f"/{base_url}/", defaults={'path': ''})
@app.route(f"/{base_url}/<path:path>")
def react_root(path):
    if path != "" and os.path.exists(f"{app.static_folder}/{path}"):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')