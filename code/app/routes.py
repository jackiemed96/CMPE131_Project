from app import myapp_obj
from flask import render_template, flash, Flask, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import NumberRange
from flask_login import login_user, logout_user, current_user, login_required

class AddToCartButton(FlaskForm):
    cartsubmit = SubmitField('Add to cart')

class RateItemButton(FlaskForm):
    rating = IntegerField('Rating (1-10):', validators=[NumberRange(min=1, max=10)])
    ratingsubmit = SubmitField('Rate') 

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



@myapp_obj.route('/additem')
def addItem():
    
