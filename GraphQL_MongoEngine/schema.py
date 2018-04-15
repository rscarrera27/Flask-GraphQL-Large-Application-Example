import logging
import graphene
import trafaret as t
from mongoengine import *
from flask import *
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
    field_names = [f.attname for f in object_type._meta.fields]
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
    department = graphene.List(DepartmentField)
    role = graphene.List(RoleField)


class DepartmentMutation(graphene.Mutation):

    class Input(object):
        name = graphene.String()

    department = graphene.Field(DepartmentField)

    @classmethod
    def mutate(cls, _, info, __):
        logger.debug("args {0}".format(info))
        dpt_schema = t.Dict({
            'name': t.String(min_length=1)
        })

        dpt_data = dpt_schema.check(info)
        department = DepartmentModel.objects.create(**dpt_data)
        department.save()

        return cls(user=construct(DepartmentField, department))


class RoleMutation(graphene.Mutation):

    class Input(object):
        name = graphene.String()

    role = graphene.Field(RoleField)

    @classmethod
    def mutate(cls, _, info, __):
        logger.debug("args {0}".format(info))
        role_schema = t.Dict({
            'name': t.String(min_length=1)
        })

        role_data = role_schema.check(info)
        role = RoleModel.objects.create(**role_data)
        role.save()

        return cls(user=construct(RoleField, role))


class EmployeeMutation(graphene.Mutation):

    class Input(object):
        name = graphene.String()
        department = graphene.List(DepartmentField)
        role = graphene.List(RoleField)

    employee = graphene.Field(EmployeeField)
    department = graphene.Field(DepartmentField)
    role = graphene.Field(RoleField)

    @classmethod
    def mutate(cls, _, info, __):
        logger.debug("args {0}".format(info))
        employee_schema = t.Dict({
            'name': t.String(min_length=2),
            'department': t.String(min_length=2),
            'role': t.String(min_length=2)
        })

        employee_data = employee_schema.check(info)
        department_name = employee_data.pop('department')
        role_name = employee_data.pop('role')

        try:
            department = DepartmentModel.objects.get(name=department_name)
            role = RoleModel.objects.get(name=role_name)

            employee_data = employee_data.update({
                'department': department,
                'role': role
            })

            employee = EmployeeModel(**employee_data)
            employee.save()

            return cls(EmployeeField, employee)

        except (MultipleObjectsReturned, DoesNotExist, ValidationError):
            abort(404)


class DepartmentQuery(graphene.ObjectType):

    department = graphene.Field(DepartmentField,
                                description="query with department name",
                                department=graphene.Argument(graphene.String))

    def resolve_department(self, args, info):
        department = DepartmentModel.objects.get(name=args.get('department'))

        return construct(DepartmentField, department)


