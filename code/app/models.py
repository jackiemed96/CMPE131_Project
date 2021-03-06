from app import db, login
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    shopping = db.Column(db.String(256))
    items = db.relationship('Item')
    cartitems = db.relationship('CartItem')
    checkout = db.relationship('CheckoutInfo')
    reviews = db.relationship('Review')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def remove(self):
        db.session.delete(self)

    def __repr__(self):
        return f'''<Seller: {self.username}, Item: {self.items},
                    Cart: {self.cartitems}>'''


class RegistrationForm(FlaskForm):
    email = StringField('email', validators = [InputRequired()])
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators = [DataRequired()])
    submit = SubmitField("Submit")

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(256))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'''{self.itemname} sold by {self.seller} for ${self.price}.'''


class Item(db.Model):
    __searchable__ = ['itemname']
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(64))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    numberofratings = db.Column(db.Integer)
    sumofratings = db.Column(db.Integer)
    img = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    reviews = db.relationship('Review')

    def updateRating(self, userrating):
        self.numberofratings = self.numberofratings + 1
        self.sumofratings = self.sumofratings + userrating
        self.rating = self.sumofratings / self.numberofratings

    def __repr__(self):
        return f'''{self.itemname} sold by {self.seller} for ${self.price} has a rating of {self.rating} stars.'''


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(64), db.ForeignKey('user.username'))
    item = db.Column(db.String(64), db.ForeignKey('item.itemname'))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.username} gave a rating of {self.rating}: "{self.body}" [{self.timestamp}]'

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

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    shopping = StringField('Shopping List')
    button = SubmitField('Sign out')

class EditingForm(FlaskForm):
    shopping = StringField('Shopping List')



class LogoutForm(FlaskForm):
    button = SubmitField('Sign out')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
