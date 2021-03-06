from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# what is the directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # where to store app.db (database file)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)

db = SQLAlchemy(myapp_obj)
login = LoginManager(myapp_obj)
# function that is called to login a user
login.login_view = 'login'
login.init_app(myapp_obj)

from app import routes, models
from app.models import User

@login.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
