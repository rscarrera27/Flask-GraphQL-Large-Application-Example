from mongoengine import connect

from model.account import AccountModel
from model.post import PostModel, CommentModel


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))