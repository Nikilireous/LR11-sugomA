from flask import Flask, render_template
from flask_login import LoginManager, UserMixin

class User(UserMixin):
    pass


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Чтобы вкусить наш сервис, войдите в аккаунт!'
login_manager.login_message_category = 'info'

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/error404.html')


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)