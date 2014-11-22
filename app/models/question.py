from app import db
from mongokit import Document


@db.register
class Question(Document):
    __collection__ = 'questions'
    __database__ = 'code-intel'

    structure = {
        'text': unicode,  # The main text for this question
        'choices': [{
            'text': unicode,
            'correct': bool
        }],
        'article': unicode  # What article this question belongs to
    }

    required_fields = ['text', 'choices']
    default_values = {}
    use_dot_notation = True
