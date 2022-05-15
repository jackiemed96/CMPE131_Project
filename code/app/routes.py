from app import myapp_obj, db
from flask import render_template, flash, Flask, request, redirect, url_for, Response
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Item, CartItem, CheckoutInfo, Review
from app.models import RegistrationForm, LoginForm, LogoutForm, ProfileForm, SearchForm
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import sqlalchemy as sql

@myapp_obj.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit ():
            usersCheck = db.session.query(User).where(User.username == form['username'].data).all() #Validates user existence
            if len(usersCheck) == 0:
                return redirect('/register')
            else:
                database_user = usersCheck[0]
                user = User(username = database_user.username, id = int(database_user.id))
                login_user(user)
                return redirect('/profile')

    return render_template('login.html', title='Sign In', form=form)

@myapp_obj.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method = 'sha256') #'sha256' is a type of encryption
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
@myapp_obj.route('/delete', methods = ['GET', 'POST'])
def delete_account():
    if request.method == "POST":
        current_user.remove()
        db.session.commit()
        flash('Your account has been deleted')
        return redirect(url_for('login'))
    return render_template('delete.html')

@myapp_obj.context_processor
def base():
    form = SearchForm()
    return dict(form = form)

@login_required
@myapp_obj.route('/search', methods = ['POST'])
def search():
    form = SearchForm()
    items = Item.query
    if form.validate_on_submit():
        Item.searched = form.searched.data
        items = items.filter(Item.itemname.like('%'+ Item.searched + '%' ))
        items = items.order_by(Item.id).all()
        return render_template('search.html', form = form, searched = Item.searched, items = items)

@login_required
@myapp_obj.route('/profile')
def profile():
    form = ProfileForm()
    return render_template('profile.html', form = form)

@login_required
@myapp_obj.route('/logout')
def logout():
    form = LogoutForm()
    logout_user()
    return render_template('logout.html', form = form)

@myapp_obj.route('/items', methods=['GET', 'POST'])
def addItem():
    if request.method == "POST":
        if request.form["add_to_store"] == "Add to store":
            
            pic = request.files["pic"]
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype

            newItem = Item(seller=current_user.username, itemname=request.form["item"], price=request.form["price"], rating=0, numberofratings=0, sumofratings=0, img=pic.read(), mimetype=mimetype, name=filename)
            db.session.add(newItem)
            db.session.commit()
            return render_template('itemspage.html', items=Item.query.all()) 
        
    return render_template('itemspage.html', items=Item.query.all())


@myapp_obj.route('/items/<int:id>')
def viewImage(id):
    img = Item.query.filter_by(id=id).first()
    return Response(img.img, mimetype=img.mimetype)


@myapp_obj.route('/cart/', methods=['GET', 'POST'])
def cart():
    if request.method == "POST":
        if request.form["add_to_cart"] == "Add to cart":
            item = Item.query.filter_by(id=request.form["item_id"]).first() #Retrieves first item with matching ID
            cart_item = CartItem(seller=item.seller, price=item.price, itemname=item.itemname)
            db.session.add(cart_item)
            db.session.commit()
    return render_template('cart.html', cart=CartItem.query.all())


@myapp_obj.route('/rate/', methods=['GET', 'POST'])
def rateItem():
    if request.method == "POST":
        if request.form["add_rating"] == "Add rating":
            item = Item.query.filter_by(id=request.form["item_id"]).first() #Retrieves first item with matching ID
            item.updateRating(int(request.form["rating"]))
            review = Review(body=request.form["review"], username=current_user.username, item=item.itemname, rating=int(request.form["rating"]))
            db.session.add(review)
            db.session.commit()
    return render_template('rate.html')

@myapp_obj.route('/reviews/<int:id>')
def itemReviews(id):
    reviews = Item.query.filter_by(id=id).first().reviews
    item = Item.query.filter_by(id=id).first()
    return render_template('reviews.html', item=item, reviews=reviews)


@myapp_obj.route('/checkout/', methods = ["GET", "POST"])
def buyItems():
    if request.method == "POST":
        if request.form["submit"] == "Buy":

            total_price_statement = CartItem.query.with_entities(sql.func.sum(CartItem.price)) #Obtains item price from CartItem database; returns statement

            total_price = total_price_statement.scalar() #Turns statement into a value

            info = CheckoutInfo(address=request.form["address"], ccNumber = request.form["number"], buyer = current_user.username)
            db.session.add(info)
            db.session.commit()

            for item in CartItem.query.all():
                itemDelete = Item.query.filter_by(itemname = item.itemname).first()

                for item_ in Item.query.all():
                    if item_ == itemDelete:
                        db.session.delete(item_)
                        db.session.commit()

                db.session.delete(item)
                db.session.commit()
                

            return render_template('shipping.html', buyInfo=CheckoutInfo.query.filter_by(buyer = current_user.username), items = CartItem.query.all(), total_price = total_price)

    return render_template('shipping.html', buyInfo=CheckoutInfo.query.filter_by(buyer = current_user.username), items = CartItem.query.all(), total_price = (CartItem.query.with_entities(sql.func.sum(CartItem.price))).scalar())

@myapp_obj.route('/', methods = ["GET", "POST"])
def splash_page():
    db.create_all()
    if request.method == "POST":
        if request.form["submit"] == "Login":
            return redirect(url_for('Login'))

        elif request.form["submit"] == "Register":
            return redirect(url_for('Register'))

    return render_template('splash.html')

@myapp_obj.route('/deleteItem', methods = ["GET", "POST"])
def deleteItem():
    if request.method == "POST":
        if request.form["delete_item"] == "Delete":
            item_to_delete = Item.query.filter_by(id = request.form["item_id"]).first()
            db.session.delete(item_to_delete)
            db.session.commit()

            return render_template('deleteItem.html', item_list = Item.query.all())

        elif request.form["back"] == "Back":
            return redirect(url_for('Back'))
        
    return render_template('deleteItem.html', item_list = Item.query.all())