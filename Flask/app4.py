from flask import Flask, render_template, request, redirect, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conferencebarrel.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'yekterces'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    price = db.Column(db.Float())


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route('/conferences')
@login_required
def conferences():
    result = Conference.query.all()
    return render_template('conferences.html', conferences=result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is not None and user.password == password:
            login_user(user)
            return redirect('conferences')
        else:
            return redirect('login')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')


@login_manager.user_loader
def load_user(uid):
    return User.query.filter_by(id=uid).first()


@app.before_request
def before_request():
    g.user = current_user
