from app import app, db
from flask import render_template

@app.route('/article/retirement')
def render_retirement():
    return render_template('article/retirement.html')

@app.route('/article/plastic')
def render_plastic():
    return render_template('article/plastic.html')

@app.route('/article/borrowing')
def render_borrowing():
    return render_template('article/borrowing.html')

@app.route('/article/expenditures')
def render_expenditures():
    return render_template('article/expenditures.html')

@app.route('/article/income')
def render_income():
    return render_template('article/income.html')

@app.route('/article/budgeting')
def render_budgeting():
    return render_template('article/budgeting.html')
