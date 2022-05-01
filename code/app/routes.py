from app import myapp_obj, db
from flask import render_template, flash, Flask, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import NumberRange
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Item, CartItem

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

@myapp_obj.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_hash(form.password.data, method = 'sha256')
        username = form.username.data
        password = hashed_password
        email = form.email.data
        
        u = User(username = username, password = password, email=email)
        db.session.add(u)
        db.session.commit
        flash("Registration was successful")
        return redirect(url_for('Login'))
    return render_template('register.html', msg = msg)

@login_required
@myapp_obj.route('/profile')
def profile():
    return ''


@myapp_obj.route('/items', methods=['GET', 'POST'])
def addItem():
    db.create_all()
    if request.method == "POST":
        if request.form["add_to_store"] == "Add to store":
            newItem = Item(seller=request.form["seller"], itemname=request.form["item"], price=request.form["price"])
            db.session.add(newItem)
            db.session.commit()
            return render_template('itemspage.html', items=Item.query.all())
    return render_template('itemspage.html', items=Item.query.all())


@myapp_obj.route('/cart/<string:item_name>')
def addToCart(item_name):
    item = Item.query.filter_by(itemname=item_name).first()
    cart_item = CartItem(seller=item.seller, price=item.price, itemname=item.itemname)
    db.session.add(cart_item)
    db.session.commit()
    return render_template('cart.html', cart=CartItem.query.all())

@myapp_obj.route('/cart/')
def cart():
    return render_template('cart.html', cart=CartItem.query.all())
