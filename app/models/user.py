from app import db
from mongokit import Document


@db.register
class User(Document):
    __collection__ = 'users'
    __database__ = 'sample'

    structure = {
        'username': unicode,
        'password': unicode,
        'points': int,
        'progress': [unicode]
    }

    required_fields = ['username', 'password', 'points', 'progress']
    default_values = {
        'points': 0,
        'progress': []
    }
    use_dot_notation = True