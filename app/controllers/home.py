from app import app, db
from app.deco import login_required
from flask import render_template

@app.route('/home')
@login_required()
def home():
    user = g.user
    return render_template('home.html', user = user)

@app.route('/')
def index():
    return render_template('index.html')
