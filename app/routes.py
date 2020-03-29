from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kasikil'}
    posts = [
        {
            'author': {'username': 'Josh'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Joel'},
            'body': 'Psweeet is the man I love!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
