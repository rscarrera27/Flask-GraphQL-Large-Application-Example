from GraphQL_SQLAlchemy.model import engine, db_session, Base, Department, Employee, Role

Base.metadata.create_all(bind=engine)

engineering = Department(name='Engineering')
hr = Department(name='Human Resources')

[db_session.add(dpt) for dpt in [engineering, hr]]

engineer = Role(name='Engineer')
manager = Role(name='Manager')

[db_session.add(role) for role in [engineer, manager]]

peter = Employee(name='Peter', department=engineering)
roy = Employee(name='Roy', department=engineering)
tracy = Employee(name='Tracy', department=hr)

[db_session.add(employee) for employee in [peter, roy, tracy]]

db_session.commit()