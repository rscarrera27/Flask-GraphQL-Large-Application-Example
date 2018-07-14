from app.schema.fields import PostField, AccountField, CommentField
from app.model import AccountModel, PostModel
from util import argument_filter, construct


def resolve_post(root, info, **kwargs):
    query = argument_filter(kwargs)

    def make_post(post):
        author = AccountModel.objects.get(id=post.author.id)
        author = construct(AccountField, author)

        comment = [construct(CommentField, object) for object in post.comment]

        post = construct(PostField, post)

        post.author = author
        post.comment = comment

        return post

    post = [make_post(object) for object in PostModel.objects(**query)]

    return post
