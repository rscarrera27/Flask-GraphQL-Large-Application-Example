import graphene


class AccountField(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()
    register_on = graphene.String()