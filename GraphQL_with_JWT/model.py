from datetime import datetime
from mongoengine import Document
from mongoengine.fields import *


class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()


class Role(Document):
    meta = {"collection": 'role'}
    name = StringField()


class Employee(Document):
    meta = {"collection": 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)


class User(Document):

    meta = {
        'collection': 'user'
    }
    name = StringField()
    password = StringField()
    authority = IntField()


class RefreshToken(Document):

    meta = {
        'collection': 'refresh_token'
    }

    token = StringField(
        primary_key=True
    )
    token_owner = ReferenceField(
        document_type=User,
        required=True
    )
    pw_snapshot = StringField(
        required=True
    )
