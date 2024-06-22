from flask import render_template, url_for, flash, redirect, abort, Blueprint
from todoapp import db
from todoapp.tasks.forms import TaskForm
from todoapp.models import Task
from flask_login import current_user, login_required

tasks = Blueprint('tasks', __name__)

@tasks.route("/task/new", methods=['GET','POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, author=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Task created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_task.html', title='Add Task', form=form, legend='Add Task')