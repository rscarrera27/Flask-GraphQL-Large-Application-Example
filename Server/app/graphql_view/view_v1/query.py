import graphene

from app.model.model_v1.DepartmentModel import DepartmentModel
from app.model.model_v1.EmployeeModel import EmployeeModel
from app.model.model_v1.RoleModel import RoleModel
from app.graphql_view.view_v1.fields import DepartmentField, RoleField, EmployeeField
from util import construct, argument_filter


class Query(graphene.ObjectType):

    department = graphene.List(of_type=DepartmentField,
                               name=graphene.String(default_value="all"))

    role = graphene.List(of_type=RoleField,
                         name=graphene.String(default_value="all"))

    employee = graphene.List(of_type=EmployeeField,
                             name=graphene.String(default_value="all"))

    hello = graphene.String(name=graphene.String(default_value="world"))

    def resolve_department(self, info, **kwargs):
        name = kwargs["name"]
        if name == "all":
            department = [construct(DepartmentField, object) for object in DepartmentModel.objects]
            return department
        else:
            department = DepartmentModel.objects.get(name=name)
            return [construct(DepartmentField, department)]

    def resolve_role(self, info, **kwargs):
        query = argument_filter(kwargs)
        if query["name"] == "all":
            role = [construct(RoleField, object) for object in RoleModel.objects]
            return role
        else:
            role = RoleModel.objects.get(**query)
            return [construct(RoleField, role)]

    def resolve_employee(self, info, **kwargs):
        name = kwargs["name"]
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

        if query["name"] == "all":
            employee = [make_employee(document) for document in EmployeeModel.objects]
            return employee
        else:
            employee = EmployeeModel.objects.get(**query)
            employee = make_employee(employee)

            return [employee]

    def resolve_hello(self, info, name):
        return 'Hello ' + name