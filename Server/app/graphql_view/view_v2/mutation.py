import graphene
from app.model.model_v2.account import AccountModel
from app.model.model_v2.post import CommentModel, PostModel
from app.graphql_view.view_v2.fields import AccountField, CommentField, PostField
from util import construct


class RegisterMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        username = graphene.String()
        password = graphene.String()
        description = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, info, **kwargs):
        AccountModel(**kwargs).save()

        return cls(message="Successfully registered")


class AuthMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()

    @classmethod
    def mutate(cls, info, **kwargs):
        pass

