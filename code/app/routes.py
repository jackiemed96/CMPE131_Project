from app import myapp_obj
from flask import render_template, flash, request, url_for, redirect

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

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

@app.route('/register', methods =['GET', 'POST'])
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



@myapp_obj.route('/additem')
def addItem():
    
