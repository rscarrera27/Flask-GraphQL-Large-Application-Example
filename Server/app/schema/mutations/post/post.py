import graphene
from flask_graphql_auth import get_jwt_identity, mutation_jwt_required

from app.model import PostModel, AccountModel
from app.schema.unions.mutation import ResponseUnion
from app.schema.fields import ResponseMessageField


class PostUploadMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        text = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, title, text):
        count = PostModel.objects.count()
        new_post = PostModel(id=count+1,
                             title=title,
                             text=text,
                             comment=[],
                             author=AccountModel.objects(id=get_jwt_identity()).first())

        new_post.save()

        return PostUploadMutation(ResponseMessageField(is_success=True,
                                  message="Upload successful"))


class PostDeleteMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, token, post_id):
        username = get_jwt_identity()
        post = PostModel.objects(id=post_id)

        if post and post.author == username:
            post.delete()

            return PostDeleteMutation(ResponseMessageField(is_success=True,
                                      message="Delete successful"))
        elif post is None:
            return PostDeleteMutation(ResponseMessageField(is_success=False,
                                      message="Unknown post id"))
        elif post.author != username:
            return PostDeleteMutation(ResponseMessageField(is_success=False,
                                      message="No authority to delete this post"))