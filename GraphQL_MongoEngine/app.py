from model import init_db
from flask import Flask
from flask_graphql import GraphQLView
import graphql_view
app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=graphql_view.schema, graphiql=True)
)

if __name__ == '__main__':
    init_db()
    app.run()