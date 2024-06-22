from flask import render_template, url_for, flash, redirect, request, Blueprint
from todoapp import db, bcrypt
from todoapp.users.forms import RegistrationForm, LoginForm
from todoapp.models import User
from flask_login import login_user, current_user

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'New account successfully created. Please log in.','success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Register", form=form)

@users.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Check email and password.','danger')
    return render_template('login.html', title='Login', form=form)