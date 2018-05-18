import graphene

from app.model.model_v2.account import AccountModel
from app.model.model_v2.post import CommentModel, PostModel
from app.graphql_view.view_v2.fields import *
from util.constructor import construct


class Query(graphene.ObjectType):
    post_list = graphene.List(of_type=PostField,
                             id=graphene.Int(default_value=None),
                             title=graphene.String(default_value=None))

    account_list = graphene.List(of_type=AccountField,
                                id=graphene.String(default_value="all"),
                                username=graphene.String(default_value="all"))

    comment = graphene.List(of_type=CommentField,
                            id=graphene.String())

    post = graphene.Field(type=PostField,
                          id=graphene.Int(default_value=0))

    account = graphene.Field(type=AccountField,
                             id=graphene.String())

    @staticmethod
    def resolve_post_ist(info, id, title):
        pass

    @staticmethod
    def resolve_account_list(info, id, username):
        pass