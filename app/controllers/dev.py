from app import app, db
from flask import render_template_string


@app.route('/dev/data')
def main():
    # Delete all items
    users = db.User.find()
    questions = db.Question.find()
    all_items = list(users) + list(questions)
    for item in all_items:
        item.delete()

    create_users()
    create_questions()

    return render_template_string("It worked :)")

def create_questions():
    questions = [
        {
            'text': u'QUESTION TEXT',
            'choices': [
                {
                    'text': u'ANSWER TEXT',
                    'correct': False,
                    'wrong_explanation': u'WRONG_EXPAILN'
                }
            ],
            'article': u'ARTICLE_NAME'
        }
    ]

    for question in questions:
        new_q = db.Question()
        new_q.text = question.text
        new_q.article = question.article
        new_q.choices = question.choices
        new_q.save()


def create_users():
    users = [
        {'username': 'j', 'password': 'j'},
        {'username': 'aaron', 'password': 'aaron'},
        {'username': 'ryan', 'password': 'ryan'},
    ]

    for user in users:
        new_user = db.User()
        new_user.username = user['username']
        new_user.password = user['password']
        new_user.save()
