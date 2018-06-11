class Config:
    GRAPHIQL = True
    DEBUG = True
    HOST = '0.0.0.0'

    SERVICE_NAME = 'graphql-flask-example'

    RUN_SETTING = {
        'host': HOST,
        'port': 5000,
        'debug': DEBUG
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': 'mongomock://localhost'
    }

    JWT_SECRET_KEY = "affogato"
