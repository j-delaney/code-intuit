from app import app, db
from datetime import datetime
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

    return render_template_string("It worked :)")

def create_users():
    users = [
        {
            'username': u'j',
            'password': u'j',
            'spending_entries': [
                {
                    'date': datetime(2014, 11, 1),
                    'school': 2.0
                }
            ]
        },
        {'username': u'aaron', 'password': u'aaron'},
        {'username': u'ryan', 'password': u'ryan'},
    ]

    for user in users:
        new_user = db.User()
        new_user.username = user['username']
        new_user.password = user['password']
        for spending_entry in user.spending_entries:
            new_user.spending_entries = spending_entry
        new_user.save()
