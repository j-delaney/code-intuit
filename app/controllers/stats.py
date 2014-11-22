from app import app, db
from flask import render_template

@app.route('/stats')
def render_stats():
    return render_template('stats.html')
