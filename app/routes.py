from app import myapp_obj, db
from flask import render_template, flash, Flask, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import NumberRange, DataRequired
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Item, CartItem, CheckoutInfo, RegistrationForm, LoginForm
from sqlalchemy import func
from werkzeug.security import generate_password_hash

@myapp_obj.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit ():
        flash('Login requested for user {}, remember_me={}' .format(form.username.data, form.remember_me.data))
        return redirect('/profile')
    return render_template('login.html', title='Sign In', form=form)

@myapp_obj.route('/register', methods =['GET', 'POST'])
def register():
    db.create_all()
    form = RegistrationForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method = 'sha256')
            username = form.username.data
            password = hashed_password
            email = form.email.data

            u = User(username = username, password_hash = password, email=email)
            db.session.add(u)
            db.session.commit()
            flash("Registration was successful")
            return redirect(url_for('login'))
    return render_template('register.html', form = form)

@login_required
@myapp_obj.route('/profile')
def profile():
    return ''


@myapp_obj.route('/items', methods=['GET', 'POST'])
def addItem():
    db.create_all()
    if request.method == "POST":
        if request.form["add_to_store"] == "Add to store":
            newItem = Item(seller=request.form["seller"], itemname=request.form["item"], price=request.form["price"], rating=0, numberofratings=0, sumofratings=0)
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


@myapp_obj.route('/rate/', methods=['GET', 'POST'])
def rateItem():
    if request.method == "POST":
        if request.form["add_rating"] == "Add rating":
            item = Item.query.filter_by(itemname=request.form["item"]).first()
            item.updateRating(int(request.form["rating"]))
            db.session.commit()
    return render_template('rate.html')


@myapp_obj.route('/checkout', methods = ["GET", "POST"])
def buyItems():
    db.create_all()
    if request.method == "POST":
        if request.form["submit"] == "Buy":

            total_price_statement = CartItem.query.with_entities(func.sum(CartItem.price))

            total_price = total_price_statement.scalar()

            info = CheckoutInfo(address=request.form["address"], ccNumber = request.form["number"])
            db.session.add(info)
            db.session.commit()

            return render_template('shipping.html', buyInfo=CheckoutInfo.query.all(), items = Item.query.all(), total_price = total_price)

    return render_template('shipping.html', buyInfo=CheckoutInfo.query.all(), items = Item.query.all(), total_price = (CartItem.query.with_entities(func.sum(CartItem.price))).scalar())


@myapp_obj.route('/', methods = ["GET", "POST"])
def splash_page():
    if request.method == "POST":
        if request.form["submit"] == "Login":
            return redirect(url_for('Login'))

        elif request.form["submit"] == "Register":
            return redirect(url_for('Register'))

    return render_template('splash.html')
