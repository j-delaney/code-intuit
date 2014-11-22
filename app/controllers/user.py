from app import app, db
from flask import render_template, request, redirect, session, url_for


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user=db.User.find_one({'username':username,'password':password})

        if user is None:
            return render_template('login.html',err=True)

        else:
            session['username'] = username
            session['password'] = password
            return redirect(url_for('home'))

    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user=db.User.find_one({'username':username})

        if user is None:
            new_user = db.User()
            new_user.username = username
            new_user.password = password
            new_user.save()
            
            session['username'] = username
            session['password'] = password
            return redirect(url_for('home'))

        else:
            return render_template('register.html',err=True)

    else:
        return render_template('register.html')
