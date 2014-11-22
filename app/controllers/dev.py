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

    return render_template_string("It worked :)")

def create_users():
    users = [
        {'username': u'j', 'password': u'j'},
        {'username': u'aaron', 'password': u'aaron'},
        {'username': u'ryan', 'password': u'ryan'},
    ]

    for user in users:
        new_user = db.User()
        new_user.username = user['username']
        new_user.password = user['password']
        new_user.save()
