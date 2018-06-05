import graphene
from app.model.model_v2.account import AccountModel
from app.model.model_v2.post import CommentModel, PostModel
from app.graphql_view.view_v2.fields import AccountField, CommentField, PostField
from util import construct
from flask_jwt_extended import create_access_token, create_refresh_token
from uuid import uuid4


class RegisterMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        username = graphene.String()
        password = graphene.String()
        description = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, **kwargs):
        AccountModel(**kwargs).save()

        return RegisterMutation(is_success=True, message="Successfully registered")


class AuthMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()

    def mutate(self, info, **kwargs):
        user = AccountModel.objects(**kwargs).first()

        if user is not None:
            access_token = create_access_token(identity=kwargs["id"])
            refresh_token = create_refresh_token(identity=str(uuid4()))

            return AuthMutation(access_token=access_token, refresh_token=refresh_token, message="Login Success")
        else:
            return AuthMutation(message="Login failed")


class RefreshMutation(graphene.Mutation):

    class Arguments(object):
        refresh_token = graphene.String()

    access_token = graphene.String()
    message = graphene.String()

    def mutate(self, info, refresh_token):
        pass


class LogoutMutation(graphene.Mutation):

    class Arguments(object):
        refresh_token = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, refresh_token):
        pass


class PostUploadMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        text = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, token, title, text):
        pass


class PostDeleteMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()

    is_success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, token, post_id):
        pass


class CommentLeaveMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()
        comment = graphene.String()

    is_success = graphene.String()
    message = graphene.String()

    def mutate(self, info, token, post_id, comment):
        pass

