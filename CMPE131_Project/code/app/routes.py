from app import myapp_obj, db
from flask import render_template, flash, Flask, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import NumberRange
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Item, CartItem
from app.forms import LoginForm



@myapp_obj.route('/')
@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit ():
        flash('Login requested for user {}, remember_me={}' .format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
    # if form inputs are valid
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
    return 'home'

@myapp_obj.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        db.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        if db.fetchone()[0]:
            msg = 'Account already exists !'
        else:
            u = User(username, password, email)
            db.session.add(u)
            db.session.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
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
