from app.schema.fields import ResponseMessageField, AccountField, PostField

from flask_graphql_auth import AuthInfoField
import graphene


class AccountUnion(graphene.Union):
    class Meta:
        types = (AccountField, ResponseMessageField, AuthInfoField)


class PostUnion(graphene.Union):
    class Meta:
        types = (PostField, ResponseMessageField, AuthInfoField)
