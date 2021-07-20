from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker
import os

engine = create_engine('postgres://127.0.0.1:5432/localtest') 

metadata = MetaData(engine)

student = Table(
    'student', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(128)),
    Column('grade', Integer),
    Column('work', Binary),
)

class Student(object):
    def __init__(self, work):
        self.work = work

    def __init__(self, name, grade, work):
        self.name = name
        self.grade = grade
        self.work = work

mapper(Student, student)

metadata.create_all()

session = sessionmaker(engine)()

work = os.urandom(10000)
stu = Student(name='kim', grade = 1, work = work)
session.add(stu)
session.commit()
obj_id = stu.id

session.expunge_all()

#Retrieve existing object
obj = session.query(Student).get(obj_id)
print(obj)
assert obj.work == work
