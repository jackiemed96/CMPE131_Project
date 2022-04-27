from app import myapp_obj
from flask import render_template, flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

@myapp_obj.route('/')
@myapp_obj.route('/login')
def login():
    # create form
    # if form inputs are valid
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
    return 'home'


@login_required
@myapp_obj.route('/profile')
def profile():
    return ''

