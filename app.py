from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import Unauthorized

from models import connect_db, db, User
from forms import LoginForm, SignupForm, DeleteForm



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth_ex_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    return redirect('/register')





@app.route('/register', methods=['GET','POST'])
def register():
    ''' show form for user to sign up'''
    if 'username' in session:
        return redirect(f"/users/{session['username']}")
    form=SignupForm()

    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        email=form.email.data
        first_name=form.first_name.data
        last_name=form.last_name.data

        user= User.register(username,password,email,first_name,last_name)
        

        db.session.commit()
        session['username']=user.username
        flash('Successfully created your account')
        return redirect(f'/user/{user.username}')

    else: 
        return render_template('register.html',form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    '''show form for user to login '''
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    form= LoginForm()

    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        user= User.authenticate(username,password)

        if user:
            flash(f'Welcome! Successfully login as {user.username}')
            session['username']=user.username
            return redirect(f"/users/{user.username}")

        else:
            form.username.errors = ["Invalid username/password."]
            return render_template('login.html',form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_user():
    session.pop('username')
    return redirect('/register')

