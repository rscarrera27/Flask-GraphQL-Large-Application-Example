import graphene

from app.graphql_view.fields import AccountField


class CommentField(graphene.ObjectType):
    text = graphene.String()
    author = graphene.Field(type=AccountField)