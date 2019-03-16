from mongoengine import *
from datetime import datetime


class AccountModel(Document):
    meta = {'collection': 'account'}
    id = StringField(required=True, primary_key=True)
    username = StringField(required=True)
    password = StringField(required=True)
    register_on = DateTimeField(required=True, default=datetime.now())