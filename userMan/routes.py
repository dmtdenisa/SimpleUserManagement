from flask.helpers import flash
from flask.wrappers import Request
from userMan import app
from flask import render_template, redirect, url_for, request, flash
from userMan.models import User
from userMan.forms import RegisterForm, LogInForm
from userMan import db


@app.route('/users')
def users_page():
    users=User.query.all()
    return render_template('users.html', users=users)


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
        username=form.username.data, 
        email=form.email.data, 
        firstName=form.firstName.data, 
        lastName=form.lastName.data, 
        password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('users_page'))
    if form.errors != {}: #if there are no errors from the validations
        for err_msg in form.errors.values():
            print(f'There was an error: {err_msg}')
    return render_template('register.html', form=form)

@app.route('/log_in', methods=['GET', 'POST'])
def logIn_page():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        inputUsername=login_form.usernameL.data
        inputPassword=login_form.passwordL.data    
        if User.query.filter_by(username=(inputUsername)).first():
            existingUser=(User.query.filter_by(username=(inputUsername)).first()).username
        else:
            existingUser=" "
        #existingUser=existingUser.username
        if User.query.filter_by(password=(inputPassword)).first():
            existingPassword=(User.query.filter_by(password=(inputPassword)).first()).password
        else:
            existingPassword=" "
        #existingPassword=existingPassword.password
        if inputUsername == existingUser and inputPassword == existingPassword:
            return redirect(url_for('users_page'))
        else:
            #print(existingUser + existingPassword)#redirect(url_for('users_page'))
            print("Incorrect data")
    if login_form.errors != {}: #if there are no errors from the validations
        for err_msg in login_form.errors.values():
            print(f'There was an error: {err_msg}')
    return render_template('logIn.html', login_form=login_form)
        
        