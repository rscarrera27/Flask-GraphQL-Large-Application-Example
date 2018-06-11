from functools import wraps
from flask_graphql_auth import jwt_required, get_jwt_identity, jwt_refresh_token_required
from app.model.model_v2.account import AccountModel
from app.graphql_view.view_v2.fields import ResponseMessageField

blacklist = set()


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        account = AccountModel.objects(id=get_jwt_identity()).first()
        if account is None:
            return ResponseMessageField(is_success=False, message="Invalid access token")
        return fn(*args, **kwargs)
    return wrapper


def refresh_required(fn):
    @wraps(fn)
    @jwt_refresh_token_required
    def wrapper(*args, **kwargs):
        if get_jwt_identity() in blacklist:
            return ResponseMessageField(is_success=False, message="Invalid refresh token")
        else:
            return fn(*args, **kwargs)
    return wrapper
