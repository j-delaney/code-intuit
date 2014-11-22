from app import app, db
from app.deco import login_required
from flask import render_template

@app.route('/progress')
@login_required
def render():
    user = g.user
    return render_template('progress.html', user = user)
