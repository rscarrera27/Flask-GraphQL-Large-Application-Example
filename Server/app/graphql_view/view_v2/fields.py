import graphene


class AccountField(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()
    register_on = graphene.String()


class CommentField(graphene.ObjectType):
    text = graphene.String()
    author = graphene.Field(type=AccountField)


class PostField(graphene.ObjectType):
    title = graphene.String()
    text = graphene.String()
    upload_on = graphene.DateTime()
    comment = graphene.List(of_type=CommentField)
    author = graphene.Field(AccountField)


class ResponseMessageField(graphene.ObjectType):
    is_success = graphene.Boolean()
    message = graphene.String()
