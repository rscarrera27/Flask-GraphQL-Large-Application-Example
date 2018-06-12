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

    @staticmethod
    def resolve_post(root, info, **kwargs):
        query = argument_filter(kwargs)

        def make_post(post):
            author = AccountModel.objects.get(id=post.author.id)
            author = construct(AccountField, author)

            comment = [construct(CommentField, object) for object in post.comment]

            post = construct(PostField, post)

            post.author = author
            post.comment = comment

            return post

        post = [make_post(object) for object in PostModel.objects(**query)]

        return post

    @staticmethod
    def resolve_account(root, info, **kwargs):

        query = argument_filter(kwargs)
        account = [object for object in AccountModel.objects(**query)]

        return account
