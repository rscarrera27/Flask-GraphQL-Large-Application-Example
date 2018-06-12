import graphene

from app.graphql_view.fields.account import AccountField
from app.graphql_view.fields.comment import CommentField


class PostField(graphene.ObjectType):
    title = graphene.String()
    text = graphene.String()
    upload_on = graphene.DateTime()
    comment = graphene.List(of_type=CommentField)
    author = graphene.Field(AccountField)