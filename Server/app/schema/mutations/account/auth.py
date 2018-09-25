from uuid import uuid4

import graphene
from flask_graphql_auth import create_access_token, create_refresh_token, get_jwt_identity, \
    mutation_jwt_refresh_token_required

from app.model import AccountModel
from app.schema.unions.mutation import AuthUnion, RefreshUnion
from app.schema.fields import AuthField, RefreshField, ResponseMessageField


class AuthMutation(graphene.Mutation):
    class Arguments(object):
        id = graphene.String()
        password = graphene.String()

    result = graphene.Field(AuthUnion)

    def mutate(self, info, **kwargs):
        user = AccountModel.objects(**kwargs).first()

        if user is not None:
            access_token = create_access_token(identity=kwargs["id"])
            refresh_token = create_refresh_token(identity=str(uuid4()))

            return AuthMutation(AuthField(access_token=access_token, refresh_token=refresh_token, message="Login Success"))
        else:
            return AuthMutation(ResponseMessageField(is_success=False, message="Login failed"))


class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    result = graphene.Field(RefreshUnion)

    @mutation_jwt_refresh_token_required
    def mutate(self, info, refresh_token):
        return RefreshMutation(RefreshField(acces_token=create_access_token(get_jwt_identity()), message="Refresh success"))

