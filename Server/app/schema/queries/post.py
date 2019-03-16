from app.schema.fields import PostField, AccountField, CommentField, ResponseMessageField, PostResults
from app.model import PostModel

from flask_graphql_auth import query_jwt_required


@query_jwt_required
def resolve_post(root, info, **kwargs):
    id = kwargs.get('id', None)
    title = kwargs.get('title', None)

    posts = PostModel.objects(id=id, title=title)

    if posts.first() is None:
        return ResponseMessageField(is_success=False, message="Not found")

    return PostResults(posts=[PostField(id=post.id,
                                        title=post.title,
                                        text=post.text,
                                        upload_on=post.upload_on,
                                        comment=[CommentField(text=c.text,
                                                              author=AccountField(id=c.author.id,
                                                                                  username=c.author.username,
                                                                                  register_on=c.author.register_on))
                                                 for c in post.comment],
                                        author=AccountField(id=post.author.id,
                                                            username=post.author.username,
                                                            register_on=post.author.register_on))
                              for post in posts])
