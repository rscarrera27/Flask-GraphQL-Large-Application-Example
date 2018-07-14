from app.model import AccountModel
from util import argument_filter


def resolve_account(root, info, **kwargs):
    query = argument_filter(kwargs)
    account = [object for object in AccountModel.objects(**query)]

    return account