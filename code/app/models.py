from re import I
from app import db, login
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item')
    cartitems = db.relationship('CartItem')
    checkout = db.relationship('CheckoutInfo')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'''<Seller: {self.username}, Item: {self.items},
                    Cart: {self.cartitems}>'''

class RegistrationForm(FlaskForm):
    email = StringField('email', validators = [InputRequired()])
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(256))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'''<Seller: {self.seller}, Item: {self.itemname}, 
                    Price: ${self.price}>'''


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(256))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f'''<Seller: {self.seller}, Item: {self.itemname},
                    Price: ${self.price}>, Rating: {self.rating}'''

class CheckoutInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    buyer = db.Column(db.String(64), db.ForeignKey('user.username'))
    address = db.Column(db.String(64))
    ccNumber = db.Column(db.Integer)

    def __repr__(self):
        return f'''Buyer Name: {self.buyer}, Shipping address: {self.address}'''

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
