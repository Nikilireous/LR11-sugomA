from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from utils.U import Database_users
from utils.hash import hash_password, verify_password


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('tasks.index'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        db_users = Database_users()
        existing = db_users.select(email)
        if existing:
            flash('Пользователь с таким email уже существует', 'danger')
            db_users.close()
            return render_template('auth/register.html')

        hashed_pw = hash_password(password)
        user_id = db_users.add([username, email, hashed_pw])
        db_users.close()

        session['user_id'] = user_id
        session['username'] = username
        flash('Аккаунт успешно создан!', 'success')
        return redirect(url_for('tasks.index'))

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('tasks.index'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db_users = Database_users()
        user = db_users.select(email)
        db_users.close()

        if user and verify_password(user[0][3], password):
            session['user_id'] = user[0][1]
            session['username'] = user[0][0]
            flash(f'Добро пожаловать, {user[0][0]}!', 'success')
            return redirect(url_for('tasks.index'))

        flash('Неверный email или пароль', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Вы успешно вышли из системы', 'info')
    return redirect(url_for('auth.login'))