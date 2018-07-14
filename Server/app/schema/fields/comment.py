import graphene

from app.schema.fields import AccountField


class CommentField(graphene.ObjectType):
    text = graphene.String()
    author = graphene.Field(type=AccountField)