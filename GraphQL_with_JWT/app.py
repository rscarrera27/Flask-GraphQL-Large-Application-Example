from database import init_db
from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from GraphQL_with_JWT.schema import schema
from uuid import uuid4
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity, create_refresh_token,
    create_access_token, jwt_refresh_token_required, get_raw_jwt
)

from GraphQL_with_JWT.model import User, RefreshToken


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


# Enable blacklisting and specify what kind of tokens to check
# against the blacklist
app.config['JWT_SECRET_KEY'] = 'Artoria'  # Change this!
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
make_access_token = create_access_token

blacklist = set()


def graphql_view():
    view = GraphQLView.as_view('graphql', schema=schema)
    return jwt_required(view)


def create_refresh_token(username, password):
    uuid = uuid4()
    RefreshToken(token=str(uuid),
                 token_owner=User.objects(name=username, password=password).first(),
                 pw_snapshot=password).save()

    refresh_token = make_access_token(identity=str(uuid))

    return refresh_token


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.objects(name=username, password=password).first()

    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401
    else:

        @jwt.user_claims_loader
        def add_claims_to_access_token(identity):
            return {
                'hello': 'world',
                'permission': user.authority
            }

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(username, password)

    ret = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }

    return jsonify(ret), 200


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200


@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200


@app.route('/logout2', methods=['DELETE'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200


app.add_url_rule(
    '/graphql',
    view_func=graphql_view()
)


if __name__ == '__main__':
    init_db()
    app.run()