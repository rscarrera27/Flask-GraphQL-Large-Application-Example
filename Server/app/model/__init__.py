from mongoengine import connect

from app.model.DepartmentModel import DepartmentModel
from app.model.EmployeeModel import EmployeeModel
from app.model.RoleModel import RoleModel


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))

        engineering = DepartmentModel(name="engineering")
        hr = DepartmentModel(name="Human Resources")

        [dpt.save() for dpt in [engineering, hr]]

        manager = RoleModel(name="manager")
        engineer = RoleModel(name="engineer")

        [role.save() for role in [engineer, manager]]

        peter = EmployeeModel(name='Peter', department=engineering, role=engineer)
        roy = EmployeeModel(name='Roy', department=engineering, role=engineer)
        tracy = EmployeeModel(name='Tracy', department=hr, role=manager)

        [employee.save() for employee in [peter, roy, tracy]]