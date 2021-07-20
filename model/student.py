from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.types import VARBINARY

import datetime

Base = declarative_base()


class Student(Base):
    __tablename__='student'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    grade = Column('grade', Integer)
    #work = Column('work', Binary(4096*1000))
    work = Column('work', String)
    #work = Column('work', VARBINARY(4096*1000))
    created = Column('created',DateTime,default=datetime.datetime.utcnow)

    def __init__(self, name: str, grade: int, work = None):
        self.name = name
        self.grade = grade
        self.work = work


    def edit(self, name = None, grade = -1, work = None):
        self.name = name
        if grade > 0:
            self.grade = grade
        self.work = work

    def __repr__(self):
        return f"<Student(id = {self.id}, name = {self.name}, grade = {self.grade})>"
