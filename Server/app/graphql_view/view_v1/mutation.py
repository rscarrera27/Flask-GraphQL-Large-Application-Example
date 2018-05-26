import graphene
from mongoengine import MultipleObjectsReturned, DoesNotExist, ValidationError
from werkzeug.exceptions import abort
from app.model.model_v1.DepartmentModel import DepartmentModel
from app.model.model_v1.EmployeeModel import EmployeeModel
from app.model.model_v1.RoleModel import RoleModel
from app.graphql_view.view_v1.fields import DepartmentField, RoleField, EmployeeField
from util.constructor import construct


class DepartmentMutation(graphene.Mutation):

    class Arguments(object):
        name = graphene.String()

    department = graphene.Field(DepartmentField)

    def mutate(self, info, name):
        name = dict({
            "name": name
        })
        department = DepartmentModel(**name)
        department.save()

        return DepartmentMutation(department=construct(DepartmentField, department))


class RoleMutation(graphene.Mutation):

    class Arguments(object):
        name = graphene.String()

    role = graphene.Field(RoleField)

    def mutate(self, info, name):
        role_data = name
        role = RoleModel.objects.create(**role_data)
        role.save()

        return RoleMutation(role=construct(RoleField, role))


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


class Mutation(graphene.ObjectType):
    create_employee = EmployeeMutation.Field()

    create_role = RoleMutation.Field()

    create_department = DepartmentMutation.Field()