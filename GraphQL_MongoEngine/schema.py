import logging
import graphene
import trafaret as t
from mongoengine import *
from flask import *
from bson import ObjectId
from model import Department as DepartmentModel
from model import Employee as EmployeeModel
from model import Role as RoleModel

logger = logging.getLogger(__package__)


def construct(object_type, mongo_obj):
    """
    :param object_type: GraphQL Field class
    :param mongo_obj: mongoengine object
    :return: GraphQL Field that _id field changed to id
    """
    field_names = list(object_type._meta.fields)

    if 'id' in field_names:
        field_names.append('_id')
    kwargs = {attr: val for attr, val in mongo_obj.to_mongo().items() if attr in field_names}

    if '_id' in kwargs:
        kwargs['id'] = str(kwargs.pop('_id'))
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


class DepartmentMutation(graphene.Mutation):

    class Arguments(object):
        name = graphene.String()

    department = graphene.Field(DepartmentField)

    @classmethod
    def mutate(cls, info, _name):
        name = dict({
            "name": _name
        })
        department = DepartmentModel.objects(**name)
        department.save()

        return cls(department=construct(DepartmentField, department))


class RoleMutation(graphene.Mutation):

    class Arguments(object):
        name = graphene.String()

    role = graphene.Field(RoleField)

    @classmethod
    def mutate(cls, info, name):
        role_data = name
        role = RoleModel.objects.create(**role_data)
        role.save()

        return cls(role=construct(RoleField, role))


class EmployeeMutation(graphene.Mutation):

    class Arguments(object):
        name = graphene.String()
        department = graphene.String()
        role = graphene.String()

    ok = graphene.Boolean()
    employee = graphene.Field(EmployeeField)

    def mutate(self, info, name, department, role):

        name = name
        department_name = department
        role_name = role

        try:
            department = DepartmentModel.objects.get(name=department_name)
            role = RoleModel.objects.get(name=role_name)

            employee_data = dict({
                'name': name,
                'department': department,
                'role': role
            })

            employee = EmployeeModel(**employee_data)
            employee.save()

            employee = construct(EmployeeField, employee)
            employee.department = construct(DepartmentField, department)
            employee.role = construct(RoleField, role)

            return EmployeeMutation(employee=employee, ok=True)

        except (MultipleObjectsReturned, DoesNotExist, ValidationError):
            abort(404)


class Query(graphene.ObjectType):

    department = graphene.List(of_type=DepartmentField,
                               name=graphene.String(default_value="all"))

    role = graphene.List(of_type=RoleField,
                         name=graphene.String(default_value="all"))

    employee = graphene.List(of_type=EmployeeField,
                             name=graphene.String(default_value="all"))

    hello = graphene.String(name=graphene.String(default_value="world"))

    def resolve_department(self, info, name):
        if name == "all":
            department = [construct(DepartmentField, object) for object in DepartmentModel.objects]
            return department
        else:
            department = DepartmentModel.objects.get(name=name)
            return [construct(DepartmentField, department)]

    def resolve_role(self, info, name):
        if name == "all":
            role = [construct(RoleField, object) for object in RoleModel.objects]
            return role
        else:
            role = RoleModel.objects.get(name=name)
            return [construct(RoleField, role)]

    def resolve_employee(self, info, name):

        def make_employee(employee):

            department = DepartmentModel.objects.get(id=employee.department.id)
            department = construct(DepartmentField, department)

            role = RoleModel.objects.get(id=employee.role.id)
            role = construct(RoleField, role)

            employee = construct(EmployeeField, employee)

            employee.department = department
            employee.role = role

            return employee

        if name == "all":
            employee = [make_employee(document) for document in EmployeeModel.objects]
            return employee
        else:
            employee = EmployeeModel.objects.get(name=name)
            employee = make_employee(employee)

            return [employee]

    def resolve_hello(self, info, name):
        return 'Hello ' + name


class Mutation(graphene.ObjectType):
    create_employee = EmployeeMutation.Field()

    create_role = RoleMutation.Field()

    create_department = DepartmentMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

# result = schema.execute('{ department{ name } }')
# print(result.data)
