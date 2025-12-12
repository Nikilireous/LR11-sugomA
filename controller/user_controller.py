from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from bcrypt import hashpw, checkpw, gensalt


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('tasks'))

    if request.method == 'POST':
        name = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # TODO check email not in db
        db_email = 'something'

        if email != db_email:
            flash('Ваш аккаунт успешно создан! Теперь вы можете войти.', 'success')
            return redirect(url_for('tasks'))

        flash('Данная электронная почта уже привязана', 'error')

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form.get("email")
        password: str = request.form.get("password")

        # TODO check email exists
        db_email = 'gog@gamil.com'
        user = 'some user'

        if user:
            if checkpw(bytes(password, 'UTF8'), bytes(user.password, 'UTF8')):
                login_user(user, remember=True)
                next_page = request.args.get('next')
                flash('Вы успешно вошли в систему!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('tasks'))
        else:
            flash('Вход не удался. Проверьте email и пароль.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно вышли из системы.', 'info')
    return redirect(url_for('index'))