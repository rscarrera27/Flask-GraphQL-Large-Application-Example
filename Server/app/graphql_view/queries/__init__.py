import graphene

from app.graphql_view.fields import PostField, AccountField
from app.graphql_view.queries.post import resolve_post
from app.graphql_view.queries.account import resolve_account


class Query(graphene.ObjectType):
    post = graphene.List(of_type=PostField,
                         id=graphene.Int(default_value=None),
                         title=graphene.String(default_value=None),
                         resolver=resolve_post)

    account = graphene.List(of_type=AccountField,
                            id=graphene.String(default_value=None),
                            username=graphene.String(default_value=None),
                            resolver=resolve_account)