from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET' , 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                print('Logged in.')
            else:
                flash('Incorrect Password, please try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", text = "Testing")


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up', methods = ['GET' , 'POST'])
def sign_up():

    if request.method == 'POST':

        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email is too short', category = 'error')
        elif len(firstName) < 2:
            flash('First name too short', category = 'error')
        elif password != confirmPassword:
            flash("Passwords don't match", category = 'error')
        elif len(password) < 7:
            flash("Password is too short", category = 'error')
        else:
            #user passed all checks
            new_user = User(email=email, firstName=firstName, lastName=lastName, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash("Account created!", category = 'success')
            return redirect(url_for('views.home'))

    return render_template("signUp.html")
