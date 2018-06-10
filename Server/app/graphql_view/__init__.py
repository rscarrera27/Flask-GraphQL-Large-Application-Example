import graphene
from flask_graphql import GraphQLView
from app.graphql_view.view_v1.mutation import Mutation
from app.graphql_view.view_v1.query import Query


class Schema:
    def __init__(self, app):
        schema = graphene.Schema(query=Query, mutation=Mutation)

        app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view('graphql',
                                          schema=schema,
                                          graphiql=app.config['GRAPHIQL'])
        )
        print('[INFO] GraphQLView was successfully added with GraphiQL:{0}'.format(app.config['GRAPHIQL']))
