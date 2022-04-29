from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddItemForm(FlaskForm):
    sellername = StringField('Seller Name')
    itemname = StringField('Item Name')
    price = IntegerField('Price')
    addbutton = SubmitField('Add to store')
