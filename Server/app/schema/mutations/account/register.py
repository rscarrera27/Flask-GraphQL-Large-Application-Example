import graphene

from app.model import AccountModel


class RegisterMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        username = graphene.String()
        password = graphene.String()
        description = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, **kwargs):
        AccountModel(**kwargs).save()

        return RegisterMutation(is_success=True, message="Successfully registered")