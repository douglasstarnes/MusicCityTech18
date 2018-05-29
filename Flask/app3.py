from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conferencebarrel.db'
db = SQLAlchemy(app)

class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float())

@app.route('/')
def index():
    conferences = Conference.query.all()
    return render_template('conferences.html', conferences=conferences)


