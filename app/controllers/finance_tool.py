from flask import render_template_string, render_template, request, url_for, redirect, g
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
        user.goals = []

        for category, value in request.form.iteritems():
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
    return render_template("tool/goals.html", user=user, err=err)

@app.route('/tool/input-daily')
@login_required
def tool_input_daily():
    return render_template_string("Hello")

@app.route('/tool/view-stats')
@login_required
def tool_view_stats():
    return render_template_string("Hello")