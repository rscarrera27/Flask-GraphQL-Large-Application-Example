from mongoengine import connect
from datetime import datetime

from app.model.account import AccountModel
from app.model.post import PostModel


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))

        lewis = AccountModel(id='lewis',
                             username='lewis',
                             password='1234',
                             description='hello world',
                             register_on=datetime.now().date())

        lewis.save()

        post = PostModel(id=1,
                         title='Hello',
                         text='World',
                         comment=[],
                         author=AccountModel.objects(id='lewis').first())

        post.save()