from flask import render_template_string, render_template, request, url_for, redirect, g
from datetime import datetime
from app import app, db
from app.deco import login_required


@app.route('/tool/main')
@login_required
def tool_main():
    user = g.user

    if 'entries' not in user:
        user['entries'] = []
    if 'goals' not in user:
        user['goals'] = []

    goals = {}
    goal_reach = {}
    for goal in user.goals:
        goals[goal['category']] = goal['amount']
        goal_reach[goal['category']] = 0

    cat_spendings = {}

    saving_series = []
    spending_series = []
    entry_count = 0
    for entry in user.entries:
        entry_count += 1
        spent = 0
        saved = 0
        for category, value in entry['spending'].iteritems():
            spent += value
            if category in goals:
                if value <= goals[category]:
                    goal_reach[category] += 1
            if category not in cat_spendings:
                cat_spendings[category] = 0
            cat_spendings[category] += value
        for category, value in entry['saving'].iteritems():
            saved += value
            if category in goals:
                if value <= goals[category]:
                    goal_reach[category] += 1
        saving_series.append(saved)
        spending_series.append(spent)

    pie = "["
    for cat, val in enumerate(cat_spendings):
        pie += '[\"%s\",%d],' % (val, cat)
    pie = pie[:-1]
    pie += "]"

    return render_template('tool/main.html', saving_series=saving_series, spending_series=spending_series, pie=pie)

@app.route('/tool/goals', methods=['GET', 'POST'])
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