from flask import render_template, url_for, flash, redirect, Blueprint
from todoapp import db, bcrypt
from todoapp.users.forms import RegistrationForm
from todoapp.models import User

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET','POST'])
def register():
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
    return redirect(url_for('main.home'))