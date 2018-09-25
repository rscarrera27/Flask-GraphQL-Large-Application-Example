import graphene

from app.model import AccountModel
from app.schema.fields import ResponseMessageField


class RegisterMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        username = graphene.String()
        password = graphene.String()
        description = graphene.String()

    result = graphene.Field(ResponseMessageField)

    @staticmethod
    def mutate(root, info, **kwargs):
        AccountModel(**kwargs).save()

        return RegisterMutation(ResponseMessageField(is_success=True, message="Successfully registered"))