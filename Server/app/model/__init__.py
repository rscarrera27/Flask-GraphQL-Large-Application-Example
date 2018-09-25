from mongoengine import connect
from datetime import datetime

from app.model.account import AccountModel
from app.model.post import PostModel


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))