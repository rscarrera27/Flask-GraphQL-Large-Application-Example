import graphene
from flask_graphql_auth import AuthInfoField

from app.schema.fields import ResponseMessageField, AuthField, RefreshField


class ResponseUnion(graphene.Union):
    class Meta:
        types = (ResponseMessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


class AuthUnion(graphene.Union):
    class Meta:
        types = (AuthField, ResponseMessageField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


class RefreshUnion(graphene.Union):
    class Meta:
        types = (RefreshField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)