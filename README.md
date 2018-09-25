#  ✨✨Awesome-GraphQL✨✨

## Summary
This is how I structure my GraphQL server with Flask + Graphene

## About
This is basic example of large Flask+Graphene server. 
all essential use examples have been covered and advanced use examples will be added step by step

- Covered
    - Query example
    - Mutauion example
    - Union example
    - Field example
    - Basic authentication example
    - MongoDB example

- Not Covered
    - Relay example
    - InputObjectType example
    - MySQL(SQLAlchemy, PeeWee) example
    - Dataloader example
    - Middleware example
    - Interfaces example
    - AbstractTypes example
    
## Project defendencies
- GraphQL framework
    - Graphene
- HTTP serving
    - Flask-GraphQL
    - Flask
- Database ORM
    - Mongoengine
- Authentication
    - [Flask-GraphQL-Auth](https://flask-graphql-auth.readthedocs.io/en/latest/) (JWT based authentication)

## How to test this example?
This repository implemented minitwit to cover examples. Use the following command to run the server

```sh
pip install -r requirements.txt
python run_server.py
```
GraphiQL enabled by default.

## Diagrams
not covered

## Core components

### /Server/app/schema
GraphQL 서버를 구성하는 필드, 쿼리, 뮤테이션을 담고 있습니다.

This directory contains fields, queries, and interactions that make up the GraphQL schema

#### /Server/app/schema/__init__.py
GraphQL 스키마를 구성하고 구성된 스키마를 Flask 인스턴스에 할당합니다.

Structure GraphQL schema and add schema with flask.add_url_rule

#### /Server/app/schema/fields
GraphQL 쿼리와 뮤테이션에서 사용하는 필드들로 구성된 디렉터리입니다.

This directory contains the fields that make up the GraphQL schema.

#### /Server/app/graphql_view/unions 
GraphQL 쿼리와 뮤테이션에서 사용하는 유니온들로 구성된 디렉터리입니다.

This directory contains the unions that make up the GraphQL schema.

#### /Server/app/schema/queries
이 디렉터리는 쿼리와 쿼리 resolver들로 구성됩니다. 유연한 구조를 위해 resolver들을 독립적인 파일에 담습니다

This directory consists root query class and query resolvers. Place the resolver in an independent file for flexible structure

#### /Server/app/schema/mutations
이 디렉터리는 뮤테이션들로 구성됩니다. 유연한 구조를 위해 뮤테이션 들을 독립적인 파일에 담습니다

This directory consists mutations. Place the mutation in an independent file for flexible structure

## I refered
### People
[Syrus Akbary](https://twitter.com/syrusakbary)

### Repository
[Flask-Large-Application-Example](https://github.com/JoMingyu/Flask-Large-Application-Example)

### Website
[Designing GraphQL mutations](https://dev-blog.apollodata.com/designing-graphql-mutations-e09de826ed97)  
[Authorization in GraphQL](https://dev-blog.apollodata.com/authorization-in-graphql-452b1c402a9)  
[GraphQL ansd authentication](https://medium.com/the-graphqlhub/graphql-and-authentication-b73aed34bbeb)

### Library Docs
[Graphene](https://medium.com/the-graphqlhub/graphql-and-authentication-b73aed34bbeb)
