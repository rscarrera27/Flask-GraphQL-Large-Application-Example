import graphene
from flask_graphql_auth import get_jwt_identity

from app.graphql_view.util import auth_required
from app.model import PostModel, AccountModel
from app.model.post import CommentModel


class CommentLeaveMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()
        comment = graphene.String()

    is_success = graphene.String()
    message = graphene.String()

    @auth_required
    def mutate(self, info, token, post_id, comment):
        post = PostModel.objects(id=post_id).first()
        new_comment = CommentModel(text=comment, author=AccountModel.objects(id=get_jwt_identity()).first())

        if post is None:
            return CommentLeaveMutation(is_success=False, message="Unknown post id")

        post.update_one(push_comment=new_comment)

        return CommentLeaveMutation(is_success=True, message="Comment successfully uploaded")