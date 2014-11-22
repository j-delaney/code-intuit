from app import app, db
from flask import render_template request


@app.route('/about')
def render():
        return render_template('about.html')
