from app import app, db
from app.deco import login_required
from flask import render_template, request, g

@app.route('/questions/<article_name>')
@login_required
def render_questions(article_name):
    user = g.user
    questions = db.Question.find({'article':article_name})
    questions = list(questions)
    
    return render_template('questions.html', questions = questions)

@app.route('/questions/<article_name>', methods=['GET', 'POST'])
@login_required
def render_answers(article_name):
    user = g.user
    if request.method == 'POST':
        num_correct = 0
        success = False
        controller_return = True

        for question_id, correct in request.form.iteritems():
            if correct == True or correct == 'True' or correct == u'True':
                num_correct+=1
      
        if num_correct == 3:
            success = True
            user.progress.append(article_name)
            user.save()

        return render_template('questions.html', num_correct=num_correct, success=success, controller_return=controller_return)

    else:
        return render_template('questions.html') 
