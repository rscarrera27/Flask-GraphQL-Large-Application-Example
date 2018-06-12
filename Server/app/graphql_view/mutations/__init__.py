import graphene

from app.graphql_view.mutations.post import (PostUploadMutation,
                                             PostDeleteMutation,
                                             CommentLeaveMutation)
from app.graphql_view.mutations.account import (AuthMutation,
                                                RefreshMutation,
                                                LogoutMutation,
                                                RegisterMutation)


class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()

    auth = AuthMutation.Field()

    refresh = RefreshMutation.Field()

    logout = LogoutMutation.Field()

    post_upload = PostUploadMutation.Field()

    post_delete = PostDeleteMutation.Field()

    comment_leave = CommentLeaveMutation.Field()
