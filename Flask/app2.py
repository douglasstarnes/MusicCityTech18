from flask import Flask, render_template

app = Flask(__name__)

class Conference(object):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return '<Conference: {0}, ${1}>'.format(self.title, self.price)

conferences = [
    Conference('Awesome Conference', 500),
    Conference('Better Conference', 1000),
    Conference('Uber Conference', 2000)
]

@app.route('/')
def index():
    return render_template('conferences.html', conferences=conferences)