import graphene

from app.model.model_v1.DepartmentModel import DepartmentModel
from app.model.model_v1.EmployeeModel import EmployeeModel
from app.model.model_v1.RoleModel import RoleModel
from app.graphql_view.view_v1.fields import DepartmentField, RoleField, EmployeeField
from util import construct, argument_filter


class Query(graphene.ObjectType):

    department = graphene.List(of_type=DepartmentField,
                               name=graphene.String(default_value=None))

    role = graphene.List(of_type=RoleField,
                         name=graphene.String(default_value=None))

    employee = graphene.List(of_type=EmployeeField,
                             name=graphene.String(default_value=None))

    hello = graphene.String(name=graphene.String(default_value="world"))

    def resolve_department(self, info, **kwargs):
        query = argument_filter(kwargs)
        department = [construct(DepartmentField, object) for object in DepartmentModel.objects(**query)]

        return department

    def resolve_role(self, info, **kwargs):
        query = argument_filter(kwargs)
        role = [construct(RoleField, object) for object in RoleModel.objects(**query)]

        return role

    def resolve_employee(self, info, **kwargs):
        query = argument_filter(kwargs)

        def make_employee(employee):

            department = DepartmentModel.objects.get(id=employee.department.id)
            department = construct(DepartmentField, department)

            role = RoleModel.objects.get(id=employee.role.id)
            role = construct(RoleField, role)

            employee = construct(EmployeeField, employee)

            employee.department = department
            employee.role = role

            return employee

        print(query)
        employee = [make_employee(document) for document in EmployeeModel.objects(**query)]

        return employee

    def resolve_hello(self, info, name):
        return 'Hello ' + name