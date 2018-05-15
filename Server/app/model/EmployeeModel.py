from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField

from app.model.DepartmentModel import DepartmentModel
from app.model.RoleModel import RoleModel


class EmployeeModel(Document):
    meta = {"collection": 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(DepartmentModel)
    role = ReferenceField(RoleModel)