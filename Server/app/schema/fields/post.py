import graphene

from app.schema.fields.account import AccountField
from app.schema.fields.comment import CommentField


class PostField(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    text = graphene.String()
    upload_on = graphene.DateTime()
    comment = graphene.List(of_type=CommentField)
    author = graphene.Field(AccountField)