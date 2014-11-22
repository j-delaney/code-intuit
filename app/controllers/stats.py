from app import app, db
from app.deco import login_required
from flask import render_template

@app.route('/stats')
@login_required()
def render():
    listVar = g.user.progress
    listVar = list(set(listVar))

    listPass = []

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



    return render_template('stats.html', listPass = listPass)
