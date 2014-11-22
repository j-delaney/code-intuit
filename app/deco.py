from functools import wraps
from flask import session, g, redirect, url_for
from app import db


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['username'] and session['password']:
            user = db.User.find_one({
                'username': session['username'],
                'password': session['password']
            })
            if user:
                g.user = user
                return f(*args, **kwargs)
            else:
                return redirect(url_for('login'))
    return decorated_function