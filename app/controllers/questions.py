from app import app, db
from flask import render_template

@app.route('/questions/<article_name>')
def render_questions(article_name):
    questions = db.Question.find({'article':article_name})
    questions = list(questions)
    
    return render_template('questions.html', questions = questions)
