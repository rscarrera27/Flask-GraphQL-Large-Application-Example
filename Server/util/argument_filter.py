def argument_filter(kwargs):
    query = {}
    for key, value in kwargs.items():
        if value is not None:
            query.update({key: value})

    return query