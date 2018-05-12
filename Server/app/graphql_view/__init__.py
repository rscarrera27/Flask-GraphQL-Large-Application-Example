import graphene
from app.graphql_view.mutation import Mutation
from app.graphql_view.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

