from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class AddItemForm(FlaskForm):
    sellername = StringField('Seller Name')
    itemname = StringField('Item Name')
    price = IntegerField('Price')
    addbutton = SubmitField('Add to store')


class AddToCartButton(FlaskForm):
    cartsubmit = SubmitField('Add to cart')

class RateItemButton(FlaskForm):
    rating = IntegerField('Rating (1-10):', validators=[NumberRange(min=1, max=10)])
    ratingsubmit = SubmitField('Rate')


