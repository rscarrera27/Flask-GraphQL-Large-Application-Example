from mongoengine import Document, StringField


class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()