from mongoengine import Document, StringField


class RoleModel(Document):
    meta = {"collection": 'role'}
    name = StringField()