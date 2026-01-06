from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from utils.T import Database_tasks
from utils.UT import Database_user_task


tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']

    db_link = Database_user_task()
    user_tasks = db_link.select(user_id)
    db_link.close()

    tasks = []
    db_tasks = Database_tasks()
    for item in user_tasks:
        task_id = item[4]
        task_data = db_tasks.get_by_id(task_id)
        if task_data:
            tasks.append({
                'id': task_data[0],
                'name': task_data[1],
                'details': task_data[2],
                'priority': item[0],
                'status': item[1],
                'date': item[2]
            })
    db_tasks.close()

    return render_template('tasks/tasks.html', tasks=tasks)


@tasks_bp.route('/new', methods=['GET', 'POST'])
def create():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        priority = request.form.get('priority', 1)

        db_tasks = Database_tasks()
        task_id = db_tasks.add([name, details])
        db_tasks.close()

        db_link = Database_user_task()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        db_link.add([int(priority), "active", current_date, session['user_id'], task_id])
        db_link.close()

        flash('Задача успешно создана!', 'success')
        return redirect(url_for('tasks.index'))

    return render_template('tasks/create.html')


@tasks_bp.route('/<int:task_id>/complete', methods=['POST'])
def complete(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db_link = Database_user_task()
    current = db_link.select(session['user_id'])

    for item in current:
        if item[4] == task_id:
            item = list(item)

            if item[1] == 'active':
                item[1] = 'completed'
            else:
                item[1] = 'active'

            db_link.update(item)
            break
    db_link.close()

    flash('Статус задачи обновлен', 'info')
    return redirect(url_for('tasks.index'))


@tasks_bp.route('/<int:task_id>/delete', methods=['POST'])
def delete(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db_link = Database_user_task()
    current = db_link.select(session['user_id'])
    for item in current:
        if item[4] == task_id:
            db_link.delete(('blank', 'blank', 'blank', session['user_id'], task_id))
            break
    db_link.close()

    db_tasks = Database_tasks()
    current = db_tasks.get_by_id(task_id)
    db_tasks.delete(current[1])
    db_tasks.close()

    flash('Задача удалена', 'success')
    return redirect(url_for('tasks.index'))