import graphene
from flask_graphql import GraphQLView
from flask import jsonify

from schema.mutations import Mutation
from schema.queries import Query


class Schema:
    def __init__(self, app):
        schema = graphene.Schema(query=Query, mutation=Mutation)

        app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view('graphql',
                                          schema=schema,
                                          graphiql=app.config['GRAPHIQL'])
        )

        schema_json = schema.introspect()

        @app.route("/schema")
        def schema_view():
            return jsonify(schema_json)

        print('[INFO] GraphQLView was successfully added with GraphiQL:{0}'.format(app.config['GRAPHIQL']))
