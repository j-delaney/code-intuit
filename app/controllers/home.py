from app import app, db
from flask import render_template

@app.route('/home')
def home():
    return render_template('home.html')



    
