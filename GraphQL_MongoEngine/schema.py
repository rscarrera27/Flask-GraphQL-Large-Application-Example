import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model import Department as DepartmentModel
from model import Employee as EmployeeModel
from model import Role as RoleModel


def construct(object_type, mongo_obj):
    """
    :param object_type: GraphQL Field class
    :param mongo_obj: mongoengine object
    :return: GraphQL Field that _id field changed to id
    """
    field_names = [f.attname for f in object_type._meta_fields]
    if 'id' in field_names:
        field_names.append('_id')
    kwargs = {attr:val for attr, val in mongo_obj.to_mongo().items() if attr in field_names}
    if '_id' in kwargs:
        kwargs['id'] = kwargs.pop('_id')

    return object_type(**kwargs)


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

# class Department(MongoengineObjectType):
#
#     class Meta:
#         model = DepartmentModel
#         interfaces = (Node, )
#
#
# class Employee(MongoengineObjectType):
#
#     class Meta:
#         model = EmployeeModel
#         interfaces = (Node, )
#
#
# class Role(MongoengineObjectType):
#
#     class Meta:
#         model = RoleModel
#         interfaces = (Node, )
#
#
# class Query(graphene.ObjectType):
#     node = Node.Field()
#     all_employees = MongoengineConnectionField(Employee)
#     all_role = MongoengineConnectionField(Role)
#     all_Department = MongoengineConnectionField(Department)
#
#     employees = graphene.Field(Employee, name=graphene.String())
#
#     def resolve_employees(self, args, context, info):
#         query = Employee.get_node()


schema = graphene.Schema(query=Query, types=[Department, Employee, Role])