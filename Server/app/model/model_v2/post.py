from mongoengine import *
from .account import AccountModel


class CommentModel(Document):
    text = StringField(required=True)
    author = ReferenceField(AccountModel)


class PostModel(Document):
    meta = {'collection': 'post'}
    title = StringField(required=True)
    text = StringField(required=True)
    comment = ListField(CommentModel)
    author = ReferenceField(AccountModel, required=True)
    upload_on = DateTimeField(required=True)