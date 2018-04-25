from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField

from model.DepartmentModel import Department
from model.RoleModel import Role


class Employee(Document):
    meta = {"collection": 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)