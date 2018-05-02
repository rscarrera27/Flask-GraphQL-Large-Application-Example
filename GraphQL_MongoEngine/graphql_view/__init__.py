import graphene
from graphql_view.mutation import Mutation
from graphql_view.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

