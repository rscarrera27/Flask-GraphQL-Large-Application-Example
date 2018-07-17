def argument_filter(kwargs):
    for key, value in kwargs.items():
        if value is None:
            del kwargs[key]

    return kwargs