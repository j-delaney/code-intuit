from app import db
from datetime import datetime
from mongokit import Document


@db.register
class User(Document):
    __collection__ = 'users'
    __database__ = 'code-intel'

    structure = {
        'username': unicode,
        'password': unicode,
        'points': int,
        'progress': [unicode],
        'entries': [{
            'date': datetime,
            'spending': {
                'school': int,
                'essentials': int,
                'snacks': int,
                'gas': int,
                'clothing': int,
                'recreation': int
            },
            'saving': {
                'car': int,
                'college': int
            }
        }],
        'goals': [{
            'category': unicode,
            'amount': int
        }]
    }

    required_fields = ['username', 'password', 'points']
    default_values = {
        'points': 0,
        'progress': []
    }
    use_dot_notation = True
