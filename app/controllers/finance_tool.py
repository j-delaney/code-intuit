from flask import render_template_string, render_template, request, url_for, redirect, g
from datetime import datetime
from app import app, db
from app.deco import login_required


@app.route('/tool/main')
@login_required
def tool_main():
    return render_template('tool/main.html')

@app.route('/tool/setup-goals', methods=['GET', 'POST'])
@login_required
def tool_setup_goals():
    user = g.user
    err = None

    if request.method == 'POST':
        user['goals'] = []

        for category, value in request.form.iteritems():
            category = unicode(category)
            value = value.strip()
            if value != u'':
                try:
                    value = int(value)
                    user.goals.append({'category': category, 'amount': value})
                except ValueError:
                    err = 'You may only use numerical values'
        user.save()
        if not err:
            return redirect(url_for('tool_main'))

    goals = {}
    if 'goals' in user:
        for goal in user.goals:
            goals[goal['category']] = goal['amount']
    return render_template("tool/goals.html", goals=goals, err=err)

@app.route('/tool/daily', methods=['GET', 'POST'])
@login_required
def tool_daily():
    user = g.user
    err = None

    # Why? Because I can
    today = datetime.today()
    today = datetime(today.year, today.month, today.day)

    if request.method == 'POST':
        i = -1
        if 'entries' in user:
            for index, entry in enumerate(user.entries):
                if entry['date'] == today:
                    i = index
        else:
            user['entries'] = [{}]
            i = 0
        if i == -1:
            user.entries.append({})
            i = len(user.entries) - 1

        user.entries[i] = {'date': today, 'spending': {}, 'saving': {}}

        for category, value in request.form.iteritems():
            category = unicode(category)
            value = value.strip()
            try:
                value = int(value)
            except ValueError:
                value = 0
                err = 'You may only use numerical values'

            m = 'spending'
            if category in ['car', 'college']:
                m = 'saving'
            user.entries[i][m][category] = value
        user.save()

        if not err:
            return redirect(url_for('tool_main'))


    daily = {}
    if 'entries' in user:
        for entry in user.entries:
            if entry['date'] == today:
                daily = entry
    if 'spending' not in daily:
        daily['spending'] = {}
    if 'saving' not in daily:
        daily['saving'] = {}


    return render_template("tool/daily.html", daily=daily, err=err)

@app.route('/tool/view-stats')
@login_required
def tool_view_stats():
    return render_template_string("Hello")