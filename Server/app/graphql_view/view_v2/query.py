import graphene

from app.model.model_v2.account import AccountModel
from app.model.model_v2.post import PostModel
from app.graphql_view.view_v2.fields import AccountField, PostField, CommentField
from util import construct, argument_filter


class Query(graphene.ObjectType):
    post = graphene.List(of_type=PostField,
                         id=graphene.Int(default_value=None),
                         title=graphene.String(default_value=None))

    account = graphene.List(of_type=AccountField,
                            id=graphene.String(default_value=None),
                            username=graphene.String(default_value=None))



            comment = [construct(CommentField, object) for object in post.comment]

    @staticmethod
    def resolve_post_ist(info, id, title):
        pass

    @staticmethod
    def resolve_account_list(info, id, username):
        pass