from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField

from app.model.model_v1.DepartmentModel import DepartmentModel
from app.model.model_v1.RoleModel import RoleModel


class EmployeeModel(Document):
    meta = {"collection": 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(DepartmentModel)
    role = ReferenceField(RoleModel)