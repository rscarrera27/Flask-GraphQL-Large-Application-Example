import graphene

from app.schema.unions.query import AccountUnion, PostUnion
from app.schema.queries.post import resolve_post
from app.schema.queries.account import resolve_account


class Query(graphene.ObjectType):
    post = graphene.List(of_type=PostUnion,
                         token=graphene.NonNull(graphene.String),
                         id=graphene.Int(default_value=None),
                         title=graphene.String(default_value=None),
                         resolver=resolve_post)

    account = graphene.List(of_type=AccountUnion,
                            token=graphene.NonNull(graphene.String),
                            id=graphene.String(default_value=None),
                            username=graphene.String(default_value=None),
                            resolver=resolve_account)
