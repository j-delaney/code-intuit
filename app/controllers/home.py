from app import app, db
from app.deco import login_required
from flask import render_template, g

@app.route('/home')
@login_required
def home():
    listVar = g.user.progress
    listVar = list(set(listVar))

    listPass = [0] * 6;

    for temp in listVar:
        if temp == u'retirement':
            listPass[0] = 1

        if temp == u'plastic':
            listPass[1] = 1

        if temp == u'borrowing':
            listPass[2] = 1

        if temp == u'expenditures':
            listPass[3] = 1

        if temp == u'income':
            listPass[4] = 1

        if temp == u'budgeting':
            listPass[5] = 1



    return render_template('home.html', listPass = listPass) 

@app.route('/')
def index():
    return render_template('index.html')
