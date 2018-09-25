from app.schema.fields import ResponseMessageField, AccountField, PostField

from flask_graphql_auth import AuthInfoField
import graphene


class AccountResults(graphene.ObjectType):
    accounts = graphene.List(of_type=AccountField)


class PostResults(graphene.ObjectType):
    posts = graphene.List(of_type=PostField)


class AccountUnion(graphene.Union):
    class Meta:
        types = (AccountResults, ResponseMessageField, AuthInfoField)


class PostUnion(graphene.Union):
    class Meta:
        types = (PostResults, ResponseMessageField, AuthInfoField)
