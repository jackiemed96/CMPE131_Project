from app import db
from app import login
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordField, BooleanField
from wtfsforms.validators import InputRequired, Email, Length
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item')
    cartitems = db.relationship('CartItem')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'''<Seller: {self.username}, Item: {self.items},
                    Cart: {self.cartitems}>'''
    
class RegistrationForm(FlaskForm)
    email = StringField('email', validators = [InputRequired()])
    username = StringField('username', validators = [InputRequired()])
    password = PassowrdField('password', validators=[InputRequired()])

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(256))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)
    
    def __repr__(self):
        return f'''<Seller: {self.seller}, Item: {self.itemname}, 
                    Price: {self.price}>'''

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(256))
    seller = db.Column(db.String(64), db.ForeignKey('user.username'))
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f'''<Seller: {self.seller}, Item: {self.itemname},
                    Price: {self.price}>, Rating: {self.rating}'''

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

