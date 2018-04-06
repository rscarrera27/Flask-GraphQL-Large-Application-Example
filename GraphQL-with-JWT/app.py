from database import init_db
from flask import Flask, request
from flask_graphql import GraphQLView
from schema import schema
from flask_jwt_extended import jwt_required


app = Flask(__name__)
app.debug = True

default_query = '''
{
  allEmployees {
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()


def graphql_view():
    view = GraphQLView.as_view('graphql', schema=schema, context={'session': db.session},
                               graphiql=True)
    return jwt_required(view)


app.add_url_rule(
    '/graphql',
    view_func=graphql_view()
)

app = Flask(__name__)
app.debug = True
app.add_url_rule(
    '/graphql',
    view_func=graphql_view()
)