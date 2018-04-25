from mongoengine import connect

from model.DepartmentModel import Department
from model.EmployeeModel import Employee
from model.RoleModel import Role

connect('graphene-mongo-example', host='mongomock://localhost', alias='default')


def init_db():

    engineering = Department(name="engineering")
    hr = Department(name="Human Resources")

    [dpt.save() for dpt in [engineering, hr]]

    manager = Role(name="manager")
    engineer = Role(name="engineer")

    [role.save() for role in [engineer, manager]]

    peter = Employee(name='Peter', department=engineering, role=engineer)
    roy = Employee(name='Roy', department=engineering, role=engineer)
    tracy = Employee(name='Tracy', department=hr, role=manager)

    [employee.save() for employee in [peter, roy, tracy]]

