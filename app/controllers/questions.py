from app import app, db
from flask import render_template, request

@app.route('/questions/<article_name>')
def render_questions(article_name):
    questions = db.Question.find({'article':article_name})
    questions = list(questions)
    
    return render_template('questions.html', questions = questions)

@app.route('/questions/<article_name>', methods=['GET', 'POST'])
def render_answers(article_name):
    if request.method == 'POST':
      for question_id, correct in request.form.iteritems():
        print question_id, correct
