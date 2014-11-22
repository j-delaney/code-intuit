from datetime import datetime
from random import random
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


@app.route('/demo')
def demo():
    user = db.User()
    user.username = unicode(random())
    user.password = unicode(random())
    user['entries'] = [
           {'date':datetime(2014,11,1),'spending':{'school': 2,'essentials': 2,'snacks': 5,'gas': 20,'clothing': 20,'recreation': 4},'saving':{'car':0,'college':1}},
           {'date':datetime(2014,11,2),'spending':{'school': 5,'essentials': 4,'snacks': 3,'gas': 10,'clothing': 10,'recreation': 3},'saving':{'car':0,'college':2}},
           {'date':datetime(2014,11,3),'spending':{'school': 4,'essentials': 2,'snacks': 2,'gas': 3,'clothing': 2,'recreation': 2},'saving':{'car':0,'college':3}},
           {'date':datetime(2014,11,4),'spending':{'school': 1,'essentials': 2,'snacks': 6,'gas': 3,'clothing': 4,'recreation': 0},'saving':{'car':10,'college':2}},
           {'date':datetime(2014,11,5),'spending':{'school': 2,'essentials': 0,'snacks': 0,'gas': 0,'clothing': 4,'recreation': 23},'saving':{'car':2,'college':0}},
           {'date':datetime(2014,11,6),'spending':{'school': 5,'essentials': 0,'snacks': 8,'gas': 2,'clothing': 3,'recreation': 4},'saving':{'car':3,'college':0}},
           {'date':datetime(2014,11,7),'spending':{'school': 3,'essentials': 0,'snacks': 5,'gas': 2,'clothing': 1,'recreation': 7},'saving':{'car':4,'college':3}},
           {'date':datetime(2014,11,8),'spending':{'school': 2,'essentials': 2,'snacks': 1,'gas': 2,'clothing': 2,'recreation': 8},'saving':{'car':10,'college':50}},
           {'date':datetime(2014,11,9),'spending':{'school': 6,'essentials': 21,'snacks': 8,'gas': 3,'clothing': 0,'recreation': 6},'saving':{'car':10,'college':23}},
           {'date':datetime(2014,11,10),'spending':{'school': 0,'essentials': 2,'snacks': 7,'gas': 3,'clothing': 4,'recreation': 4},'saving':{'car':10,'college':10}},
           {'date':datetime(2014,11,11),'spending':{'school': 0,'essentials': 1,'snacks': 4,'gas': 3,'clothing': 2,'recreation': 2},'saving':{'car':10,'college':10}},
           {'date':datetime(2014,11,12),'spending':{'school': 2,'essentials': 0,'snacks': 3,'gas': 0,'clothing': 1,'recreation': 10},'saving':{'car':10,'college':5}},
           {'date':datetime(2014,11,13),'spending':{'school': 23,'essentials': 10,'snacks': 0,'gas': 2,'clothing': 2,'recreation': 0},'saving':{'car':10,'college':0}},
           {'date':datetime(2014,11,14),'spending':{'school': 3,'essentials': 20,'snacks': 10,'gas': 1,'clothing': 0,'recreation': 0},'saving':{'car':10,'college':10}},
           {'date':datetime(2014,11,15),'spending':{'school': 2,'essentials': 2,'snacks': 0,'gas': 1,'clothing': 1,'recreation': 2},'saving':{'car':10,'college':10}},
           {'date':datetime(2014,11,16),'spending':{'school': 1,'essentials': 5,'snacks': 0,'gas': 2,'clothing': 1,'recreation': 0},'saving':{'car':10,'college':12}},
           {'date':datetime(2014,11,17),'spending':{'school': 5,'essentials': 7,'snacks': 0,'gas': 1,'clothing': 2,'recreation': 3},'saving':{'car':10,'college':15}},
           {'date':datetime(2014,11,18),'spending':{'school': 6,'essentials': 9,'snacks': 1,'gas': 0,'clothing': 2,'recreation': 1},'saving':{'car':10,'college':15}},
           {'date':datetime(2014,11,19),'spending':{'school': 7,'essentials': 8,'snacks': 2,'gas': 1,'clothing': 4,'recreation': 1},'saving':{'car':10,'college':15}},
           {'date':datetime(2014,11,20),'spending':{'school': 1,'essentials': 2,'snacks': 0,'gas': 1,'clothing': 0,'recreation': 1},'saving':{'car':10,'college':0}},
           {'date':datetime(2014,11,21),'spending':{'school': 0,'essentials': 3,'snacks': 0,'gas': 3,'clothing': 2,'recreation': 0},'saving':{'car':10,'college':25}},
           {'date':datetime(2014,11,22),'spending':{'school': 2,'essentials': 0,'snacks': 0,'gas': 0,'clothing': 0,'recreation': 0},'saving':{'car':10,'college':10}}
       ]
    user['goals'] = [
        {'category': u'car', 'amount': 2},
        {'category': u'clothing', 'amount': 5}
    ]
    user.save()

    session['username'] = user.username
    session['password'] = user.password
    return redirect(url_for('home'))


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
