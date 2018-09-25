import graphene

from app.schema.mutations.post import (PostUploadMutation,
                                       PostDeleteMutation,
                                       CommentLeaveMutation)
from app.schema.mutations.account import (AuthMutation,
                                          RefreshMutation,
                                          RegisterMutation)


class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()

    auth = AuthMutation.Field()

    refresh = RefreshMutation.Field()

    post_upload = PostUploadMutation.Field()

    post_delete = PostDeleteMutation.Field()

    comment_leave = CommentLeaveMutation.Field()
