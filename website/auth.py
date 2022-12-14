from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET' , 'POST'])
def login():

    return render_template("login.html", text = "Testing")


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up', methods = ['GET' , 'POST'])
def sign_up():
    if request.method == 'POST':
            email = request.form.get('email')
            firstName = request.form.get('firstName')
            password = request.form.get('password')
            confirmPassword = request.form.get('confirmPassword')
    if len(email) < 4:
        flash('Email is too short', category = 'error')
    elif len(firstName) < 2:
        flash('First name too short', category = 'error')
    elif password != confirmPassword:
        flash("Passwords don't match", category = 'error')
    elif len(password) < 7:
        flash("Password is too short", category = 'error')
    else:
        #user passed all checks
        flash("Account created!", category = 'success')
        pass
    return render_template("signUp.html")
