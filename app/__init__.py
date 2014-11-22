from flask import Flask
from mongokit import Connection

app = Flask(__name__)
app.debug = True
app.secret_key = 'ajdfshasljbsdb6546s4b365s4dfb31dsz3b4143iyt5q387*(*^&*&%$&^$*&$&*$$^&*$&%#$'

db = Connection()
from models.user import User
from models.question import Question

from app.controllers import *
