from mongoengine import Document, StringField


class DepartmentModel(Document):
    meta = {'collection': 'department'}
    name = StringField()