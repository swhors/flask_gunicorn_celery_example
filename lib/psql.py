from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

import os

class PSQL:
    def __init__(self):
        print(__name__, '__init__')
        #self._engine = create_engine('postgres://127.0.0.1:5432/localtest') 
        self._engine = create_engine("postgresql://simpson:aq1234@127.0.0.1:5432/simpson") 
        self._metadata = MetaData(self._engine)
        self._metadata.create_all()
        self._session = sessionmaker(self._engine)()


    def __del__(self):
        print(__name__, '__del__')
        if self._session is not None:
            self._session.close()


    @property
    def session(self):
        return self._session


    @property
    def engine(self):
        return self._engine

    
    @property
    def metadata(self):
        return self._metadata


    def insert(self, name: str, grade: int, work = None):
        from model.student import Student
        if work is None:
            work = os.urandom(10000)
        student = Student(name=name, grade = grade, work = work)
        self._session.add(student)
        self._session.commit()

        self._session.expunge_all()

        return 1

    def get_all(self) -> []:
        from model.student import Student
        return self._session.query(Student).all()

    def get(self,id: int):
        from model.student import Student
        return self._session.query(Student).get(id)

    def delete(self,id: int):
        from model.student import Student
        self._session.query.filter(Student.id == id).delete()

    def delete_all(self):
        from model.student import Student
        self._session.query(Student).delete()
        self._session.commit()

        
