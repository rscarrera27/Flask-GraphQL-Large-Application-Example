import graphene


class AccountField(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()
    register_on = graphene.String()


class CommentField(graphene.ObjectType):
    text = graphene.String()
    author = graphene.Field(type=AccountField)


class ResponseMessageField(graphene.ObjectType):
    is_success = graphene.Boolean()
    message = graphene.String()


class RefreshField(graphene.ObjectType):
    access_token = graphene.String()
    message = graphene.String()


class AuthField(graphene.ObjectType):
    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()


class PostField(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    text = graphene.String()
    upload_on = graphene.DateTime()
    comment = graphene.List(of_type=CommentField)
    author = graphene.Field(AccountField)


class AccountResults(graphene.ObjectType):
    accounts = graphene.List(of_type=AccountField)


class PostResults(graphene.ObjectType):
    posts = graphene.List(of_type=PostField)