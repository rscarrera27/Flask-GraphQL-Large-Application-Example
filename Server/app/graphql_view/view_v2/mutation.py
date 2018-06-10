import graphene
from app.model.model_v2.account import AccountModel
from app.model.model_v2.post import CommentModel, PostModel
from app.graphql_view.view_v2.fields import AccountField, CommentField, PostField
from app.graphql_view.view_v2 import refresh_required, auth_required, blacklist
from flask_graphql_auth import create_access_token, create_refresh_token, get_jwt_identity
from uuid import uuid4


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


class AuthMutation(graphene.Mutation):

    class Arguments(object):
        id = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()

    def mutate(self, info, **kwargs):
        user = AccountModel.objects(**kwargs).first()

        if user is not None:
            access_token = create_access_token(identity=kwargs["id"])
            refresh_token = create_refresh_token(identity=str(uuid4()))

            return AuthMutation(access_token=access_token, refresh_token=refresh_token, message="Login Success")
        else:
            return AuthMutation(message="Login failed")


class RefreshMutation(graphene.Mutation):

    class Arguments(object):
        refresh_token = graphene.String()

    access_token = graphene.String()
    message = graphene.String()

    @refresh_required
    def mutate(self, info, refresh_token):
        return RefreshMutation(acces_token=create_access_token(get_jwt_identity()), message="Refresh success")


class LogoutMutation(graphene.Mutation):

    class Arguments(object):
        refresh_token = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @refresh_required
    def mutate(self, info, refresh_token):
        blacklist.add(get_jwt_identity())
        return LogoutMutation(is_success=True, message="Logout successful")


class PostUploadMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        text = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @auth_required
    def mutate(self, info, token, title, text):
        count = PostModel.objects.count()
        new_post = PostModel(id=count+1,
                             title=title,
                             text=text,
                             comment=[],
                             author=AccountModel.objects(id=get_jwt_identity()))

        new_post.save()

        return PostUploadMutation(is_success=True,
                                  message="Upload successful")


class PostDeleteMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()

    is_success = graphene.Boolean()
    message = graphene.String()

    @auth_required
    def mutate(self, info, token, post_id):
        username = get_jwt_identity()
        post = PostModel.objects(id=post_id)

        if post and post.author == username:
            post.delete()

            return PostDeleteMutation(is_success=True,
                                      message="Delete successful")
        elif post is None:
            return PostDeleteMutation(is_success=False,
                                      message="Unknown post id")
        elif post.author != username:
            return PostDeleteMutation(is_success=False,
                                      message="No authority to delete this post")


class CommentLeaveMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()
        comment = graphene.String()

    is_success = graphene.String()
    message = graphene.String()

    @auth_required
    def mutate(self, info, token, post_id, comment):
        pass


class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()

    auth = AuthMutation.Field()

    refresh = RefreshMutation.Field()

    logout = LogoutMutation.Field()

    post_upload = PostUploadMutation.Field()

    post_delete = PostDeleteMutation.Field()