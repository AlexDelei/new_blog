from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex'}
    post = [
        {
            'author': {'username': 'Becky'},
            'body' : 'Its such a lovely day'
        },
        {
            'author': {'username': 'Charles'},
            'body': 'Look who is back!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=post)