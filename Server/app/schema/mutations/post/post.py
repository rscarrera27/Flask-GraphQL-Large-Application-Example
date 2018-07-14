import graphene
from flask_graphql_auth import get_jwt_identity

from app.schema.util import auth_required
from app.model import PostModel, AccountModel


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
                             author=AccountModel.objects(id=get_jwt_identity()).first())

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