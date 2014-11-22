from app import db
from mongokit import Document


@db.register
class Question(Document):
    __collection__ = 'questions'
    __database__ = 'sample'

    structure = {
        'text': unicode,
        'choices': [{
            'text': unicode,
            'correct': bool,
            'wrong_explanation': unicode
        }]
    }

    required_fields = ['text', 'choices']
    default_values = {}
    use_dot_notation = True