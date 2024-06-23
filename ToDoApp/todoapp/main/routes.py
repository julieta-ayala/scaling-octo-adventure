from flask import render_template, redirect, url_for, Blueprint
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.user_tasks', username=current_user.username))
    return render_template('home.html', title='Home')