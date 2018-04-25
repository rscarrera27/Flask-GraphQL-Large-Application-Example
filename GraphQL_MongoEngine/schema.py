import graphene
from mutation import Mutation
from query import Query


class DepartmentField(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class RoleField(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class EmployeeField(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    hired_on = graphene.DateTime()
    department = graphene.Field(DepartmentField)
    role = graphene.Field(RoleField)


schema = graphene.Schema(query=Query, mutation=Mutation)

# result = schema.execute('{ department{ name } }')
# print(result.data)
