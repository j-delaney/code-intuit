from flask import render_template_string, render_template
from app import app, db
from app.deco import login_required


@app.route('/tool/main')
@login_required
def tool_main():
    return render_template('tool/main.html')

@app.route('/tool/setup-goals')
@login_required
def tool_setup_goals():
    return render_template_string("Hello")

@app.route('/tool/input-daily')
@login_required
def tool_input_daily():
    return render_template_string("Hello")

@app.route('/tool/view-stats')
@login_required
def tool_view_stats():
    return render_template_string("Hello")