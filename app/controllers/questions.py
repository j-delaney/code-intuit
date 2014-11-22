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
        num_correct = 0
        success = False
        controller_return = True

        for question_id, correct in request.form.iteritems():
            if correct == True or correct == 'True' or correct == u'True':
                num_correct+=1
      
        if num_correct == 3:
            success = True
      
        return render_template('questions.html', num_correct=num_correct, success=success, controller_return=controller_return)

    else:
        return render_template('questions.html') 
