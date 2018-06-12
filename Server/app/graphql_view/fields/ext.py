import graphene


class ResponseMessageField(graphene.ObjectType):
    is_success = graphene.Boolean()
    message = graphene.String()