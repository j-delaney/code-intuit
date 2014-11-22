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
        {'username': 'j', 'password': 'j'},
        {'username': 'aaron', 'password': 'aaron'},
        {'username': 'ryan', 'password': 'ryan'},
    ]

    for user in users:
        new_user = db.User()
        new_user.username = user['username']
        new_user.password = user['password']
        new_user.save()
