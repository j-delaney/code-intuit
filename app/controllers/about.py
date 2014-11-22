from app import app, db
from flask import render_template


@app.route('/about')
def render_about():
    return render_template('about.html')

@app.route('/about-us')
def render_about_us():
    return render_template('about-us.html')
