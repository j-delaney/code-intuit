from app import app, db
from flask import render_template

@app.route('/questions')
def render_questions():
    
    
    
    return render_template('questions.html')

