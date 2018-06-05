from mongoengine import *


class AccountModel(Document):
    meta = {'collection': 'account'}
    id = StringField(required=True, primary_key=True)
    username = StringField(required=True)
    password = StringField(required=True)
    description = StringField()
    register_on = DateTimeField(required=True)