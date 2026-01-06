from flask import Flask, render_template

from controller.user_controller import auth_bp
from controller.task_controller import tasks_bp


app = Flask(__name__)
app.config.from_object('app.config.Config')

app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/error404.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)