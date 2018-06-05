from mongoengine import *
from .account import AccountModel


class CommentModel(Document):
    text = StringField(required=True)
    author = ReferenceField(AccountModel)


class PostModel(Document):
    meta = {'collection': 'post'}
    id = IntField(required=True, primary_key=True)
    title = StringField(required=True)
    text = StringField(required=True)
    comment = ListField(CommentModel)
    author = ReferenceField(AccountModel, required=True)
    upload_on = DateTimeField(required=True)