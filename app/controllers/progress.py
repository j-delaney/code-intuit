from app import app, db
from flask import render_template

@app.route('/progress')
def render():
    return render_template('progress.html')
