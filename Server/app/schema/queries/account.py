from app.model import AccountModel
from app.schema.fields import AccountField
from util import argument_filter, construct


def resolve_account(root, info, **kwargs):
    query = argument_filter(kwargs)
    account = [construct(AccountField, object) for object in AccountModel.objects(**query)]

    return account