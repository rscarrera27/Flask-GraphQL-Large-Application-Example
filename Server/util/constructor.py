def construct(object_type, mongo_obj):
    """
    :param object_type: GraphQL Field class
    :param mongo_obj: mongoengine object
    :return: GraphQL Field that _id field changed to id
    """
    field_names = list(object_type._meta.fields)

    if 'id' in field_names:
        field_names.append('_id')
    kwargs = {attr: val for attr, val in mongo_obj.to_mongo().items() if attr in field_names}

    if '_id' in kwargs:
        kwargs['id'] = str(kwargs.pop('_id'))

    return object_type(**kwargs)