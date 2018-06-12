#  ✨✨Awesome-GraphQL✨✨

## Summary
This is how I structure my GraphQL server with Flask + Graphene

## About
GrapQL 서버는 아직까지 쉽게 찾을 수 있는 자료가 많이 없기 때문에 (파이썬 관련해서는 더욱 없습니다) 디자인과 서버 구조에 관해서 많은 고민을 하게 됩니다. 이 저장소는 파이썬을 위한 GraphQL 라이브러리인 Grphene 과 Flask를 이용해 만드는 구조적인(?) GraphQL 서버의 예시입니다.

아직 테스트 케이스도 구성되지 않았고 Relay, InputObject나 미들웨어 사용 예시도 없고 Graphene에서 제공되는 기능들이 다 적용되지 않아 부족하지만 곧 추가될 예정입니다.

## Project defendencies
GraphQL 라이브러리로 Graphene, 웹 서버로 Flask, DB로 MongoDB(Mongoengine), 그리고 인증 처리에 JWT(Flask-GraphQL-Auth)를 사용합니다.

## How to test this example?

```sh
pip install -r requirements.txt
python run_server.py
```

쿼리, 뮤테이션 그리고 필드의 정보를 제공하기 위해 기본적으로 GraphiQL(GraphQL 서버를 위한 웹 브라우저 IDE)이 활성화되어 있습니다.

## Components
기본적인 서버의 구조는 @JoMingyu의 Flask-Large-Application-Example과 동일합니다. 여기서는 GraphQL 서버가 가지는 특징적인 요소만을 다루겠습니다.

### /Server/app/graphql_view
GraphQL 서버를 구성하는 필드, 쿼리, 뮤테이션을 담고 있습니다.

#### /Server/app/graphql_view/__init__.py
GraphQL 스키마를 구성하고 구성된 스키마를 Flask 인스턴스에 할당합니다.

#### /Server/app/graphql_view/fields
GraphQL 쿼리와 뮤테이션에서 사용하는 필드들로 구성된 디렉토리입니다.

#### /Server/app/graphql_view/queries
GraphQL의 쿼리와 그 resolver들로 구성되어 있습니다. 유연한 구조를 위해 Query 클래스 내에 resolver들을 만들지 않고 외부에 만들어서 사용합니다.
__init__.py의 Query 클래스는 /Server/app/graphql_view/__init__.py에 있는 스키마에 추가됩니다.

#### /Server/app/graphql_view/mutations
GraphQL의 뮤테이션들로 이루어져 있습니다. 유연한 구조를 위해 각각의 뮤테이션 클래스를 모두 분리하고 최상단의 __init__.py 에 있는 Mutation 클래스에 뮤테이션들을 등록합니다. 이 Mutation 클래스는 /Server/app/graphql_view/__init__.py에 있는 스키마에 추가됩니다.

#### /Server/app/graphql_view/util.py 
뮤테이션을 위한 인증 데코레이터입니다. Flask-GrpahQL-Auth의 데코레이터를 사용하여 만들어졌습니다. 이 데코레이터들은 인증이 실패한다면 각 뮤테이션 클래스로 넘어가지 않고 데코레이터가 ResponseMessageField를 반환하여 인증이 실패했다는것을 알립니다.

GraphQL 공식 문서에서는 인증을 Middleware에서 처리하는 것을 권장한다고 하지만 Graphene의 개발자 중 한명인 Syrus Akbary가 각 인증 데코레이터를 사용해  resolver에서 처리하는것이 좀 더 쉽고 확장 가능한 접근 방법이라고 조언해 주었기 때문에 resolver 단에서 인증을 수행하는 방법을 사용하고 있습니다.

## I refered
### People
[Syrus Akbary](https://twitter.com/syrusakbary/status/1005836407682682881)

### Repository
[Flask-Large-Application-Example](https://github.com/JoMingyu/Flask-Large-Application-Example)

### Website
[Designing GraphQL mutations](https://dev-blog.apollodata.com/designing-graphql-mutations-e09de826ed97)  
[Authorization in GraphQL](https://dev-blog.apollodata.com/authorization-in-graphql-452b1c402a9)  
[GraphQL ansd authentication](https://medium.com/the-graphqlhub/graphql-and-authentication-b73aed34bbeb)

### Library Docs
[Graphene](https://medium.com/the-graphqlhub/graphql-and-authentication-b73aed34bbeb)
