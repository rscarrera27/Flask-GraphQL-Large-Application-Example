from mongoengine import Document, StringField


class Role(Document):
    meta = {"collection": 'role'}
    name = StringField()