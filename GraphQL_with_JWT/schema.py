import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from GraphQL_with_JWT.model import Department as DepartmentModel
from GraphQL_with_JWT.model import Employee as EmployeeModel
from GraphQL_with_JWT.model import Role as RoleModel


class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node, )


class Employee(MongoengineObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (Node, )


class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node, )


class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_role = MongoengineConnectionField(Role)
    all_Department = MongoengineConnectionField(Department)


schema = graphene.Schema(query=Query, types=[Department, Employee, Role])