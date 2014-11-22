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
                'school': float,
                'essentials': float,
                'snacks': float,
                'gas': float,
                'clothing': float,
                'recreation': float
            },
            'saving': {
                'car': float,
                'college': float
            }
        }],
        'goals': [{
            'category': unicode,
            'amount': float
        }]
    }

    required_fields = ['username', 'password', 'points']
    default_values = {
        'points': 0,
        'progress': []
    }
    use_dot_notation = True
